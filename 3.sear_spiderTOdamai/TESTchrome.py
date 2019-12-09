# -*- coding: utf-8 -*-
import lxml.html
import requests

HTMLstr = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%8D%E4%BB%87%E8%80%85%E8%81%94%E7%9B%9F3&red_tag=p0961465567').content.decode()
selector = lxml.html.fromstring(HTMLstr)
useful = selector.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"][1]/div/div[2]/div[1]/div[1]/a')
print(useful[0].xpath('text()'))


# 淘宝：//*[@id="thread_list"]/li[4]/div/div[2]/div[1]/div/a
# 求助：//*[@id="thread_list"]/li[5]/div/div[2]/div[1]/div[1]/a
# 勇度：//*[@id="thread_list"]/li[6]/div/div[2]/div[1]/div[1]/a
