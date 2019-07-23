"""
Time： 2019-7-12
Description： AdaBoost回归
"""

from sklearn import ensemble


class MyAdaBoostRegression:
    def __init__(self):
        self.base_estimator = None,
        self.n_estimators = 50,
        self.learning_rate = 1.,

    def AdaBoost_regression(self, train_attr, train_label):
        model = ensemble.AdaBoostRegressor(base_estimator=self.base_estimator, n_estimators=self.n_estimators,
                                           learning_rate=self.learning_rate)
        model.fit(train_attr, train_label)

        return model


if __name__ == '__main__':
    pass
