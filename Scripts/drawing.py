import matplotlib.pyplot as plt
import os
import pandas as pd
"""绘制折线图"""
#读取csv文档
file_dir=r"./work.csv"
file=pd.read_csv(file_dir,header=None,encoding= 'utf-8')
#print(file)
#index=5487
index=len(file)
#index=1
#print("列数:"+file)
"""num_01、num_02、num_03为series类型数据，读取时以x[列]读取"""
num_01=file.iloc[:,0]
num_02=file.iloc[:,1]
num_03=file.iloc[:,2]
for i in range(index):
    image = plt.figure()  # 生成一个空白图形并且将其赋值给fig对象
    #print(num_01[i],num_02[i],num_03[i])
    plt.plot([num_01[i], num_02[i], num_03[i]],c='0.1')
    plt.title(str(num_01[i])+str(num_02[i])+str(num_03[i]))
    plt.xlabel("X")
    plt.ylabel("Y")
    #plt.show()
    imagename=str(i)+".png"
    image.savefig(r'E:\MatrixProject\NLPDemo\Scripts\IamgeData\{}.png'.format(i))
    plt.close(image)
print("完毕！")