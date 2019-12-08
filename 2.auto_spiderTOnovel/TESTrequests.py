# -*- coding: utf-8 -*-
import requests
import re
# get: loggin the html
html_g = requests.get('http://exercise.kingname.info/exercise_requests_get.html').content.decode()
print(html_g)

'''
# post: loggin the html
data = {'name':'kingname','password':'1234567'}
html_p = requests.post('http://exercise.kingname.info/exercise_requests_post', data=data).content.decode()
print(html_p)

data = {'name':'kingname',
        'password':'1234567'}
html_p = requests.post('http://exercise.kingname.info/exercise_requests_post', json=data).content.decode()     # post from json
print(html_p)
'''


