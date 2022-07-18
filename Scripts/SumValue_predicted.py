import os
import pandas as pd
file_dir=r"./work_02.csv"
file=pd.read_csv(file_dir,header=None,encoding= 'utf-8')
index=len(file)
menu_num=file.iloc[:,0]#序号
num_01=file.iloc[:,1]#第一个数
num_02=file.iloc[:,2]#第二个数
num_03=file.iloc[:,3]#第三个数
sum_size=file.iloc[:,6]#大小
sum_parity=file.iloc[:,7]#单双

result_size_max_01=0#第一种情况和值为大的总数
result_size_min_01=0#第一种情况和值为小的总数
result_parity_odd_01=0#第一种情况和值为单的总数
result_parity_even_01=0#第一种情况和值为双的总数

result_size_max_02=0#第二种情况和值为大的总数
result_size_min_02=0#第二种情况和值为小的总数
result_parity_odd_02=0#第二种情况和值为单的总数
result_parity_even_02=0#第二种情况和值为双的总数

result_size_max_03=0#第二种情况和值为大的总数
result_size_min_03=0#第二种情况和值为小的总数
result_parity_odd_03=0#第二种情况和值为单的总数
result_parity_even_03=0#第二种情况和值为双的总数

result_size_max_04=0#第二种情况和值为大的总数
result_size_min_04=0#第二种情况和值为小的总数
result_parity_odd_04=0#第二种情况和值为单的总数
result_parity_even_04=0#第二种情况和值为双的总数

result_size_max_05=0#第二种情况和值为大的总数
result_size_min_05=0#第二种情况和值为小的总数
result_parity_odd_05=0#第二种情况和值为单的总数
result_parity_even_05=0#第二种情况和值为双的总数

result_size_max_06=0#第二种情况和值为大的总数
result_size_min_06=0#第二种情况和值为小的总数
result_parity_odd_06=0#第二种情况和值为单的总数
result_parity_even_06=0#第二种情况和值为双的总数

result_01=0#第一种情况总数
result_02=0#第二种情况总数
result_03=0#第三种情况总数
result_04=0#第四种情况总数
result_05=0#第五种情况总数
result_06=0#第六种情况总数

for i in range(index):
    if i==index-1:#检测是否最后一个，是则跳过。
        break
        pass
    #sum_num=num_01[i]+num_02[i]+num_03[i]
    if num_01[i] == 6 and num_02[i] == 6 and num_03[i] == 6:
        result_01+=1
        #print(menu_num[i])
        size=sum_size[i + 1]
        parity=sum_parity[i + 1]
        #print(str(result_01)+":"+size + parity)
        if size=="大":
            result_size_max_01+=1
            pass
        if size=="小":
            result_size_min_01 += 1
            pass
        if parity=="单":
            result_parity_odd_01+=1
            pass
        if parity=="双":
            result_parity_even_01+=1
            pass
        pass

    if num_01[i] == 5 and num_02[i] == 5 and num_03[i] == 6:
        result_02 += 1
        size = sum_size[i + 1]
        parity = sum_parity[i + 1]
        if size == "大":
            result_size_max_02 += 1
            pass
        if size == "小":
            result_size_min_02 += 1
            pass
        if parity == "单":
            result_parity_odd_02 += 1
            pass
        if parity == "双":
            result_parity_even_02 += 1
            pass
        pass

    if num_01[i] == 5 and num_02[i] == 5 and num_03[i] == 5:
        result_03 += 1
        size = sum_size[i + 1]
        parity = sum_parity[i + 1]
        if size == "大":
            result_size_max_03 += 1
            pass
        if size == "小":
            result_size_min_03 += 1
            pass
        if parity == "单":
            result_parity_odd_03 += 1
            pass
        if parity == "双":
            result_parity_even_03 += 1
            pass
        pass
    if num_01[i] == 4 and num_02[i] == 5 and num_03[i] == 5:
        result_04 += 1
        size = sum_size[i + 1]
        parity = sum_parity[i + 1]
        if size == "大":
            result_size_max_04 += 1
            pass
        if size == "小":
            result_size_min_04 += 1
            pass
        if parity == "单":
            result_parity_odd_04 += 1
            pass
        if parity == "双":
            result_parity_even_04 += 1
            pass
        pass
    if num_01[i] == 4 and num_02[i] == 4 and num_03[i] == 5:
        result_05 += 1
        size = sum_size[i + 1]
        parity = sum_parity[i + 1]
        if size == "大":
            result_size_max_05 += 1
            pass
        if size == "小":
            result_size_min_05 += 1
            pass
        if parity == "单":
            result_parity_odd_05 += 1
            pass
        if parity == "双":
            result_parity_even_05 += 1
            pass
        pass
    if num_01[i] == 3 and num_02[i] == 4 and num_03[i] == 4:
        result_06 += 1
        size = sum_size[i + 1]
        parity = sum_parity[i + 1]
        if size == "大":
            result_size_max_06 += 1
            pass
        if size == "小":
            result_size_min_06 += 1
            pass
        if parity == "单":
            result_parity_odd_06 += 1
            pass
        if parity == "双":
            result_parity_even_06 += 1
            pass
        pass
    pass
