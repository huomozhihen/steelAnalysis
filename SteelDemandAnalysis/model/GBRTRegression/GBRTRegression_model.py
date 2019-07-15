"""
Time： 2019-7-12
Description： GBRT回归
"""

from model.com_mod import model_method
from sklearn import ensemble


def GBRT_regression():
    train_attr, train_label, test_attr, test_label = model_method.load_data()

    model = ensemble.GradientBoostingRegressor()
    model.fit(train_attr, train_label)

    model_method.result_analysis(train_attr, train_label, test_attr, test_label, model)


if __name__ == '__main__':
    GBRT_regression()
