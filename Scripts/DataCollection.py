# ---************************************************---
# @coding: utf-8
# @Time : 2022/7/21 0021 10:20
# @Author : Matrix
# @File : DataCollection.py
# @Software: PyCharm
# ---************************************************---
import argparse
from collections import Counter
import pandas as pd

def GetFile(file_path,column):
    """
    #读取文件并返回
    :param file_path:
    :param column:
    :return:
    """
    file=pd.read_csv(file_path,header=None, encoding='utf-8', converters={column: str})
    index = len(file)
    result_column = file.iloc[:, column]
    result=[]
    for i in range(index):
        result.append(result_column[i])
        if i == index - 1:  #检测是否最后一个，是则跳过。
            break
            pass
        pass

    return result
    pass

def GetNum(list_Counter):
    """
    #获取list_Counter第一个元素中的第一给元组并返回
    :param list_Counter:元素list
    :return:返回元素list
    """
    result=[]
    for i in range(500):
        result_str = list_Counter[i][0]
        result.append(result_str)
        result.sort()#list元素升序
        pass

    return result
    pass

def SaveFile(list,path):
    with open(path, 'w+') as f:
        for i in range(len(list)):
            f.write(list[i] + "\n")
            pass
        pass
    print("已保存文件:"+format(path))
    pass

def main(args):
    file_list=GetFile(args.file_path,5)

    #将元素list进行检测出现数量并降序排序
    number=Counter(file_list)
    result_Counter = number.most_common()

    result=GetNum(result_Counter)
    print("结果:\n"+str(result)+"\n数量:"+str(len(result)))

    SaveFile(result,args.result_path)

    pass

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--file_path',type=str,default='./data/data_3min.csv',help='')
    parser.add_argument('--result_path', type=str, default='./data/result.txt', help='')
    args=parser.parse_args()
    main(args)