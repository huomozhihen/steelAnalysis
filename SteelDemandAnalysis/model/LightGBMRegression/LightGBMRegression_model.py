"""
Time： 2019-7-12
Description： lightGBM回归
"""

from model.com_mod import model_method
import lightgbm as lgb


def lightGBM_regression():
    train_attr, train_label, test_attr, test_label = model_method.load_data()

    model = lgb.LGBMRegressor(objective='regression')
    model.fit(train_attr, train_label)

    model_method.result_analysis(train_attr, train_label, test_attr, test_label, model)


if __name__ == '__main__':
    lightGBM_regression()
