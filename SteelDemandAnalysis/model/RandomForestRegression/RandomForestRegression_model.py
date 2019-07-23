"""
Time： 2019-7-12
Description： 随机森林回归
"""

from model.com_mod import model_method, data_partitioning
from sklearn import ensemble
from config import global_config
from data_process.feature import feature_correlation_analysis
from data_process.feature import data_coversion


class MyRandomForestRegression:
    def __init__(self):
        self.n_estimators = 100
        self.max_depth = None
        self.min_samples_split = 2
        self.min_samples_leaf = 1

    def random_forest_regression(self, train_attr, train_label):

        model = ensemble.RandomForestRegressor(n_estimators=self.n_estimators, max_depth=self.max_depth,
                                               min_samples_split=self.min_samples_split,
                                               min_samples_leaf=self.min_samples_leaf)
        model.fit(train_attr, train_label)
        return model


if __name__ == '__main__':
    pass
