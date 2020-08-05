#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# author : fengzz

import sys
import logging

logger = logging.getLogger()
debug = logger.debug
info = logger.info
error = logger.error
warning = logger.warning


def config(log_name, log_path=None, log_level=logging.INFO, out=True):
    new_logger = logging.getLogger(log_name)
    new_logger.setLevel(log_level)
    if out is True:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
                ('[%(asctime)s](%(levelname)s)%(name)s: %(message)s'))
        handler.setFormatter(formatter)
        handler.setLevel(log_level)
        new_logger.addHandler(handler)
    if log_path:
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter(
                ('[%(asctime)s](%(levelname)s): %(message)s'))
        handler.setFormatter(formatter)
        handler.setLevel(log_level)
        new_logger.addHandler(handler)

    global logger
    global debug
    global info
    global error
    global warning

    logger = new_logger
    debug = logger.debug
    info = logger.info
    error = logger.error
    warning = logger.warning
