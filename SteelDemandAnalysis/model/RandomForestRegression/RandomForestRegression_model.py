"""
Time： 2019-7-12
Description： 随机森林回归
"""

from model.com_mod import model_method
from sklearn import ensemble


def random_forest_regression():
    train_attr, train_label, test_attr, test_label = model_method.load_data()

    model = ensemble.RandomForestRegressor()
    model.fit(train_attr, train_label)

    model_method.result_analysis(train_attr, train_label, test_attr, test_label, model)


if __name__ == '__main__':
    random_forest_regression()
