[TOC]



## action简介

### actions定义了系统对于用户的操作的响应 ( 登录、按钮、选择项目等 )

`action`可以存储在数据库中，也可以作为字典直接返回，例如按钮方法。

每个action有两个必选属性：

- `type`		当前操作的类别，决定可以使用哪些字段以及如何解释该操作。

  常用的有 `ir.actions.act_window`,,,

- `name`		简短的用户可读的操作描述，可以显示在客户端界面



### 客户端可以通过4种形式来获取action

- **False** - 会自动关闭所有的对话框
- **String** - 如果有相匹配的客户端动作，会被解释为相应动作的标签，否则会当成Number处理
- **Number** - 从数据库读取相应的action记录，一般是数据库标识id
- **Dict** - 当成客户端动作来执行



## 窗口Action(`ir.actions.act_window `)

最常用的action类型，用于将model的数据展示出来

窗口操作为模型(以及模型的特定记录)定义一组视图类型(以及可能的特定视图)。

字段列表：

> 1. `res_model` -- 需要在view里显示数据的model
> 2. `views` -- 一个(view_id, view_type) 列表，view_type代表视图类型如：form,tree,gragh...，view_id是可选的数据库id或False，如果没有指定id，客户端会自动用fields_view_get()获取相应类型的默认视图，type参数列表的第一个会被默认用来展示,在执行操作时默认打开
> 3. `res_id` (可选) -- 当默认的视图类型是form时，可用于指定加载的数据(否则应该创建一个新记录)列表
> 4. `search_view_id` (可选) -- (id, name)，id是储存在数据库的搜索视图，默认会读取model的默认搜索视图
> 5. `target` (可选) -- 定义视图是 在当前视图上打开(`current`)、使用全屏模式(`fullscreen`)、使用弹出框(`new`)、可使用`main`代替`current`来清除面包屑导航
> 6. `context` (可选) -- 额外的需要传给视图的环境数据
> 7. `domain` (可选) -- 筛选域以隐式地添加到所有视图搜索查询
> 8. `limit` (可选) -- 默认情况下列表中显示的记录数。web客户机中默认值为80
> 9. `auto_search`(可选) -- 搜索是否在加载默认视图后立即执行，默认True

```python
#用列表和表单视图来打开customer按钮
{
    "type": "ir.actions.act_window",
    "res_model": "res.partner",
    "views": [[False, "tree"], [False, "form"]],
    "domain": [["customer", "=", true]],
}
#在新的对话框中打开一个指定产品的表单
{
    "type": "ir.actions.act_window",
    "res_model": "product.product",
    "views": [[False, "form"]],
    "res_id": a_product_id,
    "target": "new",
}
```

保存在数据库里窗口action有几个不同的字段，客户端应该忽略这些字段，主要用于组合视图列表:

- view_mode -- 以逗号分隔的视图类型列表，所有类型的视图会被展示出来,出现在生成的视图列表中(至少有一个view_id)
- view_ids -- 视图对象的一系列的字段，用于定义视图的默认内容
- view_id -- 将指定的view加入到视图中，以防不被view_ids所包含,添加到views列表中的特定视图，以防其类型是view_mode列表的一部分，而view_id中的某个视图还没有填充它

上述参数一般在使用数据文件定义action的时候使用：

```xml
<record model="ir.actions.act_window" id="test_action">
    <field name="name">A Test Action</field>
    <field name="res_model">some.model</field>
    <field name="view_mode">graph</field>
    <field name="view_id" ref="my_specific_view"/>
</record>
默认使用my_specific_view，即使它不是对应模型的默认视图
```

服务端组合视图的步骤：

- 从view_ids(按顺序排序)获取每个(id，类型)
- 如果定义了view_id而且它的类型没有被包含在其中，将它的(id, type)加到最前面
- 对于所有没有指定的view_mode，加一个(False,type)



## 链接Action(`ir.actions.act_url`)

允许通过odoo的链接打开一个网站页面，可通过两个字段来自定义：

