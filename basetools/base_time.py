#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# author : fengzz

import time
import datetime


def daySeconds():
    return 86400


def getDayBegin(timestamp):
    """
    获取当日时区起始时间戳
    :param timestamp: 1596543455
    :return: 1577808000
    """
    return timestamp - timestamp % daySeconds()


def getDayUtcBegin(timestamp):
    """
    获取当日UTC起始时间戳
    :param timestamp: 1596543455
    :return: 1577808000
    """
    return int(time.mktime(datetime.date.today().timetuple()))


def getMonthBegin(timestamp):
    """
    获取当月起始时间戳
    :param timestamp: 1596543455
    :return:1577808000
    """
    today = datetime.date.today()

    return int(time.mktime(datetime.date(today.year, today.month, 1).timetuple()))


def getYearBegin(timestamp):
    """
    获取当年起始时间戳
    :param timestamp: 1596543455
    :return: 1577808000
    """
    today = datetime.date.today()

    return int(time.mktime(datetime.date(today.year, 1, 1).timetuple()))


def getTimedeltaTime(timestamp=False, days=0, hours=0, minutes=0, seconds=0):
    """
    获取当前时间延迟后的时间
    :param days:int
    :param hours:int
    :param minutes:int
    :return:1596596111.0
    """
    d1 = datetime.datetime.now()
    d2 = (d1 + datetime.timedelta(
            days=days, hours=hours, minutes=minutes, seconds=seconds)).strftime("%Y-%m-%d %H:%M:%S")
    if timestamp is True:
        d2 = time2timestamp(d2)

    return d2


def getMonthDays():
    """
    获取当月天数与最后一天的日期
    :return:
    """
    d1 = datetime.datetime.now()
    if d1.month == 12:
        next_month_first = datetime.date(d1.year + 1, 1, 1)
    else:
        next_month_first = datetime.date(d1.year, d1.month + 1, 1)
    d2 = next_month_first - datetime.timedelta(1)
    return d2, d2.day


def getNowTimeStamp(secs=False):
    """
    获取当前时间戳
    :param secs: 表示是否返回带毫秒时间戳
    :return: 1596544773.3274052， 1596544773
    """
    try:
        if secs is True:
            return time.time()
        return int(time.time())
    except Exception as e:
        return e


def getNowTime(secs=False):
    """
    获取当前格式化时间
    :return: str "2020-08-04 20:21:09"
    """
    now = time.time()
    try:
        if secs is True:
            head = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
            suffix_secs = (now - int(now)) * 1000
            return "%s.%03d" % (head, suffix_secs)
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
    except Exception as e:
        return e


def timestamp2time(timestamp, date=False):
    """
    将时间戳转换成格式化时间
    :param timestamp: int 1596543455
    :param date: 决定返回是否带有时间
    :return: str "2020-08-04 20:21:09"  or "2020-08-04"
    """
    try:
        if isinstance(timestamp, str):
            timestamp = float(timestamp)
        if date is True:
            timestampStr = time.strftime("%Y-%m-%d", time.localtime(timestamp))
        else:
            timestampStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        return timestampStr
    except Exception as e:
        return e


def time2timestamp(timeStr, date=False):
    """
    将格式化的时间转换成时间戳
    :param timeStr: "2020-08-04 20:17:35"
    :return: float 1596543455.0
    """
    try:
        timeStr = timeStr.strip()
        if date is True:
            return time.mktime(time.strptime(timeStr, "%Y-%m-%d"))

        return time.mktime(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S"))

    except Exception as e:
        return e


