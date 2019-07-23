"""
Time： 2019-7-11
Description： 线性回归
"""

from model.com_mod import model_method, data_partitioning
from sklearn import linear_model


class MyLinearRegression:
    def __init__(self):
        pass

    def linear_regression(self, attr, label):
        model = linear_model.LinearRegression()
        model.fit(attr, label)
        return model

    if __name__ == '__main__':
        pass
