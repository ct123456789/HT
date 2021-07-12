# -*- coding: utf-8 -*-
'''
@Time    : 2021/7/5 16:52
@Author  : Achen
@File    : handle_db.py
'''
import pymysql

class HandleDB(object):

    def __init__(self, link, user, passwd, db):
        self.link = link
        self.user = user
        self.passwd = passwd
        self.db = db

    def linkMySqlDataSource(self):
        try:
            conn = pymysql.connect(host=self.link, user=self.user, passwd=self.passwd, db=self.db)
            cursor = conn.cursor()
            return conn, cursor
        except Exception:
            raise Exception


    def selectMySqlData(self, sql):
        conn, cursor = self.linkMySqlDataSource()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            if len(data) == 0:
                raise ValueError("查询无结果")
            return data
        finally:
            cursor.close()
            cursor.close()
