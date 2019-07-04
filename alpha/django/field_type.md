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

*class* `CharField`**(**max_length=None***,** ***options*)**

一个字符串字段，用于小型到大型字符串。

对于大量文本，使用TextField。

该字段默认表单小部件是TextInput。

CharField有一个额外的必要参数:

`CharField.max_length`

字段的最大长度(以字符为单位)。max_length在数据库级和Django的验证中使用MaxLengthValidator强制执行。



## DateField

*class* `DateField`**(***auto_now=False***,** *auto_now_add=False***,** ***options***)**

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



## DateTimeField

*class* `DateTimeField`**(***auto_now=False***,** *auto_now_add=False***,** ***options***)

日期和时间，用Python中的`datetime.datetime`的实例。接受与DateField相同的额外参数。

该字段的默认表单小部件是单个TextInput。管理员使用两个带有JavaScript快捷方式的TextInput小部件。



## DecimalField

*class* `DecimalField`**(***max_digits=None***,** *decimal_places=None***,** ***options***)**

一种固定精度的十进制数，用十进制实例在Python中表示。它使用DecimalValidator验证输入。

有两个必要的参数:

`DecimalField.``max_digits`

该数中允许的最大位数。注意，这个数字必须大于或等于decimal_places

`DecimalField.``decimal_places`

要与该数字一起存储的小数位数。

例如，要存储最多999个分辨率为小数点后两位的数字，您可以使用:

```python
models.DecimalField(..., max_digits=5, decimal_places=2)
```

并存储高达10亿的数字，分辨率为小数点后10位:

```python
models.DecimalField(..., max_digits=19, decimal_places=10)
```

当localalize为False或TextInput为False时，此字段的默认表单小部件是NumberInput。

有关FloatField和DecimalField类之间的区别的更多信息，请参见FloatField和DecimalField。



## DurationField

用于存储时间段的字段——在Python中由timedelta建模。在PostgreSQL上使用时，使用的数据类型是interval，在Oracle上使用的数据类型是interval DAY(9)到SECOND(6)。否则将使用bigint(微秒)。

在大多数情况下，使用DurationField的算法是有效的。然而，在除PostgreSQL之外的所有数据库上，将DurationField的值与DateTimeField实例上的算术值进行比较将不会像预期的那样工作。



## EmailField

*class* `EmailField`**(***max_length=254***,** ***options***)**

使用EmailValidator检查值是否是有效的电子邮件地址的CharField。



## FileField

*class* `FileField`**(***upload_to=None***,** *max_length=100***,** ***options***)**

一个文件上传字段。

primary_key参数不受支持，如果使用该参数将引发错误。

有两个可选参数:

`FileField.upload_to`

该属性提供了一种设置上载目录和文件名的方法，可以通过两种方式进行设置。在这两种情况下，都将值传递给save()方法。

如果指定一个字符串值，它可能包含strftime()格式，该格式将被文件上载的日期/时间所替代(这样上载的文件就不会填满给定的目录)。例如:

```python
class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
```

如果使用默认的FileSystemStorage，字符串值将被附加到MEDIA_ROOT路径，以形成本地文件系统上存储上传文件的位置。如果使用不同的存储，请检查该存储的文档，以了解它如何处理upload_to。

upload_to也可以是一个可调用的函数，例如函数。这将被调用来获取上载路径，包括文件名。此可调用项必须接受两个参数，并返回一个unix样式的路径(带前斜杠)，以便传递给存储系统。这两个论点是:

|   Argument   | Description                                                  |
| :----------: | :----------------------------------------------------------- |
| **instance** | 定义FileField的模型的实例。更具体地说，这是附加当前文件的特定实例。在大多数情况下，这个对象还没有保存到数据库中，所以如果它使用默认的AutoField，那么它的主键字段可能还没有值。 |
| **filename** | 最初给定给文件的文件名。在确定最终目的地路径时，可能考虑到这一点，也可能不考虑这一点。 |

例如:

```python
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
```

`FileField.storage`

存储对象，它处理文件的存储和检索。有关如何提供此对象的详细信息，请参阅管理文件。

该字段的默认表单小部件是ClearableFileInput。

在模型中使用`FileField`或`ImageField`(见下文)需要几个步骤:

