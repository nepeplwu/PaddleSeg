# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import paddle
from paddle import nn
import paddle.nn.functional as F

from paddleseg.cvlibs import manager


@manager.LOSSES.add_component
class DiscriminativeLoss(nn.Layer):
    def __init__(self,
                 ignore_index=255,
                 delta_var=0.5,
                 delta_dist=1.5,
                 alpha=1,
                 beta=1,
                 gamma=0.001):
        super(DiscriminativeLoss, self).__init__()
        self.delta_var = delta_var
        self.delta_dist = delta_dist
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def forward(self, logit, label):
        instance_means, other_means = self._cluster_mean(logit, label)
        if isinstance(instance_means, list):
            return 0
        var_term = self._variance_term(logit, label, instance_means)
        dis_term = self._distance_term(instance_means, other_means)
        reg_term = self._regularization_term(instance_means)
        return self.alpha * var_term + self.beta * dis_term + self.gamma * reg_term

    def _variance_term(self, logit, label, instance_means):
        instance_cnt = instance_means.shape[2]
        var_term = 0
        for _idx in range(instance_cnt):
            instance_mask = (label == _idx).astype('float32')
            instance_mean = instance_means[:, :, _idx].unsqueeze(2).unsqueeze(3)
            variance = paddle.norm(logit - instance_mean, p=2, axis=1)
            variance_mask = (variance > self.delta_var).astype('float32')
            instance_mask *= variance_mask
            cnt = paddle.sum(instance_mask, axis=1)
            var_term += paddle.mean(
                paddle.sum(variance * instance_mask, axis=1) / cnt)
        return var_term

    def _distance_term(self, instance_means, other_means):
        distance = paddle.norm(instance_means - other_means, p=2, axis=1)
        mask = (distance < 2 * self.delta_dist).astype('float32')
        cnt = paddle.sum(mask, axis=1)
        return paddle.mean(paddle.sum(distance * mask, axis=1) / cnt)

    def _regularization_term(self, instance_means):
        reg_term = 0
        for mean in instance_means:
            reg_term += paddle.mean(paddle.norm(mean, p=2, axis=1))
        return reg_term

    def _cluster_mean(self, logit, label):
        instance_cnt = paddle.unique(label).shape[0]
        instance_means = []
        other_means = []
        for _idx in range(1, instance_cnt):

            instance_mask = (label == _idx).astype('int32').unsqueeze(1)
            instance_pixels = paddle.sum(instance_mask)
            instance_mean = paddle.sum(
                logit * instance_mask, axis=[2, 3]) / instance_pixels
            instance_mean = instance_mean.unsqueeze(2)
            instance_means.append(instance_mean)

            other_mask = 1 - instance_mask
            other_pixels = paddle.sum(other_mask)
            other_mean = paddle.sum(
                logit * other_mask, axis=[2, 3]) / other_pixels
            other_mean = other_mean.unsqueeze(2)
            other_means.append(other_mean)

        if len(instance_means):
            instance_means = paddle.concat(instance_means, axis=2)
            other_means = paddle.concat(other_means, axis=2)
        return instance_means, other_means
