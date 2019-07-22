# coding: utf-8
import json

def _ordered_data(data):
    '''排序'''
    complex_keys = [k for k, v in data.items() if isinstance(v, dict)]


    # 将字典类型的数据dump出来
    for key in complex_keys:
        data[key] = json.dumps(data[key], separators=(',', ':'))
        data[key] = json.dumps(data[key])
    print(data)
    return sorted([(k, v) for k, v in data.items()])



data = {'A':1,'B':2,'C':{'b':2,'a':1},'D':{'c':6,'d':7},'E':5}
_ordered_data(data)


