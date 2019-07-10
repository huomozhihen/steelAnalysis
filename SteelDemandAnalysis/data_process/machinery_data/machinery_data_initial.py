"""
Time: 2019-07-10
Description: 进行机械数据处理
"""

import pandas as pd
from config import global_config


def machinery_year_on_year_data():
    # 获取机械同比数据
    # 返回值：dataFrame
    #       时间：2013-01至2019-03
    #       属性：  产量:金属切削机床:同比增长（月）
    #               产量:发电设备:同比增长（月）
    #               产量:铁路机车:同比增长（月）
    #               产量:民用钢质船舶:同比增长（月）
    #               产量:电工仪器仪表:同比增长（月）
    config = global_config.GlobalConfig()
    data_path = config.machinery_year_on_year_data
    estate_year_on_year_df = pd.read_excel(data_path)
    return estate_year_on_year_df[
               ['产量:金属切削机床:同比增长（月）', '产量:发电设备:同比增长（月）',
                '产量:铁路机车:同比增长（月）', '产量:民用钢质船舶:同比增长（月）',
                '产量:电工仪器仪表:同比增长（月）']].loc[12:86].reset_index(drop=True)


def machinery_cumulative_year_on_year_data():
    # 获取机械累计同比数据
    # 返回值：dataFrame
    #       时间：2012-01至2019-03
    #       属性：  产量:金属切削机床:累计同比（月）
    #               产量:发电设备:累计同比（月）
    #               产量:铁路机车:累计同比（月）
    #               产量:民用钢质船舶:累计同比（月）
    #               产量:电工仪器仪表:累计同比（月）
    config = global_config.GlobalConfig()
    data_path = config.machinery_year_on_year_data
    estate_year_on_year_df = pd.read_excel(data_path)
    return estate_year_on_year_df[
               ['产量:金属切削机床:累计同比（月）', '产量:发电设备:累计同比（月）',
                '产量:铁路机车:累计同比（月）', '产量:民用钢质船舶:累计同比（月）',
                '产量:电工仪器仪表:累计同比（月）']].loc[:86].reset_index(drop=True)


if __name__ == '__main__':
    pass
