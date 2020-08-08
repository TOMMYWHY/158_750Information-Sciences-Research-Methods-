
# Update

- 2019/12/13: The pytorch implementation of ACNet has been released for the currently popular EfficientNet and the efficient DNA network families. [Jump to Pytorch ACNet](https://github.com/wanggrun/Adaptively-Connected-Neural-Networks-Pytorch).


# Adaptively Connected Neural Networks
A re-implementation of our CVPR 2019 paper "Adaptively Connected Neural Networks" (https://arxiv.org/abs/1904.03579).

[Guangrun Wang](https://wanggrun.github.io/) , Keze Wang, Liang Lin

Sun Yat-sen University (SYSU)





![intro](https://github.com/wanggrun/Adaptively-Connected-Neural-Networks/blob/master/intro.jpg)






# Table of Contents
0. [Introduction](#introduction)
0. [ImageNet](#imagenet)
0. [Cora](#cora)
0. [Citation](#citation)

# Introduction

This repository contains the training & testing code of Adaptively Connected Neural Networks (ACNet) on [ImageNet](http://image-net.org/challenges/LSVRC/2015/) and [Cora](http://linqs.cs.umd.edu/projects/projects/lbc/). 


# ImageNet

+ Training and testing curve on ImageNet：



   ![curves](https://github.com/wanggrun/Adaptively-Connected-Neural-Networks/blob/master/error.jpg)
	   
	   
	   
	   
	   
	   
	   

+ ImageNet accuracy and pretrained model (baidu pan code: ow9z):

| Model            | Top 5 Error | Top 1 Error | Download                                                                          |
|:-----------------|:------------|:-----------:|:---------------------------------------------------------------------------------:|
| ResNet50         | 6.9%       | 23.6%      | [:arrow_down:](http://models.tensorpack.com/ResNet/ImageNet-ResNet50.npz)         |
| ResNet50-ACNet   | 6.4%       | 22.5%      | google drive: [:arrow_down:](https://drive.google.com/open?id=1M0Nb6IKiGdlHy8hOOG_Rcbh861Ve1OeE)   and baidu pan: [:arrow_down:](https://pan.baidu.com/s/1KoaBmK_dr35zkmXXDlyDdA)   |
| ResNet50-ACNet-pixel-aware| 6.4% | 22.5%   | google drive: [:arrow_down:](https://drive.google.com/open?id=1OTV-LFX1VrCxRIHju036uNkNz0aJBhGJ)   and baidu pan: [:arrow_down:](https://pan.baidu.com/s/1KoaBmK_dr35zkmXXDlyDdA)     |


+ Training script:
```
cd cnn/dataset-aware/ or cd cnn/pixel-aware/

python imagenet-resnet.py  --gpu 0,1,2,3,4,5,6,7   --data [ROOT-OF-IMAGENET-DATASET]  --log_dir  [ROOT-OF-TRAINING-LOG-AND-MODEL] 
```

+ Testing script:
```
cd cnn/dataset-aware/ or cd cnn/pixel-aware/

python imagenet-resnet.py  --gpu 0,1,2,3,4,5,6,7   --data [ROOT-OF-IMAGENET-DATASET]  --log_dir  [ROOT-OF-TEST-LOG] --load   [ROOT-TO-LOAD-MODEL]  --eval
```

# Cora

Coming soon ...

# Citation

If you use these models in your research, please cite:

@inproceedings{wang2019adaptively,
  
      title={Adaptively Connected Neural Networks},
  
      author={Wang, Guangrun and Wang, Keze and Lin, Liang},
  
      booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  
      year={2019}}
      

# Dependencies
+ Python 2.7 or 3
+ TensorFlow >= 1.3.0
+ [Tensorpack](https://github.com/ppwwyyxx/tensorpack)
   The code depends on Yuxin Wu's Tensorpack. For convenience, we provide a stable version 'tensorpack-installed' in this repository. 
   ```
   # install tensorpack locally:
   cd tensorpack-installed
   python setup.py install --user
   ```
