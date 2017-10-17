#!/usr/bin/env
# coding=utf-8
from pprint import pprint

import itchat
import requests

KEY = '1a463d64b18b45d0930c68efe74d45e6'

def auto_reply(msg, uid):
    url = "http://www.tuling123.com/openapi/api"
    body = {
        'key': KEY,
        'info': msg.encode('utf8'),
        'userid': uid
    }
    r = requests.post(url, json=body)
    r = r.json()
    print('tuling resp:'); pprint(r)
    if r['code'] == 100000:
        return r['text'].replace('<br>', ' \n')
    elif r['code'] == 200000:
        return '%s\n%s' % (r['text'].replace('<br>','\n'), r['url'])
    else:
        return r['text']

@itchat.msg_register('Text')
def text_reply(msg):
    logging.debug(msg)
    return auto_reply(msg['Text'], msg['FromUserName'])

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    print('received msg:'); pprint(msg)
    if msg['isAt']:
        return u'@%s %s' % (msg['ActualNickName'], auto_reply(msg['Text'], msg['FromUserName']))

itchat.auto_login(True)
itchat.run()
