# cfg.SOLVER

SOLVER Group定义所有和训练优化相关的配置

## `LR`

初始学习率

### 默认值

0.1

<br/>
<br/>

## `LR_POLICY`

学习率的衰减策略，支持`poly` `piecewise` `cosine`三种策略

### 默认值

`poly`

### 示例
* 当使用`poly`衰减时，假设初始学习率为0.1，训练总步数为10000，则在power分别为`0.4``0.8``1``1.2``1.6`时，衰减曲线如下图：
  * power = 1 衰减曲线为直线
  * power > 1 衰减曲线内凹
  * power < 1 衰减曲线外凸

  <p align="center">
  <img src="../imgs/poly_decay_example.png" hspace='10' height="400" width="800"/> <br />
  </p>
  
* 当使用`piecewise`衰减时，假设初始学习率为0.1，GAMMA为0.9，总EPOCH数量为100，DECAY_EPOCH为[10, 20]，衰减曲线如下图：
  
  <p align="center">
  <img src="../imgs/piecewise_decay_example.png" hspace='10' height="400" width="800"/> <br />
  </p>

* 当使用`cosine`衰减时，假设初始学习率为0.1，总EPOCH数量为100，衰减曲线如下图：
  
  <p align="center">
  <img src="../imgs/cosine_decay_example.png" hspace='10' height="400" width="800"/> <br />
  </p>

<br/>
<br/>

## `POWER`

学习率Poly下降指数，仅当策略为[`LR_POLICY`](#LR_POLICY)为`poly`时有效

### 默认值

0.9

<br/>
<br/>

## `GAMMA`

学习率piecewise下降指数，仅当策略为[`LR_POLICY`](#LR_POLICY)为`piecewise`时有效

### 默认值

0.1

<br/>
<br/>

## `DECAY_EPOCH`

学习率piecewise下降间隔，仅当策略为[`LR_POLICY`](#LR_POLICY)为`piecewise`时有效

### 默认值

[10, 20]

<br/>
<br/>

## `WEIGHT_DECAY`

L2正则化系数

### 默认值

0.00004

<br/>
<br/>

## `BEGIN_EPOCH`

起始EPOCH值

### 默认值

0

<br/>
<br/>

## `NUM_EPOCHS`

训练EPOCH数

### 默认值

30（需要根据实际需求进行调整）

<br/>
<br/>

## `SNAPSHOT`

训练时，保存模型的间隔（单位为EPOCH）

### 默认值

10（意味着每训练10个EPOCH保存一次模型）

<br/>
<br/>