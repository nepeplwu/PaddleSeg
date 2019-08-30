# PaddleSeg 语义分割库

[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)

## 简介

PaddleSeg是基于[PaddlePaddle](https://www.paddlepaddle.org.cn)开发的语义分割库，覆盖了DeepLabv3+, U-Net, ICNet三类主流的分割模型。通过统一的配置，帮助用户更便捷地完成从训练到部署的全流程图像分割应用。
具备高性能、丰富的数据增强、工业级部署、全流程应用的特点。



- **丰富的数据增强**

  - 基于百度视觉技术部的实际业务经验，内置10+种数据增强策略，可结合实际业务场景进行定制组合，提升模型泛化能力和鲁棒性。
  
- **主流模型覆盖**

  - 支持U-Net, DeepLabv3+, ICNet三类主流分割网络，结合预训练模型和可调节的骨干网络，满足不同性能和精度的要求。

- **高性能**

  - PaddleSeg支持多进程IO、多卡并行、多卡Batch Norm同步等训练加速策略，通过飞桨核心框架的显存优化算法，可以大幅度节约分割模型的显存开销，更快完成分割模型训练。
  
- **工业级部署**

  - 基于[Paddle Serving](https://github.com/PaddlePaddle/Serving)和PaddlePaddle高性能预测引擎，结合百度开放的AI能力，轻松搭建人像分割和车道线分割服务。

</br>
</br>

## 在线体验

简单介绍下语义分割

* [普通分割模型体验]()
* [ACE2P体验]()
* [HumanSeg体验]()

</br>
</br>

## 使用教程

我们提供了一系列的使用教程，来说明如何使用PaddleSeg完成一个语义分割模型的训练、评估、部署。

这一系列的文档被分为`快速入门`、`基础教程`、`预测部署`、`高级功能`三个部分，三个教程由前浅至深，依次介绍PaddleSeg的设计理念和使用方法。

### 快速入门

* [常见分割模型介绍]()
* [训练/评估]()

### 基础教程

* [预训练模型列表]()
* [自定义数据的准备与标注]()
* [数据和配置校验]()
* [基于DeepLabv3+ mobilenet预训练模型进行Finetune]()
* [基于DeepLabv3+ xception预训练模型进行Finetune]()
* [基于Unet预训练模型进行Finetune]()
* [基于ICNet预训练模型进行Finetune]()
* [基于PaddleCV模型进行Finetune]()

### 预测部署

* [模型导出]()
* [预测库使用]()
* [模型部署与Serving]()

### 高级功能

* [可视化训练过程]()
* [PaddleSeg的数据增强]()
* [模型的调优技巧]()
* [特色垂类模型使用]()

</br>
</br>

## FAQ

#### Q:图像分割的数据增强如何配置，unpadding, step-scaling, range-scaling的原理是什么？

A: 数据增强的配置可以参考文档[数据增强](./docs/data_aug.md)

#### Q: 预测时图片过大，导致显存不足如何处理？

A: 降低Batch size，使用Group Norm策略等。

</br>
</br>

## 更新日志

* 2019.08.26

  **`v0.1.0`**
  * PaddleSeg分割库初始版本发布，包含DeepLabv3+, U-Net, ICNet三类分割模型, 其中DeepLabv3+支持Xception, MobileNet两种可调节的骨干网络。
  * CVPR 19' LIP人体部件分割比赛冠军预测模型发布[ACE2P](./contrib/ACE2P)
  * 预置基于DeepLabv3+网络的[人像分割](./contrib/HumanSeg/)和[车道线分割](./contrib/RoadLine)预测模型发布

</br>
</br>

## 如何贡献代码

我们非常欢迎您为PaddleSeg贡献代码或者提供使用建议。
