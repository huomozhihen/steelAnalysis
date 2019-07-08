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

    def __init__(self):
        pass
