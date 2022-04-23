# -*- coding: utf-8 -*-
"""Histogram-based Outlier Detection (HBOS)
"""
# Author: Yue Zhao <zhaoy@cmu.edu>
# License: BSD 2 clause

from __future__ import division
from __future__ import print_function

import numpy as np
from numba import njit
from sklearn.utils import check_array
from sklearn.utils.validation import check_is_fitted

from ..utils.utility import check_parameter
from ..utils.utility import invert_order
from ..utils.utility import get_optimal_n_bins

from .base import BaseDetector


class HBOS(BaseDetector):
    """Histogram- based outlier detection (HBOS) is an efficient unsupervised
    method. It assumes the feature independence and calculates the degree
    of outlyingness by building histograms. See :cite:`goldstein2012histogram`
    for details.    

    Two versions of HBOS are supported:        
    - Static number of bins: uses a static number of bins for all features.
    - Automatic number of bins: every feature uses a number of bins deemed to 
      be optimal according to the Birge-Rozenblac method
      (:cite:`birge2006many`).
      
    Parameters
    ----------
    n_bins : int or string, optional (default=10)
        The number of bins. "auto" uses the birge-rozenblac method for
        automatic selection of the optimal number of bins for each feature.

    alpha : float in (0, 1), optional (default=0.1)
        The regularizer for preventing overflow.

    tol : float in (0, 1), optional (default=0.5)
        The parameter to decide the flexibility while dealing
        the samples falling outside the bins.

    contamination : float in (0., 0.5), optional (default=0.1)
        The amount of contamination of the data set,
        i.e. the proportion of outliers in the data set. Used when fitting to
        define the threshold on the decision function.

    Attributes
    ----------
    bin_edges_ : numpy array of shape (n_bins + 1, n_features )
        The edges of the bins.

    hist_ : numpy array of shape (n_bins, n_features)
        The density of each histogram.

    decision_scores_ : numpy array of shape (n_samples,)
        The outlier scores of the training data.
        The higher, the more abnormal. Outliers tend to have higher
        scores. This value is available once the detector is fitted.

    threshold_ : float
        The threshold is based on ``contamination``. It is the
        ``n_samples * contamination`` most abnormal samples in
        ``decision_scores_``. The threshold is calculated for generating
        binary outlier labels.

    labels_ : int, either 0 or 1
        The binary labels of the training data. 0 stands for inliers
        and 1 for outliers/anomalies. It is generated by applying
        ``threshold_`` on ``decision_scores_``.
    """

    def __init__(self, n_bins=10, alpha=0.1, tol=0.5, contamination=0.1):
        super(HBOS, self).__init__(contamination=contamination)
        self.n_bins = n_bins
        self.alpha = alpha
        self.tol = tol

        check_parameter(alpha, 0, 1, param_name='alpha')
        check_parameter(tol, 0, 1, param_name='tol')

    def fit(self, X, y=None):
        """Fit detector. y is ignored in unsupervised methods.

        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The input samples.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Fitted estimator.
        """
        # validate inputs X and y (optional)
        X = check_array(X)
        self._set_n_classes(y)

        _, n_features = X.shape[0], X.shape[1]

        if isinstance(self.n_bins, str) and self.n_bins.lower() == "auto":
            # Uses the birge rozenblac method for automatic histogram size per feature
            self.hist_ = []
            self.bin_edges_ = []

            # build the histograms for all dimensions
            for i in range(n_features):
                n_bins = get_optimal_n_bins(X[:, i])
                hist, bin_edges = np.histogram(X[:, i], bins=n_bins,
                                               density=True)
                self.hist_.append(hist)
                self.bin_edges_.append(bin_edges)
                # the sum of (width * height) should equal to 1
                assert (np.isclose(1, np.sum(
                    hist * np.diff(bin_edges)), atol=0.1))

            outlier_scores = _calculate_outlier_scores_auto(X, self.bin_edges_,
                                                            self.hist_,
                                                            self.alpha,
                                                            self.tol)

        elif check_parameter(self.n_bins, low=2, high=np.inf):
            self.hist_ = np.zeros([self.n_bins, n_features])
            self.bin_edges_ = np.zeros([self.n_bins + 1, n_features])

            # build the histograms for all dimensions
            for i in range(n_features):
                self.hist_[:, i], self.bin_edges_[:, i] = \
                    np.histogram(X[:, i], bins=self.n_bins, density=True)
                # the sum of (width * height) should equal to 1
                assert (np.isclose(1, np.sum(
                    self.hist_[:, i] * np.diff(self.bin_edges_[:, i])),
                                   atol=0.1))

            outlier_scores = _calculate_outlier_scores(X, self.bin_edges_,
                                                       self.hist_,
                                                       self.n_bins,
                                                       self.alpha, self.tol)

        # invert decision_scores_. Outliers comes with higher outlier scores
        self.decision_scores_ = invert_order(np.sum(outlier_scores, axis=1))
        self._process_decision_scores()
        return self

    def decision_function(self, X):
        """Predict raw anomaly score of X using the fitted detector.

        The anomaly score of an input sample is computed based on different
        detector algorithms. For consistency, outliers are assigned with
        larger anomaly scores.

        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The training input samples. Sparse matrices are accepted only
            if they are supported by the base estimator.

        Returns
        -------
        anomaly_scores : numpy array of shape (n_samples,)
            The anomaly score of the input samples.
        """
        check_is_fitted(self, ['hist_', 'bin_edges_'])
        X = check_array(X)

        if isinstance(self.n_bins, str) and self.n_bins.lower() == "auto":
            outlier_scores = _calculate_outlier_scores_auto(X, self.bin_edges_,
                                                            self.hist_,
                                                            self.alpha,
                                                            self.tol)
        elif check_parameter(self.n_bins, low=2, high=np.inf):
            outlier_scores = _calculate_outlier_scores(X, self.bin_edges_,
                                                       self.hist_,
                                                       self.n_bins,
                                                       self.alpha, self.tol)
        return invert_order(np.sum(outlier_scores, axis=1))


