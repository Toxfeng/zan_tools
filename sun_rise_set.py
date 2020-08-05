#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# author : fengzz

import math
import datetime
import time
from math import pi


def SunRiseSet(location, today, zone=8, sunrise=True):
    """
    根据经纬度信息，获取昨日此经纬度点的日出日落时间
    :param location: {"longitude" : 116.407013, "latitude" : 39.926588}
    :param today: datetime.date.today()
    :param zone: 8
    :param sunrise: 日出，日落
    :return: timestamp
    """
    # 纬度
    Glat = location.get("latitude", "39.54")
    # 经度
    Long = location.get("longitude", "116.23")
    yesterday = today - datetime.timedelta(days=1)
    yesterday_begin = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
    h = -0.833
    UTo = 180
    # 计算格林威治时间公元2000年1月1日到今日天数days
    days = (yesterday - datetime.date(2000, 1, 1)).days
    while True:
        # 计算格林威治时间公元2000年1月1日到今日的世纪数
        t = (days + UTo / 360.0) / 36525
        # 计算太阳的平黄径L
        L = 280.460 + 36000.770 * t
        # 计算太阳的平近点角G
        G = 357.528 + 35999.050 * t
        # 计算太阳的倾角E
        E = 23.4393 - 0.0130 * t
        # 计算太阳的黄道经度w
        w = L + 1.915 * math.sin(G * pi / 180) + 0.020 * \
                                                 math.sin(2 * G * pi / 180)
        # 计算太阳的偏差p
        p = 180 / pi * math.asin(math.sin(pi / 180 * E)
                                 * math.sin(pi / 180 * w))
        # 计算格林威治时间的太阳的时间角GHA
        GHA = UTo - 180 - 1.915 * math.sin(G * pi / 180) - 0.020 * math.sin(
                2 * G * pi / 180) + 2.466 * math.sin(2 * w * pi / 180) - 0.053 * math.sin(4 * w * pi / 180)
        # 计算修正值

        e = 180 / pi * math.acos(
                (math.sin(h * pi / 180) - math.sin(Glat * pi / 180) * math.sin(
                        p * pi / 180)) / (math.cos(Glat * pi / 180) * math.cos(p * pi / 180)))
        if sunrise:
            UT = UTo - (GHA + Long + e)
        else:
            UT = UTo - (GHA + Long - e)

        if UT > UTo:
            d = UT - UTo
        else:
            d = UTo - UT
        if abs(d) > 0.1:
            UTo = UT
        else:
            UT = ((UT / 15) + zone) * 3600
            timestamp = int(UT + yesterday_begin)
            return timestamp


if __name__ == "__main__":
    location = {"longitude": 116.407013, "latitude": 39.926588}
    today = datetime.date.today()
    # 日出时间
    print(SunRiseSet(location, today, zone=8, sunrise=True))
    # 日落时间
    print(SunRiseSet(location, today, zone=8, sunrise=False))
