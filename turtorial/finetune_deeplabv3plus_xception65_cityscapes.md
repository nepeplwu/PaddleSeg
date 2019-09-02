# 关于本教程

* 本教程旨在介绍如何通过使用PaddleSeg提供的预训练模型在自定义数据集上进行训练

* 在阅读本教程前，请确保您已经了解过PaddleSeg的[快速入门](../README.md#快速入门)和[基础功能](../README.md#基础功能)等章节，以便对PaddleSeg有一定的了解

* 本教程的所有命令都基于PaddleSeg主目录进行执行

## 一. 准备预训练数据

我们提前准备好了一份数据集，通过以下代码进行下载

```shell
python dataset/download_pet.py
```

## 二. 下载预训练模型

接着我们下载预训练模型

关于PaddleSeg支持的所有预训练模型的列表，我们可以从[预训练模型]()中查看

```shell
python pretrained_model/download_model.py --name deeplabv3plus_xception65_cityscapes
```

## 三. 启动训练

在开始训练和评估之前，我们需要确定相关配置，从本教程的角度，配置分为三部分：

* 数据集
  * 训练集主目录
  * 训练集文件列表
  * 测试集文件列表
  * 评估集文件列表
* 预训练模型
  * 预训练模型名称
  * 预训练模型的backbone网络
  * 预训练模型的Normalization类型
  * 预训练模型路径
* 其他
  * 学习率
  * Batch大小
  * ...
  
数据集的配置如下：

|配置|值|
|-|-|
|DATASET.DATA_DIR|./dataset/mini_pet/|
|DATASET.TRAIN_FILE_LIST|./dataset/mini_pet/file_list/train_list.txt|
|DATASET.TEST_FILE_LIST|./dataset/mini_pet/file_list/test_list.txt|
|DATASET.VAL_FILE_LIST|./dataset/mini_pet/file_list/val_list.txt|

预训练模型的配置，可以从下载预训练模型时的输出看到：

|配置|值|
|-|-|
|MODEL.MODEL_NAME|deeplabv3p|
|MODEL.DEEPLAB.BACKBONE|xception65|
|MODEL.DEFAULT_NORM_TYPE|bn|
|TRAIN.PRETRAINED_MODEL|./pretrained_model/deeplabv3plus_xception65_cityscapes|

其他配置，如学习率相关的，我们直接使用configs里面提供的默认配置`configs/unet_pet.yaml`


```shell
python pdseg/train.py --use_gpu \
                       --cfg ./configs/unet_pet.yaml \
                       DATASET.DATA_DIR ./dataset/mini_pet/ \
                       DATASET.TRAIN_FILE_LIST ./dataset/mini_pet/file_list/train_list.txt \
                       DATASET.TEST_FILE_LIST ./dataset/mini_pet/file_list/test_list.txt \
                       DATASET.VAL_FILE_LIST ./dataset/mini_pet/file_list/val_list.txt \
                       MODEL.MODEL_NAME deeplabv3p \
                       MODEL.DEEPLAB.BACKBONE xception65 \
                       MODEL.DEFAULT_NORM_TYPE bn \
                       TRAIN.PRETRAINED_MODEL ./pretrained_model/deeplabv3plus_xception65_cityscapes 
```

## 四. 进行评估

```shell
python pdseg/eval.py --use_gpu \
                       --cfg ./configs/unet_pet.yaml \
                       DATASET.DATA_DIR ./dataset/mini_pet/ \
                       DATASET.TRAIN_FILE_LIST ./dataset/mini_pet/file_list/train_list.txt \
                       DATASET.TEST_FILE_LIST ./dataset/mini_pet/file_list/test_list.txt \
                       DATASET.VAL_FILE_LIST ./dataset/mini_pet/file_list/val_list.txt \
                       MODEL.MODEL_NAME deeplabv3p \
                       MODEL.DEEPLAB.BACKBONE mobilenet \
                       MODEL.DEEPLAB.DEPTH_MULTIPLIER 1.0 \
                       MODEL.DEFAULT_NORM_TYPE bn \
                       TRAIN.PRETRAINED_MODEL ./pretrained_model/deeplabv3plus_xception65_cityscapes 
```
