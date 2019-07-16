"""
Time: 2019-7-5
Description: 进行钢铁需求数据处理
"""

import pandas as pd
from config import global_config


class SteelDemand:
    def __init__(self, path_config=global_config.PathConfig(), param_config=global_config.ParamConfig()):
        self.path_config = path_config
        self.param_config = param_config

    def cal_steel_demand_year_on_year(self):
        # 计算钢铁需求同比增长、累计同比增长
        steel_demand_data_path = self.path_config.steel_demand_data
        steel_demand_df = pd.read_excel(steel_demand_data_path)
        steel_demand_df.index.name = '时间'
        steel_demand_df.reset_index(inplace=True)
        steel_demand_array = steel_demand_df['表观需求（万吨）'].values
        steel_demand_cumulative_array = steel_demand_df['累计表观需求（万吨）'].values

        steel_demand_year_on_year_list = []
        steel_demand_cumulative_year_on_year_list = []
        for i in range(len(steel_demand_array)):
            if i < 12:
                steel_demand_year_on_year_list.append(None)
                steel_demand_cumulative_year_on_year_list.append(None)
            else:
                steel_demand_year_on_year_list.append(
                    (steel_demand_array[i] - steel_demand_array[i - 12]) / steel_demand_array[i - 12] * 100)
                steel_demand_cumulative_year_on_year_list.append(
                    (steel_demand_cumulative_array[i] - steel_demand_cumulative_array[i - 12])
                    / steel_demand_cumulative_array[i - 12] * 100)
        steel_demand_df['同比增长'] = pd.Series(steel_demand_year_on_year_list)
        steel_demand_df['累计同比增长'] = pd.Series(steel_demand_cumulative_year_on_year_list)

        steel_demand_df.to_excel(self.path_config.steel_demand_year_on_year_data,
                                 header=True, index=False, float_format=None)

    def steel_demand_year_on_year_data(self):
        # 获取钢铁需求同比数据
        # 返回值： dataFrame
        #       属性：需求同比数据
        steel_demand_year_on_year_df = pd.read_excel(self.path_config.steel_demand_year_on_year_data)
        steel_demand_year_on_year_df.set_index('时间', inplace=True)
        return steel_demand_year_on_year_df[['同比增长']].loc[self.param_config.begin_time:self.param_config.end_time]

    def steel_demand_cumulative_year_on_year_data(self):
        # 获取钢铁需求累计同比数据
        # 返回值： dataFrame
        #       属性：累计需求同比数据
        steel_demand_cumulative_year_on_year_df = pd.read_excel(self.path_config.steel_demand_year_on_year_data)
        steel_demand_cumulative_year_on_year_df.set_index('时间', inplace=True)
        return steel_demand_cumulative_year_on_year_df[['累计同比增长']].loc[
               self.param_config.begin_time:self.param_config.end_time]

    def steel_demand_data(self):
        # 获取钢铁需求数据
        # 返回值： dataFrame
        #       属性：需求数据
        steel_demand_df = pd.read_excel(self.path_config.steel_demand_year_on_year_data)
        steel_demand_df.set_index('时间', inplace=True)
        return steel_demand_df[['表观需求（万吨）']].loc[self.param_config.begin_time:self.param_config.end_time]

    def steel_demand_cumulative_data(self):
        # 获取钢铁累计需求数据
        # 返回值： dataFrame
        #       属性：累计需求数据
        steel_demand_cumulative_df = pd.read_excel(self.path_config.steel_demand_year_on_year_data)
        steel_demand_cumulative_df.set_index('时间', inplace=True)
        return steel_demand_cumulative_df[['累计表观需求（万吨）']].loc[self.param_config.begin_time:self.param_config.end_time]


if __name__ == '__main__':
    SteelDemand.cal_steel_demand_year_on_year()
