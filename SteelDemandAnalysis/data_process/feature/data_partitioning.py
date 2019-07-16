"""
Time: 2019-7-11
Description: 数据集划分
"""

from config import global_config
import pandas as pd


class DataPartition:
    def __init__(self, path_config=global_config.PathConfig(), param_config=global_config.ParamConfig()):
        self.path_config = path_config
        self.param_config = param_config

    def divide_data(self, initial_data):
        # 划分训练集与测试集
        # 输入：
        #       initial_data：全部数据dataFrame
        train_data = initial_data[0:-self.param_config.test_period]
        test_data = initial_data[-self.param_config.test_period:]
        train_data.to_csv(self.path_config.train_data, sep=',', header=True, index=True)
        test_data.to_csv(self.path_config.test_data, sep=',', header=True, index=True)
        return

    def data_partitioning(self):
        f = open(self.path_config.converted_model_data)
        # f = open(path_config.initial_model_data)
        all_data_df = pd.read_csv(f, header=0, index_col=0)
        self.divide_data(all_data_df)


if __name__ == '__main__':
    DataPartition().data_partitioning()
