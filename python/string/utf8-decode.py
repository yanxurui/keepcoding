#!/usr/bin/env
# coding=utf-8

import urllib
import quopri

with open('in.txt', 'w') as f:
    f.write(repr('你好').replace("'", ''))

with open('in.txt', 'r') as f:
    url = f.read()
    # it's different than this
    # url = '\xe4\xbd\xa0\xe5\xa5\xbd'
    print('----%s' % url)
    # url2 = url.decode('utf8')
    url2 = url.decode('string-escape') # only this works
    # url2 = quopri.decodestring(url)
    
    print('++++%s' % url2)
