#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 启动:
# python checknews.py > checknews.out 2>&1 &
# 中文乱码的临时解决办法：
# export LESSCHARSET=utf-8

import os
import time
import logging
import traceback
from unittest import TestCase, skip

import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s',
    level=logging.INFO
)


class NewsMonitor:
    def __init__(self, url, pattern):
        self.url = url
        self.pattern = pattern
        self.last_title = None

    def check(self):
        logging.info('checking...')
        # requests frozen because server does not respond
        # https://stackoverflow.com/a/45267074
        r = requests.get(self.url, timeout=60)
        r.encoding = r.apparent_encoding
        parsed_html = BeautifulSoup(r.text, features="html.parser")
        # news = parsed_html.body.select('div.list-content ul li')
        news = parsed_html.select(self.pattern)
        title = news[0].find('a').text.strip()
        if self.isNewsFound(title):
            NewsMonitor.notifyByEmail(title, self.url)

    def isNewsFound(self, title):
        logging.info(title)
        if not self.last_title:
            try:
                with open('tmp.data') as f:
                    self.last_title = f.read()
            except FileNotFoundError:
                print('tmp.data does not exist')
            if not self.last_title:
                self.last_title = title
        if title != self.last_title:
            self.last_title = title
            with open('tmp.data', 'w') as f:
                f.write(title)
            return True
        return False


    @staticmethod
    def notifyByEmail(text, url, receiver='734692788@qq.com'):
        logging.info('send email...')
        #qq邮箱smtp服务器
        host_server = 'smtp.qq.com'
        #sender_qq为发件人的qq号码
        sender_qq = 'yanxurui1993@qq.com'
        #pwd为qq邮箱的授权码
        pwd = 'qhdvgvfjxjrebfhc'
        #发件人的邮箱
        sender_qq_mail = sender_qq
        #收件人邮箱

        #邮件的正文内容
        mail_content = '{}\n\r{}'.format(text, url)
        #邮件标题
        mail_title = '有新通知！'

        #ssl登录
        smtp = SMTP_SSL(host_server)
        #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        # smtp.set_debuglevel(1)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)

        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()


class TestNewsMonitor(TestCase):
    @skip("reason for skipping")
    def testNotifyByEmail(self):
        NewsMonitor.notifyByEmail('hello world', 'fake url', receiver='yxr1993@gmail.com')

    def testDoWorkIfNewsFound(self):
        try:
            os.remove('tmp.data')
        except OSError:
            pass

        monitor = NewsMonitor('fake url', 'fake pattern')
        title1 = 'good news'
        self.assertFalse(monitor.isNewsFound(title1))
        self.assertEqual(title1, monitor.last_title)

        self.assertFalse(monitor.isNewsFound(title1))
        self.assertEqual(title1, monitor.last_title)

        title2 = 'bad news'
        self.assertTrue(monitor.isNewsFound(title2))
        self.assertEqual(title2, monitor.last_title)
        with open('tmp.data') as f:
            self.assertEqual(title2, f.read())

        monitor = NewsMonitor('fake url', 'fake pattern')
        self.assertFalse(monitor.isNewsFound(title2))

        title3 = 'so good!'
        monitor = NewsMonitor('fake url', 'fake pattern')
        self.assertTrue(monitor.isNewsFound(title3))


def main():
    inteval = 60
    # url = 'http://www.ynqjrs.gov.cn/subsite_list.asp?id=12&lb=1&zl=0&Twzbh=2'
    # url = 'http://www.yn.gov.cn/zwgk/gsgg/'
    url = 'http://www.qjdj.gov.cn/news/c/tzgg286/list_1.htm'
    pattern = '.main .content .right_list .list-content ul'
    monitor = NewsMonitor(url, pattern)
    while True:
        try:
            monitor.check()
        except:
            logging.error('\n'+traceback.format_exc())
        time.sleep(inteval)


if __name__ == '__main__':
    main()
