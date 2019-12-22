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



## GenericIPAddressField

*class* `GenericIPAddressField`**(***protocol='both'***,** *unpack_ipv4=False***,** ***options***)**

字符串格式的IPv4或IPv6地址(例如192.0.2.30或2a02:42fe::4)。该字段的默认表单小部件是TextInput。

IPv6地址标准化遵循RFC 4291#section-2.2 section 2.2，包括使用该部分第3段中建议的IPv4格式，如::ffff:192.0.2.0。例如，2001:0::0:01将被规范化为2001::1，并且::ffff:0a0a:0a0a::ffff:10.10.10.10。所有字符都转换为小写。

`GenericIPAddressField.protocol`

限制指定协议的有效输入。接受的值是“both”(默认值)、“IPv4”或“IPv6”。匹配不区分大小写。

`GenericIPAddressField.unpack_ipv4`

解压缩IPv4映射地址，如::ffff:192.0.2.1。如果启用此选项，该地址将解压缩到192.0.2.1。默认是禁用的。只能在协议被设置为“both”时使用。

如果允许使用空值，则必须允许使用空值，因为空值存储为null。



## TextField

一个大的文本字段。该字段的默认表单小部件是Textarea。

如果指定max_length属性，它将反映在自动生成表单字段的Textarea小部件中。然而，在模型或数据库级别并没有强制执行。使用CharField



## TimeField

*class* `TimeField`**(***auto_now=False***,** *auto_now_add=False***,** ***options***)**

时间，在Python中用datetime表示。时间的实例。接受与DateField相同的自动填充选项。

该字段的默认表单小部件是TextInput。管理员添加了一些JavaScript快捷方式。



## URLField

*class* `URLField`**(***max_length=200***,** ***options***)**

URL的CharField，由URLValidator验证。

该字段的默认表单小部件是TextInput。

与所有CharField子类一样，URLField接受可选的max_length参数。如果没有指定max_length，则使用默认值200。



## UUIDField

用于存储通用惟一标识符的字段。使用Python的UUID类。在PostgreSQL上使用时，它以uuid数据类型存储，否则以char(32)存储。

对于primary_key，通用惟一标识符是AutoField的一个很好的替代方案。数据库不会为您生成UUID，所以建议使用default:

```python
import uuid
from django.db import models

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other fields
```

注意，一个可调用的(省略括号)被传递给default，而不是UUID的实例。



## 关系领域



## ForeignKey

*class* `ForeignKey`**(***to***,** *on_delete***,** ***options***)**

一个多对一的关系。需要两个位置参数:与模型相关的类和on_delete选项。

要创建递归关系(对象本身具有多对一关系)，请使用

`models.ForeignKey('self', on_delete=models.CASCADE)`.

如果需要在尚未定义的模型上创建关系，可以使用模型的名称，而不是模型对象本身:

```python
from django.db import models

class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
    )
    # ...

class Manufacturer(models.Model):
    # ...
    pass
```

当抽象模型被子类化为具体模型，且与抽象模型的app_label无关时，抽象模型上以这种方式定义的关系将被解析:

```python
from django.db import models

class AbstractCar(models.Model):
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    class Meta:
        abstract = True
```

```python
from django.db import models
from products.models import AbstractCar

class Manufacturer(models.Model):
    pass

class Car(AbstractCar):
    pass

# Car.manufacturer will point to `production.Manufacturer` here.
```

要引用在另一个应用程序中定义的模型，可以显式地指定带有完整应用程序标签的模型。例如，如果上面的制造商模型是在另一个名为production的应用程序中定义的，则需要使用:

```python
class Car(models.Model):
    manufacturer = models.ForeignKey(
        'production.Manufacturer',
        on_delete=models.CASCADE,
    )
```

这种类型的引用称为延迟关系，在解决两个应用程序之间的循环导入依赖关系时非常有用。

在外键上自动创建数据库索引。您可以通过将db_index设置为False禁用此功能。如果您要创建一个外键来保持一致性而不是连接，或者要创建一个替代索引，比如部分索引或多列索引，那么您可能希望避免索引的开销。

