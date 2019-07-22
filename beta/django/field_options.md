[TOC]



**这个文档包含字段的所有API引用，包括Django提供的字段选项。**

------

如果内置字段不起作用，您可以尝试django-localflavor(文档)，它包含对特定国家和文化有用的各种代码片段。

此外，您可以轻松地编写自己的自定义模型字段。

------

**模型中每一个字段都应该是某个 `Field`类的实例， Django 利用这些字段类来实现以下功能：**

- 字段类型用以指定数据库数据类型（如：`INTEGER`, `VARCHAR`, `TEXT`）。
- 在渲染表单字段时默认使用的 HTML 视图 (如： `<input type="text">`, `<select>`)。
- 基本的有效性验证功能，用于 Django 后台和自动生成的表单。

从技术上讲，这些模型是在`django.db.models.fields`中定义的。但为了方便起见，它们被导入到`django.db.models`;标准约定是使用from django.db导入模型，并将字段引用为models.<Foo>Field。



## Field options  字段属性

以下参数对所有字段类型都可用。都是可选的。



## null

`Field.null`

如果为 True，Django将在数据库中将空值存储为NULL。默认是False。

避免在基于字符串的字段(如CharField和TextField)上使用null。如果基于字符串的字段有null=True，这意味着它有两个“no data”可能的值:null和空字符串。在大多数情况下，对于“no data”有两个可能的值是多余的;Django约定使用空字符串，而不是NULL。一个例外是，一个CharField同时设置unique=True和blank=True。在这种情况下，null=True是必要的，以避免在保存多个具有空白值的对象时违反惟一约束。

对于基于字符串和非基于字符串的字段，如果希望表单中允许空值，还需要设置blank=True，因为null参数只影响数据库存储(参见blank)。

当使用Oracle数据库后端时，无论该属性是什么，都会存储NULL值来表示空字符串。



## blank

`Field.blank`

如果为True，则允许该字段为空。默认是False。

注意，这与null不同。null纯粹与数据库相关，而blank则与验证相关。如果字段为blank=True，表单验证将允许输入空值。如果字段为blank=False，则必须提交该字段。



## choices

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



## db_column

`Field.db_column`

要用于此字段的数据库列的名称。如果没有给出，Django将使用字段的名称。

如果您的数据库列名是一个SQL保留字，或者包含Python变量名中不允许的字符(特别是连字符)，这是可以的。Django在幕后引用列和表名。



## db_index

`Field.db_index`

如果为**True**，将为该字段创建一个数据库索引。



## db_tablespace

`Field.db_tablespace`

如果该字段被索引，则为该字段的索引使用的数据库表空间的名称。默认值是项目的DEFAULT_INDEX_TABLESPACE设置(如果设置)，或者模型的db_tablespace(如果有的话)。如果后端不支持索引的表空间，则忽略此选项。



## default

`Field.default`

字段的默认值。这可以是一个值，也可以是一个可调用对象。如果可调用，它将在每次创建新对象时被调用。

默认值不能是一个可变的对象(模型实例、列表、集合等)，因为对该对象的同一个实例的引用将作为所有新模型实例的默认值。相反，将所需的缺省值包装在一个可调用的中。例如，如果您想为JSONField指定默认dict，请使用一个函数:

```python
def contact_default():
    return {"email": "to1@example.com"}

contact_info = JSONField("ContactInfo", default=contact_default)
```

lambdas不能用于像default这样的字段选项，因为它们不能通过迁移序列化。有关其他注意事项，请参阅该文档。

对于像ForeignKey这样映射到模型实例的字段，默认值应该是它们引用的字段的值(pk，除非设置to_field)，而不是模型实例。

当创建了新的模型实例，而没有为字段提供值时，将使用默认值。当字段是主键时，当字段设置为None时也使用默认值。



## editable

`Field.editable`

如果为False，则该字段不会显示在admin或任何其他ModelForm中。在模型验证期间也会跳过它们。默认是True.



## error_messages

`Field.error_messages`

error_messages参数允许您覆盖字段将引发的默认消息。传入一个字典，其中的键与要覆盖的错误消息匹配。

错误消息键包括null、blank、invalid、invalid_choice、unique和unique_for_date。在下面的字段类型部分中，为每个字段指定了额外的错误消息键。

这些错误消息通常不会传播到表单。



## help_text

`Field.help_text`

与表单小部件一起显示的额外“帮助”文本。它对于文档很有用，即使表单上没有使用字段。

注意，这个值不是html在自动生成的表单中转义的。如果您愿意，可以在help_text中包含HTML。例如:

```python
help_text="Please use the following format: <em>YYYY-MM-DD</em>."
```

或者，您可以使用纯文本和django.utils.html.escape()来转义任何HTML特殊字符。确保转义来自不可信用户的任何帮助文本，以避免跨站点脚本攻击。



## primary_key

`Field.primary_key`

如果为**True**，则此字段是模型的主键。

如果您没有为模型中的任何字段指定primary_key=True, Django将自动添加一个AutoField来保存主键，所以您不需要在任何字段上设置primary_key=True，除非您想覆盖默认的主键行为。更多信息,见自动设置主键。

primary_key=True意味着null=False和unique=True。对象上只允许有一个主键。

主键字段是只读的。如果更改现有对象上的主键值并保存它，将在旧对象旁边创建一个新对象。



## unique

`Field.unique`

如果为**True**，则此字段在整个表中必须是惟一的。

这是在数据库级和通过模型验证实现的。如果您试图将具有重复值的模型保存在惟一字段中，即django.db。模型的save()方法将引起`django.db.IntegrityError`

此选项对除`ManyToManyField`和`OneToOneField`之外的所有字段类型都有效。

注意，当unique为真时，不需要指定db_index，因为unique意味着创建索引。



## unique_for_date

`Field.unique_for_date`

将其设置为`DateField`或`DateTimeField`的名称，以要求该字段对于date字段的值是惟一的。

例如，如果您的字段标题具有unique_for_date="pub_date"，那么Django将不允许输入具有相同标题和pub_date的两条记录。

注意，如果将此设置为指向DateTimeField，则只会考虑该字段的日期部分。此外，当USE_TZ为True时，将在保存对象时的当前时区执行检查。

这是由model .validate_unique()在模型验证期间执行的，但不是在数据库级别。如果任何unique_for_date约束涉及不属于ModelForm的字段(例如，如果其中一个字段列在exclude或editable=False中)，Model.validate_unique()将跳过对该特定约束的验证。



## unique_for_month

`Field.unique_for_month`

与unique_for_date类似，但是要求字段对于月份是惟一的。



## unique_for_year

`Field.unique_for_year`

比如unique_for_date和unique_for_month。



## verbose_name

`Field.verbose_name`

字段的可读名称。如果没有给出详细的名称，Django将使用字段的属性名自动创建它，将下划线转换为空格。参见详细字段名。



## validators

`Field.validators`

要为该字段运行的验证器列表。有关更多信息，请参阅验证器文档。

注册和获取查找

字段实现查找注册API。该API可用于自定义字段类的哪些查找可用，以及如何从字段获取查找。