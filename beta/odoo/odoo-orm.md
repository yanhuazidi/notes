

[TOC]

# ORM

## Recordsets

**与模型和记录的交互是通过记录集执行的，记录集是同一模型的有序记录集。 **

```python
class AModel(models.Model):
    _name = 'a.model'
    def a_method(self):
        # self can be anywhere between 0 records and all records in the
        # database
        self.do_operation()
        #模型上定义的方法在记录集上执行，它们self是记录集
        print(self)# => a.model(1, 2, 3, 4, 5)
        #迭代记录集将产生新的单个记录集 （“单例”）
        for record in self:
        print record # => a.model(1), then a.model(2), then a.model(3), ...
```



**记录集提供“活动记录”界面：**

模型字段可以作为属性直接从记录中读取和写入，但仅限于单个记录（单记录记录集）。字段值也可以像dict项一样访问，这比`getattr()`动态字段名称更优雅，更安全。设置字段的值会触发对数据库的更新： 

```python
>>> record.name
Example Name
>>> record.company_id.name
Company Name
>>> record.name = "Bob"
>>> field = "name"
>>> record[field]
Bob
#尝试在多个记录上读取或写入字段会引发错误。
```



**设置字段**

对字段的每个设置都会触发数据库更新，当同时设置多个字段或在多个记录上设置字段（到相同的值）时，使用[`write()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.write)： 

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



**记录缓存和预取**

Odoo维护记录字段的缓存，因此并非每个字段访问都会发出数据库请求，这对性能来说太糟糕了。以下示例仅针对第一个语句查询数据库

```python
record.name             # first access reads value from database
record.name             # second access gets value from cache
```

为了避免一次在一条记录上读取一个字段，Odoo会根据一些启发式方法*预取*记录和字段以获得良好的性能。一旦必须在给定记录上读取字段，ORM实际上会在较大的记录集上读取该字段，并将返回的值存储在缓存中供以后使用。预取记录集通常是记录集，记录来自迭代。此外，所有简单的存储字段（boolean, integer, float, char, text, date, datetime, selection, many2one ）都被完全取出; 它们对应于模型表的列，并在同一查询中有效获取 



## 集合操作

记录集是不可变的，但可以使用各种set操作组合相同模型的集合，返回新的记录集。设置操作不会保留顺序。

- `record in set`返回是否存在`record`（必须是1元素记录集）`set`。`record not in set`是逆操作
- `set1 <= set2`并`set1 < set2`返回是否`set1`是`set2`（resp. stric 严格模式）的子集
- `set1 >= set2`并`set1 > set2`返回是否`set1`是`set2`（resp. stric）的超集
- `set1 | set2` 返回两个记录集的并集，一个包含任一源中存在的所有记录的新记录集
- `set1 & set2` 返回两个记录集的交集，一个新记录集仅包含两个源中存在的记录
- set1  -  set2返回一个新记录集，其中只包含set1中不在set2中的记录

### 其他记录集操作

记录集是可迭代的，因此普通的Python工具可用于转化他们（[`map()`](https://docs.python.org/3/library/functions.html#map)，[`sorted()`](https://docs.python.org/3/library/functions.html#sorted)，`itertools.ifilter`，...），但是这些操作返回的是一个 [`list`](https://docs.python.org/3/library/stdtypes.html#list)或一个迭代器，删除了调用他们的结果的方法和记录集操作的能力。 

因此，记录集提供这些操作返回记录集本身（如果可能）： 

[`filtered()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.filtered)

返回仅包含满足提供的谓词函数的记录的记录集。谓词也可以是一个字符串，按字段为true或false进行过滤： 

```Python
#仅保留其公司是当前用户
records.filtered(lambda r: r.company_id == user.company_id)

#仅保留其合作伙伴是公司
records.filtered("partner_id.is_company")
```

[`sorted()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.sorted)

返回按提供的键函数排序的记录集。如果未提供密钥，请使用模型的默认排序顺序： 

```Python
# 按名称记录排序记录集
records.sorted(key=lambda r: r.name)
```

[`mapped()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.mapped)