### 代表数据库

在后台，Django将“_id”附加到字段名，以创建它的数据库列名。在上面的例子中，汽车模型的数据库表将有一个manufacturer_id列。(您可以通过指定db_column显式地更改这一点)但是，您的代码永远不必处理数据库列名，除非您编写自定义SQL。您总是要处理模型对象的字段名。

#### Arguments

外键接受定义关系如何工作的细节的其他参数。

`ForeignKey.on_delete`

当一个由外键引用的对象被删除时，Django将模拟on_delete参数指定的SQL约束的行为。例如，如果你有一个可空的外键，并且你想在被引用的对象被删除时将其设置为空:

```python
user = models.ForeignKey(
    User,
    models.SET_NULL,
    blank=True,
    null=True,
)
```

on_delete不会在数据库中创建SQL约束。稍后可能实现对数据库级联选项的支持。

on_delete的可能值可以在django.db.models中找到:

- CASCADE

  级联删除。Django模拟DELETE级联上的SQL约束的行为，并删除包含外键的对象。

  elete()不会调用相关的模型，但是会为所有被删除的对象发送pre_delete和post_delete信号。

- PROTECT

  通过引发ProtectedError (django.db.IntegrityError的子类)防止删除引用的对象。

- SET_NULL

  设置外键为空;这只有在null为真时才有可能。

- SET_DEFAULT

  将外键设置为其默认值;必须为外键设置默认值。

- SET()

  将外键设置为传递给Set()的值，或者如果传入一个可调用项，则设置调用它的结果。在大多数情况下，传递一个可调用函数是必要的，以避免在导入模型时执行查询。

  ```python
  from django.conf import settings
  from django.contrib.auth import get_user_model
  from django.db import models
  
  def get_sentinel_user():
      return get_user_model().objects.get_or_create(username='deleted')[0]
  
  class MyModel(models.Model):
      user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.SET(get_sentinel_user),
      )
  ```

- DO_NOTHING

  采取任何行动。如果数据库后端强制执行引用完整性，这将导致IntegrityError，除非手动向数据库字段添加SQL ON DELETE约束。

`ForeignKey.limit_choices_to`

当使用ModelForm或admin呈现该字段时，为该字段的可用选项设置一个限制(默认情况下，queryset中的所有对象都可用来选择)。可以使用字典、Q对象或返回字典或Q对象的可调用对象。

```python
staff_member = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    limit_choices_to={'is_staff': True},
)
```

使ModelForm上对应的字段只列出is_staff=True的用户。这可能对Django管理很有帮助。

例如，当与Python datetime模块一起使用时，可调用表单可以很有帮助，可以根据日期范围限制选择。例如:

```python
def limit_pub_date_choices():
    return {'pub_date__lte': datetime.date.utcnow()}

limit_choices_to = limit_pub_date_choices
```

如果limit_choices_to是或返回一个Q对象，这对于复杂的查询非常有用，那么只有当模型的ModelAdmin中的raw_id_fields中没有列出该字段时，它才会对admin中可用的选项产生影响。

如果将callable用于limit_choices_to，则每次实例化新表单时都会调用它。当模型被验证时，也可以调用它，例如通过管理命令或管理员。管理员构造queryset，以便在各种边缘情况下多次验证表单输入，因此您的可调用项可能被多次调用。

`ForeignKey.related_name`

要用于从相关对象返回到此对象的关系的名称。它也是related_query_name(用于目标模型的反向过滤器名称)的默认值。有关详细说明和示例，请参阅相关对象文档。注意，在定义抽象模型上的关系时，必须设置此值;当你这样做的时候，一些特殊的语法是可用的。

如果希望Django不创建向后关系，可以将related_name设置为'+'或以'+'结尾。例如，这将确保用户模型不会与该模型有反向关系:

```python
user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='+',
)
```

`ForeignKey.related_query_name`

要用于目标模型的反向筛选器名称的名称。默认值为related_name，如果设置为default_related_name，则默认值为:

