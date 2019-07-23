"""
Time： 2019-7-12
Description： GBRT回归
"""

from model.com_mod import model_method
from sklearn import ensemble


class MyGBRTRegression:
    def __init__(self):
        self.learning_rate = 0.1
        self.n_estimators = 100
        self.subsample = 1.0
        self.min_samples_split = 2
        self.max_depth = 3

    def GBRT_regression(self, train_attr, train_label):
        model = ensemble.GradientBoostingRegressor(learning_rate=self.learning_rate, n_estimators=self.n_estimators,
                                                   subsample=self.subsample, min_samples_leaf=self.min_samples_split,
                                                   max_depth=self.max_depth)
        model.fit(train_attr, train_label)

        return model


if __name__ == '__main__':
    pass
