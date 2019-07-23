"""
Time: 2019-7-11
Description: 数据集划分
"""

from config import global_config
import pandas as pd
import datetime


class DataPartition:
    def __init__(self, path_config=global_config.PathConfig(), param_config=global_config.ParamConfig()):
        self.path_config = path_config
        self.param_config = param_config

    def divide_data(self, initial_data, x_s=datetime.datetime(2007, 1, 1), x_e=datetime.datetime(2018, 5, 1),
                    y_s=datetime.datetime(2018, 6, 1), y_e=datetime.datetime(2019, 5, 1)):
        # 划分训练集与测试集
        # 输入：
        #       initial_data：全部数据dataFrame
        #       x_s: 训练集起始时间datetime
        #       x_e: 训练集结束时间datetime
        #       y_s: 测试集起始时间datetime
        #       y_s: 测试集结束时间datetime
        # 返回：
        #       train_data: 训练集dataFrame
        #       test_data: 测试集dataFrame
        initial_data.index = pd.to_datetime(initial_data.index)
        train_data = initial_data[(initial_data.index <= x_e) & (initial_data.index >= x_s)]
        test_data = initial_data[(initial_data.index <= y_e) & (initial_data.index >= y_s)]
        return train_data, test_data

    def all_data(self):
        # 读取数据集
        # 返回：
        #       all_data_df: 全部数据dataFrame
        f = open(self.path_config.converted_model_data)
        all_data_df = pd.read_csv(f, header=0, index_col=0)
        return all_data_df


if __name__ == '__main__':
    pass