#test=round((result_size_max/result_01),3)
#print("113的结果为大的概率:"+str(round(result_size_max/result_01,3)))
#print("113的结果为小的概率:"+str(round(result_size_min/result_01,3)))
#print("113的结果为单的概率:"+str(round(result_parity_odd/result_01,3)))
#print("113的结果为双的概率:"+str(round(result_parity_even/result_01,3)))
print("___！！！---666---！！！___结果:"+"\n总数:"+str(result_01)
      +"\t大的个数:"+str(result_size_max_01)+"\t小的个数:"+str(result_size_min_01)
      +"\t单的个数:"+str(result_parity_odd_01)+"\t双的个数:"+str(result_parity_even_01)
      +"\n大:"+str(round(result_size_max_01/result_01,3))
      +"\t小:"+str(round(result_size_min_01/result_01,3))
      +"\t单:"+str(round(result_parity_odd_01/result_01,3))
      +"\t双:"+str(round(result_parity_even_01/result_01,3)))
"""
print("___！！！---556---！！！___结果:"+"\n总数:"+str(result_02)
      +"\t大的个数:"+str(result_size_max_02)+"\t小的个数:"+str(result_size_min_02)
      +"\t单的个数:"+str(result_parity_odd_02)+"\t双的个数:"+str(result_parity_even_02)
      +"\n大:"+str(round(result_size_max_02/result_02,3))
      +"\t小:"+str(round(result_size_min_02/result_02,3))
      +"\t单:"+str(round(result_parity_odd_02/result_02,3))
      +"\t双:"+str(round(result_parity_even_02/result_02,3)))

print("___！！！---555---！！！___结果:"+"\n总数:"+str(result_03)
      +"\t大的个数:"+str(result_size_max_03)+"\t小的个数:"+str(result_size_min_03)
      +"\t单的个数:"+str(result_parity_odd_03)+"\t双的个数:"+str(result_parity_even_03)
      +"\n大:"+str(round(result_size_max_03/result_03,3))
      +"\t小:"+str(round(result_size_min_03/result_03,3))
      +"\t单:"+str(round(result_parity_odd_03/result_03,3))
      +"\t双:"+str(round(result_parity_even_03/result_03,3)))

print("___！！！---455---！！！___结果:"+"\n总数:"+str(result_04)
      +"\t大的个数:"+str(result_size_max_04)+"\t小的个数:"+str(result_size_min_04)
      +"\t单的个数:"+str(result_parity_odd_04)+"\t双的个数:"+str(result_parity_even_04)
      +"\n大:"+str(round(result_size_max_04/result_04,3))
      +"\t小:"+str(round(result_size_min_04/result_04,3))
      +"\t单:"+str(round(result_parity_odd_04/result_04,3))
      +"\t双:"+str(round(result_parity_even_04/result_04,3)))

print("___！！！---445---！！！___结果:"+"\n总数:"+str(result_05)
      +"\t大的个数:"+str(result_size_max_05)+"\t小的个数:"+str(result_size_min_05)
      +"\t单的个数:"+str(result_parity_odd_05)+"\t双的个数:"+str(result_parity_even_05)
      +"\n大:"+str(round(result_size_max_05/result_05,3))
      +"\t小:"+str(round(result_size_min_05/result_05,3))
      +"\t单:"+str(round(result_parity_odd_05/result_05,3))
      +"\t双:"+str(round(result_parity_even_05/result_05,3)))

print("___！！！---344---！！！___结果:"+"\n总数:"+str(result_06)
      +"\t大的个数:"+str(result_size_max_06)+"\t小的个数:"+str(result_size_min_06)
      +"\t单的个数:"+str(result_parity_odd_06)+"\t双的个数:"+str(result_parity_even_06)
      +"\n大:"+str(round(result_size_max_06/result_06,3))
      +"\t小:"+str(round(result_size_min_06/result_06,3))
      +"\t单:"+str(round(result_parity_odd_06/result_06,3))
      +"\t双:"+str(round(result_parity_even_06/result_06,3)))
"""