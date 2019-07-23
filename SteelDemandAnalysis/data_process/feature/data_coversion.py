"""
Time: 2019-7-12
Description: 数据集转换
"""

import pandas as pd
import datetime
from config import global_config
from sklearn import preprocessing


class DataCoversion:
    def __init__(self, path_config=global_config.PathConfig(), param_config=global_config.ParamConfig()):
        self.path_config = path_config
        self.param_config = param_config

    def add_month_index(self, old_df):
        # 数据集添加月份属性
        # 输入：
        #       old_df: 原数据dataFrame
        # 返回：
        #       new_df: 新数据dataFrame
        col_name = old_df.columns.tolist()
        col_name.insert(-1, 'month_index')
        new_df = old_df.reindex(columns=col_name)
        new_df['month_index'] = new_df.apply(lambda x: pd.to_datetime(x.index).month)

        return new_df

    def scale_handler(self, old_df):
        # min_max特征缩放
        X_df = old_df.ix[:, :-1]
        Y_df = old_df.ix[:, [-1]]
        scaler = preprocessing.StandardScaler()
        X_minmax = scaler.fit_transform(X_df)

        X_minmax_df = pd.DataFrame(X_minmax, index=X_df.index, columns=X_df.columns)
        new_df = pd.concat([X_minmax_df, Y_df], axis=1)

        return new_df

    def data_coversion(self):
        f = open(self.path_config.initial_model_data)
        old_data_df = pd.read_csv(f, header=0, index_col=0)
        new_data_df = old_data_df
        # new_data_df = self.add_month_index(old_data_df)
        # new_data_df = self.scale_handler(old_data_df)
        new_data_df.to_csv(self.path_config.converted_model_data, sep=',', header=True, index=True)


if __name__ == '__main__':
    DataCoversion().data_coversion()
