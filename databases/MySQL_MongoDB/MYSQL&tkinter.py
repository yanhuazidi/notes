
# MYSQL事务回朔 与　tkinker 交互
　
import pymysql
import tkinter

windows = tkinter.Tk()
windows.title("t1")
windows.geometry("900x300")
var = tkinter.StringVar()
l = tkinter.Label(windows,textvariable=var,bg='yellow',fg='red',font=("宋体",20))

my = pymysql.connect("localhost","root","123456"
                    ,database = "db5",charset = "utf8")
cursor = my.cursor()
try:
    cursor.execute("use db5")

    shur =input("输入记录:")
    # name_ =input("输入姓名:")
    if shur!='':
        cursor.execute('insert into t1(name,score) values(%s)'%shur)
    # if name_!='':
    #     cursor.execute('delete from t1 where name=%s'%name_)
    # cursor.execute('update t1 set score=98 where name="李白"')
    cursor.execute("select * from t1;")
    # a1=cursor.fetchone()
    # a2=cursor.fetchmany(2)
    a3 = cursor.fetchall()
    var.set(a3)
    my.commit()
    print("ok")
except Exception as e:
    my.rollback()
    print(e)
cursor.close()
my.close()
l.pack()
windows.mainloop()
