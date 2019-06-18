



[TOC]



## 记录集

**与模型和记录的交互通过记录集执行，记录集是同一模型的一组已排序的记录。**

与名称的含义相反，目前记录集可能包含重复项。这在未来可能会改变。

模型上定义的方法在记录集上执行，它们`self`是记录集：

```python
class AModel(models.Model):
    _name = 'a.model'
    def a_method(self):
        # self can be anywhere between 0 records and all records in the
        # database
        self.do_operation()
```

迭代记录集将产生新*的单个记录*集 （“单例”），就像迭代Python字符串产生单个字符的字符串一样：

```python
def do_operation(self):
    print self # => a.model(1, 2, 3, 4, 5)
    for record in self:
        print record # => a.model(1), then a.model(2), then a.model(3), ...
```



## 现场访问

记录集提供了一个“活动记录”接口:模型字段可以作为属性直接从记录中读取和写入，但只能在单例(单记录记录集)上。字段值也可以像dict项一样访问，对于动态字段名，dict项比getattr()更优雅、更安全。设置字段的值会触发对数据库的更新:

```python
>>> record.name
Example Name
>>> record.company_id.name
Company Name
>>> record.name = "Bob"
>>> field = "name"
>>> record[field]
Bob
```

尝试在多个记录上读取或写入字段会引发错误。

访问关系字段(Many2one, One2many, Many2many)总是返回一个记录集，如果没有设置该字段，则返回空。

危险
每个字段的赋值都会触发数据库更新，当同时设置多个字段或在多个记录上设置字段(值相同)时，使用write():

```python
# 3 * len(records) database updates
for record in records:
    record.a = 1
    record.b = 2
    record.c = 3
# len(records) database updates
for record in records:
    record.write({'a': 1, 'b': 2, 'c': 3})
# 1 database update
records.write({'a': 1, 'b': 2, 'c': 3})
```



## 记录缓存和预取

Odoo为记录的字段维护缓存，因此不是每个字段访问都会发出数据库请求，这对性能来说是很糟糕的。下面的示例仅为第一个语句查询数据库:

```python
record.name             # first access reads value from database
record.name             # second access gets value from cache
```

为了避免一次读取一条记录上的一个字段，Odoo根据一些启发式方法预取记录和字段，以获得良好的性能。一旦必须读取给定记录上的字段，ORM就会在更大的记录集中读取该字段，并将返回的值存储在缓存中，供以后使用。预取的记录集通常是通过迭代获得记录的记录集。此外，所有简单的存储字段(boolean、integer、float、char、text、date、datetime、selection、many2one)都被同时获取;它们对应于模型表的列，并在同一个查询中有效地获取。

考虑下面的例子，其中合作伙伴是由1000条记录组成的记录集。如果没有预取，循环将对数据库进行2000次查询。预取时，只进行一个查询:

```python
for partner in partners:
    print partner.name          # first pass prefetches 'name' and 'lang'
                                # (and other fields) on all 'partners'
    print partner.lang
```

预取也适用于辅助记录:当读取关系字段时，将订阅它们的值(即记录)，以便将来预取。访问其中一个辅助记录将从同一个模型中预先获取所有辅助记录。这使得下面的示例只生成两个查询，一个用于伙伴，一个用于国家:

```python
countries = set()
for partner in partners:
    country = partner.country_id      # first pass prefetches all partners
    countries.add(country.name)   	  # first pass prefetches all countries
```



## 集合操作

记录集是不可变的，但是相同模型的集可以使用不同的集合操作组合，返回新的记录集。Set操作不保留顺序。

- record in set返回record(必须是一个1元素的记录集)是否存在于set中。record not in set是相反的操作

- set1 <= set2 和 set1 < set2返回set1是否是set2的子集(resp. strict)

- set1 >= set2 和 set1 > set2返回set1是否是set2的超集(resp. strict)

- set1 | set2 返回两个记录集的并集，这是一个新的记录集，包含两个源中存在的所有记录

- set1 & set2 返回两个记录集的交集，一个新的记录集只包含在两个源中出现的记录

- set1 - set2 返回一个新的记录集，其中只包含不在set2中的set1的记录



### 其他记录集操作

