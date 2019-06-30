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





