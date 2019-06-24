# coding:utf-8

import pymysql
import os

# print(os.getenv("MYSQL_DB"))
# print(os.getenv("MYSQL_USER"))
DB_CONF = {"host":os.getenv('MYSQL_HOST'), "user" :os.getenv('MYSQL_USER'), "password" :os.getenv('MYSQL_PASSWORD'), "db":os.getenv('MYSQL_DB'),"charset":os.getenv('MYSQL_CHARSET'), "autocommit" :os.getenv('MYSQL_AUTOCOMMIT')}
# DB_CONF = {"host": "115.28.108.130",
#            "user": "test",
#            "password": 123456,
#            "db": "longtengserver",
#            "charset": "utf8",
#            "autocommit": True}


class DB(object):
    def __init__(self):
        # self.conn = pymysql.connect(host='115.28.108.130',db="longtengserver",port=3306,user='test',password='123456',charset='utf8',autocommit=True)
        self.conn = pymysql.connect(**DB_CONF)

        self.cur = self.conn.cursor()

    def excu(self, sql):
        print("执行的sql语句：" + sql)
        self.cur.execute(sql)
        res = self.cur.fetchall()
        print(res)
        return res


class LongTengServer(DB):

    def delete_card(self,card_number):
        print("添加加油卡"+card_number)
        sql = f'delete from cardinfo where cardNumber={card_number}'


    def check_card(self,card_number):
        print("查询加油卡"+card_number)
        sql = f"select cardnumber from cardinfo where cardNumber={card_number}"
        res = self.excu(sql)
        return True if res else False

    def close(self):
        self.close()

        # print()
#
# 只有调用本身的模块时，才执行此语句
if __name__ == "__main__":  # __name__,模块名如果调用本身的模块则等于本身模块名，如果调用的其他模块，则是其他模块名
    db = DB()
    db.excu("select * from cardinfo where cardNumber=111001")
    # print()
    SERVER = LongTengServer()
    SERVER.check_card(3322112)
    print()
