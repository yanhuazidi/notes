## 

[TOC]



**这个文档包含字段的所有API引用，包括Django提供的字段选项和字段类型。**

------

如果内置字段不起作用，您可以尝试django-localflavor(文档)，它包含对特定国家和文化有用的各种代码片段。

此外，您可以轻松地编写自己的自定义模型字段。

------

**模型中每一个字段都应该是某个 `Field`类的实例， Django 利用这些字段类来实现以下功能：**

- 字段类型用以指定数据库数据类型（如：`INTEGER`, `VARCHAR`, `TEXT`）。
- 在渲染表单字段时默认使用的 HTML 视图 (如： `<input type="text">`, `<select>`)。
- 基本的有效性验证功能，用于 Django 后台和自动生成的表单。

从技术上讲，这些模型是在`django.db.models.fields`中定义的。但为了方便起见，它们被导入到`django.db.models`;标准约定是使用from django.db导入模型，并将字段引用为models.<Foo>Field。



## Field options

以下参数对所有字段类型都可用。都是可选的。

### null

`Field.null`

如果为 True，Django将在数据库中将空值存储为NULL。默认是False。

避免在基于字符串的字段(如CharField和TextField)上使用null。如果基于字符串的字段有null=True，这意味着它有两个“no data”可能的值:null和空字符串。在大多数情况下，对于“no data”有两个可能的值是多余的;Django约定使用空字符串，而不是NULL。一个例外是，一个CharField同时设置unique=True和blank=True。在这种情况下，null=True是必要的，以避免在保存多个具有空白值的对象时违反惟一约束。

对于基于字符串和非基于字符串的字段，如果希望表单中允许空值，还需要设置blank=True，因为null参数只影响数据库存储(参见blank)。

当使用Oracle数据库后端时，无论该属性是什么，都会存储NULL值来表示空字符串。



### blank

`Field.blank`

如果为True，则允许该字段为空。默认是False。

注意，这与null不同。null纯粹与数据库相关，而blank则与验证相关。如果字段为blank=True，表单验证将允许输入空值。如果字段为blank=False，则必须提交该字段。



### choices

`Field.choices`

一种序列，它本身由恰好两项(例如[(A, B)， (A, B)…]的迭代对象组成，可作为该字段的选择。如果提供了选项，则通过模型验证强制执行，默认的表单小部件将是一个包含这些选项的选择框，而不是标准文本字段。

每个元组中的第一个元素是要在模型上设置的实际值，第二个元素是人类可读的名称。例如:

```python
YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
]
```

通常，最好在模型类中定义选项，并为每个值定义一个适当命名的常量:

```python
from django.db import models

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
```

虽然您可以在模型类的外部定义一个选择列表，然后引用它，但是为模型类内部的每个选择定义选择和名称，可以将所有这些信息保存在使用它的类中，并使选择易于引用(e.g   ,   Student.SOPHOMORE   可以在任何导入学生模型的地方工作)。

您也可以将可用的选项收集到指定的组中，这些组可用于组织目的:

```python
MEDIA_CHOICES = [
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
]
```

对于每个设置了选项的模型字段，Django将添加一个方法来检索字段当前值的可读名称。参见数据库API文档中的get_FOO_display()。

每次选择的顺序发生变化时，都会创建一个新的迁移。

除非字段上同时设置了blank=False和缺省值，否则选择框将呈现一个包含“——”的标签。若要覆盖此行为，请将元组添加到包含None的选项;例如(None, Your String For Display)。或者，您可以在有意义的地方使用空字符串，而不是None，例如在CharField上。

<https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#db-column>



