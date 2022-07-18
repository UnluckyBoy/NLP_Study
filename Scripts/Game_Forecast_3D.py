# -*- coding: utf-8 -*-
# @Time : 2022/7/18 0018 16:08
# @Author : Matrix
# @File : Game_Forecast_3D.py
# @Software: PyCharm
import argparse
import pandas as pd


def DoForecast(file_path,column):
    """获取csv文件内容并返回
    :param file_path: 文件地址,类型为str
    :param column: 要查询的列数,类型为int
    :return: 返回的list值,result为返回结果list
    """
    file = pd.read_csv(file_path, header=None, encoding='utf-8')
    index = len(file)
    num=file.iloc[:,column]
    result=[]
    for i in range(index):
        result.append(num[i])
        if i == index - 1:  #检测是否最后一个，是则跳过。
            break
            pass
        pass

    return result
    pass

def main(args):
    """定义储存三个数的数组"""
    result_num_01 =DoForecast(args.file_path,0)
    result_num_02 =DoForecast(args.file_path,1)
    result_num_03 =DoForecast(args.file_path,2)
    print("获取结果_result_num_01:" + str(result_num_01)
          +"\nresult_num_02:"+str(result_num_02)+"\nresult_num_03:"+str(result_num_03))
    pass

if __name__=='__main__':
    #file_dir = r"./work.csv"
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str,default='./work.csv',help='csv文件地址')
    args = parser.parse_args()
    main(args)