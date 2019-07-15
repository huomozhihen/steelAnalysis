"""
Time: 2019-7-12
Description: 数据集转换
"""

import pandas as pd
import datetime
from config import global_config

path_config = global_config.PathConfig


def add_month_index(old_df):
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


if __name__ == '__main__':
    f = open(path_config.initial_model_data)
    old_data_df = pd.read_csv(f, header=0, index_col=0)
    new_data_df = add_month_index(old_data_df)
    new_data_df.to_csv(path_config.converted_model_data, sep=',', header=True, index=True)
