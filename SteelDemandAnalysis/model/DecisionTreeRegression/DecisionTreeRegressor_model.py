"""
Time： 2019-7-12
Description： 决策树回归
"""

from model.com_mod import model_method, data_partitioning
from sklearn import tree
from data_process.feature import feature_correlation_analysis
from data_process.feature import data_coversion
from config import global_config
from sklearn.model_selection import GridSearchCV


class MyDecisionTreeRegression:
    def __init__(self):
        self.max_depth = 3
        self.min_samples_leaf = 2
        self.min_samples_split = 3

    def decision_tree_regression(self, train_attr, train_label):
        model = tree.DecisionTreeRegressor(max_depth=self.max_depth, min_samples_leaf=self.min_samples_leaf,
                                           min_samples_split=self.min_samples_split)
        model.fit(train_attr, train_label)

        return model

    def param_adjust(self, train_attr, train_label):
        cv_params = {'max_depth': [1, 2, 3, 4, 5, 6, 7, 8],
                     'min_samples_leaf': [1, 2, 3, 4, 5, 6, 7, 8],
                     'min_samples_split': [2, 3, 4, 5, 6, 7, 8],
                     }
        other_params = {'max_depth': 1,
                        # 'min_samples_split': 2,
                        # 'min_samples_leaf': 1,
                        }

        model = tree.DecisionTreeRegressor(**other_params)
        optimized_GBM = GridSearchCV(estimator=model, param_grid=cv_params, scoring='neg_mean_squared_error', cv=10,
                                     verbose=1, n_jobs=2)
        optimized_GBM.fit(train_attr, train_label)
        cv_result = optimized_GBM.cv_results_
        print('运行结果:{0}'.format(cv_result))
        print('参数的最佳取值：{0}'.format(optimized_GBM.best_params_))
        print('最佳模型得分:{0}'.format(optimized_GBM.best_score_))


if __name__ == '__main__':
    pass