1. 在设置文件中，需要将`MEDIA_ROOT`定义为希望Django存储上传文件的目录的完整路径。(为了提高性能，这些文件不存储在数据库中。)将MEDIA_URL定义为该目录的基本公共URL。确保此目录可由Web服务器的用户帐户写入。

2. 将`FileField`或`ImageField`添加到模型中，定义`upload_to`选项，以指定`MEDIA_ROOT`的子目录，用于上传文件。

3. 所有将存储在数据库中的都是文件的路径(相对于MEDIA_ROOT)。您很可能希望使用Django提供的便利url属性。例如，如果您的ImageField被称为mug_shot，那么您可以在模板中获得图像的绝对路径

   **{{** **object.mug_shot.url** **}}**

例如，假设MEDIA_ROOT设置为'/home/media'， upload_to设置为'photos/%Y/%m/%d'。upload_to的'%Y/%m/%d'部分是strftime()格式化;“%Y”是四位数字的年份，“%m”是两位数字的月份，“%d”是两位数字的日子。如果您在2007年1月15日上传一个文件，它将被保存在/home/media/photos/2007/01/15目录中。

如果要检索上载文件的磁盘文件名或文件大小，可以分别使用名称和大小属性;有关可用属性和方法的更多信息，请参见文件类引用和管理文件主题指南。

<https://docs.djangoproject.com/zh-hans/2.2/topics/files/>

该文件是作为将模型保存到数据库中的一部分保存的，因此在保存模型之前，不能依赖磁盘上使用的实际文件名。

可以使用URL属性获得上传文件的相对URL。在内部，它调用底层存储类的url()方法

请注意，无论何时处理上载的文件，都应密切注意上载文件的位置和类型，以避免出现安全漏洞。验证所有上传的文件，以确保这些文件是您所认为的。例如，如果您盲目地让某人在未经验证的情况下将文件上传到Web服务器的文档根目录中，那么某人就可以上传到CGI或PHP脚本，并通过访问该脚本在您的站点上的URL来执行该脚本。不允许。

还要注意，即使是上传的HTML文件，由于它可以由浏览器执行(虽然不是由服务器执行)，也可能造成相当于XSS或CSRF攻击的安全威胁。

FileField实例在数据库中创建为varchar列，默认最大长度为100个字符。与其他字段一样，可以使用max_length参数更改最大长度。

#### FileField and FieldFile

当您访问模型上的文件字段时，您将获得一个FieldFile实例作为访问底层文件的代理。

FieldFile的API反映了File的API，但有一个关键区别:类包装的对象不一定是Python内置File对象的包装器。相反，它是storage .open()方法结果的包装器，该方法可以是File对象，也可以是File API的自定义存储实现。

除了从read()和write()等文件继承的API之外，FieldFile还包含几个方法，可用于与底层文件交互:

这个类的两个方法save()和delete()默认保存数据库中相关字段文件的模型对象。

`FieldFile.name`

文件的名称，包括来自关联文件字段的存储根的相对路径。

`FieldFile.size`

[`Storage.size()`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.Storage.size) 方法的结果。

`FieldFile.url`

一个只读属性，通过调用底层存储类的URL()方法来访问文件的相对URL。

`FieldFile.``open`**(***mode='rb'***)**

以指定模式打开或重新打开与此实例关联的文件。与标准Python open()方法不同，它不返回文件描述符。

由于底层文件在访问时是隐式打开的，因此除了重置指向底层文件的指针或更改模式外，可能没有必要调用此方法。

`FieldFile.close`**()**

行为类似于标准Python file.close()方法，并关闭与此实例关联的文件。

`FieldFile.save`**(***name***,** *content***,** *save=True***)**

此方法接受文件名和文件内容，并将它们传递给字段的存储类，然后将存储的文件与模型字段关联起来。如果您想手动地将文件数据与模型上的FileField实例关联起来，那么save()方法将用于保存该文件数据。

获取两个必需参数:name(文件的名称)和content(包含文件内容的对象)。可选的save参数控制与此字段关联的文件更改后是否保存模型实例。默认值为True。

注意，content参数应该是django.core.files.File的一个实例。而不是Python的内置文件对象。您可以从现有的Python文件对象构造一个文件，如下所示:

