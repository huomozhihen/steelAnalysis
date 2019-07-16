"""
Time： 2019-7-12
Description： XGBoost回归
"""

from model.com_mod import model_method
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
from xgboost import plot_importance
from sklearn.model_selection import GridSearchCV


def XGBoost_regression():
    train_attr, train_label, test_attr, test_label = model_method.load_data()

    #     cv_params = {'learning_rate': [0.01, 0.03, 0.1, 0.3, 1]}
    #     other_params = {'learning_rate': 0.1,
    #                     'n_estimators': 600,
    #                     'max_depth': 5,
    #                     'min_child_weight': 7,
    #                     'seed': 0,
    #                     'subsample': 0.2,
    #                     'colsample_bytree': 1.0,
    #                     'gamma': 1.0,
    #                     'reg_alpha': 0.3,
    #                     'reg_lambda': 3}
    #
    #     model = XGBRegressor(**other_params)
    #     optimized_GBM = GridSearchCV(estimator=model, param_grid=cv_params, scoring='neg_mean_squared_error', cv=5,
    #                                  verbose=1, n_jobs=2)
    #     optimized_GBM.fit(train_attr, train_label)
    #     cv_result = optimized_GBM.cv_results_
    #     print('运行结果:{0}'.format(cv_result))
    #     print('参数的最佳取值：{0}'.format(optimized_GBM.best_params_))
    #     print('最佳模型得分:{0}'.format(optimized_GBM.best_score_))

    model = XGBRegressor()
    model.fit(train_attr, train_label)

    # fig, ax = plt.subplots(figsize=(10, 15))
    # plot_importance(model, height=0.5, max_num_features=64, ax=ax)
    # plt.show()

    model_method.result_analysis(train_attr, train_label, test_attr, test_label, model)


if __name__ == '__main__':
    XGBoost_regression()
