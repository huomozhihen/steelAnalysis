"""
Time: 2019-07-10
Description: 进行基建数据处理
"""

import pandas as pd
from config import global_config


def infrastructure_cumulative_year_on_year_data():
    # 获取基建累计同比数据
    # 返回值：dataFrame
    #       时间：2012-01至2019-03
    #       属性：  固定资产投资完成额:累计同比
    #               固定资产投资完成额:基础设施建设投资:累计同比
    config = global_config.GlobalConfig()
    data_path = config.infrastructure_year_on_year_data
    estate_year_on_year_df = pd.read_excel(data_path)
    return estate_year_on_year_df[['固定资产投资完成额:累计同比', '固定资产投资完成额:基础设施建设投资:累计同比']].loc[:86].reset_index(drop=True)


if __name__ == '__main__':
    pass
