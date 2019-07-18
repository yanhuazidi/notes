import pymysql

mydb = pymysql.connect(host='192.168.0.15',user='wei',password='123456',database='webdb',charset='utf8',port=3306)
cursor = mydb.cursor()
sql = 'select * from wife'
cursor.execute(sql)  #只能一条一条插入
mydb.commit()
cursor.close()
mydb.close()