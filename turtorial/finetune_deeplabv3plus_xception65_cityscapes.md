# 关于本教程

本章节旨在介绍如何通过使用PaddleSeg提供的预训练模型在自定义数据集上进行训练

在阅读本教程前，请确保您已经了解过PaddleSeg的[快速入门]()和[基础功能]()等章节，以便对PaddleSeg有一定的了解

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


|配置|选项|含义|值|
|-|-|-|-|
|数据集|DATASET.DATA_DIR|数据集根目录||
||DATASET.TRAIN_FILE_LIST|训练集文件列表||
||DATASET.TEST_FILE_LIST|测试集文件列表||
||DATASET.VAL_FILE_LIST|评估集文件列表||

```shell
python pdseg/train.py --use_gpu \
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