"""
Time： 2019-7-12
Description： AdaBoost回归
"""

from model.com_mod import model_method
from sklearn import ensemble


def AdaBoost_regression():
    train_attr, train_label, test_attr, test_label = model_method.load_data()

    model = ensemble.AdaBoostRegressor()
    model.fit(train_attr, train_label)

    model_method.result_analysis(train_attr, train_label, test_attr, test_label, model)


if __name__ == '__main__':
    AdaBoost_regression()
