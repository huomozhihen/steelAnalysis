"""
Time: 2019-07-10
Description: 进行机械数据处理
"""

import pandas as pd
from config import path_config


def machinery_year_on_year_data():
    # 获取机械同比数据
    # 返回值：dataFrame
    #       时间：2013-01至2019-03
    #       属性：  产量:金属切削机床:同比增长（月）
    #               产量:发电设备:同比增长（月）
    #               产量:铁路机车:同比增长（月）
    #               产量:民用钢质船舶:同比增长（月）
    #               产量:电工仪器仪表:同比增长（月）
    config = path_config.GlobalConfig()
    data_path = config.machinery_year_on_year_data
    machinery_year_on_year_df = pd.read_excel(data_path)
    machinery_year_on_year_df.set_index('时间', inplace=True)
    return machinery_year_on_year_df[
               ['产量:金属切削机床:同比增长（月）', '产量:发电设备:同比增长（月）',
                '产量:铁路机车:同比增长（月）', '产量:民用钢质船舶:同比增长（月）',
                '产量:电工仪器仪表:同比增长（月）']].loc['2013-01':'2019-03']


def machinery_cumulative_year_on_year_data():
    # 获取机械累计同比数据
    # 返回值：dataFrame
    #       时间：2012-01至2019-03
    #       属性：  产量:金属切削机床:累计同比（月）
    #               产量:发电设备:累计同比（月）
    #               产量:铁路机车:累计同比（月）
    #               产量:民用钢质船舶:累计同比（月）
    #               产量:电工仪器仪表:累计同比（月）
    config = path_config.GlobalConfig()
    data_path = config.machinery_year_on_year_data
    machinery_cumulative_year_on_year_df = pd.read_excel(data_path)
    machinery_cumulative_year_on_year_df.set_index('时间', inplace=True)
    return machinery_cumulative_year_on_year_df[
               ['产量:金属切削机床:累计同比（月）', '产量:发电设备:累计同比（月）',
                '产量:铁路机车:累计同比（月）', '产量:民用钢质船舶:累计同比（月）',
                '产量:电工仪器仪表:累计同比（月）']].loc['2013-01':'2019-03']


if __name__ == '__main__':
    print(machinery_cumulative_year_on_year_data())
    pass
