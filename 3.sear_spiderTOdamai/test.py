# -*- coding: utf-8 -*-
import lxml.html
import requests
import re

doubanURL = 'https://movie.douban.com/subject/1292052/reviews'
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
HTMLstr = requests.get(doubanURL,headers={'User-Agent': user_agent}).content.decode()
# lxml: analyse the html
selector = lxml.html.fromstring(HTMLstr)
shawReview = selector.xpath('//*[@id="content"]/div/div[1]/div[1]/div')
name = shawReview[0].xpath('div/header/a[contains(@class,"name")]/text()')
title = shawReview[0].xpath('div/div/h2/a/text()')
useful = shawReview[0].xpath('div/div/div[@class="action"]/a[contains(@title,"有用")]/span/text()')
useful = useful[0].replace('\n','')
useful = useful.replace(' ','')
reply = shawReview[0].xpath('div/div/div[@class="action"]/a[contains(@class,"reply ")]/text()')
# content
content = shawReview[0].xpath('//*[@id="review_1000369_short"]/div/text()')
attr = shawReview[0].xpath('//*[@id="review_1000369_short"]/div')
attr = attr[0].attrib['class']

next_page = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/span[4]/a')

print(1)