记录集是可迭代的，因此常用的Python工具可用于转换(map()、sort()和迭代工具。然而，这些方法要么返回一个列表，要么返回一个迭代器，从而消除了对结果调用方法或使用set操作的能力。

因此，记录集提供这些操作返回记录集本身(如果可能的话):

**filtered()**

返回一个记录集，其中只包含满足所提供谓词函数的记录。谓词也可以是一个字符串，通过字段为真或为假来过滤:

```python
# only keep records whose company is the current user's
records.filtered(lambda r: r.company_id == user.company_id)
# only keep records whose partner is a company
records.filtered("partner_id.is_company")
```

**sorted()**

返回按提供的键函数排序的记录集。如果没有提供密钥，则使用模型的默认排序顺序:

```python
# sort records by name
records.sorted(key=lambda r: r.name)
```

**mapped()**

将提供的函数应用于记录集中的每个记录，如果结果是记录集，则返回一个记录集:

```python
# returns a list of summing two fields for each record in the set
records.mapped(lambda r: r.field1 + r.field2)
```

所提供的函数可以是一个字符串来获取字段值:

```python
# returns a list of names
records.mapped('name')
# returns a recordset of partners
record.mapped('partner_id')
# returns the union of all partner banks, with duplicates removed
record.mapped('partner_id.bank_ids')
```



## 环境

环境存储ORM使用的各种上下文数据:数据库游标(用于数据库查询)、当前用户(用于访问权限检查)和当前上下文(存储任意元数据)。环境还存储缓存。

所有记录集都有一个环境，该环境是不可变的，可以使用env访问，并允许访问当前用户(user)、游标(cr)或上下文(context):

```python
>>> records.env
<Environment object ...>
>>> records.env.user
res.user(3)
>>> records.env.cr
<Cursor object ...)
```

当从其他记录集创建记录集时，环境将被继承。该环境可用于获取另一个模型中的空记录集，并查询该模型:

```python
>>> self.env['res.partner']
res.partner
>>> self.env['res.partner'].search([['is_company', '=', True], ['customer', '=', True]])
res.partner(7, 18, 12, 14, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74)
```

### 改变环境

环境可以从记录集中定制。这将使用更改后的环境返回记录集的新版本。

**sudo()**

使用提供的用户集创建一个新环境，如果没有提供，则使用管理员(在安全上下文中绕过访问权限/规则)，返回在使用新环境时调用的记录集的副本:

```python
# create partner object as administrator
env['res.partner'].sudo().create({'name': "A Partner"})

# list partners visible by the "public" user
public = env.ref('base.public_user')
env['res.partner'].sudo(public).search([])
```

**with_context()**

可以使用一个位置参数来替换当前环境的上下文

可以通过关键字获取任意数量的参数，这些参数可以添加到当前环境的上下文中，也可以添加到步骤1中设置的上下文中

```python
# look for partner, or create one with specified timezone if none is
# found
env['res.partner'].with_context(tz=a_tz).find_or_create(email_address)
```

**with_env()**

完全替换现有环境



## 常见的ORM方法

**search()**

获取一个搜索域，返回一组匹配的记录。可以返回匹配记录子集(偏移量和限制参数)和被排序(顺序参数):

```python
>>> # searches the current model
>>> self.search([('is_company', '=', True), ('customer', '=', True)])
res.partner(7, 18, 12, 14, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74)
>>> self.search([('is_company', '=', True)], limit=1).name
'Agrolait'
```

要检查是否有任何记录匹配域，或者计算匹配域的记录数量，可以使用search_count()

**create()**

提供字段值字典或此类字典的列表，并返回包含已创建记录的记录集:

```python
>>> self.create({'name': "Joe"})
res.partner(78)
>>> self.create([{'name': "Jack"}, {'name': "William"}, {'name': "Averell"}])
res.partner(79, 80, 81)
```

**write()**

提供若干字段值，并将它们写入其记录集中的所有记录。不返回任何东西:

```python
self.write({'name': "Newer Name"})
```

**browse()**

提供数据库id或id列表，并返回一个记录集，当从Odoo外部获取记录id(例如，通过外部系统的往返)或调用旧API中的方法时非常有用:

```python
>>> self.browse([7, 18, 12])
res.partner(7, 18, 12)
```

**exists()**

返回一个只包含数据库中存在的记录的新记录集。可用于检查记录(例如从外部取得的)是否仍然存在:

```python
if not record.exists():
    raise Exception("The record has been deleted")
```

或者在调用了一个可以删除一些记录的方法之后:

```python
records.may_remove_some()
# only keep records which were not deleted
records = records.exists()
```

**ref()**

环境方法返回与提供的外部id匹配的记录:

```python
>>> env.ref('base.group_public')
res.groups(2)
```

**ensure_one()**

检查记录集是否为单例(只包含一条记录)，否则会引发错误:

```python
records.ensure_one()
# is equivalent to but clearer than:
assert len(records) == 1, "Expected singleton"
```



## 创建模型

模型字段定义为模型本身的属性:

```python
from odoo import models, fields
class AModel(models.Model):
    _name = 'a.model.name'
    
    field1 = fields.Char()
```

不能定义具有相同名称的字段和方法，它们将发生冲突

默认情况下，字段的标签(用户可见的名称)是字段名称的大写版本，这可以用字符串参数覆盖:

```python
field2 = fields.Integer(string="an other field")
```

默认值定义为字段上的参数，或者是一个值:

```python
a_field = fields.Char(default="a value")
```

或者调用一个函数来计算默认值，该函数应该返回该值:

```python
def compute_default_value(self):
    return self.get_value()
a_field = fields.Char(default=compute_default_value)
```



### odoo 支持的字段类型

| 字段类型       | 介绍                     | 专有参数 |
| -------------- | ------------------------ | -------- |
| Char           | 字符串、短文本           |          |
| Binary         | 二进制、图像、文件       |          |
| Boolean        | 布尔值                   |          |
| Date           | 日期 年月日              |          |
| Datetime       | 日期 年月日时分秒        |          |
| Float          | 小数                     |          |
| Integer        | 整数                     |          |
| Selection      | 下拉菜单、键值对（字典） |          |
| Moetary        | 金额字段 货币 金融       |          |
| Text/html Html | 页面                     |          |
| Many2many      | 多对多关系 中间表        |          |
| Many2one       | 多对一                   |          |
| One2many       | 一对多                   |          |
| Reference      | 继承                     |          |

### 参数

newline：只有在组内有用，早早的结束了当前行，立即切换到一个新的行（事先没有填充任何剩余列）
separator：小的水平间距，具有字符串属性的行为作为一个章节标题
sheet：可以作为一个直接的子类，以形成一个更窄、更敏感的形式布局
header：结合表，在框架本身上提供了一个完整的宽度位置，一般用于显示工作流按钮和状态部件的宽度
button：把系统通过动作串联起来
field 定义显示字符串：
name (mandatory)
要渲染的字段的名称
widget
字段有一个默认的基于类型的渲染（如 char、many2one）。widget 属性允许使用不同的渲染方法和上下文
options
JSON 对象知道配置选项字段的控件（包括默认的部件）
class：HTML 类设置的生成元素，普通字段类
oe_inline： 防止常规线中断以下字段
oe_left,oe_right: 相应方向的浮点字段
oe_read_only,oe_edit_only：仅在相应的表格模式显示字段
oe_no_button: 避免在 Many2one 显示导航按钮
oe_avata: 在图像字段显示图像（正方形、90 x 90最大大小，一些图像装饰）
groups: 只为特定用户显示该字段
on_change： 在该字段的值被编辑时调用指定的方法，可以生成更新其它字段或显示警告
在 模块里使用 openerp.ap.onchange()
attrs： 基于记录值的动态元参数
domain: 对于关键字段，在显示选定的记录时应用的筛选器
context: 对于关系字段，在获取可能值时要通过上下文
readonly：在只读模式和编辑显示字段，但不需要编辑
required：如果该字段没有值就会产生一个错误，并防止保存记录
nolabel：不要自动显示该字段的标签，只有在该字段是一个组要元素子组时才有意义
placeholder：帮助信息显示在空白字段。可以用复数形式替换字段标签。 不应将数据作为用户的一个例子 是容易混淆的占位符文本填充字段
mode：对于 one2many，使用字段的联系记录显示模式（型），tree，form,kanban or graph 中一个。默认为 tree（列表显示）
help：靠近字段或它的标签时显示提示用户
filename：对于二进制字段，相关字段的名称提供该文件的名称
password：char 字段存储一个密码，它的数据不应该显示

**视图的优先级大于模板的优先级**

self.env # 为请求提供权限参数和其他参数
self.env.cr或self._cr 是数据库的光标对象，它用于查询数据库
self.env.uid或self._uid是当前用户的数据库id
self.env.user # 是当前用户的记录
self.env.context或self.context是上下文字典
self.env.ref（xml_id）# 用于返回xml在数据库中的记录
self.env[model_name] # 返回给定模型的空实例集合

widget="statusbar"   # 头部状态条标签
widget="email"  # 电子邮件地址标签
widget="selection" # 下拉选择标签
widget="mail_followers" # 关注者标签
widget="mail_thread" # 消息标签
widget="progressbar" # 进度条，按百分比标签
widget="one2many_list" # 一对多列表标签
widget="many2many_tags" # 多对多显示标签
widget="url"  # 网站链接标签
widget='image' # 图片标签
widget="many2many_kanban" # 看版标签
widget="handler" # 触发标签
widget="radio" # 单选标签
widget="char_domain"   # 字符域标签
widget="monetary"  # 价格（和精度位数相关）标签
widget="float_time" # 单精度时间标签
widget="html" # html相关标签
widget="pad" # pad显示相关标签
widget="date" # 日期标签
widget="monetary" # 金额标签
widget='text' # 文本标签
widget="sparkline_bar" # 燃尽标签
widget="checkbox" # 复选框标签
widget="reference" # 关联标签



## 计算字段

可以使用compute参数计算字段(而不是直接从数据库中读取)。它必须将计算值分配给字段。如果使用其他字段的值，则应该使用depends()指定这些字段:

```python
from odoo import api
total = fields.Float(compute='_compute_total')

@api.depends('value', 'tax')
def _compute_total(self):
    for record in self:
        record.total = record.value + record.value * record.tax
```

依赖项可以在使用子字段时点状路径:

```python
@api.depends('line_ids.value')
def _compute_total(self):
    for record in self:
        record.total = sum(line.value for line in record.line_ids)
```

默认情况下不存储计算字段，而是在请求时计算并返回它们。设置store=True将把它们存储在数据库中，并自动启用搜索

还可以通过设置搜索参数来启用对计算字段的搜索。值是返回域的方法名:

```python
upper_name = field.Char(compute='_compute_upper', search='_search_upper')
def _search_upper(self, operator, value):
    if operator == 'like':
        operator = 'ilike'
    return [('name', operator, value)]
```

若要允许在计算字段上设置值，请使用逆参数。它是反转计算并设置相关字段的函数名:

```python
document = fields.Char(compute='_get_document', inverse='_set_document')
def _get_document(self):
    for record in self:
        with open(record.get_document_path) as f:
            record.document = f.read()
def _set_document(self):
    for record in self:
        if not record.document: continue
        with open(record.get_document_path()) as f:
            f.write(record.document)
```

多个字段可以用相同的方法同时计算，只需对所有字段使用相同的方法并设置所有字段:

```python
discount_value = fields.Float(compute='_apply_discount')
total = fields.Float(compute='_apply_discount')

@depends('value', 'discount')
def _apply_discount(self):
    for record in self:
        # compute actual discount from discount percentage
        discount = record.value * record.discount
        record.discount_value = discount
        record.total = record.value - discount
```

#### 相关领域

计算字段的特殊情况是相关(代理)字段，它在当前记录上提供子字段的值。它们是通过设置相关参数来定义的，就像普通的计算字段一样，它们可以存储:

```python
nickname = fields.Char(related='user_id.partner_id.name', store=True)
```



### onchange:动态更新UI

当用户更改表单中某个字段的值(但尚未保存该表单)时，根据该值自动更新其他字段是很有用的，例如，在更改税收或添加新的发票行时更新最终的总额。

计算字段会自动检查和重新计算，它们不需要onchange

对于非计算字段，onchange()修饰符用于提供新的字段值:

```python
@api.onchange('field1', 'field2') # if these fields are changed, call method
def check_change(self):
    if self.field1 < self.field2:
        self.field3 = True
```

然后，将方法期间执行的更改发送到客户机程序，并对用户可见

客户端自动调用computed字段和new-API onchanges，而无需在视图中添加它们

可以通过在视图中添加on_change="0"来抑制特定字段的触发器:

```xml
<field name="name" on_change="0"/>
```

当用户编辑字段时，不会触发任何接口更新，即使有函数字段或显式onchange依赖于该字段。

onchange方法对这些记录的虚拟记录进行赋值，而不是写入数据库，只是用来知道要将哪个值发送回客户机

警告

one2many或many2many字段不可能通过onchange修改自身。这是一个webclient限制—请参见#2693。



## 低级的SQL

环境上的cr属性是当前数据库事务的指针，允许直接执行SQL，无论是对于使用ORM难以表达的查询(例如复杂连接)，还是出于性能原因:

```python
self.env.cr.execute("some_sql", param1, param2, param3)
```

由于模型使用相同的游标，并且环境包含各种缓存，因此在原始SQL中修改数据库时必须使这些缓存失效，否则模型的进一步使用可能变得不一致。在SQL中使用CREATE、UPDATE或DELETE时需要清除缓存，而不是SELECT(它只读取数据库)。

清除缓存可以使用BaseModel对象的invalidate_cache()方法执行。

## 新API和旧API之间的兼容性

Odoo目前正在从一个较老的(不太规范的)API过渡到另一个API，有必要手动地从一个API过渡到另一个API:

RPC层(XML-RPC和JSON-RPC)都是用旧API表示的，纯用新API表示的方法在RPC上不可用

可覆盖方法可以从仍然使用旧API风格编写的旧代码段中调用

新旧api的主要区别在于:

​		环境的值(游标、用户id和上下文)被显式地传递给方法

​		记录数据(id)显式地传递给方法，可能根本不传递

​		方法倾向于处理id列表，而不是记录集

默认情况下，假定方法使用新的API样式，并且不能从旧的API样式调用方法。

从新API到旧API的调用被桥接

当使用新的API样式时，对使用旧API定义的方法的调用会被动态自动转换，不需要做任何特殊的事情:

```python
>>> # method in the old API style
>>> def old_method(self, cr, uid, ids, context=None):
...    print ids

>>> # method in the new API style
>>> def new_method(self):
...     # system automatically infers how to call the old-style
...     # method from the new-style method
...     self.old_method()

>>> env[model].browse([1, 2, 3, 4]).new_method()
[1, 2, 3, 4]
```

两个装饰器可以向旧API公开一个新风格的方法:

model()

该方法公开为不使用id，其记录集通常为空。它的“老API”签名是cr, uid， *参数，上下文:

```python
@api.model
def some_method(self, a_value):
    pass
# can be called as
old_style_model.some_method(cr, uid, a_value, context=context)
```

multi()

该方法公开了一个id列表(可能是空的)，它的“老API”签名是cr, uid, id， *参数，上下文:

```python
@api.multi
def some_method(self, a_value):
    pass
# can be called as
old_style_model.some_method(cr, uid, [id1, id2], a_value, context=context)
```

注意，用model()修饰的create方法总是用一个字典调用。使用变体model_create_multi()修饰的create方法总是使用dict列表调用。修饰符负责将参数转换为一种或另一种形式:

```python
@api.model
def create(self, vals):
    ...

@api.model_create_multi
def create(self, vals_list):
    ...
```

因为新风格的api倾向于返回记录集，而旧风格的api倾向于返回id列表，所以也有一个装饰器来管理这个:

returns()

假设函数返回一个记录集，第一个参数应该是记录集的模型名或self(对于当前模型)。

如果方法以新的API风格调用，则没有效果，但是当从旧的API风格调用时，将记录集转换为id列表:

```python
>>> @api.multi
... @api.returns('self')
... def some_method(self):
...     return self
>>> new_style_model = env['a.model'].browse(1, 2, 3)
>>> new_style_model.some_method()
a.model(1, 2, 3)
>>> old_style_model = pool['a.model']
>>> old_style_model.some_method(cr, uid, [1, 2, 3], context=context)
[1, 2, 3]
```



## 模型参考

**class odoo.models.Model(*pool*, *cr*)**

常规数据库持久化Odoo模型的主超类。

Odoo模型是通过继承这个类创建的:

```python
class user(Model):
    ...
```

稍后，系统将根据每个数据库实例化该类一次(在该数据库上安装类的模块)。

### 结构属性

**_name**

​	业务对象名称，用点符号表示(在模块名称空间中)

**_rec_name**

​	可选字段用作名称，由osv的name_get()使用(默认:'name')

**_inherit**

如果设置了_name属性，它的取值是单个或多个父级的模型名称；没有设置_name属性时，只能是单个模型名称

**_order**

​	在没有指定顺序的情况下搜索order字段(默认值:'id')

​		Type		str

**_auto**

是否应该创建数据库表(默认值:True)

如果设置为False，则覆盖init()以创建数据库表

​	要创建没有任何表的模型，可以从odo .models. abstractmodel继承

**_table**

​	支持在_auto时创建的模型的表的名称，默认情况下自动生成。

**_inherits**

```python
_inherits = {
    'a.model': 'a_field_id',
    'b.model': 'b_field_id'
}
```

实现基于组合的继承:新模型公开_inherits-ed模型的所有字段，但不存储任何字段:值本身仍然存储在链接的记录中。

警告

​	如果在多个_inherit -ed上定义了相同的字段

**_constraints**

定义Python约束的列表(constraint_function, message, fields)。字段列表是指示性的

从8.0版开始就不提倡使用constrains()

**_sql_constraints**

列表(name、sql_definition、message)定义了在生成支持表时要执行的SQL约束

**_parent_store**

在parent_path字段旁边，设置记录树结构的索引存储，以便使用child_of和parent_of域操作符对当前模型的记录进行更快的层次查询。(默认值:False)

​	Type		bool



## CRUD

### create(*vals_list*) → records

为模型创建新记录。

使用dicts vals_list列表中的值初始化新记录，必要时使用default_get()列表中的值初始化新记录。

参数

vals_list(列表)

模型字段的值，作为字典列表:

```python
[{'field_name': field_value, ...}, ...]
```

为了向后兼容性，vals_list可以是一个字典。它被视为一个单例列表[vals]，并返回一条记录。

有关详细信息，请参见write()

Returns

​	创建的记录

Raises

AccessError -

如果用户对请求的对象没有创建权限

如果用户试图绕过用于在所请求对象上创建的访问规则

ValidateError—如果用户试图为不在选择中的字段输入无效值

UserError—如果在对象层次结构中创建一个循环，这是操作的结果(例如将对象设置为它自己的父对象)



### browse([*ids*]) → records

返回当前环境中作为参数提供的id的记录集。

不能接受任何id，单个id或id序列。

### unlink()

删除当前集的记录

Raises

- [**AccessError**](https://www.odoo.com/documentation/12.0/webservices/iap.html#odoo.exceptions.AccessError) –如果用户对请求的对象没有取消链接的权限

  如果用户试图绕过请求对象上解除链接的访问规则

  UserError—如果记录是其他记录的默认属性

### write(*vals*)

使用提供的值更新当前集中的所有记录。

参数

**vals** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict)) –

