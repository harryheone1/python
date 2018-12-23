import csv
import os
import numpy as np
import config

def load_data(data_file, usecols):
    """
        读取数据文件，加载数据
        参数：
            - data_file:    文件路径
            - usecols:      所使用的列
        返回：
            - data_arr:     数据的多维数组表示
    """
    data = []
    with open(data_file, 'r') as csvfile:
        data_reader = csv.DictReader(csvfile)
        # === Step 2. 数据处理 ===
        for row in data_reader:
            # 取出每行数据，组合为一个列表放入数据列表中
            row_data = []
            # 注意csv模块读入的数据全部为字符串类型
            # filter column
            for col in usecols:
                str_val = row[col]
                row_data.append(float(str_val) if str_val != 'NA' else np.nan)
            # filter data
            if not any(np.isnan(row_data)):
                # 二维list 类似二维数组
                data.append(row_data)

    # 将data转换为ndarray
    data_arr = np.array(data)
    return data_arr

def get_avg_pm_per_season(data_arr):
    """
        获取每个区每月的平均PM值
        参数：
            - data_arr: 数据的多维数组表示
        返回：
            - results_arr:  多维数组结果
    """
    results = []

    # 获取年份
    years = np.unique(data_arr[:, 0])
    for year in years:
        # 获取当前年份数据
        year_data_arr = data_arr[data_arr[:, 0] == year]
        season_list = np.unique(year_data_arr[:, 2])

        for season in season_list:
            season_data_arr = year_data_arr[year_data_arr[:, 2] == season]
            mean_val = np.mean(season_data_arr[:, 3:], axis=0).tolist()

            row_data = ['{}-{}'.format(year, season)] + mean_val
            results.append(row_data)
    results_arr = np.array(results)
    return results_arr


def main():
    """
        主函数
    """
    for city_name, (filename, cols) in config.data_config_dict.items():
        data_file = os.path.join(config.dataset_path, filename)
        # list merge
        usecols = config.common_cols + config.season_cols + ['PM_' + col for col in cols]
        data_arr = load_data(data_file, usecols)

        print('{}共有{}行有效数据'.format(city_name, data_arr.shape[0]))
        # 预览前10行数据
        print('{}的前10行数据：'.format(city_name))
        print(data_arr[:10])

        results_arr = get_avg_pm_per_season(data_arr)
        print('{}的每月平均PM值预览：'.format(city_name))
        print(results_arr[:10])

if __name__ == '__main__':
    main()