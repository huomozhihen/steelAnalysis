"""
Time: 2019-7-9
Description: 相关性分析工具
"""
import scipy.stats as stats


def cal_r2(array1, array2):
    # 计算R2
    r, prob = stats.pearsonr(array1, array2)
    return r**2


def best_period(basic_array, variable_array, max_period):
    # 基于相关系数计算两组数据间最优滞后期数
    # 输入：
    #       basic_array: 用于判断的基数据
    #       variable_array: 变量数据，与基数据等长
    #       max_period： 最大期数
    # 返回：
    #       滞后期数：[-max_period, max_period]
    #       R2：[0, 1]
    period_r2 = {}
    for i in range(-max_period, 0):
        basic_temp = basic_array[:i]
        variable_temp = variable_array[-i:]
        period_r2[i] = cal_r2(basic_temp, variable_temp)
    period_r2[0] = cal_r2(basic_array, variable_array)
    for i in range(1, max_period+1):
        basic_temp = basic_array[i:]
        variable_temp = variable_array[:-i]
        period_r2[i] = cal_r2(basic_temp, variable_temp)
    corr_period = max(period_r2, key=lambda x: period_r2[x])
    # return period_r2
    return corr_period, period_r2[corr_period]
