#!/usr/bin/env python
# encoding: utf-8
'''
@author: bobby
@file: serializers.py
@time: 7/20/20 3:16 AM
'''

#APIview　方法实现后台ｐｏｓｔ到前端页面
from rest_framework import serializers


class CRISPRSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=100)
    click_num = serializers.IntegerField(default=0)
    # CRISPR_front_image = serializers.ImageField()