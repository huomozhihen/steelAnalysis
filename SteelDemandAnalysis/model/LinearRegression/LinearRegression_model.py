"""
Time： 2019-7-11
Description： 线性回归
"""

from model.com_mod import model_method
from sklearn import linear_model


def linear_regression():
    train_attr, train_label, test_attr, test_label = model_method.load_data()

    model = linear_model.LinearRegression()
    model.fit(train_attr, train_label)

    model_method.result_analysis(train_attr, train_label, test_attr, test_label, model)


if __name__ == '__main__':
    linear_regression()
