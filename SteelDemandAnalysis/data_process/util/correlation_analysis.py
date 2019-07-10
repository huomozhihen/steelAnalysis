"""
Time: 2019-7-9
Description: 相关性分析
"""
import scipy.stats as stats


def cal_r2(array1, array2):
    r, prob = stats.pearsonr(array1, array2)
    return r**2


def best_period(basic_array, variable_array, max_period):
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
    # return period_r2
    return max(period_r2, key=lambda x: period_r2[x])
