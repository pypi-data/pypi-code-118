
__all__ = ["DLRegressionExperiments"]

import os

from ._main import Experiments
from ai4water import Model
from ai4water.hyperopt import Integer, Real, Categorical
from ai4water.utils.utils import dateandtime_now
from ai4water.models import MLP, CNN, LSTM, CNNLSTM, LSTMAutoEncoder, TFT


class DLRegressionExperiments(Experiments):
    """
    a framework for comparing several basic DL architectures for a given data.

    To check the available models
    >>> exp = DLRegressionExperiments(...)
    >>> exp.models

    If learning rate, batch size, and lookback are are to be optimzied,
    their space can be specified in the following way:
    >>> exp = DLRegressionExperiments(...)
    >>> exp.lookback_space = [Integer(1, 100, name='lookback')]

    Example
    -------
    >>> from ai4water.experiments import DLRegressionExperiments
    >>> from ai4water.datasets import busan_beach
    >>> data = busan_beach()
    >>> exp = DLRegressionExperiments(
    >>> input_features = data.columns.tolist()[0:-1],
    >>> output_features = data.columns.tolist()[-1:],
    >>> epochs=300,
    >>> train_fraction=1.0,
    >>> y_transformation="log",
    >>> x_transformation="minmax",
    >>> )

    >>> exp.fit(data=data)

    """
    def __init__(
            self,
            input_features:list,
            param_space=None,
            x0=None,
            cases: dict = None,
            exp_name: str = None,
            num_samples: int = 5,
            verbosity: int = 1,
            **model_kws):
        """initializes the experiment."""
        self.input_features = input_features
        self.param_space = param_space
        self.x0 = x0
        self.model_kws = model_kws

        self.lookback_space = []
        self.batch_size_space = Categorical(categories=[4, 8, 12, 16, 32],
                                            name="batch_size")
        self.lr_space = Real(1e-5, 0.005, name="lr")

        exp_name = exp_name or 'DLExperiments' + f'_{dateandtime_now()}'

        super().__init__(cases=cases,
                         exp_name=exp_name,
                         num_samples=num_samples,
                         verbosity=verbosity)

    @property
    def input_shape(self)->tuple:
        features = len(self.input_features)
        shape = features,
        if "ts_args" in self.model_kws:
            if "lookback" in self.model_kws['ts_args']:
                shape = self.model_kws['ts_args']['lookback'], features

        return shape

    @property
    def lookback_space(self):
        return self._lookback_space
    
    @lookback_space.setter
    def lookback_space(self, space):
        self._lookback_space = space

    @property
    def batch_size_space(self):
        return self._batch_size_space
    
    @batch_size_space.setter
    def batch_size_space(self, bs_space):
        self._batch_size_space = bs_space

    @property
    def lr_space(self):
        return self._lr_space
    
    @lr_space.setter
    def lr_space(self, lr_space):
        self._lr_space = lr_space

    @property
    def static_space(self):
        _space = []
        if self.lookback_space:
            _space.append(self.lookback_space)
        if self.batch_size_space:
            _space.append(self.batch_size_space)
        if self.lr_space:
            _space.append(self.lr_space)
        return _space

    @property
    def static_x0(self):
        _x0 = []
        if self.lookback_space:
            _x0.append(self.model_kws.get('lookback', 5))
        if self.batch_size_space:
            _x0.append(self.model_kws.get('batch_size', 32))
        if self.lr_space:
            _x0.append(self.model_kws.get('lr', 0.001))
        return _x0

    @property
    def mode(self):
        return "regression"

    @property
    def tpot_estimator(self):
        return None

    def build_from_config(self, data, config_path, weight_file, **kwargs):

        model = Model.from_config_file(config_path=config_path)
        weight_file = os.path.join(model.w_path, weight_file)
        model.update_weights(weight_file=weight_file)

        test_true, test_pred = model.predict(data=data, return_true=True)

        train_true, train_pred = model.predict(data='training', return_true=True)

        setattr(self, 'model_', model)

        return (train_true, train_pred), (test_true, test_pred)

    def model_MLP(self, **kwargs):
        """multi-layer perceptron model"""

        self.param_space = [
            Integer(8, 128, name="units"),
            Categorical([1,2,3], name="num_layers"),
            Real(0.0, 0.4, name="dropout"),
            Categorical(["relu", "linear", "leakyrelu", "elu", "tanh", "sigmoid"],
                        name="activation")
        ] + self.static_space

        self.x0 = [32, 1, 0.0, "relu"] + self.static_x0

        return {'model': MLP(input_shape=self.input_shape,
                              **kwargs)}

    def model_LSTM(self, **kwargs):
        self.param_space = [
            Integer(8, 128, name="units"),
            Categorical([1, 2, 3], name="num_layers"),
            Real(0.0, 0.4, name="dropout"),
            Categorical(["relu",  "leakyrelu", "elu", "tanh", "sigmoid"],
                        name="activation")
        ] + self.static_space

        self.x0 = [32, 1, 0.0, "relu"] + self.static_x0
        return {'model': LSTM(input_shape=self.input_shape,
                              **kwargs)}

    def model_CNN(self, **kwargs):
        self.param_space = [
            Integer(8, 128, name="filters"),
            Categorical([2,3,4,5], name="kernel_size"),
            Categorical([1, 2, 3], name="num_layers"),
            Real(0.0, 0.4, name="dropout"),
            Categorical(["relu", "leakyrelu", "elu", "tanh", "sigmoid"],
                        name="activation")
        ] + self.static_space

        self.x0 = [32, 2, 1, 0.0, "relu"] + self.static_x0
        return {'model': CNN(input_shape=self.input_shape,
                              **kwargs)}

    def model_CNNLSTM(self, **kwargs):
        """CNN-LSTM model"""

        self.param_space = [
            Categorical([1,2,3], name="cnn_layers"),
            Categorical([1, 2, 3], name="lstm_layers"),
            Integer(8, 128, name="units"),
            Integer(8, 128, name="filters"),
            Categorical([2,3,4,5], name="kernel_size")
        ] + self.static_space

        self.x0 = [2, 1, 32, 32, 2] + self.static_x0

        return {'model': CNNLSTM(
            input_shape=self.input_shape,
            **kwargs)
        }

    def model_LSTMAutoEncoder(self, **kwargs):
        """LSTM based auto-encoder model."""

        self.param_space = [
            Integer(8, 128, name="encoder_units"),
            Integer(8, 128, name="decoder_units"),
            Categorical([1,2,3], name="encoder_layers"),
            Categorical([1,2,3], name="decoder_layers"),
        ] + self.static_space

        self.x0 = [32, 32, 1, 1] + self.static_x0

        return {'model': LSTMAutoEncoder(
            input_shape=self.input_shape,
            **kwargs)
        }

    def model_TCN(self, **kwargs):
        """Temporal Convolution network based model."""

        self.param_space = [
            Integer(8, 128, name="filters"),
            Categorical([1,2,3], name="kernel_size"),
        ] + self.static_space

        self.x0 = [32, 2] + self.static_x0

        return {'model': LSTMAutoEncoder(
            input_shape=self.input_shape,
            **kwargs)
        }

    def model_TemporalFusionTransformer(self, **kwargs):
        """temporal fusion transformer model."""

        self.param_space = [
            Integer(16, 128, name="hidden_units"),
            Categorical([1,2,3,4,5], name="num_heads")
        ] + self.static_space

        self.x0 = [64, 2]

        return {'model': TFT(
            input_shape=self.input_shape,
            **kwargs)
        }