将提供的函数应用于记录集中的每个记录，如果结果是记录集，则返回记录集： 

```Python
# 返回记录集中每条记录的两个字段的汇总列表
records.mapped(lambda r: r.field1 + r.field2)
```

提供的函数可以是一个字符串来获取字段值： 

```Python
# 返回名称记录列表
records.mapped('name')

#返回合作伙伴记录的记录集
record.mapped('partner_id')

#返回所有合作伙伴银行删除重复记录的并集
record.mapped('partner_id.bank_ids')
```



## 环境Environment 

Environment 由ORM用于存储各种上下文数据：数据库游标cursor （数据库查询），当前用户current user （访问权限检查）和当前的上下文（存储任意元数据）,环境还存储缓存.

所有记录集都有一个不可变的环境，可以使用`env`它来访问，并提供对当前user（`user`），cursor（`cr`）或context（`context`）的访问： 

```python
>>> records.env
<Environment object ...>
>>> records.env.user
res.user(3)
>>> records.env.cr
<Cursor object ...)
```

从其他记录集创建记录集时，将继承环境。环境可用于在其他模型中获取空记录集，并查询该模型： 

```python
>>> self.env['res.partner']
res.partner
>>> self.env['res.partner'].search([['is_company', '=', True], ['customer', '=', True]])
res.partner(7, 18, 12, 14, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74)
```



### 改变环境

可以从记录集中自定义环境。这将使用更改的环境返回记录集的新版本。

sudo()

使用提供的用户集创建新环境，如果未提供任何用户，则使用管理员（绕过安全上下文中的访问权限/规则），使用新环境返回调用它的记录集的副本：

```python
# create partner object as administrator以管理员身份创建合作伙伴
env['res.partner'].sudo().create({'name': "A Partner"})

# list partners visible by the "public" user 列出“公共”用户可见的合作伙伴
public = env.ref('base.public_user')
env['res.partner'].sudo(public).search([])
```

with_context()

1. 可以采用单个位置参数，它替换当前环境的上下文
2. 可以通过关键字获取任意数量的参数，这些参数被添加到当前环境的上下文或步骤1中设置的上下文中

```python
# look for partner, or create one with specified timezone if none is found 查找指定时区的合作伙伴,如果找不到合作伙伴就创建指定时区的合作伙伴
env['res.partner'].with_context(tz=a_tz).find_or_create(email_address)
```

with_env()

完全取代现有环境



## 常见的ORM方法

search()

采用搜索域，返回匹配记录的记录集。可以返回匹配记录（`offset` 和`limit`参数）的子集并进行排序（`order`参数）：

```python
>>> # searches the current model
>>> self.search([('is_company', '=', True), ('customer', '=', True)])
res.partner(7, 18, 12, 14, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74)
>>> self.search([('is_company', '=', True)], limit=1).name
'Agrolait'
```

只是检查是否有任何记录与域匹配，或者计算使用的记录数 search_count()

create()

获取字段值的字典或此类字典的列表，并返回包含所创建记录的记录集： 

```python
>>> self.create({'name': "Joe"})
res.partner(78)
>>> self.create([{'name': "Jack"}, {'name': "William"}, {'name': "Averell"}])
res.partner(79, 80, 81)
```

