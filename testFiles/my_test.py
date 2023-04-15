import ast
import base64
import sys
import urllib.request

import redis
import pymysql
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QVBoxLayout, QPushButton

from client.utils.models import User


class TestWidget(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    # redisPool = redis.ConnectionPool(host='47.113.229.66', port=6379)
    # r = redis.Redis(connection_pool=redisPool)
    # user = User('10001', '111111', '飞翔的企鹅')
    # mysql = pymysql.connect(host="47.113.229.66", port=3306, user='root', password='111111', database='pysocket')
    # cursor = mysql.cursor()
    # sql = """select * from channel_info"""
    # try:
    #     execStatus = cursor.execute(sql)
    #     result = cursor.fetchall()
    #     mysql.commit()
    #     print(result)
    #     print(type(result))
    #     print(len(result))
    #     result = list(result)
    #     print(result)
    #     # print(result[2])
    # except Exception as e:
    #     mysql.rollback()
    #     print(e)
    # cursor.close()
    # print(mysql.ping(True))
    # mysql.close()
    pass