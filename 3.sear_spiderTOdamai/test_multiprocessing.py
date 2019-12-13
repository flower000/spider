# -*- coding: utf-8 -*-
import lxml.html
import requests
import re
import time
import random
from fake_useragent import UserAgent       # fake userhead
import csv
import pandas as pd
from multiprocessing.dummy import Pool

def func(a,b):
    return 2*a, 2*b

if __name__=='__main__':
    pool = Pool(4)
    # 多参数情况使用Pool.starmap函数
    a,b,c = pool.starmap(func,[(1,2),(3,4),(5,6)])
    print('a={},b={},c={}'.format(a,b,c))

