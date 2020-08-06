#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# author : fengzz

import json
import requests
import urllib.request
from bs4 import BeautifulSoup
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import threading
import base_time


def getWord():
    """
    通过爱词霸获取每日一句的内容
    :return: 当日美句
    """
    url = 'http://open.iciba.com/dsapi/'
    response = requests.get(url)
    content = json.loads(response.text)
    EnglishWord = content.get("content")
    ChineseWord = content.get("note")
    return EnglishWord + "\n" + ChineseWord


def getWeather(city):
    """
    获取今日天气预报内容
    :return:天气查询内容
    """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    url = "http://www.tianqi.com/" + city
    req = urllib.request.Request(url, headers=header)
    page = urllib.request.urlopen(req)
    html = page.read()
    # 使用html.parser解析
    soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
    today_weather = ""
    for node in soup.find_all('dd'):
        temp = node.get_text()
        if temp.find(('[切换城市]')):
            temp = temp[:temp.find('[切换城市]')]
        today_weather += temp
    result = "".join([s for s in today_weather.splitlines(True) if s.strip()])
    return result


def pushEmail(word):
    """
    通过qq邮箱发送信息
    """
    HOST = 'smtp.qq.com'
    SUBJECT = '每日天气 小亲亲'
    FROM = '947456230@qq.com'
    TO = '947456230@qq.com'
    message = MIMEMultipart('related')
    # 发送邮件正文到对方的邮箱中
    message_html = MIMEText(word, 'plain', 'utf-8')
    message.attach(message_html)

    # 设置邮件发件人
    message['From'] = FROM
    # 设置邮件收件人
    message['To'] = TO
    # 设置邮件标题
    message['Subject'] = SUBJECT
    email_client = smtplib.SMTP_SSL()
    email_client.connect(HOST, '465')
    # 登陆密钥需要自己通过qq邮箱申请
    result = email_client.login(FROM, 'miyao')
    email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
    email_client.close()


def timeTimer(interval, city):
    while True:
        result_word = getWord()
        result_weather = getWeather(city)
        word = result_word + "\n" + result_weather
        pushEmail(word)
        time.sleep(interval)


if __name__ == "__main__":
    # 获取当前时间戳
    now_time = base_time.getNowTimeStamp()

    # 获取明天北京8点时间戳
    tomorrow_time = base_time.getDayBegin(timestamp=now_time) + base_time.daySeconds()

    # 获取距离明天8点时间，单位为秒
    timer_start_time = (tomorrow_time - now_time)

    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
    timer = threading.Timer(timer_start_time, timeTimer, (base_time.daySeconds(), "chaoyang"))
    timer.start()
