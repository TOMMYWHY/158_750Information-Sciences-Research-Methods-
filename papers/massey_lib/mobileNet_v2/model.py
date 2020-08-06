from torch import nn
import torch


class ConvBNReLU(nn.Sequential):
    def __init__(self,in_channel,out_channel,kernel_size=3,stride=1,groups=1):
        padding=(kernel_size-1)//2
        super(ConvBNReLU, self).__init__(
            nn.Conv2d(in_channel,out_channel,kernel_size,stride,padding,groups=groups,bias=False), #todo group
            nn.BatchNorm2d(out_channel),
            nn.ReLU6(inplace=True)
        )

class InvertedResidual(nn.Module):
    def __init__(self,in_channel,out_channel,stride,expand_ratio):
        super(InvertedResidual,self).__init__()
        hidden_channel=in_channel*expand_ratio #tk
        self.use_shotcut=stride == 1 and in_channel == out_channel
        layers=[]
        if expand_ratio != 1:
            
