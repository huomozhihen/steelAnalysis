"""
Time： 2019-7-12
Description： SVM回归
"""

from SteelDemandAnalysis.model.com_mod import model_method, data_partitioning
from sklearn import svm
from SteelDemandAnalysis.data_process.feature import feature_correlation_analysis
from SteelDemandAnalysis.data_process.feature import data_coversion
from SteelDemandAnalysis.config import global_config
from sklearn.model_selection import GridSearchCV


class MySVMRegression:
    def __init__(self):
        self.C = 1
        self.degree = 10
        self.gamma = 'auto'

    def svm_regression(self, train_attr, train_label):

        model = svm.SVR(C=self.C, degree=self.degree, gamma=self.gamma)
        model.fit(train_attr, train_label)

        return model

    def param_adjust(self, train_attr, train_label):
        cv_params = {'C': [0.1, 0.3, 1, 3, 10, 30, 100],
                     'degree': [1, 2, 3, 4, 5],
                     'gamma': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
                     }
        other_params = {'C': 1,
                        # 'min_samples_split': 2,
                        # 'min_samples_leaf': 1,
                        }

        model = svm.SVR(**other_params)
        optimized_GBM = GridSearchCV(estimator=model, param_grid=cv_params, scoring='neg_mean_squared_error', cv=10,
                                     verbose=1, n_jobs=2)
        optimized_GBM.fit(train_attr, train_label)
        cv_result = optimized_GBM.cv_results_
        print('运行结果:{0}'.format(cv_result))
        print('参数的最佳取值：{0}'.format(optimized_GBM.best_params_))
        print('最佳模型得分:{0}'.format(optimized_GBM.best_score_))


if __name__ == '__main__':
    pass
