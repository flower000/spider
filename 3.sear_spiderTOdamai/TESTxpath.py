# -*- coding: utf-8 -*-
import lxml.html

source = '''
<html>
  <head>
    <title>测试</title>
  </head>
  <body>
    <div class="useful">
      <ul>
        <li class="info">我需要的信息1</li>
        <li class="info">我需要的信息2</li>
        <li class="info">我需要的信息3</li>
      </ul>
    </div>
    <div class="useful">
      <ul>
        <li class="info">我需要的信息4</li>
        <li class="info">我需要的信息5</li>
        <li class="info">我需要的信息6</li>
      </ul>
    </div>
    <div class="useless">
      <ul>
        <li class="info">垃圾1</li>
        <li class="info">垃圾2</li>
      </ul>
    </div>
  </body>
</html>
'''

selector = lxml.html.fromstring(source)
useful = selector.xpath('//div[@class="useful"]')
info_list = useful[1].xpath('ul/li/text()')
print(info_list)

# string(.)
data = selector.xpath('//body')[0]
data2str = data.xpath('string(.)')
print(data2str)


