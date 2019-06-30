
# ＭySQL python 交互模块，创建对象时需传参库名
# 被 insert 导入

from pymysql import *

class Mysqlpython:
    def __init__(self,database,host="localhost",
                user = "root",password = "123456",
                charset="utf8",port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port
        
    def __open(self):		#创建数据库链接对象,调用初始化属性
        self.db = connect(host=self.host,
                        user=self.user,
                        password=self.password,
                        database=self.database,
                        charset=self.charset)
        self.cur = self.db.cursor()	# 创建游标对象

    def __close(self):		#关闭库对象与游标对象
        self.cur.close()
        self.db.close()

    def zhixing(self,sql,L=[]):		#执行ＳＱＬ命令，需传参MYSQL命令字符串
        self.__open()
        self.cur.execute(sql,L)
        self.db.commit()
        self.__close()

    def all(self,sql,L=[]):	# 读取并返回查询的信息,需传参MYSQL命令字符串
        self.__open()
        self.cur.execute(sql,L)
        result = self.cur.fetchall()
        self.__close()
        return result

# if __name__ == "__main__":
#     sqlh = Mysqlpython("db5")

#     upd = 'update t1 set score=0 where name ="李白"'
#     sqlh.zhixing(upd)

#     r = sqlh.all("select * from t1")
#     print(r)
