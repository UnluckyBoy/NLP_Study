# -*- coding: utf-8 -*-
# @Time : 2022/7/18 0018 16:08
# @Author : Matrix
# @File : Game_Forecast_3D.py
# @Software: PyCharm
import argparse
import random

import pandas as pd


def DoForecast(file_path,column):
    """获取csv文件内容并返回
    :param file_path: 文件地址,类型为str
    :param column: 要查询的列数,类型为int
    :return: 返回的list值,result为返回结果list
    """
    file = pd.read_csv(file_path, header=None, encoding='utf-8')
    index = len(file)
    #index=5266
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

def GetLastIndex(mIndex,mListIndex):
    """预测下一次的值
    :param mIndex:数字下标
    :param mListIndex:数字列表
    :return:返回可能出现的list值
    """
    result=[]
    for i in range(len(mListIndex)):
        if i == len(mListIndex) - 1:  #检测是否最后一个，是则跳过。
            break
            pass

        if mListIndex[i]==mIndex:
            #print("下一次可能出现的值:"+str(mListIndex[i+1]))
            result.append(mListIndex[i+1])
            pass
        pass

    return result
    pass

def GetMin(num_01,num_02,num_03):
    """三元运算获得最小数
    :param num_01:
    :param num_02:
    :param num_03:
    :return:
    """
    return num_01 if num_01 < num_02 and num_01 < num_03 else num_02 if num_02 < num_03 else num_03
    #return num_01 if num_01 > num_02 and num_01 > num_03 else num_02 if num_02 > num_03 else num_03#最大数
    pass

def GetResult_01(list_01,list_02,list_03):
    min = GetMin(len(list_01), len(list_02), len(list_03))
    print("下一次可能出现的结果:")
    for i in range(min):
        print(str(list_01[i]) + str(list_02[i]) + str(list_03[i]))
        pass
    print("总可能数:" + str(min))
    pass

def main(args):
    """定义储存csv获取到三列数的数组"""
    result_num_01 =DoForecast(args.file_path,0)
    result_num_02 =DoForecast(args.file_path,1)
    result_num_03 =DoForecast(args.file_path,2)
    print("获取结果:"+"\nresult_num_01:" + str(result_num_01)+"\nresult_num_02:"+str(result_num_02)+"\nresult_num_03:"+str(result_num_03))

    indexList=[1,8,1]#上一期数字
    result_index_01=GetLastIndex(indexList[0],result_num_01)
    result_index_02=GetLastIndex(indexList[1],result_num_02)
    result_index_03=GetLastIndex(indexList[2],result_num_03)
    #print("01_下标数:"+str(len(result_index_01))+"\t可能出现:"+str(result_index_01))
    #print("02_下标数:"+str(len(result_index_02))+"\t可能出现:"+str(result_index_02))
    #print("03_下标数:" + str(len(result_index_03)) + "\t可能出现:" + str(result_index_03))

    #result_01=random.randrange(0,len(result_index_01))

    #使用方法一预测
    GetResult_01(result_index_01,result_index_02,result_index_03)
    print("上一期:" +str(indexList))

    pass

if __name__=='__main__':
    #file_dir = r"./work.csv"
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str,default='./data/work.csv',help='csv文件地址')
    args = parser.parse_args()
    main(args)