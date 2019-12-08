# -*- coding: utf-8 -*-
import re
import csv
import os

with open(r'text.txt', encoding='utf-8') as f:
    source = f.read()

result_list = []
every_reply = re.findall('<a style="" target="_blank" class="p_author_face "(.*?)<div class="user-hide-post-position"></div><div class="d_author">', source, re.S)

for each in every_reply:
    result = {}
    temp_content = []
    # name extract
    result['username'] = re.findall('username="(.*?)"', each, re.S)[0]
    # content extract
    #result['content'] = re.findall('class="d_post_content j_d_post_content  clearfix" style="display:;">(.*?)</div><br>            </cc><br><div class="user-hide-post-down" style="display: none;"></div>', each, re.S)[0].replace('            ','')
    temp_content = re.findall('class="d_post_content j_d_post_content  clearfix" style="display:;">(.*?)</div><br>            </cc><br><div class="user-hide-post-down" style="display: none;"></div>', each, re.S)[0].replace('            ','')
    deletePart = set(re.findall('(<.*?>)', temp_content, re.S))
    deletePart = list(deletePart)
    for piece in deletePart:
        temp_content = temp_content.replace(piece,'');
    result['content'] = temp_content   
    # reply_time extract
    result['reply_time'] = re.findall('date&quot;:&quot;(2018.*?)&quot', each, re.S)[0]
    result_list.append(result)
    
with open(r'tieba.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['username','content','reply_time'])
    writer.writeheader()
    writer.writerows(result_list)
