# -*- coding: utf-8 -*-
import lxml.html
import requests
import re
import time
import random
from fake_useragent import UserAgent       # fake userhead

global count
count = 0

# oneself
def GetName(node):
    return node.xpath('div/header/a[contains(@class,"name")]/text()')
def GetRetime(node):
    return node.xpath('div/header/span[contains(@class,"main-meta")]/text()')
def GetTitle(node):
    return node.xpath('div/div/h2/a/text()')
def GetContent(node):
    content = node.xpath('div/div/div[1]/div/text()')
    content = content[0].replace('\n','')
    return content.replace(' ','')
# followers
def GetUseful(node):
    useful = node.xpath('div/div/div[@class="action"]/a[contains(@title,"有用")]/span/text()')
    useful = useful[0].replace('\n','')
    return useful.replace(' ','')
def GetUseless(node):
    useless = node.xpath('div/div/div[@class="action"]/a[contains(@title,"没用")]/span/text()')
    useless = useless[0].replace('\n','')
    return useless.replace(' ','')
def GetReplies(node):
    return node.xpath('div/div/div[@class="action"]/a[contains(@class,"reply ")]/text()')
# next page
def GetNextp(node):
    global count
    count = count + 1
    print('{}'.format(count))
#    selector.xpath('//*[@id="content"]/div/div[1]/div[2]/span[4]/a')
#//*[@id="content"]/div/div[1]/div[2]/span[contains(@data-total-page,"426")]   
    try:
        pageNode = node.xpath('//*[@id="content"]/div/div[1]/div[2]/span[contains(@data-total-page,"426")]')
    except pageNode.__len__()==0:
        print('*************************')
        return ''
    else:
        nowpage = pageNode[0].xpath('text()')
        allpage = pageNode[0].attrib['data-total-page']
        if str(nowpage[0]) == allpage:     # the last page
            return ''
        else:
            temp = node.xpath('//*[@id="content"]/div/div[1]/div[2]/span[contains(@class,"next")]/a')
            return temp[0].attrib['href']   

# write .CSV file 
def writeFile():
    pass
   
def shawReview(URL):
    name_list, reply_timeList, title_list, content_list = [], [], [], []
    useful_list, useless_list, reply_list = [], [], []
    doubanURL = URL
    # random userAgent
    user_agent = UserAgent().random
#    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
    while True:
        HTMLstr = requests.get(doubanURL,headers={'User-Agent': user_agent}).content.decode()
        selector = lxml.html.fromstring(HTMLstr)
        shawReview = selector.xpath('//*[@id="content"]/div/div[1]/div[1]/div')
        for each in range(shawReview.__len__()):
            tempNode = shawReview[each]
            # oneself
            name_list.append(GetName(tempNode))
            reply_timeList.append(GetRetime(tempNode))
            title_list.append(GetTitle(tempNode))
            content_list.append(GetContent(tempNode))
            # followers
            useful_list.append(GetUseful(tempNode))
            useless_list.append(GetUseless(tempNode))
            reply_list.append(GetReplies(tempNode))
        nextPage = GetNextp(selector)
        if nextPage == '':
            break
        doubanURL = URL + nextPage
        time.spleep(random.randint(0,1))
        
        

if __name__=='__main__':
    # chrome TEST_1: damai.com
    # problem: can't choose the obvious link
    '''
    # try damai.cn
    damaiURL = 'https://search.damai.cn/search.htm'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
    HTMLstr = requests.get(damaiURL,headers={'User-Agent': user_agent}).content.decode()
    selector = lxml.html.fromstring(HTMLstr)
    concertPAGE = selector.xpath('//body/div[2]/div[2]/div[1]/div[3]/div[1]/div')
    '''
    
    # chrome TEST_2: douban.com
    '''
    NOTICE: hide your spider beneath a browser agent
    '''
    doubanURL = 'https://movie.douban.com/subject/1292052/reviews'
    #HTMLstr = requests.get(doubanURL,headers={'User-Agent': user_agent}).content.decode()
    # lxml: analyse the html
    #selector = lxml.html.fromstring(HTMLstr)
    #shawReview = selector.xpath('//*[@id="content"]/div/div[1]/div[1]/div')
    
    shawReview(doubanURL)
    '''
    # initialize of the parameters
    name, reply_time, title, content = '', '', '', ''   # oneself
    useful, useless, reply = '', '', ''     # his followers
    name_list, reply_timeList, title_list, content_list = [], [], [], []
    useful_list, useless_list, reply_list = [], [], []
    while True:
        HTMLstr = requests.get(doubanURL,headers={'User-Agent': user_agent}).content.decode()
        selector = lxml.html.fromstring(HTMLstr)
        shawReview = selector.xpath('//*[@id="content"]/div/div[1]/div[1]/div')     
        for each in range(shawReview.__len__()):
            name = shawReview[each].xpath('div/header/a[contains(@class,"name")]/text()')
            name_list.append(name)
            reply_time = shawReview[each].xpath('div/header/span[contains(@class,"main-meta")]/text()')
            reply_timeList.append(reply_time)
            title = shawReview[each].xpath('div/div/h2/a/text()')
            title_list.append(title)
            # useful commnets
            useful = shawReview[each].xpath('div/div/div[@class="action"]/a[contains(@title,"有用")]/span/text()')
            useful = useful[0].replace('\n','')
            useful = useful.replace(' ','')
            useful_list.append(useful)
            # useless commnets
            useless = shawReview[each].xpath('div/div/div[@class="action"]/a[contains(@title,"没用")]/span/text()')
            useless = useless[0].replace('\n','')
            useless = useless.replace(' ','')
            useless_list.append(useless)
            # replies
            reply = shawReview[each].xpath('div/div/div[@class="action"]/a[contains(@class,"reply ")]/text()')
            reply_list.append(reply)
            # content
            content = shawReview[each].xpath('div/div/div[1]/div/text()')
            content = content[0].replace('\n','')
            content = content.replace(' ','')
            content_list.append(content)
        next_page = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/span[4]/a')
        doubanURL = doubanURL + next_page[0].attrib['href']
    '''
    
    
    
    print(1+1)




