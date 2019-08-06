"""
Time： 2019-7-12
Description： lightGBM回归
"""

from SteelDemandAnalysis.model.com_mod import model_method
import lightgbm as lgb


class MyLightGBM:
    def __init__(self):
        pass

    def lightGBM_regression(self, train_attr, train_label):
        model = lgb.LGBMRegressor()
        model.fit(train_attr, train_label)

        return model


if __name__ == '__main__':
    pass
