from typing import List, Optional

import numpy as np
import pandas as pd
import plotly.express as px

from FastExplain.utils import COLOURS, is_ebm, is_rf


def plot_feature_importance(
    m: type,
    xs: pd.DataFrame,
    feature_highlights: list = [],
    limit: int = 10,
    plotsize: Optional[List[int]] = None,
):
    """
    Plot feature importance for for Random Forest, XGBoost or Explainable Boosting Machine

    Args:
        m (type):
            Trained model
        xs (pd.DataFrame):
            Dataframe used by model to predict.
        feature_highlights (list, optional):
            List of features to highlight on plot. Defaults to [].
        limit (int, optional):
            Limit to the most important features. Defaults to 10.
        plotsize (Optional[List[int]], optional):
            Custom plotsize supplied as (width, height). Defaults to None.

    """

    df = _get_feature_importance_df(m, xs)
    df = df.sort_values("Importance")
    df = df[-1 * limit :]
    plot_dict = {"x": "Importance", "y": "Feature", "orientation": "h"}

    if "Error" in df.columns:
        plot_dict["error_x"] = "Error"

    fig = px.bar(df, **plot_dict)

    if len(feature_highlights) > 0:
        colour = df.apply(
            lambda x: COLOURS["blue"]
            if x["Feature"] in feature_highlights
            else COLOURS["grey"],
            axis=1,
        )
    else:
        colour = COLOURS["blue"]

    fig.update_traces(marker=dict(color=colour))
    if plotsize:
        fig.update_layout(
            width=plotsize[0],
            height=plotsize[1],
        )
    fig.update_layout(plot_bgcolor="white")

    return fig


def _get_feature_importance_df(m, xs):
    """Base function for getting feature importance. Only works for Random Forest, XGBoost and Explainable Boosting Machine"""

    if is_ebm(m):
        df_dict = {
            "Feature": m.explain_global().data()["names"],
            "Importance": m.explain_global().data()["scores"],
        }
    else:
        df_dict = {
            "Feature": xs.columns,
            "Importance": m.feature_importances_,
        }

    if is_rf(m):
        df_dict["Error"] = np.std(
            [tree.feature_importances_ for tree in m.estimators_], axis=0
        )

    return pd.DataFrame(df_dict)


class Importance:
    def __init__(self, m, xs):
        self.m = m
        self.xs = xs

    def plot_feature_importance(self, *args, **kwargs):
        return plot_feature_importance(self.m, self.xs, *args, **kwargs)
