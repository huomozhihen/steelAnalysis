"""
Time： 2019-7-12
Description： 极端随机森林回归
"""

from model.com_mod import model_method
from sklearn.tree import ExtraTreeRegressor


def extra_tree_regression():
    train_attr, train_label, test_attr, test_label = model_method.load_data()

    model = ExtraTreeRegressor(random_state=0)
    model.fit(train_attr, train_label)

    model_method.result_analysis(train_attr, train_label, test_attr, test_label, model)


if __name__ == '__main__':
    extra_tree_regression()
