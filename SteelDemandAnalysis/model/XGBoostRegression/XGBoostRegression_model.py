"""
Time： 2019-7-12
Description： XGBoost回归
"""

from model.com_mod import model_method
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
from xgboost import plot_importance


def XGBoost_regression():
    train_attr, train_label, test_attr, test_label = model_method.load_data()

    model = XGBRegressor()
    model.fit(train_attr, train_label)

    # fig, ax = plt.subplots(figsize=(10, 15))
    # plot_importance(model, height=0.5, max_num_features=64, ax=ax)
    # plt.show()

    model_method.result_analysis(train_attr, train_label, test_attr, test_label, model)


if __name__ == '__main__':
    XGBoost_regression()
