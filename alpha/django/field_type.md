[TOC]



**这个文档包含字段的所有API引用，包括Django提供的字段类型。**

------

如果内置字段不起作用，您可以尝试django-localflavor(文档)，它包含对特定国家和文化有用的各种代码片段。

此外，您可以轻松地编写自己的自定义模型字段。

------

**模型中每一个字段都应该是某个 `Field`类的实例， Django 利用这些字段类来实现以下功能：**

- 字段类型用以指定数据库数据类型（如：`INTEGER`, `VARCHAR`, `TEXT`）。
- 在渲染表单字段时默认使用的 HTML 视图 (如： `<input type="text">`, `<select>`)。
- 基本的有效性验证功能，用于 Django 后台和自动生成的表单。

从技术上讲，这些模型是在`django.db.models.fields`中定义的。但为了方便起见，它们被导入到`django.db.models`;标准约定是使用from django.db导入模型，并将字段引用为models.<Foo>Field。



## AutoField

根据可用id自动递增的整数字段。通常不需要直接使用;如果不指定，主键字段将自动添加到模型中。看到自动设置主键。



## BigAutoField

一个64位整数，很像一个AutoField，除了它被保证适合从1到9223372036854775807的数字。



## BigIntegerField

一个64位的整数，很像整数字段，除了它保证适合-9223372036854775808到9223372036854775807之间的数字。该字段的默认表单小部件是TextInput。



## BinaryField

存储原始二进制数据的字段。可以为它分配字节`bytes`、字节数组`bytearray`或内存视图`memoryview`。 

默认情况下，BinaryField将editable设置为False，在这种情况下，它不能包含在ModelForm中。

BinaryField有一个额外的可选参数:

`BinaryField.max_length`

字段的最大长度(以字符为单位)。最大长度在Django的验证中使用MaxLengthValidator强制执行。

尽管您可能会考虑在数据库中存储文件，但是99%的情况下，这都是糟糕的设计。此字段不能替代正确的静态文件处理。



## BooleanField

一个true/false 字段。

该字段的默认表单小部件是CheckboxInput，如果null=True，则为NullBooleanSelect。

未定义`Field.default`时，`BooleanField`的默认值为`None`。



## CharField

一个字符串字段，用于小型到大型字符串。

对于大量文本，使用TextField。

该字段默认表单小部件是TextInput。

CharField有一个额外的必要参数:

`CharField.max_length`

字段的最大长度(以字符为单位)。max_length在数据库级和Django的验证中使用MaxLengthValidator强制执行。



## DateField

一个日期，用Python中的datetime表示。日期的实例。有一些额外的可选参数:

`DateField.auto_now`

每次保存对象时自动将字段设置为now。用于“最后修改”时间戳。注意，总是使用当前日期;它不仅仅是一个可以覆盖的默认值。

该字段只在调用Model.save()时自动更新。当以其他方式(如QuerySet.update())更新其他字段时，该字段不会被更新，不过您可以在这样的更新中为该字段指定自定义值。

`DateField.auto_now_add`

在第一次创建对象时自动将字段设置为now。用于创建时间戳。注意，总是使用当前日期;它不仅仅是一个可以覆盖的默认值。因此，即使在创建对象时为该字段设置了值，它也会被忽略。如果您希望能够修改该字段，请将auto_now_add=True设置为:

- For [`DateField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateField): `default=date.today` - from [`datetime.date.today()`](https://docs.python.org/3/library/datetime.html#datetime.date.today)
- For [`DateTimeField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateTimeField): `default=timezone.now` - from [`django.utils.timezone.now()`](https://docs.djangoproject.com/zh-hans/2.2/ref/utils/#django.utils.timezone.now)

该字段的默认表单小部件是TextInput。管理员添加了JavaScript日历和“Today”快捷方式。包含一个附加的invalid_date错误消息键。

auto_now_add、auto_now和default选项是互斥的。这些选项的任何组合都将导致错误。

与当前实现的一样，将auto_now或auto_now_add设置为True将导致字段具有editable=False和blank=True set。

auto_now和auto_now_add选项将始终在创建或更新时使用默认时区中的日期。如果您需要一些不同的东西，您可以考虑简单地使用您自己的可调用默认值或覆盖save()，而不是使用auto_now或auto_now_add;或者使用DateTimeField而不是DateField，并决定如何在显示时处理从datetime到date的转换。



<https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#datetimefield>