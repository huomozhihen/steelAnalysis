"""
Time: 2019-07-10
Description: 进行基建数据处理
"""

import pandas as pd
from config import global_config


class Infrastruture:

    def __init__(self, path_config=global_config.PathConfig(), param_config=global_config.ParamConfig()):
        self.path_config = path_config
        self.param_config = param_config

    def infrastructure_cumulative_year_on_year_data(self):
        # 获取基建累计同比数据
        # 返回值：dataFrame
        #       属性：  固定资产投资完成额:累计同比
        #               固定资产投资完成额:基础设施建设投资:累计同比
        data_path = self.path_config.infrastructure_year_on_year_data
        infrastructure_cumulative_year_on_year_df = pd.read_excel(data_path)
        infrastructure_cumulative_year_on_year_df.set_index('时间', inplace=True)
        if self.param_config.begin_time >= '2014-01':
            return infrastructure_cumulative_year_on_year_df[
                       ['固定资产投资完成额:累计同比', '固定资产投资完成额:基础设施建设投资:累计同比', '固定资产投资完成额:基础设施建设投资(不含电力):累计同比']].loc[
                   self.param_config.begin_time:self.param_config.end_time]
        else:
            return infrastructure_cumulative_year_on_year_df[['固定资产投资完成额:累计同比', '固定资产投资完成额:基础设施建设投资:累计同比']].loc[
                   self.param_config.begin_time:self.param_config.end_time]


if __name__ == '__main__':
    pass
