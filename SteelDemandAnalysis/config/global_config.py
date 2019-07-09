"""
Time： 2019-7-5
Description： 用于数据路径配置
"""
import os


class GlobalConfig:
    basic_data_path = 'E:\\htsc\\行业景气度\\数据\\'   # 数据根目录

    steel_data_path = os.path.join(basic_data_path, '钢铁-需求\\')  # 钢铁-需求
    macro_data_path = os.path.join(basic_data_path, '钢铁-宏观指标\\')  # 钢铁-宏观指标
    infrastructure_data_path = os.path.join(basic_data_path, '钢铁-需求-基建\\')  # 钢铁-需求-基建
    manufacturing_data_path = os.path.join(basic_data_path, '钢铁-需求-制造业\\')  # 钢铁-需求-制造业
    estate_data_path = os.path.join(basic_data_path, '钢铁-需求-房地产\\')  # 钢铁-需求-房地产
    machinery_data_path = os.path.join(basic_data_path, '钢铁-需求-机械\\')  # 钢铁-需求-机械
    homeAppAndCar_data_path = os.path.join(basic_data_path, '钢铁-需求-家电汽车\\')  # 钢铁-需求-家电汽车

    steel_importAndExport_data = os.path.join(steel_data_path, '钢材进出口.xlsx')  # 钢铁进出口数据
    steel_output_data = os.path.join(steel_data_path, '钢材产量.xlsx')  # 钢铁产量数据
    steel_stock_data = os.path.join(steel_data_path, '钢联数据-社会库存&钢厂库存.xls')  # 钢材库存数据
    steel_demand_data = os.path.join(steel_data_path, '表观需求.xlsx')  # 钢材需求数据
    steel_demand_year_on_year_data = os.path.join(steel_data_path, '表观需求同比数据.csv')  # 钢材需求同比数据

    def __init__(self):
        pass
