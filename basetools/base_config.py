#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# author : fengzz

class Config(object):
    configs = {}

    def __init__(self, path=None):
        if path:
            self.load(path)

    def load(self, path):
        import configparser
        cf = configparser.ConfigParser()
        cf.read(path)
        for section in cf.sections():
            for k, v in cf.items(section):
                self.configs[section + '_' + k] = v

    def get(self, section, key):
        return self.configs.get(section + "_" + key, None)


def load_config(path='base.conf'):
    cfg = Config()
    cfg.load(path)


def get_config(section, keys):
    cfg = Config()
    if isinstance(keys, list):
        return [cfg.get(section, key) for key in keys]
    else:
        return cfg.get(section, keys)


def get_log_config_file():
    return get_config("log", "config_file")


def get_log_path():
    log_path = get_config("log", "log_path")
    if not log_path:
        log_path = "./"
    return log_path
