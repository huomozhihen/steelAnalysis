"""
Time: 2019-7-5
Description: 进行宏观数据处理
"""

import pandas as pd
from config import global_config


class Macro:
    def __init__(self, path_config=global_config.PathConfig(), param_config=global_config.ParamConfig()):
        self.path_config = path_config
        self.param_config = param_config


    def BDI_data(self):
        # 获取波罗的海干散货运价指数数据
        # 返回值：dataFrame
        #       属性：  BDI
        data_path = self.path_config.BDI_data
        BDI_df = pd.read_excel(data_path)
        BDI_df.set_index('时间', inplace=True)
        return BDI_df[['BDI']].loc[self.param_config.begin_time:self.param_config.end_time]


    def PMI_data(self):
        # 获取采购经理指数数据
        # 返回值：dataFrame
        #       属性：  PMI（月）
        #               PMI:新订单（月）
        data_path = self.path_config.macro_year_on_year_data
        PMI_df = pd.read_excel(data_path)
        PMI_df.set_index('时间', inplace=True)
        return PMI_df[['PMI（月）', 'PMI:新订单（月）']].loc[self.param_config.begin_time:self.param_config.end_time]

    def macro_year_on_year_data(self):
        # 获取宏观同比数据
        # 返回值：dataFrame
        #       属性：  社会消费品零售总额:当月同比（月）
        #               M1:同比（月）
        #               M2:同比（月）
        #               CPI:当月同比（月）
        #               PPI:全部工业品:当月同比（月）
        data_path = self.path_config.macro_year_on_year_data
        macro_year_on_year_df = pd.read_excel(data_path)
        macro_year_on_year_df.set_index('时间', inplace=True)
        return macro_year_on_year_df[
                   ['社会消费品零售总额:当月同比（月）', 'M1:同比（月）',
                    'M2:同比（月）', 'CPI:当月同比（月）',
                    'PPI:全部工业品:当月同比（月）']].loc[self.param_config.begin_time:self.param_config.end_time]

    def macro_cumulative_year_on_year_data(self):
        # 获取宏观累计同比数据
        # 返回值：dataFrame
        #       属性：  社会消费品零售总额:累计同比（月）(整理）
        data_path = self.path_config.macro_year_on_year_data
        macro_cumulative_year_on_year_df = pd.read_excel(data_path)
        macro_cumulative_year_on_year_df.set_index('时间', inplace=True)
        return macro_cumulative_year_on_year_df[
                   ['社会消费品零售总额:累计同比（月）(整理）']].loc[self.param_config.begin_time:self.param_config.end_time]


if __name__ == "__main__":
    pass