```python
from django.core.files import File
# Open an existing file using Python's built-in open()
f = open('/path/to/hello.world')
myfile = File(f)
```

或者你可以像这样用Python字符串构造一个:

```python
from django.core.files.base import ContentFile
myfile = ContentFile("hello world")
```

有关更多信息，请参见管理文件。

`FieldFile.``delete`**(***save=True***)**

删除与此实例关联的文件并清除字段上的所有属性。注意:如果在调用delete()时恰好打开文件，则此方法将关闭该文件。

可选的save参数控制与此字段关联的文件删除后是否保存模型实例。默认值为True。

注意，当一个模型被删除时，相关的文件不会被删除。如果您需要清理孤立的文件，您将需要自己处理它(例如，使用一个定制的管理命令，可以手动运行，也可以通过例如cron定期运行)。



## FilePathField

*class* `FilePathField`**(***path=None***,** *match=None***,** *recursive=False***,** *max_length=100***,** ***options***)**

一个CharField，它的选择仅限于文件系统上某个目录中的文件名。有三个特殊的参数，其中第一个是必需的:

`FilePathField.path`

必需的。指向目录的绝对文件系统路径，此FilePathField应该从该目录获得其选择。例如:**"/home/images"**。

`FilePathField.match`

可选的。FilePathField用于过滤文件名的正则表达式，如字符串。注意，regex将应用于基本文件名，而不是完整路径。示例: `"foo.*\.txt$"`,它将匹配一个名为foo23.txt的文件，但不匹配bar.txt或foo23.png。

`FilePathField.recursive`

可选的。要么`True` ，要么 `False`。默认是 `False`。指定是否应包括path的所有子目录

`FilePathField.allow_files`

可选的。要么`True` ，要么 `False`。默认是True。指定是否应包括指定位置中的文件。这个或allow_folders必须为真。

`FilePathField.allow_folders`

可选的。要么`True` ，要么 `False`。默认是 `False`。指定是否应包括指定位置中的文件夹。这个或allow_files必须为真。

当然，这些参数可以一起使用。

一个潜在的问题是，match应用于基本文件名，而不是完整路径。所以,这个例子:

```python
FilePathField(path="/home/images", match="foo.*", recursive=True)
```

…将匹配/home/images/foo.png，但不匹配/home/images/foo/bar.png，因为匹配应用于基本文件名(foo.png和bar.png)。

FilePathField实例在数据库中创建为varchar列，默认最大长度为100个字符。与其他字段一样，可以使用max_length参数更改最大长度。



## FloatField

Python中由浮点实例表示的浮点数。

当localalize为False或TextInput为False时，此字段的默认表单小部件是NumberInput。

`FloatField` **vs.** `DecimalField`

FloatField类有时与DecimalField类混合在一起。虽然它们都表示实数，但它们表示这些数的方式不同。FloatField在内部使用Python的float类型，而DecimalField使用Python的Decimal类型。有关两者之间差异的信息，请参阅Python的decimal模块文档。



## ImageField

*class* `ImageField`**(***upload_to=None***,** *height_field=None***,** *width_field=None***,** *max_length=100***,** ***options***)**

从FileField继承所有属性和方法，但也验证上载的对象是有效的图像。

除了用于FileField的特殊属性之外，ImageField还具有**height**和**width**属性。

为了方便查询这些属性，ImageField有两个额外的可选参数:

`ImageField.height_field`

模型字段的名称，该字段将在每次保存模型实例时自动填充图像的高度。

`ImageField.width_field`

模型字段的名称，该字段将在每次保存模型实例时自动填充图像的宽度。

需要 [Pillow](https://pillow.readthedocs.io/en/latest/) 库。

mageField实例在数据库中创建为varchar列，默认最大长度为100个字符。与其他字段一样，可以使用max_length参数更改最大长度。

该字段的默认表单小部件是ClearableFileInput。



## IntegerField

一个整数。在Django支持的所有数据库中，-2147483648到2147483647之间的值是安全的。

它使用MinValueValidator和MaxValueValidator根据默认数据库支持的值验证输入。

当localalize为False或TextInput为False时，此字段的默认表单小部件是NumberInput。

### `GenericIPAddressField`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#genericipaddressfieldd



