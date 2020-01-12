# -*- coding: utf-8 -*-
# 开发人员：Tryrus
# 开发时间：2020/1/11  0:02
# 文件名称：get_stations.py
# 开发工具：PyCharm

import re
import requests
import os
import json


def get_station():
	# 发送请求获取所有车站名称，通过输入的站名称转化查询地址的参数
	url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9140"

	response = requests.get(url, verify = True) # 请求并进行验证
	stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)  # 获取需要的车站名称
	stations = dict(stations)  # 转换为dic
	stations = str(stations)  # 转换为字符串类型否则无法写入文件
	write(stations, 'stations.text')  # 调用写入方法

def write(stations,file_name):
	file = open(file_name, 'w', encoding='utf_8_sig')  # 以写模式打开文件
	file.write(stations)  # 写入数据
	file.close()

def read(file_name):
	file = open(file_name, 'r', encoding='utf_8_sig')  # 以写模式打开文件
	data = file.readline()  #读取文件
	file.close()
	return data

def is_stations(file_name):
	is_stations = os.path.exists(file_name)      #判断文件是否存在,文件名称作为参数
	return is_stations

def get_selling_time():
	url = 'https://www.12306.cn/index/script/core/common/qss_v10072.js'
	response = requests.get(url, verify=True)  # 请求并进行验证
	json_str = re.findall('{[^}]+}', response.text)  # 匹配括号内所有内容
	time_js = json.loads(json_str[0])  # 解析json数据
	write(str(time_js), 'time.text')  # 调用写入方法