要更新的字段和要设置的值，例如:

```python
{'foo': 1, 'bar': "Qux"}
```

将字段foo设置为1，如果有效，字段栏设置为“Qux”(否则将触发错误)。

Raises

- [**AccessError**](https://www.odoo.com/documentation/12.0/webservices/iap.html#odoo.exceptions.AccessError) –

如果用户对请求的对象没有写权限

如果用户试图绕过对请求对象进行写操作的访问规则

ValidateError—如果用户试图为不在选择中的字段输入无效值

UserError—如果在对象层次结构中创建一个循环，这是操作的结果(例如将对象设置为它自己的父对象)

对于数值字段(Integer, Float)，值应该是对应的类型

对于布尔值，值应该是bool

对于选择，该值应该匹配选择值(通常是str，有时是int)

对于Many2one，该值应该是要设置的记录的数据库标识符

其他非关系字段使用字符串作为值

危险

出于历史和兼容性的原因，Date和Datetime字段使用字符串作为值(写入和读取)，而不是Date或Datetime。这些日期字符串只支持utc，并且根据odo .tools.misc进行格式化。DEFAULT_SERVER_DATE_FORMAT和odoo.tools.misc.DEFAULT_SERVER_DATETIME_FORMAT



One2many和Many2many使用一种特殊的“命令”格式来操作存储在/与字段关联的一组记录。

这种格式是一个按顺序执行的三元组列表，其中每个三元组都是要在一组记录上执行的命令。并不是所有的命令都适用于所有的情况。可能的命令是:

(0, _, values)

​	添加从提供的值dict创建的新记录。

(1, id, values)

​	用值中的值更新id的现有记录。不能在create()中使用。

(2, id, _)

​	从集合中删除id的记录，然后(从数据库中)删除它。不能在create()中使用。

(3, id, _)

​	从集合中删除id的记录，但不删除它。不能在一个2个以上使用。不能在create()中使用。

(4, id, _)

​	将id的现有记录添加到集合中。不能在一个2many上使用。

(5, _, _)

​	从集合中删除所有记录，相当于显式地对每个记录使用命令3。不能在一个2个以上使用。不能在create()中使用。

(6, _, ids)

替换ids列表中集合中的所有现有记录，相当于对ids中的每个id使用命令5后面跟着命令4。

面列表中标记为_的值将被忽略，可以是任何值，通常为0或False。



### read([*fields*])

为self、低级/RPC方法中的记录读取请求字段。在Python代码中，首选browse()。

参数

字段-要返回的字段名称列表(默认为所有字段)

Returns

将字段名称映射到其值的字典列表，每个记录对应一个字典

Raises

AccessError——如果用户没有对某些给定记录的读权限



### read_group(*domain*, *fields*, *groupby*, *offset=0*, *limit=None*, *orderby=False*, *lazy=True*)

获取按给定groupby字段分组的列表视图中的记录列表

参数

**domain** –指定搜索条件[[' field_name '， ' operator '， ' value ']，…]

**fields** ([`list`](https://docs.python.org/3/library/stdtypes.html#list)) – 对象上指定的列表视图中显示的字段的列表。每个元素要么是' field '(使用默认聚合的字段名)，要么是' field:agg '(使用聚合函数' agg '聚合字段)，要么是' name:agg(字段)'(使用' agg '聚合字段并将其返回为' name ')。可能的聚合函数是由PostgreSQL (https://www.postgresql.org/docs/current/static/functions-aggregate.html)和' count_distinct '提供的函数，具有预期的含义。

**groupby** ([`list`](https://docs.python.org/3/library/stdtypes.html#list)) –将记录分组的groupby描述列表。groupby描述要么是一个字段(然后根据该字段进行分组)，要么是一个字符串“field:groupby_function”。目前，只支持“day”、“week”、“month”、“quarter”或“year”等函数，它们只适用于date/datetime字段。

**offset** ([`int`](https://docs.python.org/3/library/functions.html#int)) –可选的要跳过的记录数

**limit** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 可选的返回记录的最大数量

**orderby** ([`list`](https://docs.python.org/3/library/stdtypes.html#list)) –要覆盖组的自然排序顺序，请参见search()(目前仅支持许多2one字段)

**lazy** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 如果为真，则只根据第一个groupby对结果进行分组，其余的groupby放在_context键中。如果为false，则所有groupbys都在一个调用中完成。

Returns

字典一览表(每项纪录一部字典)，包括:

按groupby参数中的字段分组的字段的值

__domain:指定搜索条件的元组列表

__context: 带有groupby这样的参数的字典

Return type

​	[{‘field_name_1’: value, ..]

Raises

[**AccessError**](https://www.odoo.com/documentation/12.0/webservices/iap.html#odoo.exceptions.AccessError) –

如果用户对请求的对象没有读权限

如果用户试图绕过对请求对象进行读取的访问规则



### 搜索

### search(*args[, offset=0][, limit=None][, order=None][, count=False]*)

基于args搜索域搜索记录

参数

- **args** – [A search domain](https://www.odoo.com/documentation/12.0/reference/orm.html#reference-orm-domains).使用空列表匹配所有记录。
- **offset** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 要忽略的结果数量(默认值:none)
- **limit** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 返回的最大记录数(默认值:all)
- **order** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) –排序字符串
- **count** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) –如果为真，则只计数并返回匹配记录的数量(默认值:False)

Returns

​	最多限制匹配搜索条件的记录

Raises

**AccessError**

如果用户试图绕过对请求对象进行读取的访问规则。



### search_count(*args*) → int

返回当前模型中与提供的域匹配的记录的数量。



### name_search(*name=''*, *args=None*, *operator='ilike'*, *limit=100*) → records

搜索具有与给定操作符相匹配的显示名称匹配给定名称模式的记录，同时也匹配可选搜索域(args)。

例如，它用于根据关系字段的部分值提供建议。有时可以看作是name_get()的反函数，但不能保证一定是。

这个方法等价于使用基于display_name的搜索域调用search()，然后根据搜索结果调用name_get()。

参数

- **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 要匹配的名称模式
- **args** ([`list`](https://docs.python.org/3/library/stdtypes.html#list)) – 可选搜索域(有关语法，请参阅search())，指定进一步的限制
- **operator** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) –用于匹配名称的域操作符，如“like”或“=”。
- **limit** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 可选的返回记录的最大数量

Return type

​		list

Returns 

所有匹配记录的对列表(id, text_repr)。



## 记录集的操作

### ids

此记录集中实际记录id的列表(忽略要创建记录的占位符id)

### ensure_one()

验证当前记录集是否保存一条记录。否则引发异常raise ValueError("Expected singleton: %s" % self)

### exists() → records

返回self中存在的记录子集，并在缓存中标记已删除的记录。它可以用作对记录的测试:

```python
if record.exists():
    ...
```

按照惯例，新记录作为现有记录返回。

### filtered(*func*)

选择self中的记录，使func(rec)为真，并将它们作为记录集返回。

参数

**func** – 一个函数或字段名的点分隔序列



### sorted(*key=None*, *reverse=False*)

返回按键自排序的记录集。

参数

**key** – 一个参数的函数，它为每个记录返回一个比较键，或者一个字段名，或者一个None，在这种情况下，记录是按照默认模型的顺序排序的

**reverse** – 如果为真，则以相反的顺序返回结果



### mapped(*func*)

对self中的所有记录应用func，并以列表或记录集的形式返回结果(如果func返回记录集)。在后一种情况下，返回记录集的顺序是任意的。

Parameters

**func** – 一个函数或一个点分隔的字段名序列(字符串);任何错误值只返回记录集self

```python
self.mapped('line_ids').unlink()
#删除明细行
```



## 环境交换

### sudo([*user=SUPERUSER*])

返回附加到所提供用户的此记录集的新版本。

默认情况下，它返回一个超级用户记录集，在那里访问控制和记录规则被绕过。

使用sudo可能会导致数据访问跨越记录规则的边界，可能会混合那些应该隔离的记录(例如，在多公司环境中来自不同公司的记录)。

它可能会导致在方法中从许多记录中选择一条的不直观的结果——例如获得默认的公司，或者选择一份材料清单。

由于必须重新评估记录规则和访问控制，因此新记录集将无法从当前环境的数据缓存中获益，因此以后的数据访问可能会在重新从数据库获取数据时产生额外的延迟。返回的记录集具有与self相同的预取对象。



### with_context(*[context][, **overrides]*) → records

返回附加到扩展上下文的此记录集的新版本。

扩展上下文是提供的合并重写的上下文，或者是合并重写的当前上下文，例如:

```python
# current context is {'key1': True}
r2 = records.with_context({}, key2=True)
# -> r2._context is {'key2': True}
r2 = records.with_context(key2=True)
# -> r2._context is {'key1': True, 'key2': True}
```



### with_env(*env*)

返回附加到所提供环境的此记录集的新版本

警告

新环境不会从当前环境的数据缓存中获益，因此以后的数据访问可能会在重新从数据库获取数据时产生额外的延迟。返回的记录集具有与self相同的预取对象。



## 查询字段和视图

### fields_get(*[fields][, attributes]*)

返回每个字段的定义。

返回的值是字典的字典(由字段名指示)。包含_inherits 'd字段。翻译字符串、帮助和选择(如果存在)属性。

Parameters

- **allfields** – 要记录的字段列表，所有字段(如果为空或未提供)
- **attributes** – 为每个字段返回的描述属性列表，如果为空或未提供，则全部返回

### fields_view_get([*view_id | view_type='form'*])

获取所请求视图的详细组成，如字段、模型、视图体系结构

Parameters

- **view_id** – 视图的id或None
- **view_type** – 如果view_id为None (' form '， ' tree '，…)，则返回视图的类型。
- **toolbar** – true用于包含上下文操作
- **submenu** – 弃用

Returns

描述请求视图(包括继承视图和扩展)组成的字典

- **AttributeError**

   

  –

  - 如果继承的视图除了“before”、“after”、“inside”之外还有未知的位置可以使用，则使用“replace”
  - 如果在父视图中找到“位置”以外的标记

- **Invalid ArchitectureError** –如果结构上定义了除表单、树、日历、搜索之外的视图类型



## 各种各样的方法

### default_get(*fields*) → default_values

返回fields_list中的字段的默认值。默认值由上下文、用户默认值和模型本身决定。

Parameters

**fields_list** – 字段名的列表

Returns

字典将每个字段名映射到对应的默认值(如果有)。



### copy(*default=None*)

重复记录用默认值自动更新它

Parameters

**default** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict)) – 要在复制记录的原始值中重写的字段值字典，e。g: {'field_name': overridden_value，…}`

Returns

new record



### name_get() → [(id, name), ...]

返回self中记录的文本表示形式。默认情况下，这是display_name字段的值。

Returns	每个记录的对列表(id, text_repr)

Return type		list(tuple)



### name_create(*name*) → record

通过调用Create()创建一条新记录，只提供一个值:新记录的显示名称。

新记录将使用适用于此模型的任何缺省值初始化，或者通过上下文提供。create()的通常行为是适用的。

Parameters

**name** – 显示要创建的记录的名称

Return type

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)

Returns

创建的记录的name_get()对值



## 自动字段

### id

标识符字段

### _log_access

是否应该生成日志访问字段(create_date, write_uid，…)(默认值:True)

### create_date

记录创建的日期

​		Type		Datetime

### create_uid

关系字段到创建记录的用户

​		Type		res.users

### write_uid

关系字段到最后修改记录的用户

​		Type	res.users



## 保留字段名称

一些字段名保留给预定义的行为，而不是自动字段的行为。当需要相关行为时，应该在模型上定义它们:

### name

_rec_name的默认值，用于在需要代表性“命名”的上下文中显示记录。

​		Type		Char

### active

切换记录的全局可见性，如果active设置为False，则记录在大多数搜索和列表中都是不可见的

​		Type		Boolean

### sequence

可更改的排序标准，允许在列表视图中拖放模型的重新排序

​		Type		Integer

### state

对象的生命周期阶段，由字段上的状态属性使用

​		Type		Selection

### parent_id

用于对树结构中的记录进行排序，并在域中启用 child_of 和 parent_of 操作符

​		Type		Many2one

### parent_path

当_parent_store被设置为True时，用于存储树结构的索引—必须使用index=True声明，以便正确操作。

​		Type		Char



## 方法修饰符

这个模块提供了管理两种不同API样式的元素，即“传统”和“记录”样式。

在“传统”样式中，像数据库游标、用户id、上下文字典和记录id(通常表示为cr、uid、上下文、id)这样的参数显式地传递给所有方法。在“record”样式中，这些参数隐藏在模型实例中，这给了它一种更面向对象的感觉。

例如:

```python
model = self.pool.get(MODEL)
ids = model.search(cr, uid, DOMAIN, context=context)
for rec in model.browse(cr, uid, ids, context=context):
    print rec.name
model.write(cr, uid, ids, VALUES, context=context)
```

也可写成:

```python
env = Environment(cr, uid, context) # cr, uid, context wrapped in env
model = env[MODEL]                  # retrieve an instance of MODEL
recs = model.search(DOMAIN)         # search returns a recordset
for rec in recs:                    # iterate over the records
    print rec.name
recs.write(VALUES)                  # update all records in recs
```

使用“传统”样式编写的方法会根据一些基于参数名称的启发式方法自动修饰。

### odoo.api.multi(*method*)

修饰记录风格的方法，其中self是一个记录集。该方法通常在记录上定义一个操作。这样一个方法:

```python
@api.multi
def method(self, args):
    ...
```

可被称为在记录和传统风格，如:

```python
# recs = model.browse(cr, uid, ids, context)
recs.method(args)

model.method(cr, uid, ids, args, context=context)
```

### odoo.api.model(*method*)

修饰一个记录风格的方法，其中self是一个记录集，但是它的内容不相关，只有模型相关。这样一个方法:

```python
@api.model
def method(self, args):
    ...
```

可被称为在记录和传统风格，如:

```python
# recs = model.browse(cr, uid, ids, context)
recs.method(args)

model.method(cr, uid, args, context=context)
```

注意，传统样式中没有传递id给方法。

### odoo.api.depends(**args*)

返回一个装饰器，它指定“compute”方法的字段依赖关系(对于新样式的函数字段)。每个参数必须是一个字符串，由一个点分隔的字段名序列组成:

```python
pname = fields.Char(compute='_compute_pname')

@api.one
@api.depends('partner_id.name', 'partner_id.is_company')
def _compute_pname(self):
    if self.partner_id.is_company:
        self.pname = (self.partner_id.name or "").upper()
    else:
        self.pname = self.partner_id.name
```

也可以将单个函数作为参数传递。在这种情况下，依赖关系是通过调用带有字段模型的函数来给出的。

### odoo.api.constrains(**args*)

修饰约束检查器。每个参数必须是一个字段名用于检查:

```python
@api.one
@api.constrains('name', 'description')
def _check_description(self):
    if self.name == self.description:
        raise ValidationError("Fields name and description must be different")
```

在已修改其中一个命名字段的记录上调用。

如果验证失败，应该引发ValidationError。

Warning

`@constrains`只支持简单的字段名，点状名称(关系字段的字段，如partner_id.customer)不受支持，将被忽略

`@constrains仅当修饰方法中的声明字段包含在create或write调用中时才会触发。它意味着视图中不存在的字段在创建记录期间不会触发调用。覆盖create是必要的，以确保约束总是被触发(例如，测试值的缺失)。`



### odoo.api.onchange(**args*)

返回装饰器来装饰给定字段的onchange方法。每个参数必须是一个字段名:

```python
@api.onchange('partner_id')
def _onchange_partner(self):
    self.message = "Dear %s" % (self.partner_id.name or "")
```

在字段出现的表单视图中，当某个给定字段被修改时，将调用该方法。方法在包含表单中呈现的值的伪记录上调用。该记录上的字段分配会自动发送回客户机。

该方法可能会返回一个字典，用于更改字段域，并弹出一条警告消息，就像在旧的API中一样:

```python
return {
    'domain': {'other_id': [('partner_id', '=', partner_id)]},
    'warning': {'title': "Warning", 'message': "What is this?"},
}
```

### Warning

@onchange 只支持简单的字段名，点名(关系字段的字段，如partner_id.tz)不受支持，将被忽略

### odoo.api.returns(*model*, *downgrade=None*, *upgrade=None*)

返回返回模型实例的方法的装饰器。

Parameters

- **model** – 当前模型的模型名称或“self”
- **downgrade** – 函数降级(self、value、*args、**kwargs)，将记录样式的值转换为传统样式的输出
- **upgrade** – 函数升级(self、value、*args、**kwargs)，将传统样式的值转换为记录样式的输出

参数self、*args和**kwargs是以记录样式传递给方法的参数。

decorator将方法输出调整为api风格:id, id或False用于传统风格，记录集用于记录风格:

```python
@model
@returns('res.partner')
def find_partner(self, arg):
    ...     # return some record

# output depends on call style: traditional vs record style
partner_id = model.find_partner(cr, uid, arg, context=context)

# recs = model.browse(cr, uid, ids, context)
partner_record = recs.find_partner(arg)
```

注意，修饰后的方法必须满足该约定。

这些装饰器将自动继承:覆盖已装饰的现有方法的方法将使用相同的@returns(模型)进行装饰。

### odoo.api.one(*method*)

修饰一个记录风格的方法，其中self应该是一个单例实例。修饰后的方法会自动循环记录，并使用结果生成一个列表。如果方法被returns()修饰，它将连接结果实例。这样一个方法:

```python
@api.one
def method(self, args):
    return self.name
```

可被称为在记录和传统风格，如:

```python
# recs = model.browse(cr, uid, ids, context)
names = recs.method(args)
names = model.method(cr, uid, ids, args, context=context)
```

自9.0版以来一直不提倡使用one():它常常使代码变得不那么清晰，并且以开发人员和读者可能不期望的方式运行。

强烈建议使用multi()，并对self记录集进行迭代，或者确保记录集是一条带有ensure_one()的记录。

### odoo.api.v7(*method_v7*)

修饰只支持旧式api的方法。通过重新定义具有相同名称并使用v8()装饰的方法，可以提供一种新型的api:

```python
@api.v7
def foo(self, cr, uid, ids, context=None):
    ...

@api.v8
def foo(self):
    ...
```

如果一个方法调用另一个方法，必须特别小心，因为该方法可能被覆盖!在这种情况下，应该从当前类调用方法(比如MyClass)，例如:

```python
@api.v7
def foo(self, cr, uid, ids, context=None):
    # Beware: records.foo() may call an overriding of foo()
    records = self.browse(cr, uid, ids, context)
    return MyClass.foo(records)
```

注意，包装器方法使用第一个方法的docstring。

### odoo.api.v8(*method_v8*)

修饰只支持新样式api的方法。通过重新定义具有相同名称的方法，并使用v7()装饰，可以提供旧式的api:

```python
@api.v8
def foo(self):
    ...

@api.v7
def foo(self, cr, uid, ids, context=None):
    ...
```

注意，包装器方法使用第一个方法的docstring。







## 字段

### 基本字段

*class* odoo.fields.Field(*string=<object object>*, ***kwargs*)

字段描述符包含字段定义，并管理记录上相应字段的访问和分配。在即时化字段时，可能会提供以下属性:

### 基础字段属性

- **string** – 用户看到的字段标签(字符串);如果没有设置，ORM接受类中的字段名(大写)。
- **help** – 用户看到的字段的工具提示(字符串)
- **readonly** – 字段是否为只读(布尔值，默认为False)
- **required** – 是否需要该字段的值(布尔值，默认为False)
- **index** – 是否在数据库中索引字段。注意:对非存储和虚拟字段没有影响。(布尔值，默认为False)
- **default** – 字段的默认值;这要么是一个静态值，要么是一个获取记录集并返回值的函数;使用default=None放弃字段的默认值
- **states** – 将状态值映射到UI属性值对列表的字典;可能的属性有:' readonly '、' required '、' invisible '。注意:任何基于状态的条件都要求状态字段值在客户端UI上可用。这通常是通过将其包含在相关视图中来实现的，如果与最终用户无关，则可能使其不可见。
- **groups** – 以逗号分隔的组xml id列表(字符串);这只限制了对给定组的用户的字段访问
- **copy** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 记录复制创建新的记录时是否应该复制字段值(默认值:对于普通字段为True，对于one2many和computed字段为False，包括属性字段和相关字段)
- **oldname** (`string`) – 此字段的前一个名称，以便ORM可以在迁移时自动重命名它



### 计算字段

可以定义一个字段，该字段的值是计算出来的，而不是简单地从数据库中读取。下面给出了特定于计算字段的属性。要定义这样一个字段，只需为属性compute提供一个值。

Parameters

- **compute** – 计算字段的方法的名称
- **inverse** – 与字段反向的方法的名称(可选)
- **search** – 实现字段搜索的方法的名称(可选)
- **store** – 字段是否存储在数据库中(布尔值，计算字段默认为False)
- **compute_sudo** – 是否应该将字段重新计算为超级用户以绕过访问权限(布尔值，默认为False)，请注意，这对非存储的计算字段没有影响

给出的计算方法、反演方法和搜索方法都是模型方法。他们的签名如下例所示:

```python
upper = fields.Char(compute='_compute_upper',
                    inverse='_inverse_upper',
                    search='_search_upper')

@api.depends('name')
def _compute_upper(self):
    for rec in self:
        rec.upper = rec.name.upper() if rec.name else False

def _inverse_upper(self):
    for rec in self:
        rec.name = rec.upper.lower() if rec.upper else False

def _search_upper(self, operator, value):
    if operator == 'like':
        operator = 'ilike'
    return [('name', operator, value)]
```

compute方法必须为调用的记录集的所有记录分配字段。必须对计算方法应用decorator odo .api.depends()来指定字段依赖关系;这些依赖关系用于确定何时重新计算字段;重新计算是自动的，并保证缓存/数据库的一致性。注意，相同的方法可以用于多个字段，您只需分配方法中的所有给定字段;方法将为所有这些字段调用一次。

默认情况下，computed字段不会存储到数据库中，而是动态计算的。添加属性store=True将在数据库中存储字段的值。存储字段的优点是，对该字段的搜索由数据库本身完成。缺点是，当必须重新计算字段时，它需要数据库更新。

顾名思义，逆方法执行计算方法的逆操作:调用的记录具有字段的值，您必须对字段依赖关系应用必要的更改，以便计算给出预期值。注意，没有逆方法的计算字段在默认情况下是只读的。

在对模型进行实际搜索之前处理域时调用搜索方法。它必须返回一个与条件等价的域:字段操作符值。



### 相关领域

相关字段的值是通过遵循一系列关系字段并在到达的模型上读取一个字段来给出的。要遍历的字段的完整序列由属性指定

Parameters

​	**related** – 字段名序列

如果没有重新定义某些字段属性，则会自动从源字段复制它们:string、help、readonly、required(仅当序列中的所有字段都是必需的)、组、数字、大小、翻译、清理、选择、comodel_name、域、上下文。所有无语义的属性都从源字段复制。

默认情况下，相关字段的值不会存储到数据库中。添加属性store=True使其存储，就像计算字段一样。当相关字段的依赖项被修改时，将自动重新计算相关字段。

### Company-dependent字段

以前被称为“property”字段，这些字段的价值取决于公司。换句话说，属于不同公司的用户可能在给定记录上看到字段的不同值。

Parameters

**company_dependent** – 字段是否依赖于company_dependent(布尔值)



### 增量定义

字段定义为模型类上的类属性。如果扩展了模型(参见模型)，还可以通过在子类上重新定义具有相同名称和类型的字段来扩展字段定义。在这种情况下，字段的属性取自父类，并由子类中给出的属性覆盖。

例如，下面的第二个类只在字段状态上添加了一个工具提示:

```python
class First(models.Model):
    _name = 'foo'
    state = fields.Selection([...], required=True)

class Second(models.Model):
    _inherit = 'foo'
    state = fields.Selection(help="Blah blah blah")
```



### class odoo.fields.Char(*string=<object object>*, ***kwargs*)

Bases: `odoo.fields._String`

基本字符串字段，可以限制长度，通常在客户端显示为单行字符串。

Parameters

- **size** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 为该字段存储的值的最大大小
- **trim** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 声明值是否被修剪(默认情况下为True)。注意，微调操作仅由web客户机应用。
- **translate** – 启用字段值的翻译;使用translate=True将字段值转换为整体;翻译也可以是可调用的，比如翻译(回调，值)通过使用回调(术语)来检索术语的翻译来翻译值。



### class odoo.fields.Boolean(*string=<object object>*, ***kwargs*)

Bases: `odoo.fields.Field`

### *class* odoo.fields.Integer(*string=<object object>*, ***kwargs*)

Bases: `odoo.fields.Field`

###### ### class odoo.fields.Float(*string=<object object>*, *digits=<object object>*, ***kwargs*)[source]

Bases: `odoo.fields.Fiel`

精度数字由属性给出

Parameters

**digits** – 一对(total, decimal)，或者一个函数获取数据库游标并返回一对(total, decimal)



### class odoo.fields.Text(*string=<object object>*, ***kwargs*)

Bases: `odoo.fields._String`

与Char非常相似，但用于更长的内容，没有大小，通常显示为多行文本框。

Parameters

**translate** – 启用字段值的翻译;使用translate=True将字段值转换为整体;翻译也可以是可调用的，比如翻译(回调，值)通过使用回调(术语)来检索术语的翻译来翻译值。



### class odoo.fields.Selection(*selection=<object object>*, *string=<object object>*,***kwargs*)

Bases: `odoo.fields.Field`

Parameters

- **selection** – 指定此字段的可能值。它以对列表(值、字符串)或模型方法或方法名的形式给出。
- **selection_add** –在覆盖字段的情况下提供选择的扩展。它是对的列表(值、字符串)。

除了在相关字段或字段扩展的情况下，属性选择是强制性的。

### class odoo.fields.Html(*string=<object object>*, ***kwargs*)

Bases: `odoo.fields._String`



### 日期和日期时间字段

日期和日期时间是非常重要的在任何类型的业务应用程序,他们大量使用在许多流行的Odoo应用,如物流或会计及其滥用还创造无形的痛苦的错误,这段的目的是为Odoo开发者提供所需的知识,避免滥用这些字段。

当为Date/Datetime字段赋值时，以下选项是有效的:

- 用于日期字段的服务器格式(YYYY-MM-DD)字符串，用于日期时间字段的服务器格式(YYYY-MM-DD HH:MM:SS)字符串。
- A `date` or `datetime` object.
- `False` or `None`.

如果不确定类型的值被分配给一个日期/ Datetime对象,最好的做法是将值传递给to_date()或to_datetime()将试图将值转换为一个日期或Datetime对象分别可以分配给该领域的问题。

例子

解析来自外部资源的日期/日期时间:

```python
fields.Date.to_date(self._context.get('date_from'))
```



Date / Datetime最佳实践:

Date字段只能与Date对象进行比较。

Datetime字段只能与Datetime对象进行比较。

警告

表示dates 和datetimes的字符串可以相互比较，但是结果可能不是预期的结果，因为datetime字符串总是大于date字符串，因此强烈反对这种做法。

使用日期和日期时间的常见操作(如加法、减法或获取句点的开始/结束)通过Date和Datetime公开。通过导入odo .tools.date_utils，还可以使用这些帮助程序。

###### `*class* odoo.fields.Date(*string=<object object>*, ***kwargs*)`

Bases: [`odoo.fields.Field`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Field)

###### `*static* add(**args*, ***kwargs*)`

返回值和一个relativedelta的和。

Parameters

- **value** – 初始日期或日期时间。
- **args** – 要直接传递到的位置参数 `relativedelta`.
- **kwargs** – 要直接传递到的关键字args `relativedelta`.

Returns

产生的 date/datetime.



### static context_today(*timestamp=None*)

以适合日期字段的格式返回在客户端时区中看到的当前日期。此方法可用于计算默认值。

Parameters

- **record** – 将从中获得时区的记录集。
- **timestamp** (`datetime`) – 使用可选的datetime值代替当前日期和时间(必须是datetime，不能在时区之间转换常规日期)。

Return type

date



### static end_of(*granularity*)

从日期或日期时间中获取时间段的末尾。

Parameters

- **value** – 初始日期或日期时间。
- **granularity** – Type of period in string, can be year, quarter, month, week, day or hour.字符串中的句点类型，可以是年、季度、月、周、日或小时。

Returns

A date/datetime object 一个日期/日期时间对象，对应于指定周期的开始。



### static start_of(*granularity*)

从日期或日期时间开始计时。

Parameters

- **value** –初始日期或日期时间。
- **granularity** – type of period in string, can be year, quarter, month, week, day or hour.字符串中的句点类型，可以是年、季度、月、周、日或小时。

Returns

a date/datetime object corresponding to the start of the specified period.一个日期/日期时间对象，对应于指定周期的开始。



### static subtract(**args*, ***kwargs*)

返回值和相对值之间的差值。

Parameters

- **value** – 初始日期或日期时间。
- **args** – 要直接传递到的位置参数 `relativedelta`.
- **kwargs** – 要直接传递到的关键字args `relativedelta`.

Returns

the resulting date/datetime.

### static to_date()

尝试将值转换为日期对象。

这个函数可以作为输入不同类型:

一个伪对象，在这种情况下不会返回任何值。

表示日期或日期时间的字符串。

一个日期对象，在这种情况下，对象将按原样返回。

一个datetime对象，在这种情况下，它将被转换为一个date对象，所有与datetime相关的信息都将丢失(HMS、TZ、…)。

Parameters

**value** – 转换值

Returns

表示值的对象。

Return type

date



### static to_string()

将日期或datetime对象转换为字符串。

Parameters

**value** –转换值

Returns

以服务器的日期格式表示值的字符串，如果值的类型是datetime，则小时、分钟、秒、tzinfo将被截断。

Return type		str



### static today()

以ORM期望的格式返回当前日期。这个函数可以用来计算默认值。

###### `*class* odoo.fields.Datetime(*string=<object object>*, ***kwargs*)`

Bases: [`odoo.fields.Field`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Field)

###### `*static* add(**args*, ***kwargs*)`

返回值和一个relativedelta的和。

Parameters

- **value** – 初始日期或日期时间。
- **args** – 位置参数直接传递给relativedelta`.
- **kwargs** –关键字args直接传递`relativedelta`.

Returns

the resulting date/datetime.



### static context_timestamp(*timestamp*)

返回转换到客户机时区的给定时间戳。此方法不用于默认初始化器，因为datetime字段在客户端显示时将自动转换。对于默认值，应该使用fields. date .now()。

Parameters

- **record** – 将从中获得时区的记录集。
- **timestamp** (`datetime`) – 要转换到客户机时区的朴素datetime值(用UTC表示)。

Return type

datetime

Returns

timestamp converted to timezone-aware datetime in context timezone.在上下文时区中转换为时区感知的datetime的时间戳。



### static end_of(*granularity*)

从日期或日期时间中获取时间段的末尾。

从日期或日期时间开始计时。

Parameters

- **value** –初始日期或日期时间。
- **granularity** – type of period in string, can be year, quarter, month, week, day or hour.字符串中的句点类型，可以是年、季度、月、周、日或小时。

Returns

a date/datetime object corresponding to the start of the specified period.一个日期/日期时间对象，对应于指定周期的开始。



### static now()

以ORM期望的格式返回当前日期和时间。这个函数可以用来计算默认值。



### static start_of(*granularity*)

从日期或日期时间开始计时。

Parameters

- **value** –初始日期或日期时间。
- **granularity** – type of period in string, can be year, quarter, month, week, day or hour.字符串中的句点类型，可以是年、季度、月、周、日或小时。

Returns

a date/datetime object corresponding to the start of the specified period.一个日期/日期时间对象，对应于指定周期的开始。



### static subtract(**args*, ***kwargs*)

返回值和相对值之间的差值。Return the difference between `value` and a `relativedelta`.

Parameters

- **value** – initial date or datetime.
- **args** – positional args to pass directly to `relativedelta`.
- **kwargs** – keyword args to pass directly to `relativedelta`.

Returns

the resulting date/datetime.



### static to_datetime()

将ORM值转换为datetime值。

这个函数可以作为输入不同类型:

一个伪对象，在这种情况下不会返回任何值。

表示日期或日期时间的字符串。

datetime对象，在这种情况下，对象将按原样返回。

一个日期对象，在这种情况下，它将被转换为一个datetime对象。

Parameters

**value** – value to convert.

Returns

an object representing `value`.

Return type

datetime



###### `*static* to_string()`

Convert a `datetime` or `date` object to a string.

Parameters

**value** – value to convert.

Returns

a string representing `value` in the server’s datetime format, if `value` is of type `date`, the time portion will be midnight (00:00:00).

Return type		str

###### `*static* today()`

Return the current day, at midnight (00:00:00).



## 关联字段

### *class* odoo.fields.Many2one(*comodel_name=<object object>*, *string=<object object>*,***kwargs*)

Bases: `odoo.fields._Relational`

此类字段的值是大小为0(无记录)或1(单个记录)的记录集。

Parameters

- **comodel_name** – 目标模型的名称(字符串)
- **domain** – an optional domain to set on candidate values on the client side (domain or string)
- **context** – 可选域，用于在客户端(域或字符串)上设置候选值
- **ondelete** – 删除所引用的记录时应怎样做;可能的值是: `'set null'`, `'restrict'`, `'cascade'`
- **auto_join** – 是否在搜索该字段时生成连接(boolean, by default `False`)
- **delegate** – 将其设置为True，使目标模型的字段可以从当前模型访问(对应于_inherits)

属性comodel_name是强制性的，除非在相关字段或字段扩展的情况下。



### *class* odoo.fields.One2many(*comodel_name=<object object>*, *inverse_name=<object object>*,*string=<object object>*, ***kwargs*)

Bases: `odoo.fields._RelationalMulti`

One2many领域;这样一个字段的值是comodel_name中所有记录的记录集，以便字段inverse_name等于当前记录。

Parameters

- **comodel_name** – 目标模型的名称(字符串)
- **inverse_name** – comodel_name (string)中的Many2one字段的倒数
- **domain** – 可选域，用于在客户端(域或字符串)上设置候选值
- **context** – 在客户端处理该字段时使用的可选上下文(字典)
- **auto_join** – 是否在搜索该字段时生成连接(布尔值，默认为False)
- **limit** – 读取时使用的可选限制(整数)

除了在相关字段或字段扩展的情况下，属性comodel_name和inverse_name是必需的。



### class odoo.fields.Many2many(*comodel_name=<object object>*, *relation=<object object>*,*column1=<object object>*, *column2=<object object>*, *string=<object object>*, ***kwargs*)

Bases: `odoo.fields._RelationalMulti`

Many2many领域;这样一个字段的值就是记录集。

Parameters

- **comodel_name** – 目标模型的名称(字符串)

属性comodel_name是强制性的，除非在相关字段或字段扩展的情况下。

- **relation** – 在数据库中存储关系的表的可选名称(字符串)
- **column1** – 引用表关系(字符串)中的“这些”记录的列的可选名称
- **column2** – 引用表关系(字符串)中的“那些”记录的列的可选名称

属性关系column1和column2是可选的。如果没有给出，名称将自动从模型名称生成，前提是model_name和comodel_name是不同的!

Parameters

- **domain** – 可选域，用于在客户端(域或字符串)上设置候选值
- **context** – 在客户端处理该字段时使用的可选上下文(字典)
- **limit** – 读取时使用的可选限制(整数)



###### class odoo.fields.Reference(*selection=<object object>*, *string=<object object>*,***kwargs*)

Bases: odoo.fields.Selection



## 继承和扩展

Odoo提供了三种不同的机制，以模块化的方式扩展模型:

odoo有三种模块化的模型继承机制：

- 根据原有模型创建一个全新的模型，并基于新创建的模型修改，新模型与已存在的视图兼容，并保存在同一张表中
- 从其他模块中扩展模型，并进行替换，一般用于复制，已存在的视图会忽略新建的模型，数据保存在新的数据表中
- 通过代理访问其他模型的字段，可以同时继承多个模型，数据保存在新的数据表中，新的模型会包含一个嵌入的原模型，并且该模型数据是同步的

![](https://www.odoo.com/documentation/12.0/_images/inheritance_methods1.png)

### 古典继承

当同时使用`_inherit`和`_name`属性时，Odoo使用现有的(通过_inherit提供)作为基础创建一个新模型。新模型从其基础获取所有字段、方法和元信息(default & al)。

```python
class Inheritance0(models.Model):
    _name = 'inheritance.0'
    _description = 'Inheritance Zero'

    name = fields.Char()

    def call(self):
        return self.check("model 0")

    def check(self, s):
        return "This is {} record {}".format(s, self.name)

class Inheritance1(models.Model):
    _name = 'inheritance.1'
    _inherit = 'inheritance.0'
    _description = 'Inheritance One'

    def call(self):
        return self.check("model 1")
```

和使用:

```python
a = env['inheritance.0'].create({'name': 'A'})
b = env['inheritance.1'].create({'name': 'B'})
    a.call()
    b.call()
```

将收益率:

```
            "This is model 0 record A"
            "This is model 1 record B"
```

第二个模型继承了第一个模型的check方法及其name字段，但是覆盖了call方法，就像使用标准Python继承时一样。



## 扩展

当使用`_inherit`而不使用`_name`时，新模型将替换现有模型，本质上是就地扩展它。这对于向现有模型(在其他模块中创建的)添加新字段或方法，或自定义或重新配置它们(例如更改它们的默认排序顺序)非常有用:

```python
    _name = 'extension.0'
    _description = 'Extension zero'

    name = fields.Char(default="A")

class Extension1(models.Model):
    _inherit = 'extension.0'

    description = fields.Char(default="Extended")
```

```python
record = env['extension.0'].create({})
record.read()[0]
```

将收益率:

```python
{'name': "A", 'description': "Extended"}
```

它还将生成各种自动字段，除非禁用了它们



### 委托继承

第三种继承机制提供了更大的灵活性(可以在运行时更改)，但功能更少:使用_inherits模型将当前模型上没有找到的任何字段的查找委托给“子”模型。委托是通过在父模型上自动设置的引用字段来执行的:

```python
class Child0(models.Model):
    _name = 'delegation.child0'
    _description = 'Delegation Child zero'

    field_0 = fields.Integer()

class Child1(models.Model):
    _name = 'delegation.child1'
    _description = 'Delegation Child one'

    field_1 = fields.Integer()

class Delegating(models.Model):
    _name = 'delegation.parent'
    _description = 'Delegation Parent'

    _inherits = {
        'delegation.child0': 'child0_id',
        'delegation.child1': 'child1_id',
    }

    child0_id = fields.Many2one('delegation.child0', required=True, ondelete='cascade')
    child1_id = fields.Many2one('delegation.child1', required=True, ondelete='cascade')
```

```python
        record = env['delegation.parent'].create({
            'child0_id': env['delegation.child0'].create({'field_0': 0}).id,
            'child1_id': env['delegation.child1'].create({'field_1': 1}).id,
        })
            record.field_0
            record.field_1
```

将导致:

```
            0
            1
```

也可以直接写在委托字段上:

```
        record.write({'field_1': 4})
```

警告

当使用委托继承时，方法不是继承的，而是字段



## Domains域

域是一个标准列表，每个标准是(field_name, operator, value)的三元组(列表或元组)，其中:

`field_name` **(**`str`**)**

当前模型的字段名，或使用点符号遍历Many2one的关系，例如。“street”或“partner_id.country”

`operator` (`str`)

用于将field_name与值进行比较的操作符。有效的操作符是:

|           |                                                              |      |
| :-------: | :----------------------------------------------------------: | ---- |
|     =     |                             等于                             |      |
|    !=     |                            不等于                            |      |
|     >     |                             大于                             |      |
|    >=     |                          大于或等于                          |      |
|     <     |                             小于                             |      |
|    <=     |                          小于或等于                          |      |
|    =?     | unset或equals to(如果值为None或False，返回true，否则行为类似=) |      |
|   =like   | 根据值模式匹配field_name。模式中的下划线_表示(匹配)任何单个字符;百分号%匹配任何由0或多个字符组成的字符串。 |      |
|   like    | 将field_name与%value%模式匹配。类似于=like，但是在匹配之前用' % '包装值 |      |
| not like  |                       与%值%模式不匹配                       |      |
|   ilike   |                        不分大小写like                        |      |
| not ilike |                      不分大小写not like                      |      |
|  =ilike   |                       不分大小写=like                        |      |
|    in     |      等于value中的任何一项，value应该是a list of items       |      |
|  not in   |                     不等于所有项目的价值                     |      |
| child_of  | 是值记录的子(后代)。考虑模型的语义(i.e在由_parent_name命名的关系字段后面)。 |      |



### value

变量类型，必须(通过操作符)与指定字段相比较



**域标准可以使用前缀形式的逻辑运算符组合:**

```
'&'
```

逻辑和默认操作，以将下列标准组合在一起。浓度2(使用接下来的两个标准或组合)。

```
'|'
```

逻辑的或者，浓度2。

```
'!'
```

不符合逻辑，是浓度1。

主要是否定标准的组合

单个准则通常有一个负数形式(例如= -> !=，< -> >=)，这比否定正数要简单。

例子

寻找来自比利时或德国、母语非英语的ABC合作伙伴:

```
[('name','=','ABC'),
 ('language.code','!=','en_US'),
 '|',('country_id.code','=','be'),
     ('country_id.code','=','de')]
```

这个域可以解释为:

```
    (name is 'ABC')
AND (language is NOT english)
AND (country is Belgium OR Germany)
```



## 从旧API移植到新API

- 在新的API中要避免使用id的裸列表，而是使用记录集

- 仍然在旧API中编写的方法应该由ORM自动桥接，不需要切换到旧API，只需像调用新API方法一样调用它们。有关详细信息，请参阅旧API方法的自动桥接。

- [`search()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.search) 返回一个记录集，没有意义，例如浏览其结果
- `fields.related` and `fields.function`。函数的替换方法是使用一个普通字段类型，其中包含一个related=或compute=参数

- depends()  依赖于compute =methods 必须是完整的，它必须列出计算方法使用的所有字段和子字段。有太多的依赖关系(在不需要的情况下将重新计算字段)比没有足够的依赖关系(将忘记重新计算字段，然后值将不正确)要好
- 删除计算字段上的所有onchange方法。当其中一个依赖项更改时，计算字段将自动重新计算，该依赖项用于客户端自动生成onchange

- decorators model()和multi()用于在从旧API上下文中调用时进行桥接，对于内部或纯新API(例如compute)，它们是无用的
- 删除_default，替换为default=对应字段上的参数
- 如果字段的string=是字段名的标题化版本:

```
name = fields.Char(string="Name")
```

​		它是无用的，应该被删除

- multi=参数对新的API字段不做任何操作，对所有相关字段使用相同的compute=方法得到相同的结果

- 按名称提供compute=、reverse =和search=方法(作为字符串)，这使它们可覆盖(消除了对中间“trampoline”函数的需要)


- 仔细检查所有字段和方法是否有不同的名称，在发生冲突时没有警告(因为Python在Odoo看到任何东西之前就处理了它)


- 通常的新api导入from odoo import fields, models。如果兼容性装饰器是必要的，使用from odoo import api, fields, models


- 避免使用one()装饰器，它可能不会做您期望的事情


- 删除create_uid、create_date、write_uid和write_date字段的显式定义:它们现在被创建为常规的“合法”字段，可以像任何其他开箱即用的字段一样读写


- 当不可能进行直接转换(语义无法桥接)或不希望使用“旧API”版本，并且可以对新API进行改进时，可以使用v7()和v8()对相同的方法名使用完全不同的“旧API”和“新API”实现。方法应该首先使用旧的api样式定义并使用v7()进行装饰，然后使用完全相同的名称重新定义，但是使用新api样式并使用v8()进行装饰。来自旧api上下文的调用将被发送到第一个实现，而来自新api上下文的调用将被发送到第二个实现。一个实现可以通过切换上下文调用(并且经常调用)另一个实现。

危险

使用这些装饰器使方法非常难以覆盖，并且更难理解和记录

- _columns或_all_columns的使用应该替换为_fields，它提供了对新型odo .fields实例的访问。字段实例(而不是旧式的odo .os .fields._column)。

  使用新API样式创建的非存储计算字段在_columns中不可用，只能通过_fields进行检查

- 在方法中重新分配self可能是不必要的，并且可能会破坏翻译内省
- 环境对象依赖于一些threadlocal状态，在使用它们之前必须设置这些状态。当尝试在尚未设置新API的上下文中(如新线程或Python交互环境)使用新API时，有必要使用odo . API . environment .manage()上下文管理器:

```python
>>> from odoo import api, modules
>>> r = modules.registry.RegistryManager.get('test')
>>> cr = r.cursor()
>>> env = api.Environment(cr, 1, {})
Traceback (most recent call last):
  ...
AttributeError: environments
>>> with api.Environment.manage():
...     env = api.Environment(cr, 1, {})
...     print env['res.partner'].browse(1)
...
res.partner(1,)
```



## 旧API方法的自动桥接

当模型初始化时，如果所有方法看起来像在旧API样式中声明的模型，那么它们将被自动扫描并桥接。这种桥接使它们可以从new- api样式的方法透明地调用。

如果方法的第二个位置参数(在self之后)被调用为cr或cursor，那么方法将被匹配为“old-API style”。系统还可以识别第三个位置参数uid或user和第四个位置参数id或id。它还可以识别任何名为context的参数的存在。

当从新的API上下文调用这些方法时，系统将自动填充当前环境(用于cr、用户和上下文)或当前记录集(用于id和id)中的匹配参数。

在极少数情况下，如有需要，可采用旧式装饰方法定制桥接:

- 完全禁用它，通过使用noguess()装饰方法，将不存在桥接，并且方法的调用方式将与新旧API样式完全相同
- 显式定义桥，这主要是针对方法匹配不正确(因为参数的命名方式出人意料):

**cr()**

是否会自动将当前游标定位到显式提供的参数前

**cr_uid()**

是否会自动将当前游标和用户id预先设置为明确提供的参数

**cr_uid_ids()**

是否会自动将当前游标、用户id和记录集的id预先设置为显式提供的参数

**cr_uid_id()**

将循环遍历当前记录集，并为每个记录调用该方法一次，将当前游标、用户id和记录id置于显式提供的参数之前。

危险

当从新api上下文调用时，这个包装器的结果总是一个列表

所有这些方法都有一个_context后缀版本(例如cr_uid_context())，它也通过关键字传递当前上下文。

- 使用v7()和v8()的双重实现将被忽略，因为它们提供了自己的“桥接”