了解[如何使用一个API或另一个API定义方法`create`](https://www.odoo.com/documentation/12.0/reference/orm.html#reference-orm-oldapi)。 

write()

获取许多字段值，将它们写入其记录集中的所有记录。不返回值：

```python
self.write({'name': "Newer Name"})
```

browse()

获取数据库ID或id列表并返回记录集，当从外部Odoo获取记录ID（例如，通过外部系统往返）或[在旧API中调用方法时](https://www.odoo.com/documentation/12.0/reference/orm.html#reference-orm-oldapi)非常有用：

```python
>>> self.browse([7, 18, 12])
res.partner(7, 18, 12)
```

exists()

返回仅包含数据库中存在的记录的新记录集。可用于检查记录（例如，从外部获得）是否仍然存在：

```python
if not record.exists():
    raise Exception("The record has been deleted")
```

或者在调用可能删除了一些记录的方法之后： 

```python
records.may_remove_some()
# only keep records which were not deleted仅保留未删除
records = records.exists()
```

ref()

环境方法,返回与提供的[外部id](https://www.odoo.com/documentation/12.0/glossary.html#term-external-id)匹配的记录 ： 

```python
>>> env.ref('base.group_public')
res.groups(2)
```

ensure_one()

检查记录集是否为单例（仅包含单个记录），否则会引发错误： 

```python
records.ensure_one()
# is equivalent to but clearer than:相当于但更清晰：
assert len(records) == 1, "Expected singleton"
```



## 创建模型

模型字段定义为模型本身的属性：

```python
from odoo import models,fields
class AModel(models.Model):
    _name = 'a.model.name'
    field1 = fields.Char()
#警告 这意味着您无法定义具有相同名称的字段和方法，它们会发生冲突
```

默认情况下，字段的标签（用户可见名称）是字段名称的大写版本，可以使用以下`string`参数覆盖：

```python
field2 = fields.Integer(string="an other field")
```

默认值定义为字段上的参数，值为： 

```python
a_field = fields.Char(default="a value")
```

或者一个被调用来计算默认值的函数，它应返回该值： 

```python
def compute_default_value(self):
    return self.get_value()
a_field = fields.Char(default=compute_default_value)
```



### 计算字段

可以使用`compute`参数计算字段（而不是直接从数据库中读取） 。**它必须将计算值分配给字段**。如果它使用其他*字段*的值，则应使用depends()

以下命令指定这些字段 ：

```python
from odoo import api

total = fields.Float(compute='_compute_total')

@api.depends('value', 'tax')
def _compute_total(self):
    for record in self:
        record.total = record.value + record.value * record.tax
```

- 使用子字段时，依赖关系可以是虚线路径： 

```python
@api.depends('line_ids.value')
def _compute_total(self):
    for record in self:
        record.total = sum(line.value for line in record.line_ids)
```

- 默认情况下不会存储计算字段，它们会在请求时计算并返回。设置`store=True`会将它们存储在数据库中并自动启用搜索
- 也可以通过设置`search` 参数来启用在计算字段上搜索。该值是返回域的方法名称 ：

```python
upper_name = field.Char(compute='_compute_upper', search='_search_upper')

def _search_upper(self, operator, value):
    if operator == 'like':
        operator = 'ilike'
    return [('name', operator, value)]
```

- 要允许在计算字段上*设置*值，请使用该`inverse` 参数。它是反转计算和设置相关字段的函数的名称： 

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

- 可以通过相同的方法同时计算多个字段，只需在所有字段上使用相同的方法并设置所有字段： 

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



### 关联字段

计算字段的特殊情况是*相关*（代理）字段，其提供当前记录上的子字段的值。它们是通过设置`related`参数来定义的，就像它们可以存储的常规计算字段一样：

```python
nickname = fields.Char(related='user_id.partner_id.name', store=True)
```

### onchange：动态更新UI

当用户更改表单中的字段值（但尚未保存表单）时，根据该值自动更新其他字段可能很有用，例如，当税收更改或新发票行更新时更新最终总计添加。

- 计算字段会自动检查并重新计算，它们不需要 `onchange`
- 对于非计算字段，[`onchange()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.api.onchange)装饰器用于提供新的字段值：

```python
@api.onchange('field1', 'field2') # if these fields are changed, call method
def check_change(self):
    if self.field1 < self.field2:
        self.field3 = True
```

- 然后，在方法期间执行的更改将发送到客户端程序并对用户可见
- 客户端自动调用计算字段和new-API onchanges，而无需在视图中添加它们
- 可以通过`on_change="0"`在视图中添加来禁止来自特定字段的触发器 ：

```xml
<field name="name" on_change="0"/>
```

当用户编辑字段时，即使有功能字段或显式onchange取决于该字段，也不会触发任何接口更新。 

`onchange` 方法对虚拟记录的工作分配这些记录不会写入数据库，只是用于知道要将哪个值发送回客户端

警告 `one2many`或`many2many`field 不可能通过onchange修改自身。这是webclient限制 - 请参阅[＃2693](https://github.com/odoo/odoo/issues/2693)

### 低级SQL

在`cr`上的环境属性是光标用于当前数据库事务，并允许直接执行的SQL，无论是对查询其难以用ORM来表达（例如复杂的连接），或者出于性能的原因：

```python
self.env.cr.execute("some_sql", param1, param2, param3)
```

由于模型使用相同的游标并`Environment` 保存各种缓存，因此在原始SQL中*更改*数据库时，这些缓存必须无效，否则模型的进一步使用可能会变得不连贯。在使用时`CREATE`，`UPDATE`或`DELETE`在SQL中，有必要清除缓存，而不是`SELECT`（只是读取数据库）。

可以使用对象的`invalidate_cache()`方法 来执行清除高速缓存 `BaseModel`。



### CRUD

###### `create(vals_list) → records`

为模型创建新记录。

新记录使用dicts列表中的值进行初始化 `vals_list`，如果需要，可以使用[`default_get()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.default_get)。

参数

​	vals_list（`list`） -

模型字段的值，作为字典列表：

```
[{ 'field_name' ： field_value ， ... }， ... ]
```

为了向后兼容，`vals_list`可能是字典。它被视为单例列表`[vals]`，并返回单个记录。

看[`write()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.write)详情

返回

创建的记录

加薪

- **AccessError**

   -

  - 如果用户对请求的对象没有创建权限
  - 如果用户尝试绕过请求对象上的create的访问规则

- **ValidateError** - 如果用户尝试为不在选择中的字段输入无效值

- [**UserError**](https://www.odoo.com/documentation/12.0/webservices/iap.html#odoo.exceptions.UserError) - 如果在对象层次结构中创建循环操作的结果（例如将对象设置为其自己的父对象）

###### `browse([*ids*]) → records`

返回当前环境中作为参数提供的ID的记录集。

不能使用任何ID，单个ID或一系列ID。

###### `unlink()`

删除当前集的记录

加薪

- **AccessError**

   -

  - 如果用户对请求的对象没有取消链接权限
  - 如果用户试图绕过请求对象上取消链接的访问规则

- [**UserError**](https://www.odoo.com/documentation/12.0/webservices/iap.html#odoo.exceptions.UserError) - 如果记录是其他记录的默认属性

###### `write(*vals*)`

使用提供的值更新当前集中的所有记录。

参数

vals

（

`dict`

） -

要更新的字段和要在其上设置的值，例如：

```
{ 'foo' ： 1 ， 'bar' ： “Qux” }
```

将字段设置`foo`为`1`和字段`bar`为 `"Qux"`if如果它们是有效的（否则它将触发错误）。

加薪

- **AccessError**

   -

  - 如果用户对请求的对象没有写权限
  - 如果用户试图绕过访问规则以写入所请求的对象

- **ValidateError** - 如果用户尝试为不在选择中的字段输入无效值

- [**UserError**](https://www.odoo.com/documentation/12.0/webservices/iap.html#odoo.exceptions.UserError) - 如果在对象层次结构中创建循环操作的结果（例如将对象设置为其自己的父对象）

- 对于数字字段（[`Integer`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Integer)， [`Float`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Float)），值应为相应的类型
- 因为[`Boolean`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Boolean)，值应为a [`bool`](https://docs.python.org/3/library/functions.html#bool)
- 对于[`Selection`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Selection)，值应与选择值匹配（通常[`str`](https://docs.python.org/3/library/stdtypes.html#str)，有时 [`int`](https://docs.python.org/3/library/functions.html#int)）
- 对于[`Many2one`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Many2one)，该值应该是要设置的记录的数据库标识符
- 其他非关系字段使用字符串作为值

- 历史和兼容性的原因， [`Date`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Date)和 [`Datetime`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Datetime)字段使用字符串作为值（写入和读出），而不是[`date`](https://docs.python.org/3/library/datetime.html#datetime.date)或 [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime)。这些日期字符串是UTC，仅其格式`odoo.tools.misc.DEFAULT_SERVER_DATE_FORMAT`和`odoo.tools.misc.DEFAULT_SERVER_DATETIME_FORMAT`

- [`One2many`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.One2many)并 [`Many2many`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Many2many)使用特殊的“命令”格式来操作存储在字段中/与字段相关联的记录集。

  此格式是按顺序执行的三元组列表，其中每个三元组是在记录集上执行的命令。并非所有命令都适用于所有情况。可能的命令是：

  - `(0, _, values)`

    添加从提供的`value`词典创建的新记录。

  - `(1, id, values)`

    `id`使用中的值 更新现有id的记录`values`。不能用于[`create()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.create)。

  - `(2, id, _)`

    `id`从集合中删除id的记录，然后删除它（从数据库中）。不能用于[`create()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.create)。

  - `(3, id, _)`

    `id`从集合中删除id的记录，但不删除它。不能用 [`One2many`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.One2many)。不能用于 [`create()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.create)。

  - `(4, id, _)`

    将id的现有记录添加`id`到集合中。不能用[`One2many`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.One2many)。

  - `(5, _, _)`

    从集合中删除所有记录，相当于`3`明确地在每条记录上使用该命令。不能用[`One2many`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.One2many)。不能用于 [`create()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.create)。

  - `(6, _, ids)`

    替换由集合中的所有现有的记录`ids`列表，等同于使用该命令`5`，然后命令 `4`每个`id`中`ids`。

  标记为`_`上面列表中的值将被忽略，并且可以是任何内容，通常`0`或`False`。

###### `read([*fields*])`

在`self`低级/ RPC方法中读取记录的请求字段。在Python代码中，首选[`browse()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.browse)。

参数

**fields** - 要返回的字段名称列表（默认为所有字段）

返回

将字段名称映射到其值的字典列表，每个记录使用一个字典

加薪

[**AccessError**](https://www.odoo.com/documentation/12.0/webservices/iap.html#odoo.exceptions.AccessError) - 如果用户对某些给定记录没有读取权限

###### `read_group(*domain*, *fields*, *groupby*, *offset=0*, *limit=None*, *orderby=False*, *lazy=True*)`

获取按给定`groupby`字段分组的列表视图中的记录列表

参数

- **domain** - 列出指定搜索条件的列表[['field_name'，'operator'，'value']，...]
- **fields**（[`list`](https://docs.python.org/3/library/stdtypes.html#list)） - 在对象上指定的列表视图中存在的字段列表。每个元素都是'field'（字段名称，使用默认聚合）或'field：agg'（聚合字段聚合函数'agg'）或'name：agg（field）'（聚合字段带'agg'）并将其作为“名称”返回）。可能的聚合函数是PostgreSQL（https://www.postgresql.org/docs/current/static/functions-aggregate.html）和'count_distinct'提供的函数，具有预期的含义。
- **groupby**（[`list`](https://docs.python.org/3/library/stdtypes.html#list)） - 将记录分组的groupby描述列表。groupby描述是字段（然后它将按该字段分组）或字符串'field：groupby_function'。目前，支持的唯一功能是“日”，“周”，“月”，“季度”或“年”，它们只适用于日期/日期时间字段。
- **offset**（[`int`](https://docs.python.org/3/library/functions.html#int)） - 要跳过的可选记录数
- **limit**（[`int`](https://docs.python.org/3/library/functions.html#int)） - 可选的最大返回记录数
- **orderby**（[`list`](https://docs.python.org/3/library/stdtypes.html#list)） - 可选`order by`规范，用于覆盖组的自然排序顺序，另请参阅`search()` （仅支持当前的多个字段）
- **lazy**（[`bool`](https://docs.python.org/3/library/functions.html#bool)） - 如果为true，则结果仅按第一个groupby分组，其余的groupbys放在__context键中。如果为false，则所有groupbys都在一次调用中完成。

返回

字典列表（每个记录一个字典）包含：

- 按`groupby`参数中的字段分组的字段值
- __domain：指定搜索条件的元组列表
- __context：带参数的字典 `groupby`

返回类型

[{'field_name_1'：值，..]

加薪

**AccessError**

 -

- 如果用户对请求的对象没有读取权限
- 如果用户试图绕过访问规则以读取请求的对象

### 搜索

###### `search(*args[, offset=0][, limit=None][, order=None][, count=False]*)`

根据`args` [搜索域](https://www.odoo.com/documentation/12.0/reference/orm.html#reference-orm-domains)搜索记录。

参数

- **args** - [搜索域](https://www.odoo.com/documentation/12.0/reference/orm.html#reference-orm-domains)。使用空列表匹配所有记录。
- **offset**（[`int`](https://docs.python.org/3/library/functions.html#int)） - 要忽略的结果数（默认值：无）
- **limit**（[`int`](https://docs.python.org/3/library/functions.html#int)） - 要返回的最大记录数（默认值：全部）
- **order**（[`str`](https://docs.python.org/3/library/stdtypes.html#str)） - 排序字符串
- **count**（[`bool`](https://docs.python.org/3/library/functions.html#bool)） - 如果为True，则只计算并返回匹配记录的数量（默认值：False）

返回

最多`limit`匹配搜索条件的记录

加薪

**AccessError**

 -

- 如果用户试图绕过访问规则以读取请求的对象。

###### `search_count(*args*) → int`

返回与[提供的域](https://www.odoo.com/documentation/12.0/reference/orm.html#reference-orm-domains)匹配[的](https://www.odoo.com/documentation/12.0/reference/orm.html#reference-orm-domains)当前模型中的记录数。

###### `name_search(*name=''*, *args=None*, *operator='ilike'*, *limit=100*) → records`

搜索与给定`name`模式相比具有与给定模式匹配的显示名称的记录 `operator`，同时还匹配可选搜索域（`args`）。

这用于例如基于关系字段的部分值来提供建议。有时被视为反函数[`name_get()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.name_get)，但不能保证。

此方法相当于[`search()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.search)使用基于搜索结果的搜索域进行调用，`display_name`然后[`name_get()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.name_get)搜索结果。

参数

- **name**（[`str`](https://docs.python.org/3/library/stdtypes.html#str)） - 要匹配的名称模式
- **args**（[`list`](https://docs.python.org/3/library/stdtypes.html#list)） - 可选的搜索域（参见[`search()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.search)语法），指定进一步的限制
- **operator**（[`str`](https://docs.python.org/3/library/stdtypes.html#str)） - 用于匹配的域运算符`name`，例如 `'like'`或`'='`。
- **limit**（[`int`](https://docs.python.org/3/library/functions.html#int)） - 可选的最大返回记录数

返回类型

[名单](https://docs.python.org/3/library/stdtypes.html#list)

返回

`(id, text_repr)`所有匹配记录的对列表。

### 记录集操作

###### `ids`

此记录集中的实际记录ID列表（忽略要创建的记录的占位符ID）

###### `ensure_one()`

验证当前的recorset是否包含单个记录。否则会引发异常。

###### `exists() → records`

返回`self`存在的记录子集，并在缓存中标记已删除的记录。它可以用作记录的测试：

```
如果 记录。exists （）：
    ...
```

按照惯例，新记录将作为现有记录返回。

###### `filtered(*func*)`

在选择的记录`self`，从而`func(rec)`为真，并返回它们作为一个记录。

参数

**func** - 字段名称的函数或点分隔序列

###### `sorted(*key=None*, *reverse=False*)`

返回`self`订购的记录集`key`。

参数

- **key** - 返回每个记录的比较键的一个参数的函数，或字段名称，或者`None`，在这种情况下，记录按照默认模型的顺序排序
- **反向** - 如果`True`，以相反的顺序返回结果

###### `mapped(*func*)`

应用于`func`所有记录`self`，并将结果作为列表或记录集（如果`func`返回记录集）返回。在后一种情况下，返回的记录集的顺序是任意的。

参数

**func** - 一个函数或以点分隔的字段名称序列（字符串）; 任何falsy值只返回记录集`self`

### 环境交换

###### `sudo([*user=SUPERUSER*])`

返回附加到提供的用户的此记录集的新版本。

默认情况下，它返回一个`SUPERUSER`记录集，其中绕过访问控制和记录规则。

使用`sudo`可能导致数据访问跨越记录规则的边界，可能混合要隔离的记录（例如，来自多公司环境中的不同公司的记录）。

这可能会导致在多种方法中选择一条记录的方法产生不直观的结果 - 例如获取默认公司或选择物料清单。

由于必须重新评估记录规则和访问控制，因此新记录集不会从当前环境的数据高速缓存中受益，因此以后的数据访问可能会在从数据库重新获取时产生额外的延迟。返回的记录集具有与之相同的预取对象`self`。

###### `with_context(*[context][, \**overrides]*) → records`

返回附加到扩展上下文的此记录集的新版本。

扩展上下文要么是合并提供的`context`， 要么`overrides`合并*当前*上下文， `overrides`例如：

```
#current context is {'key1'：True} 
r2  =  records 。with_context （{}， key2 = True ）
＃ - > r2._context是{'key2'：True} 
r2  =  记录。with_context （key2 = True ）
＃ - > r2._context是{'key1'：True，'key2'：True}
```

###### `with_env(*env*)`

返回附加到提供的环境的此记录集的新版本

### 警告

新环境不会受益于当前环境的数据缓存，因此以后的数据访问可能会在从数据库重新获取时产生额外的延迟。返回的记录集具有与之相同的预取对象`self`。

### 字段和视图查询

###### `fields_get(*[fields][, attributes]*)`

返回每个字段的定义。

返回的值是字典的字典（由字段名称指示）。_inherits'd字段包括在内。字符串，帮助和选择（如果存在）属性已翻译。

参数

- **allfields** - 要记录的字段列表，全部为空或未提供
- **attributes** - 要为每个字段返回的描述属性列表，如果为空或未提供则全部

###### `fields_view_get([*view_id | view_type='form'*])`

获取所请求视图的详细组成，如字段，模型，视图体系结构

参数

- **view_id** - 视图的id或None
- **view_type** - 如果view_id为None（'form'，'tree'，...）则返回的视图的类型
- **toolbar** - 如果包含上下文操作，则为true
- **子菜单** - 已弃用

返回

描述所请求视图组成的字典（包括继承的视图和扩展）

加薪

- **AttributeError**

   -

  - 如果继承的视图具有未知的位置，可以使用“之前”，“之后”，“内部”，“替换”以外的其他视图
  - 如果在父视图中找到“position”以外的某些标记

- **无效的ArchitectureError** - 如果在结构上定义了除窗体，树，日历，搜索等之外的视图类型

### 杂项方法

###### `default_get(*fields*) → default_values`

返回字段中的默认值`fields_list`。默认值由上下文，用户默认值和模型本身确定。

参数

**fields_list** - 字段名称列表

返回

将每个字段名称映射到其对应的默认值的字典（如果有的话）。

###### `copy(*default=None*)`

重复记录`self`使用默认值更新它

参数

**default**（[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)） - 要在复制记录的原始值中覆盖的字段值字典，例如：`{'field_name': overridden_value, ...}`

返回

新纪录

###### `name_get() → [(id, name), ...]`

返回记录中的文本表示`self`。默认情况下，这是`display_name`字段的值。

返回

`(id, text_repr)`每条记录的对列表

返回类型

[列表](https://docs.python.org/3/library/stdtypes.html#list)（[元组](https://docs.python.org/3/library/stdtypes.html#tuple)）

###### `name_create(*name*) → record`

通过[`create()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.create)仅提供一个值来调用创建新记录：新记录的显示名称。

新记录将使用适用于此模型的任何默认值进行初始化，或通过上下文提供。通常的行为[`create()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.create)适用。

参数

**name** - 要创建的记录的显示名称

返回类型

[元组](https://docs.python.org/3/library/stdtypes.html#tuple)

返回

[`name_get()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.name_get)创建记录的对值



### 自动字段

###### `id`  	

​	识别field

###### `_log_access`

​	无论日志的访问域（`create_date`，`write_uid`，...）应生成（默认值：`True`）

###### `create_date`

​	创建记录的日期

​	类型

​		`Datetime`

###### `create_uid`

​	创建记录的用户的关系字段

​	类型

​		`res.users`

###### `write_date`

​	上次修改记录的日期

​	类型

​		`Datetime`

###### `write_uid`

​	修改记录的最后一个用户的关系字段

​	类型

​		`res.users`



## 字段

### 基本领域

###### `class odoo.fields.Field(string=<object object>, **kwargs)`

字段描述符包含字段定义，并管理记录上相应字段的访问和分配。在实例化字段时可能会提供以下属性：

参数

- **string** - 用户看到的字段的标签（字符串）; 如果未设置，ORM将获取类中的字段名称（大写）。
- **help** - 用户看到的字段的工具提示（字符串）
- **readonly** - 字段是否为readonly（默认为boolean `False`）
- **required** - 是否**需要**字段的值（默认为boolean `False`）
- **index** - 字段是否在数据库中建立索引（默认为布尔值`False`）
- **default** - 字段的默认值; 这可以是静态值，也可以是记录集并返回值的函数; 用于 `default=None`丢弃该字段的默认值
- **states** - 将状态值映射到UI属性 - 值对列表的字典; 可能的属性是：'readonly'，'required'，'invisible'。注意：任何基于状态的条件都要求`state`在客户端UI上提供字段值。这通常通过将其包括在相关视图中来完成，如果与最终用户不相关，则可能使其不可见。
- **groups** - 以逗号分隔的组xml id列表（字符串）; 这限制了仅对给定组的用户的字段访问
- **copy**（[`bool`](https://docs.python.org/3/library/functions.html#bool)） - 是否应在复制记录时复制字段值（默认值：`True`对于普通字段，`False`对于 `one2many`和计算字段，包括属性字段和相关字段）
- **oldname**（`string`） - 此字段的先前名称，以便ORM可以在迁移时自动重命名

#### 计算字段

可以定义一个字段，其值是计算的，而不是简单地从数据库中读取。下面给出了特定于计算字段的属性。要定义此类字段，只需为该属性提供值即可`compute`。

参数

- **compute** - 计算字段的方法的名称
- **inverse** - 反转字段的方法的名称（可选）
- **search** - 在字段上实现搜索的方法的名称（可选）
- **store** - 字段是否存储在数据库中（默认情况下，`False`在计算字段上为boolean ）
- **compute_sudo** - 是否应将该字段重新计算为超级用户以绕过访问权限（默认为布尔值`False`）请注意，这对非存储的计算字段没有影响

对于给定的方法`compute`，`inverse`并`search`在模型的方法。它们的签名如下例所示：

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

compute方法必须在调用的记录集的所有记录上分配字段。[`odoo.api.depends()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.api.depends)必须在compute方法上应用装饰器来指定字段依赖性; 这些依赖关系用于确定何时重新计算字段; 重新计算是自动的，并保证缓存/数据库的一致性。请注意，相同的方法可用于多个字段，您只需分配方法中的所有给定字段; 对于所有这些字段，将调用该方法一次。

默认情况下，计算字段不会存储到数据库中，而是即时计算。添加属性`store=True`会将字段的值存储在数据库中。存储字段的优点是在该字段上搜索由数据库本身完成。缺点是在必须重新计算字段时需要数据库更新。

inverse正如其名称所示，反向方法执行计算方法的反转：调用的记录具有字段的值，您必须对字段依赖项应用必要的更改，以便计算给出预期值。请注意，默认情况下，只读取没有逆方法的计算字段。

在对模型进行实际搜索之前处理域时会调用搜索方法。它必须返回一个等同于条件的域：`field operator value`。











