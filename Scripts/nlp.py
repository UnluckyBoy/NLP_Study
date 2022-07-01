import torch
import torch.nn as nn
from torch.optim import SGD
from matplotlib import pyplot as plt
import time

#线性回归AI训练测试
#准备数据
x=torch.rand([50,1])
y=3*x+0.8

#定义模型
class NLP_Model(nn.Module):
    def __init__(self):
        #继承父类init
        super(NLP_Model,self).__init__()
        self.linear=nn.Linear(1,1)

    def forward(self,x):
        out=self.linear(x)
        return out

#定义训练环境  torch.cuda.is_available()判断是否支持cuda,即gpu训练;否则以cpu
mDevice=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
x,y=x.to(mDevice),y.to(mDevice)#将x、y进行类型转化

#实例化模型、优化器类实例化、loss实例化
mNLP_Model=NLP_Model().to(mDevice)#将模型进行类型转化
mOptim=SGD(mNLP_Model.parameters(),0.001)
mLoss=nn.MSELoss()

#循环，进行梯度下降，参数更新
for i in range(40000):
    #获取预测值
    y_predict=mNLP_Model(x)
    loss=mLoss(y_predict,y)
    #梯度预置为0
    mOptim.zero_grad()
    #反向传播
    loss.backward()
    #设置参数更新
    mOptim.step()
    if i%20==0:
        #params=list(mNLP_Model.parameters())
        #print(loss.item(),params[0].item(),params[1].item())
        print('Epoch[{}/{}],loss:{:.6f}'.format(i,40000,loss.data))

#模型评估
mNLP_Model.eval()#设置模型为评估模型
predict=mNLP_Model(x)
#predict=predict.data.numpy() #CPU环境
#plt.scatter(x.data.numpy(),y.data.numpy(),c="r")
#plt.plot(x.data.numpy(),predict)
predict=predict.cpu().detach().numpy() #GPU环境,detach()与data类似；detach()是深拷贝，data为浅拷贝
plt.scatter(x.cpu().detach().numpy(),y.cpu().detach().numpy(),c="r")
plt.plot(x.cpu().detach().numpy(),predict)
plt.show()