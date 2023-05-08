import ast
import os
import sys
import time

import pymysql
import redis
from pathlib import Path

if __name__ == '__main__':
    db = pymysql.connect(host="47.113.229.66", port=3306, user='root', password='111111', database='pysocket')
    cur = db.cursor()
    cur.execute("""select max(account) from user""")
    res = cur.fetchone()
    print(res)
    print(type(res))
