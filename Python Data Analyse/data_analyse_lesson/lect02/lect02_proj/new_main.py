# -*- coding: utf-8 -*-

"""
    作者:     Robin
    版本:     1.0
    日期:     2018/02
    文件名:    main.py
    功能：     主程序

    实战案例1-2：中国五大城市PM2.5数据分析 (2)
    任务：
        - 统计每个城市每天的平均PM2.5的数值
        - 基于天数对比中国环保部和美国驻华大使馆统计的污染状态

    数据集来源：https://www.kaggle.com/uciml/pm25-data-for-five-chinese-cities

    声明：小象学院拥有完全知识产权的权利；只限于善意学习者在本课程使用，
         不得在课程范围外向任何第三方散播。任何其他人或机构不得盗版、复制、仿造其中的创意，
         我们将保留一切通过法律手段追究违反者的权利
"""

import os
import pandas as pd
import numpy as np

import config


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    probabilities = list(map(lambda score: np.exp(score), x))
    p_sum = np.sum(probabilities)
    return list(map(lambda prob: prob / p_sum, probabilities))


def main():
    scores = [3.0, 1.0, 0.2]
    result = softmax(scores)
    print(result)



if __name__ == '__main__':
    main()
