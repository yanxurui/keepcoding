#!/usr/bin/env
# coding=utf-8

import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

## 0. paramters
mobile='18811409643'
pwd='yxr123'
doctorName='赵作涛'
url='http://www.bjguahao.gov.cn/dpt/appoint/12-200004215.htm?week=2'
when = 'pm' # am or pm

browser = webdriver.Chrome()

browser.get('http://www.bjguahao.gov.cn')
assert u'北京市预约挂号统一平台' in browser.title

## 1. login
browser.find_element_by_id('bdtj1').click()
login_mobile = browser.find_element_by_id('mobileQuickLogin')
login_mobile.send_keys(mobile)
login_pwd = browser.find_element_by_id('pwQuickLogin')
login_pwd.send_keys(pwd)
login_submit = browser.find_element_by_id('quick_login')
login_submit.click()

wait = WebDriverWait(browser, 5)
wait.until(EC.visibility_of_element_located((By.LINK_TEXT, '个人中心')))

## 2. refresh
count = 0
while True:
    browser.get(url)
    td=browser.find_element_by_xpath('//table/tbody/tr[%d]/td[last()]' % (2 if when=='am' else 3))
    if u'预约' in td.text:
        break
    time.sleep(1)
    count = count + 1
    print('%ds...' % count)

## 3. order
td.click()

button = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '%s')]/ancestor::div[1]//a" % doctorName))
)
button.send_keys(Keys.RETURN)
# button is not clickable because it's covered by other element
# have look at https://stackoverflow.com/questions/11908249/debugging-element-is-not-clickable-at-point-error
# below is an alternative method:
# browser.find_element_by_id('float-div-close').click()
# button.click()

browser.find_element_by_id('btnSendCodeOrder').click()

## 4. todo: enter the verification code automatically
# smsVerifyCode = raw_input('Enter 短信验证码：')
# browser.find_element_by_id('Rese_db_dl_dxyzid').send_keys(smsVerifyCode)
# browser.find_element_by_link_text('预约').click()