```python
# Declare the ForeignKey with related_query_name
class Tag(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="tags",
        related_query_name="tag",
    )
    name = models.CharField(max_length=255)

# That's now the name of the reverse filter
Article.objects.filter(tag__name="important")
```

像related_name一样，related_query_name通过一些特殊的语法支持应用程序标签和类插值。

`ForeignKey.to_field`

关系所指向的相关对象上的字段。默认情况下，Django使用相关对象的主键。如果引用不同的字段，则该字段必须具有unique=True。

`ForeignKey.db_constraint`

控制是否应在数据库中为该外键创建约束。默认值为True，这几乎肯定是您想要的;将此设置为False对数据完整性非常不利。也就是说，下面是一些你可能想要这样做的场景:

- 您有无效的遗留数据。

- 您正在分片数据库。

如果将其设置为False，则访问不存在的相关对象将引发其DoesNotExist异常。

`ForeignKey.swappable`

如果此外键指向可切换模型，则控制迁移框架的反应。如果为真——默认值——那么如果外键指向的模型与当前设置值匹配。AUTH_USER_MODEL(或另一个可切换的模型设置)将使用对设置的引用(而不是直接对模型的引用)将关系存储在迁移中。

只有当您确信您的模型应该始终指向插入模型时，您才希望将其重写为False—例如，如果它是专为您的自定义用户模型设计的概要文件模型。

将它设置为False并不意味着你可以引用一个可切换模型即使是换出——假只是意味着迁移用此ForeignKey总是参考的模型指定(这将会失败如果用户试图运行一个用户模型你不支持,例如)。

如果有疑问，让它默认为True。



## ManyToManyField

*class* `ManyToManyField`**(***to***,** ***options***)**

多对多的关系。需要一个位置参数:与模型相关的类，它的工作原理与使用外键完全相同，包括递归关系和延迟关系。

可以使用字段的RelatedManager添加、删除或创建相关对象。

### 代表数据库

在幕后，Django创建了一个中间连接表来表示多对多关系。默认情况下，这个表名是使用多对多字段的名称和包含它的模型的表名生成的。由于一些数据库不支持超过一定长度的表名，这些表名将被自动截断，并使用唯一性散列，例如author_books_9cdf。您可以使用db_table选项手动提供联接表的名称。

#### Arguments

ManyToManyField接受一组额外的参数(都是可选的)，这些参数控制关系的工作方式。

`ManyToManyField.related_name`

Same as [`ForeignKey.related_name`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_name).

`ManyToManyField.related_query_name`

Same as [`ForeignKey.related_query_name`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name).

`ManyToManyField.limit_choices_to`

Same as [`ForeignKey.limit_choices_to`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.limit_choices_to).

limit_choices_to在使用through参数指定自定义中间表的ManyToManyField上使用时没有效果。

`ManyToManyField.symmetrical`

仅用于定义自我上的多个任意域。考虑以下模型:

```python
from django.db import models

class Person(models.Model):
    friends = models.ManyToManyField("self")
```

当Django处理这个模型时，它识别出它本身有一个ManyToManyField，因此，它没有向Person类添加person_set属性。相反，ManyToManyField被认为是对称的——也就是说，如果我是你的朋友，那么你就是我的朋友。

如果您不希望在与自我的多对多关系中对称，请将对称设置为False。这将迫使Django为反向关系添加描述符，从而允许许多tomanyfield关系是非对称的。

`ManyToManyField.through`

Django将自动生成一个表来管理多对多关系。但是，如果希望手动指定中间表，可以使用through选项指定表示要使用的中间表的Django模型。

此选项最常见的用法是，当您希望将额外数据与多对多关系关联时。

如果不指定显式透模型，仍然可以使用隐式透模型类直接访问为保存关联而创建的表。它有三个字段来链接模型。

如果源模型和目标模型不同，则生成以下字段:

- `id`:关系的主键。
- `<containing_model>_id`: 声明“ManyToManyField”的模型的“id”。
- `<other_model>_id`: 模型的“id”指的是模型的“id”。

如果“ManyToManyField”指向同一个模型，则生成以下字段:

