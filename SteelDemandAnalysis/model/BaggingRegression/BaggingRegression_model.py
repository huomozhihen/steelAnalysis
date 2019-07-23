"""
Time： 2019-7-12
Description： Bagging回归
"""

from model.com_mod import model_method, data_partitioning
from sklearn import ensemble
from data_process.feature import feature_correlation_analysis
from data_process.feature import data_coversion
from config import global_config


class MyBaggingRegression:
    def __init__(self):
        self.base_estimator = None
        self.n_estimators = 100
        self.max_samples = 1.0
        self.max_features = 1.0

    def Bagging_regression(self, train_attr, train_label):
        model = ensemble.BaggingRegressor(base_estimator=self.base_estimator, n_estimators=self.n_estimators,
                                          max_samples=self.max_samples, max_features=self.max_features)
        model.fit(train_attr, train_label)

        return model


if __name__ == '__main__':
    pass
