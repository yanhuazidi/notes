



```python
import pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
#在实例化的时候，将属性cursor设置为pymysql.cursors.DictCursor
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

#查询
sql = "select * from group where id=%s"
L = ['2']
cur.execute(sql,L)#L里的参数会按位置传递给 %s，   %s只接收字符串参数
db.commit()
result = cursor.fetchall()
cursor.close()
db.close()
print(result )
#运行结果
[{'id': 2, 'name':'aaa', 'is_running':True, 'passwd': '321'}]

#修改
sql = 'update queue set name=%s,passwd=%s where id=%s'
username = 'bbbb'
password = 333
L =[username ,password,'2']
cur.execute(sql,L)
db.commit()
```