- `url` -- 当激活action时所打开的链接
- `target `--   new：在新窗口打开，self：替换当前页面内容，默认new

```python
{
    "type": "ir.actions.act_url",
    "url": "http://odoo.com",
    "target": "self",
}
```

将用Odoo主页替换当前的内容部分。



## 服务器Action 

###  `ir.actions.server`

允许从任何有效的操作位置触发复杂的服务器代码。需要有两个两个字段与客户相关:

- `id` -- 服务端action在数据库存储的id
- `context` (可选) -- 执行服务端action的上下文环境
   储存在数据库中的action可以基于state执行一些特别的动作，部分字段在state之间是相互共享的
- `model_id` -- 与action相关联的model，在 evaluation contexts中可用
- `condition` (可选) -- 使用服务端的  evaluation contexts 来执行python代码，如果是False则阻止action执行，默认值是True

有效动作类型是可以随意扩展的，默认的动作类型**：

### `code`

默认和最灵活的服务器操作类型，使用操作的评估上下文执行任意的python代码。仅使用一个特定类型的字段：

code

当调用action时执行的python代码

```xml
<record model="ir.actions.server" id="print_instance">
    <field name="name">Res Partner Server Action</field>
    <field name="model_id" ref="model_res_partner"/>
    <field name="code">
        raise Warning(object.name)
    </field>
</record>
```

代码段可以定义一个名为action的变量，该变量将作为下一个要执行的操作返回给客户端:

```xml
<record model="ir.actions.server" id="print_instance">
    <field name="name">Res Partner Server Action</field>
    <field name="model_id" ref="model_res_partner"/>
    <field name="code">
        if object.some_condition():
            action = {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model": object._name,
                "res_id": object.id,
            }
    </field>
</record>
```

如果表格符合某些条件，会否要求客户开启表格以作记录

这往往是惟一从数据文件创建的操作类型，除了multi之外，从UI定义其他类型比从Python代码更简单，但不是从数据文件。

###  `object_create`  

从头创建一条新记录(通过create())或复制一条现有记录(通过copy())

- `use_create`

>1. `new`	 基于指定的 model_id指定的模型中创建一条记录
>2. `new_other	`	 基于指定的 crud_model_id指定的模型中创建一条记录
>3. `copy_current`	复制action所引用的记录
>4. `copy_other`		复制通过ref_object获得的其他记录

- `fields_lines`在创建或复制记录时需要修改的字段。One2many会有以下字段:

>1. `col1`	在use_create里所包含的需要被重赋值的`ir.model.fields`
>
>2. `value`   字段对应的值，基于`type`进行解析
>
>3. `type`  取值value, 就是value字段的值.为一个文字值(可能被转换)，
>
>   ​			取值equation：value字段会当成python表达式来解析

- crud_model_id -- 当use_create为new_other时，表示用于创建新记录的model id
- ref_object -- 当use_create为copy_other时用于指定创建记录时引用的记录
- link_new_record -- 是否用`link_field_id`将新记录和当前记录进行many2one关联，默认`False`
- link_field_id -- 指定当前记录与新记录进行many2one关联的字段

### `object_write`

与object_create相似，只是只修改当前记录而不创建新记录

- `use_write`

>- `current` 修改更新到当前记录
>- `other` 修改更新到通过crud_model_id 或 ref_object指定的新记录
>- `expression`  修改更新到通过crud_model_id 以及 write_expression筛选过后的记录

- `write_expression `返回一条记录或对象id的python表达式，当将use_write设置为expression时使用，以便决定应该修改哪条记录`fields_lines`
- `fields_lines`,`crud_model_id`,`ref_object`与`object_create`一致

### `multi`

将通过`child_ids` many2many关系定义的action一个个执行，如果有action自己返回action，最后一个action被返回给客户端作为将前multi action的下一个action

### `client_action`

直接返回使用action_id定义的其他操作的间接方向。只需将该操作返回给客户端执行即可。



### 上下文环境

有些键在上下文环境和服务端action里是可用的：

`model` -- 通过model_id与action关联的model

`object`, `obj` -- 只在有active_model 和active_id才可用，给出经过active_id过滤的记录

