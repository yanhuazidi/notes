[TOC]



## 模型

**基础：**

- 每一个模型都映射一张数据库表；
- 每个模型都是一个 Python 的类，这些类继承 `django.db.models.Model`；
- 模型类的每个属性都相当于一个数据库的字段；
- 利用这些，Django 提供了一个自动生成访问数据库的 API。

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

上面的 `Person` 模型会创建一个如下的数据库表：

```sql
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```





## 字段

模型中每一个字段都应该是某个 `Field`类的实例， Django 利用这些字段类来实现以下功能：

- 字段类型用以指定数据库数据类型（如：`INTEGER`, `VARCHAR`, `TEXT`）。
- 在渲染表单字段时默认使用的 HTML 视图 (如： `<input type="text">`, `<select>`)。
- 基本的有效性验证功能，用于 Django 后台和自动生成的表单。



## 增加数据

1. `Entry.object.create(属性=值，属性=值)`
   Entry : 实体类类名，可以表示任意一个实体类
   返回值 : 将创建好的实体对象进行返回

2. 创建 Entry 对象，并通过对象`.save()`进行保存

   obj = Entry(属性=值，属性=值)
   obj.属性 = 值
   obj.save()
   注意 : 该方法无返回值， obj会被重新赋值

3.  使用字典创建对象，并通过 save()进行保存
               dic = {
                   "属性" : "值",
               }
   obj = Entry(**dic)
   obj.save()

   注意 : 该方法无返回值， obj会被重新赋值



## 查询数据

Entry.objects 属性调用查询接口

1. 基本查询操作
            语法： all()
            用法 : Entry.objects.all()
            返回 : QuerySet[对象]  查询的结果以对象封装在列表中
        
2. 查询返回指定列

       语法: values() | values("列1"，"列2")
                  用法 :
                      Entry.objects.values("列1"，"列2")
                      Entry.objects.all().values("列1"，"列2")
                  返回 : QuerySet[{key:value},]  会将查询出来的部分列封装到字典中，再封装到列表中

3. 查询返回指定列 
                  语法: values_list('列1','列2')
                  用法: 同上
                  返回值: QuerySet[(),]  会将查询出来的部分列封装到元组中，再封装到列表中

4. 只查询一条数据
                  语法 : get(条件) （条件只能是 属性=值 ）
                  作用 : 查询只能返回一条数据
                  返回值 : 对象
                  用法 : Entry.objects.get('条件')
                      注意: 该方法只能返回一条数据，查询结果多余一条或没有就报错

5. filter(**kwargs):　返回符合筛选条件的数据集
                  语法: filter(条件)
                  用法 : Entry.objects.filter('条件')
                  返回值 : QuerySet[对象,]

      ```python
      1.查询 id 为1的Book的信息
                          list = Book.objects.filter(id=1)
      查询 publicate_date 为 2015-10-12 的 Book
                          list = Book.objects.filter(publicate_date='2015-10-12')
                      
                      books = Book.objects.filter(id=1,publicate_date='2015-10-12')
      ```



如果需要非等值条件查询的话，可以使用 Django提供的查询谓词来实现




    
    
    如果需要非等值条件查询的话，可以使用 Django提供的查询谓词来实现
            谓词	 含义	        示例	                                       等价SQL语句
        exact	  精确等于	Comment.objects.filter(id__exact=14)	                select * from Comment where id=14
        iexact    大小写不敏感的等于Comment.objects.filter(headline__iexact=’I like this’)	select * from Comment where upper(headline)=’I LIKE THIS’
        contains  模糊匹配	Comment.objects.filter(headline__contains=’good’)	 select * from Comment where headline like “%good%”
        in	      包含	Comment.objects.filter(id__in=[1,5,9])	               select * from Comment where id in (1,5,9)
        gt	      大于	Comment.objects.filter(n_visits__gt=30)	                  select * from Comment where n_visits>30
        gte	     大于等于	Comment.objects.filter(n_visits__gte=30)	          select * from COmment where n_visits>=30
        lt	      小于	 	 
        lte	    小于等于	
    
        startswith	以…开头	Comment.objects.filter(body_text__startswith=”Hello”)	select * from Comment where body_text like ‘Hello%’
        endswith	以…结尾	
    
        range	    在…范围内	start_date=datetime.date(2015,1,1)end_date=datetime.date(2015.2.1)
                Comment.objects.filter(pub_date__range=(start_date,end_date))	
                select * from Comment where pub_datebetween ‘2015-1-1’ and ‘2015-2-1’
    
        year	年	Comment.objects.filter(pub_date__year=2015)	
                select * from Comment where pub_datebetween ‘2015-1-1 0:0:0’ and ‘2015-12-31 23:59:59’
        month	月	 	 
        day	日	 	 
        week_day	星期几	 
    
        isnull	是否为空	Comment.objects.filter(pub_date__isnull=True)	
                            select * from Comment where pub_date is NULL


                Entry.objects.filter(属性__谓词=值)
    
            6.  exclude(**kwargs): 返回不符合筛选条件的数据集
                语法: exclude(条件)
                用法 : Entry.objects.exclude(条件)
    
            7. 排序查询
                语法 : order_by()
                用法 : Entry.objects.order_by("Field","-Field")
                默认是升序，如果想要降序在列名前添加 - 即可
    
            8. 聚合查询(不带分组)
    
                from django.db.models import aggregate,annotate,Avg...
    
                语法: aggregate()
                用法: Entry.objects.aggregate(名 = 聚合函数('列'))
                    聚合函数:
                        1. Avg():平均值
                        2. Sum()
                        3. Count()
                        4. Min()
                        5. Max()
    
                带分组聚合查询
                    语法: annotate()
                    用法 : Entry.objects.values('分组Field').annotate(聚合Field=聚合函数(Field)).values('分组Field'，'聚合Field')



修改
    1. 查询
        得到查询实体对象 / QuerySet

    2. 改
        通过对象的属性修改对象的值
    
    3. 保存
        实体对象.save()
    
      快捷方式
        QuerySet:
            QuerySet 的 update(属性=值，属性=值) 能实现批量修改+保存

删除
    1. 删除单个对象
        au = Entry.objects.get(条件)
        au.delete()
        
    2. 批量删除
        au = Entry.objects.all()
        au.delete()

5 . F查询和 Q查询

    F 查询
        1. 作用
            在执行过程中获取某列的值
        2. 语法：
            from django.db.models import F
    
            Entry.objects.all().update(age=F('age')+10) 查询并修改某列的值再返回
    
    Q 查询
        1. 作用：
            在条件中充当或(or)的实现方式
    
        2. 语法：
            from django.db.models import Q
    
            Q(条件1)|Q(条件2)
    
            Entry.objects.filter(Q(id=1)|Q(age=30))

6. 原生的数据库操作方法
    1. 查询
        函数 : raw(sql)
        语法 : Entry.objects.raw(sql)
        返回 : QuerySet

    2. 增删改 
        from django.db import connection
        def doSql(request):
            with connection.cursor() as cursor
                sql = "insert .. .."
                cursor.execute(sql)
            return 