# @njit #due to variable size of histograms, can no longer naively use numba for jit
def _calculate_outlier_scores_auto(X, bin_edges, hist, alpha,
                                   tol):  # pragma: no cover
    """The internal function to calculate the outlier scores based on
    the bins and histograms constructed with the training data. The program
    is optimized through numba. It is excluded from coverage test for
    eliminating the redundancy.

    Parameters
    ----------
    X : numpy array of shape (n_samples, n_features
        The input samples.

    bin_edges : list of length n_features containing numpy arrays
        The edges of the bins.

    hist : =list of length n_features containing numpy arrays
        The density of each histogram.

    alpha : float in (0, 1)
        The regularizer for preventing overflow.

    tol : float in (0, 1)
        The parameter to decide the flexibility while dealing
        the samples falling outside the bins.

    Returns
    -------
    outlier_scores : numpy array of shape (n_samples, n_features)
        Outlier scores on all features (dimensions).
    """

    n_samples, n_features = X.shape[0], X.shape[1]
    outlier_scores = np.zeros(shape=(n_samples, n_features))

    for i in range(n_features):

        # Find the indices of the bins to which each value belongs.
        # See documentation for np.digitize since it is tricky
        # >>> x = np.array([0.2, 6.4, 3.0, 1.6, -1, 100, 10])
        # >>> bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])
        # >>> np.digitize(x, bins, right=True)
        # array([1, 4, 3, 2, 0, 5, 4], dtype=int64)

        bin_inds = np.digitize(X[:, i], bin_edges[i], right=True)

        # Calculate the outlying scores on dimension i
        # Add a regularizer for preventing overflow
        out_score_i = np.log2(hist[i] + alpha)

        optimal_n_bins = get_optimal_n_bins(X[:, i])

        for j in range(n_samples):

            # If the sample does not belong to any bins
            # bin_ind == 0 (fall outside since it is too small)
            if bin_inds[j] == 0:
                dist = bin_edges[i][0] - X[j, i]
                bin_width = bin_edges[i][1] - bin_edges[i][0]

                # If it is only slightly lower than the smallest bin edge
                # assign it to bin 1
                if dist <= bin_width * tol:
                    outlier_scores[j, i] = out_score_i[0]
                else:
                    outlier_scores[j, i] = np.min(out_score_i)

            # If the sample does not belong to any bins
            # bin_ind == optimal_n_bins+1 (fall outside since it is too large)
            elif bin_inds[j] == optimal_n_bins + 1:
                dist = X[j, i] - bin_edges[i][-1]
                bin_width = bin_edges[i][-1] - bin_edges[i][-2]

                # If it is only slightly larger than the largest bin edge
                # assign it to the last bin
                if dist <= bin_width * tol:
                    outlier_scores[j, i] = out_score_i[optimal_n_bins - 1]
                else:
                    outlier_scores[j, i] = np.min(out_score_i)
            else:
                outlier_scores[j, i] = out_score_i[bin_inds[j] - 1]

    return outlier_scores