`pool` -- 当前数据库注册

`datetime`, `dateutil`,` time `-- python模块

`cr` -- 当前查询游标

`user` -- 当前用户记录

`context` -- 执行上下文环境

`Warning` -- 警告异常的构造器



## 报表Action (ir.actions.report)

- `name`(必选) -- 在一个列表里进行查找时使用,仅可用作报告的助记/描述
- `model` (必选) -- 报表所反映的数据来源model
- `report_type`  (必选) -- qweb-pdf | qweb-html用于PDF报告的qweb-pdf，还是用于HTML的qweb-html
- `report_name` -- 报表命名，用于输出的pdf文件名
- `groups_id` -- 可以读取或使用当前报表的用户组，Many2many字段
- `paperformat_id` -- 报表所使用的纸张格式，默认使用公司的格式，Many2one字段
- `attachment_use` -- 当取值true的时候只在第一次请求时生成报表，之后直接从保存的报表打印，可用于生成后不会有改变的报表
- `attachment` -- 使用python表达式来定义报表名字，该记录可用变量object访问



## 客户端Actions (ir.actions.client)

触发一个完全在客户端实现的action

- `tag` -- action在客户端的标识符，一般是一个专用的字符串
- `params` (可选) -- 用来传给客户端的python数据字典格式数据
- `target`(可选) -- `current`:当前内容区打开action,`fullscreen`:以全屏模式打开，`new`：以弹出框打开

```python
#例：打开一个pos界面，不需要服务端知道它是如何运行的
{
    "type": "ir.actions.client",
    "tag": "pos.ui"
}
```



## 按钮

根据按钮的不同类型，type有不同的值

### type = “object”

需要在py文件中定义一个方法，并且在button的name属性值与方法名相同

- name="some_code"
- states="draft,in_progress,ongoing"模型的states字段的状态，

python文件中

```python
def some_code(self):
    pass
```

```xml
<xml>
    <record>
        <button name="some_code" type="object"/>
    </record>
</xml>点击按钮则会调用py文件的some_code方法
```

**点击按钮则会调用py文件的some_code方法**



### type=”action”

用于页面中视图的跳转

- name=”%(moduleName.id)d”

>- moduleName:模块名
>- id：想要显示的视图的id
>

- attrs="{'invisible': [('state', 'not in', ('in_progress', 'ongoing'))]}

```xml
<record id="action_asset_modify" model="ir.actions.act_window">
     <field name="name">Modify Asset</field>
     <field name="res_model">asset.modify</field>
     <field name="type">ir.actions.act_window</field>
     <field name="view_type">form</field>
     <field name="view_mode">tree,form</field>
     <field name="view_id" ref="asset_modify_form"/>
     <field name="target">new</field>
</record>
<button name="stock.action_asset_modify" type="action"/>
```

**点击按钮，则会跳转到id为“action_asset_modify”的视图页面**



### type=”workflow”

向工作流实例传递信号已达到活动的转换条件

```xml
<button name="confirm" type="workflow"
                       string="Confirm" states="draft"
                       class="oe_highlight"/>

<record model="workflow.activity" id="draft">
    <field name="name">Draft</field>
    <field name="wkf_id" ref="wkf_session"/>
    <field name="flow_start" eval="True"/>
    <field name="kind">function</field>
    <field name="action">action_draft()</field>
</record>
<record model="workflow.activity" id="confirmed">
    <field name="name">Confirmed</field>
    <field name="wkf_id" ref="wkf_session"/>
    <field name="kind">function</field>
    <field name="action">action_confirm()</field>
</record>

<record model="workflow.transition" id="session_draft_to_confirmed">
    <field name="act_from" ref="draft"/>
    <field name="act_to" ref="confirmed"/>
    <field name="signal">confirm</field>
</record>

```

点击确认按钮，将confirm信号发送给当前工作流实例，触发转换条件（活动从“draft”到“confirmed”），然后开始处理活动“confirmed”，执行action_confirm()函数将状态从draft改变为confirm.


