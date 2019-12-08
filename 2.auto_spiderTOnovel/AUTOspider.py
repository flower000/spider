# -*- coding: utf-8 -*-
import requests
import re
import os
from multiprocessing.dummy import Pool

def get_subURL(urlhead, maintext):
    url_list = []
    subURL = re.findall('href="(.*?)">', maintext, re.S)
    for each in subURL:
        url_list.append(urlhead+each)
    return url_list 
    
def spyPieChap(url):
    html = requests.get(url).content.decode('GBK')      # use 'GBK' instead of 'UTF-8'
    ChaTITLE = re.findall('<title>(.*?)小说在线阅读</title>', html, re.S)[0].replace(' ','')
    html = re.findall('size="4">(.*?</p>)', html, re.S)[0]
    ChaCont = re.findall('<p>(.*?)</p>', html, re.S)[0].replace('<br />','')
    return ChaTITLE, ChaCont

def saveFILES(ChaTITLE, ChaCont):
    # make a file for novels
    os.makedirs('动物农场', exist_ok=True)
    with open(os.path.join('动物农场', ChaTITLE + '.txt'), 'w', encoding = 'utf-8', newline = '') as f:
        f.write(ChaCont)
    
    
if __name__=='__main__':
    # get: loggin the html
    html_g = requests.get('https://www.kanunu8.com/book3/6879/').content.decode('GBK')      # use 'GBK' instead of 'UTF-8'
    #print(html_g)

    # get: subURLs
    maintext = re.findall('<strong>正文(.*?)<td>&nbsp;</td>', html_g, re.S)[0]
    suburl_list = get_subURL('https://www.kanunu8.com/book3/6879/', maintext)
    
    '''
    # multithreadx
    title_list = []
    content_list = []
    pool = Pool(5)
    [title_list, content_list] = pool.map(spyPieChap, suburl_list)
'''
    # singlethread
    title_list = []
    content_list = []
    for index in range(len(suburl_list)):
        [temp_tit, temp_con] = spyPieChap(suburl_list[index])
        title_list.append(temp_tit)
        content_list.append(temp_con)
    
    # save
    for each in range(len(title_list)):
        saveFILES(title_list[each], content_list[each])
    
    