@njit
def _calculate_outlier_scores(X, bin_edges, hist, n_bins, alpha,
                              tol):  # pragma: no cover
    """The internal function to calculate the outlier scores based on
    the bins and histograms constructed with the training data. The program
    is optimized through numba. It is excluded from coverage test for
    eliminating the redundancy.

    Parameters
    ----------
    X : numpy array of shape (n_samples, n_features)
        The input samples.

    bin_edges : numpy array of shape (n_bins + 1, n_features )
        The edges of the bins.

    hist : numpy array of shape (n_bins, n_features)
        The density of each histogram.

    n_bins : int
        The number of bins. 

    alpha : float in (0, 1)
        The regularizer for preventing overflow.

    tol : float in (0, 1)
        The parameter to decide the flexibility while dealing
        the samples falling outside the bins.

    Returns
    -------
    outlier_scores : numpy array of shape (n_samples, n_features)
        Outlier scores on all features (dimensions).
    """

    n_samples, n_features = X.shape[0], X.shape[1]
    outlier_scores = np.zeros(shape=(n_samples, n_features))

    for i in range(n_features):

        # Find the indices of the bins to which each value belongs.
        # See documentation for np.digitize since it is tricky
        # >>> x = np.array([0.2, 6.4, 3.0, 1.6, -1, 100, 10])
        # >>> bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])
        # >>> np.digitize(x, bins, right=True)
        # array([1, 4, 3, 2, 0, 5, 4], dtype=int64)

        bin_inds = np.digitize(X[:, i], bin_edges[:, i], right=True)

        # Calculate the outlying scores on dimension i
        # Add a regularizer for preventing overflow
        out_score_i = np.log2(hist[:, i] + alpha)

        for j in range(n_samples):

            # If the sample does not belong to any bins
            # bin_ind == 0 (fall outside since it is too small)
            if bin_inds[j] == 0:
                dist = bin_edges[0, i] - X[j, i]
                bin_width = bin_edges[1, i] - bin_edges[0, i]

                # If it is only slightly lower than the smallest bin edge
                # assign it to bin 1
                if dist <= bin_width * tol:
                    outlier_scores[j, i] = out_score_i[0]
                else:
                    outlier_scores[j, i] = np.min(out_score_i)

            # If the sample does not belong to any bins
            # bin_ind == n_bins+1 (fall outside since it is too large)
            elif bin_inds[j] == n_bins + 1:
                dist = X[j, i] - bin_edges[-1, i]
                bin_width = bin_edges[-1, i] - bin_edges[-2, i]

                # If it is only slightly larger than the largest bin edge
                # assign it to the last bin
                if dist <= bin_width * tol:
                    outlier_scores[j, i] = out_score_i[n_bins - 1]
                else:
                    outlier_scores[j, i] = np.min(out_score_i)
            else:
                outlier_scores[j, i] = out_score_i[bin_inds[j] - 1]

    return outlier_scores
