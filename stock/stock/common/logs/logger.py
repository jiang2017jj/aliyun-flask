# -*- coding = utf-8 -*-
"""
@time:2020-06-18 09:24:40
@project:stock
@file:logger.py
@author:Jiang ChengLong
"""

"""
用于记录任务执行的信息。
由于celery的运行是独立的，在flask中定义的logger对象的配置在celery的程序中是失效的，必须使用get_task_logger创建logger;
指定celery日志的输出等级，通过启动时用--loglevel参数来指定；
"""

# import enum
import datetime


# class LogLevel(enum.Enum):
#     """
#     # debug为调试信息
#     # info为日志默认输出等级
#     # warn为requests请求异常信息
#     # error为clover异常信息
#     """
#     DEBUG = 1
#     INFO = 2
#     WARN = 3
#     ERROR = 4


class Logger(object):

    logs = []

    @classmethod
    def log(cls, message, step, tag=[], level='info'):
        cls.logs.append({
            'time': datetime.datetime.now(),
            'level': level,
            'step': step,
            'message': message,
            'tag': tag
        })

    @classmethod
    def clear(cls):
        cls.logs = []

    @classmethod
    def to_dict(cls):
        def translate(data):
            data['time'] = data['time'].strftime("%Y-%m-%d %H:%M:%S")
            # data['level'] = data['level'].name.lower()
            return data
        return [translate(log) for log in cls.logs]