- `id`: 关系的主键。
- `from_<model>_id`: 指向模型的实例的“id”(即源实例)。
- `to_<model>_id`: 关系指向的实例的“id”(即目标模型实例)。

该类可用于查询给定模型实例的相关记录，就像普通模型一样。

`ManyToManyField.through_fields`

仅在指定自定义中介模型时使用。Django通常会决定使用中介模型的哪些字段来自动建立多对多关系。但是，考虑以下模型:

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)
```

成员关系对Person (Person和inviter)有两个外键，这使得关系很模糊，Django不知道使用哪个外键。在本例中，必须使用上面的示例显式指定Django应该使用哪些外键。

通过_fields接受一个2元组('field1'， 'field2')，其中field1是模型的外键的名称ManyToManyField是在(本例中是group)上定义的，而field2是目标模型的外键的名称(本例中是person)。

当中介模型上有多个外键指向参与多对多关系的模型中的任何一个(甚至两个)时，必须指定through_fields。当使用中介模型并且模型有两个以上的外键时，或者您希望显式地指定应该使用哪两个Django时，这也适用于递归关系。

使用中介模型的递归关系总是被定义为非对称关系——也就是说，对称=False——因此，存在“源”和“目标”的概念。在这种情况下，“field1”将被视为关系的“源”，而“field2”将被视为“目标”。

`ManyToManyField.db_table`

为存储多对多数据而创建的表的名称。如果没有提供此选项，Django将根据以下名称假定一个默认名称:定义关系的模型表和字段本身的名称。

`ManyToManyField.db_constraint`

控制是否应在数据库中为中介表中的外键创建约束。默认值为True，这几乎肯定是您想要的;将此设置为False对数据完整性非常不利。也就是说，下面是一些你可能想要这样做的场景:

- 您有无效的遗留数据。

- 您正在分片数据库。

同时传递db_constraint和through是一个错误。

`ManyToManyField.swappable`

如果这个ManyToManyField指向可切换模型，则控制迁移框架的反应。如果它是真的——默认值——那么如果ManyToManyField指向的模型匹配当前设置的值。AUTH_USER_MODEL(或另一个可切换的模型设置)将使用对设置的引用(而不是直接对模型的引用)将关系存储在迁移中。

只有当您确信您的模型应该始终指向插入模型时，您才希望将其重写为False—例如，如果它是专为您的自定义用户模型设计的概要文件模型。

如果有疑问，让它默认为True。

ManyToManyField不支持验证器。null没有效果，因为没有办法在数据库级别上要求关系。



## OneToOneField

*class* `OneToOneField`**(***to***,** *on_delete***,** *parent_link=False***,** ***options***)**

一个一对一的关系。从概念上讲，这类似于一个具有unique=True的外键，但是关系的“反向”部分将直接返回一个对象。

这对于以某种方式“扩展”另一个模型的模型的主键是最有用的;通过添加一个隐式多表继承实现一对一的关系从子模型到父模型,例如。

需要一个位置参数:与模型相关的类。这与对ForeignKey的操作完全相同，包括所有关于递归和延迟关系的选项。

如果没有为OneToOneField指定related_name参数，Django将使用当前模型的小写名称作为默认值。

用下面的例子:

```python
from django.conf import settings
from django.db import models

class MySpecialUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='supervisor_of',
    )
```

您得到的用户模型将具有以下属性:

```
>>> user = User.objects.get(pk=1)
>>> hasattr(user, 'myspecialuser')
True
>>> hasattr(user, 'supervisor_of')
True
```

如果相关表中的条目不存在，则在访问反向关系时引发DoesNotExist异常。例如，如果用户没有MySpecialUser指定的管理器:

```
>>> user.supervisor_of
Traceback (most recent call last):
    ...
DoesNotExist: User matching query does not exist.
```

此外，OneToOneField接受所有外键接受的额外参数，外加一个额外参数:

`OneToOneField.parent_link`

当为True并在继承自另一个具体模型的模型中使用时，表示该字段应该用作返回父类的链接，而不是通常通过子类化隐式创建的额外的OneToOneField。

关OneToOneField的使用示例，请参见一对一关系。



## API参考

