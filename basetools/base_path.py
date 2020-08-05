#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : fengzz

import os
import sys


def getFilePath(dir=False):
    """
    获取文件的绝对路径，当dir为True时返回文件所在目录和文件名
    :param dir: boolean True/False
    :return:
    """
    if dir is True:
        dir_name, file_name = os.path.split(os.path.abspath(sys.argv[0]))
        return dir_name, file_name
    return os.path.abspath(sys.argv[0])


def getFatherPath():
    """
    获取文件所在目录的父级目录
    :return: dir
    """
    return os.path.dirname(os.path.dirname(getFilePath()))


def getFileSplit(path):
    """
    获取文件路径名，文件名和后缀名
    :param path:
    :return:tuple
    """
    try:
        if os.path.isfile(path):
            file = os.path.split(path)
            return file[0], file[1].split(".")[0], "%s%s" % (".", file[1].split(".")[1])
        if os.path.isdir(path):
            return "path [%s] is dir please input file path" % path
    except Exception as e:
        return e


def getJoinPath(path, file_name, f=''):
    """
    拼接路径
    :param path: 文件路径
    :param file_name: 文件名称
    :return: 完整文件路径名称
    """
    try:
        if "." in file_name:
            full_path = os.path.join(path, file_name)
        else:
            file_name = file_name + f
            full_path = os.path.join(path, file_name)
        return full_path
    except Exception as e:
        return e


def batchRename(dir_path, word="-副本"):
    """
    批量修改路径下文件名称
    :param dir_path: 目录
    :param word: 后缀名称
    :return: 修改后名称
    """
    items = os.listdir(dir_path)
    for item in items:
        item_path = getJoinPath(dir_path, item)
        if os.path.isfile(item_path):
            new_name = os.path.splitext(item_path)[0] + word + os.path.splitext(item_path)[1]
            os.rename(item_path, new_name)


def walkExtFile(dir_path, ext):
    """
    循环遍历指定目录下文件，返回指定格式文件
    :param dir_path: 文件目录
    :param ext: 后缀格式 eg:.txt
    :return: list
    """
    files_list = []
    for path, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_path = getJoinPath(path, file_name)
            file_ext = getFileSplit(file_path)[2]
            if ext == file_ext:
                files_list.append(file_path)
    return files_list

def sortFile(dir_path, reverse=False):
    """
    对指定目录下文件按照创建时间排序
    :param dir_path: 指定目录
    :param reverse: 是否逆序
    :return: 排序后的文件列表
    """

    file_list = os.listdir(dir_path)
    # 正向排序
    file_list.sort(key=lambda file_name: os.path.getmtime(getJoinPath(dir_path, file_name)))
    # 反向排序
    if reverse is True:
        file_list.sort(key=lambda file_name: os.path.getmtime(getJoinPath(dir_path, file_name)), reverse=reverse)
    return  file_list




