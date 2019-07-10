"""
Time: 2019-7-5
Description: 进行钢铁需求数据处理
"""

import pandas as pd
from config import global_config


def cal_steel_demand_year_on_year():
    # 计算钢铁需求同比增长、累计同比增长
    config = global_config.GlobalConfig()

    steel_demand_data_path = config.steel_demand_data
    steel_demand_df = pd.read_excel(steel_demand_data_path, usecols=[6, 7])
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
                (steel_demand_array[i]-steel_demand_array[i-12])/steel_demand_array[i-12] * 100)
            steel_demand_cumulative_year_on_year_list.append(
                (steel_demand_cumulative_array[i] - steel_demand_cumulative_array[i - 12])
                / steel_demand_cumulative_array[i - 12] * 100)
    steel_demand_df['同比增长'] = pd.Series(steel_demand_year_on_year_list)
    steel_demand_df['累计同比增长'] = pd.Series(steel_demand_cumulative_year_on_year_list)

    steel_demand_df.to_excel(config.steel_demand_year_on_year_data,
                           header=True, index=False, float_format=None)


if __name__ == '__main__':
    cal_steel_demand_year_on_year()
