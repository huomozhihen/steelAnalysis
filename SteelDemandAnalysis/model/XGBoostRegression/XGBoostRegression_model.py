"""
Time： 2019-7-12
Description： XGBoost回归
"""

from SteelDemandAnalysis.model.com_mod import model_method, data_partitioning
from xgboost import XGBRegressor
from SteelDemandAnalysis.data_process.feature import feature_correlation_analysis
from SteelDemandAnalysis.data_process.feature import data_coversion
from SteelDemandAnalysis.config import global_config


class MyXGBoost:
    def __init__(self):
        self.max_depth = 3
        self.learning_rate = 0.1
        self.n_estimators = 100
        self.min_child_weight = 1
        self.subsample = 1
        self.gamma = 0
        self.reg_alpha = 0
        self.reg_lambda = 1

    def XGBoost_regression(self, train_attr, train_label):
        model = XGBRegressor(learning_rate=self.learning_rate, max_depth=self.max_depth, n_estimators=self.n_estimators,
                             min_child_weight=self.min_child_weight, subsample=self.subsample, gamma=self.gamma,
                             reg_alpha=self.reg_alpha, reg_lambda=self.reg_lambda)
        model.fit(train_attr, train_label)

        return model


if __name__ == '__main__':
    pass
