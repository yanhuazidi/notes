[TOC]



## 基本视图

视图定义了模型记录的显示方式。每种类型的视图代表一种可视化模式（记录列表，其聚合图，......）。可以通过类型（例如*合作伙伴列表*）或特别是通过其ID 来一般性地请求视图。对于通用请求，将使用具有正确类型和最低优先级的视图（因此每种类型的最低优先级视图是该类型的默认视图）。

视图继承允许更改在其他地方声明的视图（添加或删除内容）。

### 通用视图声明

视图被声明为模型的记录`ir.ui.view`。视图类型由`arch`字段的根元素隐含：

```xml
<record model="ir.ui.view" id="view_id">
    <field name="name">view.name</field>
    <field name="model">object_name</field>
    <field name="priority" eval="16"/>优先级
    <field name="arch" type="xml">
        <!-- view content: <form>, <tree>, <graph>, ... -->
    </field>
</record>
```

视图的内容是XML。

`arch`必须声明该字段`type="xml"`以便正确解析。



## 常见的结构

视图对象公开许多字段，除非另有指定，否则它们是可选的。

- `name` (必选) 用于通过名字查找

- `model `与view相关联的model

- `priority` 当搜索查找view时，优先级最低的view会被返回

- `arch` 视图layout的描述

- `groups_id` 指定可查看、使用视图的用户组id，many2many关系

- `inherit_id` 当前视图的父级视图

- `mode` 继承模式，当inherit_id没有设置时，它的值是primary（初级）,当设置了inherit_id后，它默认值是extension（扩展），可手动设置为primary

- `application` 定义哪些视图可以被切换，默认情况下所有视图都可以

- `banner_route`要获取并预先写入视图的路由地址。如果设置了此属性，控制器路由url将被获取并显示在视图上方。控制器的json响应应该包含一个“html”键。如果html包含样式表标记，它将被删除并附加到\<head>。要与后端交互，可以使用标记\<a type="action"> 

  Example:

  ```xml
  <tree banner_route="/module_name/hello" />
  ```

  ```python
  class MyController(odoo.http.Controller):
      @http.route('/module_name/hello', auth='user', type='json')
      def hello(self):
          return {
              'html': """
                  <div>
                      <link href="/module_name/static/src/css/banner.css"
                          rel="stylesheet">
                      <h1>hello, world</h1>
                  </div> """
          }
  ```

  

## 继承

### 视图匹配

- 当通过(model, type)来请求视图时，与model、type匹配且`mode=primary` 优先级最低的视图会被返回
- 当通过id请求视图时，如果它的模型不是primary，那么最取他的最近的`mode=primary`的父级视图

### 视图解析

解析符合mode=primary的视图并得到arch内容：

- 如果当前视图有一个父视图，且父视图是完全确定的，直接应用当前视图的继承规范
- 如果当前视图没有父视图，那么arch将直接被使用
- 查找当前视图的extensino模式子视图，使用深度优先算法应用它们的继承规范

应用到子视图之后的结果产生最终的arch

### 继承规范

继承规范由一个定位元素组成，用来匹配父视图中被继承的元素、和 子视图中会被用来修改的继承元素
 一共有三种用来匹配目标元素的定位元素：

- 带有`expr`属性的`xpath`元素 ，`expr`是一个用在`arch`中的`xpath`表达式，找到的第一个节点就是匹配结果
- 带有`name`属性的`field`元素，匹配第一个一样`name`的`field`元素，其他的属性在匹配时被忽略
- 其他的元素：匹配第一个拥有一样的`name`及其他属性的元素（忽略`position`,`version`属性）

继承规范通过可选的position属性来指定如何修改匹配的节点

- `inside`（默认） - 添加到匹配的节点前
- `replace` - 替换匹配的节点
- `after `- 添加到匹配的节点的父节点之后
- `before `- 添加到匹配的节点的父节点之前

**fields** 继承的内容是一系列拥有name属性的field 元素，且有可选的内容主体
1.如果field有内容主体，就在匹配的节点上添加以name命名的、以内容主体为值的属性
2.如果field没有内容主体，就将匹配节点上名字为name的属性删除，如果没有对应的属性，抛出一个错误

此外，`position` `move` 可以作为规范的直接子元素使用，其中包含用于移动节点的`inside`、`replace`、`after`或`before`位置属性。

```xml
<xpath expr="//@target" position="after">
    <xpath expr="//@node" position="move"/>
</xpath>
<field name="target_field" position="after">
    <field name="my_field" position="move"/>
</field>
```

视图的规格按顺序应用。



## 树视图

树视图（也称为列表视图）以表格形式显示记录。

列表视图的根元素是`<tree>`,它可以有以下几种属性：

### editable

默认情况下选择单行记录时会打开对应记录的表单，该属性让数据可以在列表内进行编辑，有效的值是top和bottom，可让新的记录出现在列表的顶部或底部

```xml
<tree string="Budget Items" editable="top">
```

### on_write

只当启用editable时有用，在调用时会传给函数新增或修改后的记录，该函数需要返回一个用于更新列表的记录id列表

### default_order

重定义视图的排序规则，以逗号分隔多个字段，可使用desc来进行倒序

```xml
<tree default_order="sequence,name desc">
```

### decoration-{$name}

允许基于相应记录的属性更改行文本的样式。

值是Python表达式。对于每个记录，表达式都使用记录的属性作为上下文值进行计算，如果为真，则将相应的样式应用于行。其他上下文值是uid(当前用户的id)和current_date(当前日期作为yyyy-MM-dd格式的字符串)。

``{$name}` 可为 `bf` (`font-weight: bold`), `it` (`font-style: italic`),或其他 bootstrap样式如(`danger`, `info`, `muted`, `primary`, `success` or `warning`).

```xml
<tree decoration-info="state == 'draft'" decoration-muted="state == 'cancel'" decoration-bf="not partner_id" string="Vendor Bill" js_class="account_bills_tree">
```

### create, edit, delete

可以通过将它们设置为false来禁用视图中的对应操作

```xml
<tree decoration-info="state == 'draft'" decoration-muted="state == 'cancel'" string="Voucher Entries" create="0" edit="0">
```

### button

在一个列表单元格中显示按钮

>**属性列表：**
>
>1. `icon` -- 用来展示按钮的图标  可以是 font-awesome
>
>   ```xml
>   <button type="object" name="compute_depreciation_board" string="Compute Depreciation"
>    icon="fa-arrow-right" states="draft"/>
>   ```
>
>2. `string` -- 当没有icon的时候，button显示的文字，有icon的时候、相当于alt属性值
>
>3. `type` -- 按钮类型，表示点击它之后如何影响系统
>
>>1)`workflow`（默认）：将按钮name作为信号发送给工作流，记录的内容作为参数
>>2)`object `： 调用当前数据列表模型的方法，方法名是按钮的name，调用时带有记录id和当前上下文环境
>>
>>```xml
>><button name="action_cancel_draf" states="draft" string="Confirm" type="object" class="oe_highlight"/>
>>```
>>
>>3)`action` ： 加载`ir.actions`，按钮`name`是该`action`在数据库的id，`action`上下文环境添加此列表的`model`(作为`active_model`)、当前记录(`active_id`)、所有当前加载记录的id(`active_ids`)
>>
>>**name** 的值为 `action` 外部ID 或 %()d 转换后的数据库ID
>>
>>```xml
>><button name="%(action_asset_modify)d" states="open,draft" string="Modify Depreciation" type="action"/>
>>name="%(action_asset_modify)d" 会将外部id转换为数据库记录id
>>```
>
>4. `name`,`args` 与`type`一样
>
>5. `attrs` 基于记录值的动态属性，将`domain`表达式应用在记录上，当返回值为`True`的时候设置相应的属性，一般用于`invisible` （隐藏按钮）、`readonly` （禁用按钮但显示）这两种属性
>
>   ```xml
>   <button name="set_to_draft" string="Set to Draft" type="object"
>   attrs="{'invisible': ['|', ('entry_count', '!=', 0), ('state', '!=', 'open')]}"/>
>   ```
>
>6. `states`   `invisible`属性的简写，`attrs`给出一个以逗号分隔的state列表，**需要模型有一个对应的state属性，可以将不在state列表中的记录的按钮隐藏**
>
>   ```xml
>   <button name="%(action_asset_modify)d" states="open,draft" string="Modify Depreciation" type="action"/>
>   ```
>
>7. `context` 当响应odoo的调用时，合并到视图的上下文环境中
>
>8. `confirm` 当点击按钮时给出的确认消息
>
>   ```xml
>   <button name="cancel_voucher" string="Cancel Receipt" type="object" states="posted" confirm="Are you sure you want to cancel this receipt?"/>
>   ```

### field

定义一个所有记录都需要展示的列

>**属性列表：**
>
>1. `name` 需要显示的字段名
>2. `string` 该列的名称
>3. `invisible` 查询而且保存该字段但不显示
>4. `groups` 可以看到该字段的用户组列表
>5. `widget` 用来展示该字段的可选形式
>
>>`progressbar` 进度条用于展示浮点数
>>`many2onebutton`当关联字段值存在时显示勾，不存在显示X
>>`handle`对于排序字段，直接显示向上向下箭头
>
>6. `sum`, `avg` 在**底部**显示基于当前页面数据的计算
>
>   ```xml
>   <field name="practical_amount" avg="Practical Amount" widget="monetary"/>
>   <field name="theoritical_amount" sum="Theoritical Amount" widget="monetary"/>
>   ```
>
>7. `attrs` 基于记录值的动态属性，**只对当前栏有效**，即可以第一条记录中该字段显示，第二条隐藏

如果列表视图是可编辑的，那么表单视图中的任何字段属性都是有效的，并将在设置内联表单视图时使用

### control

为当前视图定义自定义控件。如果父树视图位于一个One2many字段中，这是有意义的。

不支持任何属性，但可以有子元素:

>`create` 添加按钮以在当前列表中创建新元素。如果定义了任何create，它将覆盖默认的“add a line”按钮。
>
>支持以下属性:
>
>>`string` (必填)  显示在按钮上的文本。
>>
>>`context`当检索新记录的默认值时，该上下文将合并到现有上下文中。
>>
>>例如，它可以用来覆盖默认值。

下面的示例将用3个新按钮替换默认的“add a line”按钮，从而覆盖“add a line”按钮:“add a product”、“add a section”和“add a note”。

“Add a product”将字段“display_type”设置为其默认值。

另外两个按钮将把字段“display_type”分别设置为“line_section”和“line_note”。

```xml
<control>
  <create string="Add a product"/>
  <create string="Add a section" context="{'default_display_type': 'line_section'}"/>
  <create string="Add a note" context="{'default_display_type': 'line_note'}"/>
</control>
```



## 表单视图

表单用于展示,创建和编辑单个记录。

根元素是`<form>`，由常规html和构造部分、语义部分组成

### 构造部分

构造部分提供了结构和可视特性，以元素或者元素的子元素的形式应用到表单视图的元素中

#### notebook

定义一个tab块，每一个tab通过一个page子元素定义，每个page可以有以下属性：

- string (required) --tab标签的名称
- accesskey --HTML访问键
- attrs --基于记录值的动态属性

#### group

用于定义栏目在表单中布局，默认情况下一个group定义两个列，并且每个最直接的子元素占用一个列，field类型的元素默认显示一个标签
group占用的列数是可以通过**col**属性自定义的，默认2个；
其他元素可以通过**colspan**属性来定义占的列数，子元素是横向布局的，可以通过设置string 属性来定义group所展示的标题

```xml
<form string="Idea form">
    <group col="4">
        <group col="2">
            <separator string="General stuff" colspan="2"/>
            <field name="name"/>
            <field name="inventor_id"/>
        </group>

        <group col="2">
            <separator string="Dates" colspan="2"/>
            <field name="active"/>
            <field name="invent_date" readonly="1"/>
        </group>

        <notebook colspan="4">
            <page string="Description">
                <field name="description" nolabel="1"/>
            </page>
        </notebook>

        <field name="state"/>
    </group>
</form>
```

#### newline

只在group元素里才有用，代表开启新的行

#### separator

一条水平线，可以通过string属性来设置该区域的标题

#### sheet

可以用作form的子元素用来表示更加狭义的表单

#### header

与sheet一起使用，显示在sheet的上方的一个条，一般用于显示工作流和状态栏

### 语义部分

语义部分用于与odoo系统交互

#### button 

调用Odoo系统，类似于列表视图按钮。此外，还可以指定以下属性:

>`special` 对于对话框中打开的窗体视图:`save`以保存记录并关闭对话框，`cancel`以不保存而关闭对话框。
>
>```xml
><button string="Cancel" class="btn-secondary" special="cancel"/>
>```

#### field

展示当前记录的某个字段，有以下属性：
- `name` (必选) -- 用于展示字段名

- `widget` -- 每个字段根据其数据类型有一个默认的展示方式，widget属性可指定用一个别的方式来展示

- `options` -- 用于指定widget字段配置的json对象

  ```xml
  <field name="value_residual" widget="monetary" options="{'currency_field': 'currency_id'}"/>
  ```

- `class` -- 用于设置当前元素的html class属性：

  >`oe_inline` -  防止它自动将之后的字段换行
  >`oe_left`, `oe_right` - 相当于css的float
  >`oe_read_only`, `oe_edit_only` - 只在相应的模式下展示该字段
  >`oe_no_button` - 不为many2one字段显示导航按钮
  >`oe_avatar` - 当该字段为图片时，将它展示为头像（90*90的正方形）

- `groups` - 只将该字段展示给指定用户组

- `on_change` - 在字段值改变时调用对应方法，从8.0开始改用模型中的 odoo.api.onchange()

- `attrs` - 基于记录值的动态参数

- `domain` - 当以选择的方式显示关联字段时，用过过滤数据

- `context `- 用于关联字段，显示数据时提供上下文环境

- `readonly` - 该字段可在读和编辑模式下展示，但是永远是不能编辑的

- `required` - 当该值没有设置就保存时给出一个错误提示并阻止保存

- `nolabel` - 不显示字段的标签，只有在该字段是group子元素时用意义

- `placeholder` - 字段值为空时展示的提示

- `mode` - 对于one2many字段，用于展示其关联的记录的形式，有tree, form, kanban , graph，默认是tree

- `help` - 当将鼠标放在字段或标签时显示的提示

- `filename` - 对于二进制的字段，相关字段给出文件名

- `password` - 表示该字段是一个密码，不明文展示

### 业务视图规则

业务视图是指向普通用户的，像：机会、产品、合作伙伴、任务、项目等

![](https://www.odoo.com/documentation/12.0/_images/oppreadonly.png)

一般情况下，业务视图由以下元素组成：

- 展示在顶部的业务流程的状态按钮
- 中间展示一个表单的表格
- 底部展示评论和历史操作记录

从技术上讲，新的表单视图结构如下:

```xml
<form>
    <header> ... content of the status bar  ... </header>
    <sheet>  ... content of the sheet       ... </sheet>
    <div class="oe_chatter"> ... content of the bottom part ... </div>
</form>
```

#### 状态条

用于展示当前记录的状态和相应的动作按钮

![img](https://www.odoo.com/documentation/12.0/_images/status.png)

- **按钮**
   按钮的顺序与业务流程的顺序一致，例如在销售流程中，流程如下：

  >->发送询价单
  >
  >->确认询价
  >
  >->创建发货单
  >
  >->发货


高亮的按钮强调下一步的流程，用于提示用户，通常放在第一个。另外取消按钮一般被设置成灰色，如在发货里退款按钮不会被设置为高亮。通过设置oe_highlight的class属性来将按钮元素高亮显示

  ```xml
  <button class="oe_highlight" name="..." type="..." states="..."/>
  ```

- **状态**

  使用statusbar小部件，并用红色显示当前状态。所有流共有的状态(例如，一个销售订单以报价开始，然后我们发送它，然后它变成一个完整的销售订单，最后它完成了)应该在任何时候都是可见的，但是例外情况或依赖于特定子流的状态只应该在当前时可见。

  >![img](https://www.odoo.com/documentation/12.0/_images/status1.png)![img](https://www.odoo.com/documentation/12.0/_images/status2.png)
  >
  >

  states是根据字段值对应的顺序来展示的，一直显示的状态可通过statusbar_visible属性指定：

  >```xml
  ><field name="state" widget="statusbar" statusbar_visible="draft,sent,progress,invoiced,done" />
  >```

#### 表格

业务视图展示出来要像一张表格一样

![img](https://www.odoo.com/documentation/12.0/_images/sheet.png)

- 在page或form里的元素不会自动分组，它们会根据普通的html规则来布局，可以通过group或div标签来进行分组展示
- 默认情况下group标签定义两列，可以通过col="n"来指定多列，并且每列的宽度是一样的。
- 可以给group标签添加string属性来给该区块内容添加标题
   `<group string="Time-sensitive operations">` 
- 不在group内的field标签默认是不生成label的，可以通过<label for="field_name>来指定label

##### 表格头
某些表格是它们只在编辑模式下才显示字段的标签

| View mode                                                    | Edit mode                                                    |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| ![img](https://www.odoo.com/documentation/12.0/_images/header.png) | ![img](https://www.odoo.com/documentation/12.0/_images/header2.png) |

使用HTML文本`<div>`, `<h1>`,` <h2>`…来生成漂亮的标题

使用`oe_edit_only` 的`class`属性来指定label只在编辑模式下才展示，`oe_inline` 属性将多字段设置展示到单行中

```xml
<label for="name" class="oe_edit_only"/>
<h1><field name="name"/></h1>
<label for="planned_revenue" class="oe_edit_only"/>
<h2>
    <field name="planned_revenue" class="oe_inline"/>
    <field name="company_currency" class="oe_inline oe_edit_only"/> at
    <field name="probability" class="oe_inline"/> % success rate
</h2>
```

##### 按钮箱

可以在表单中显示许多相关操作按钮或链接。例如，在机会形式中，“安排一个电话”和“安排一个会议”在CRM的使用中占有重要地位。不要将它们放在“More”菜单中，而是直接将它们作为按钮(在顶部)放在工作表中，以使它们更容易看到和访问。

![img](https://www.odoo.com/documentation/12.0/_images/header3.png)

从技术上讲，按钮被放置在`<div>`中，以便将它们作为工作表顶部的一个块进行分组。

```xml

<div class="oe_button_box" name="button_box">
    <button string="安排电访" name="..." type="action"/>
    <button string="安排会面" name="action_makeMeeting" type="object"/>
</div>
```

##### 分组和标题

为了方便视图扩展，需要给`<group>`指定一个name属性，这样在扩展视图中可以更容易的找到添加字段的正确位置

![img](https://www.odoo.com/documentation/12.0/_images/screenshot-03.png)

```xml
<group string="Payment Options">
    <field name="writeoff_amount"/>
    <field name="payment_option"/>
</group>
```

建议表单上有两列字段。为此，只需将包含字段的`<group>`元素放在顶级 `<group>`元素中。

为了使视图扩展更简单，建议将`name`属性放在 `<group>`元素上，这样就可以很容易地在正确的位置添加新字段。

##### 特殊案例：小计

某些class是用来展示小计时使用的，比如发货单：

![img](https://www.odoo.com/documentation/12.0/_images/screenshot-00.png)

```xml
<group class="oe_subtotal_footer">
    <field name="amount_untaxed"/>
    <field name="amount_tax"/>
    <field name="amount_total" class="oe_subtotal_footer_separator"/>
    <field name="residual" style="margin-top: 10px"/>
</group>
```

##### placeholder和行内输入框

有时候字段的标签把表单搞的太复杂了，可以将标签隐藏而采用placeholder来提示用户该输入框需要输入什么，同时可以通过div包裹多个inline输入框来让它们像是单个字段一样显示，例：

| Edit mode                                                    | View mode                                                    |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| ![img](https://www.odoo.com/documentation/12.0/_images/placeholder.png) | ![img](https://www.odoo.com/documentation/12.0/_images/screenshot-01.png) |

```xml
<group>
    <label for="street" string="Address"/>
    <div>
        <field name="street" placeholder="Street..."/>
        <field name="street2"/>
        <div>
            <field name="zip" class="oe_inline" placeholder="ZIP"/>
            <field name="city" class="oe_inline" placeholder="City"/>
        </div>
        <field name="state_id" placeholder="State"/>
        <field name="country_id" placeholder="Country"/>
    </div>
</group>
```

##### 图片

图片一般在表单的右边显示

![img](https://www.odoo.com/documentation/12.0/_images/screenshot-02.png)

```xml
上面的表单包含一个元素，它的开头是
<field name="product_image" widget="image" class="oe_avatar oe_right"/>
```

##### 标签
大多数多对多关系字段，如分类，一般使用多标签来展示

![img](https://www.odoo.com/documentation/12.0/_images/screenshot-04.png)

```xml
<field name="category_id" widget="many2many_tags"/>
```

### 配置表单指导原则

一般不需要header（因为没有状态、工作流、按钮），不需要表格，如：阶段配置

![img](https://www.odoo.com/documentation/12.0/_images/nosheet.png)

### 弹出框表单指导原则

例：商机的安排电话访问表单

![img](https://www.odoo.com/documentation/12.0/_images/wizard-popup.png)

1. 避免使用分隔线
2. 不使用取消按钮（因为一般用户会直接关闭弹框来替代）
3. 操作钮钮必须被高亮显示
4. 如果是文本框，使用placeholder来代替label
5. 将按钮放在header元素中

### 配置向导指导原则

例：设置-配置-销售
1.单行显示（没有弹出框）2.没有表格 3.保留取消按钮 4.保存按钮标红

**表单视图还可以使用纯HTML来实现更灵活的布局**



## 图表

图表是用于将数据进行聚合显示用的，它的根标签是`<gragh>`，有以下几种属性：

- `type` - bar 柱形图（默认）、line 线形图 、 pie 扇形图
- `stacked` - 只在柱形图里使用，设置为True的时候，会在将柱形图排到group里

图表里唯一能插入的元素就是field，它有以下几种属性

- `name` (必选 )-- 用在图表中的字段名
- `title` (可选)显示在图形顶部的字符串。
- `type` -- 指定该字段是进行分类统计还是总计

>`row` 默认 -- 根据指定字段分组，所有图表至少支持一级分组，有些支持多级，在pivot视图中，每个分组拿自己的记录
>`col` -- 只在pivot表中使用，创建一个列优先的分组集合
>`measure` -- 分组中用来聚合的字段

- interval -- 在基于date或datetime字段进行分组统计时使用day, week, month, quarter , year来计算

从模型字段自动生成度量;只使用可聚合字段。这些度量也按字段字符串的字母顺序排序

警告

图视图聚合是对数据库内容执行的，图视图中不能使用非存储的函数字段



## 枢轴

主视图用于将聚合可视化为一个主表。它的根元素是`<pivot>` ,可以取以下属性:

- `disable_linking`设置为True时取消单元格和数据列表视图之间的链接

- `display_quantity`设置为True时以默认方式显式数量

- `default_order`度量的名称和在视图中用作默认顺序的顺序(asc或desc)。

>```xml
><pivot default_order="foo asc">
>   <field name="foo" type="measure"/>
></pivot>
>```

pivot跟其他图表一样也只允许field元素，它可以有以下属性:

- `type` - bar 柱形图（默认）、line 线形图 、 pie 扇形图
- `stacked` - 只在柱形图里使用，设置为True的时候，会在将柱形图排到group里

图表里唯一能插入的元素就是field，它有以下几种属性

- `name` (必选 )-- 用在图表中的字段名
- `title` (可选)显示在图形顶部的字符串。
- `type` -- 指定该字段是进行分类统计还是总计

> `row` 默认 -- 根据指定字段分组，所有图表至少支持一级分组，有些支持多级，在pivot视图中，每个分组拿自己的记录
> `col` -- 只在pivot表中使用，创建一个列优先的分组集合
> `measure` -- 分组中用来聚合的字段
>
> `interval` -- 在基于date或datetime字段进行分组统计时使用day, week, month, quarter , year来计算

- `invisible`如果为真，则该字段既不会出现在活动度量中，也不会出现在可选择度量中(对于聚合没有意义的字段非常有用，例如不同单位中的字段，例如€和$)。

从模型字段自动生成度量;只使用可聚合字段。这些度量也按字段字符串的字母顺序排序。

警告

与graph视图一样，pivot聚合数据库内容上的数据，这意味着不能在pivot视图中使用非存储的函数字

在Pivot视图中，`field`可以有一个`widget`属性来指定其格式。小部件应该是一个字段格式化器，其中最有趣的是date、datetime、float_time和monetary。

例如，timesheet pivot视图可以定义为:

```xml
<pivot string="Timesheet">
    <field name="employee_id" type="row"/>
    <field name="date" interval="month" type="col"/>
    <field name="unit_amount" type="measure" widget="float_time"/>
</pivot>
```



## 看板视图

看板视图是看板板的可视化:它以“卡片”的形式显示记录，介于列表视图和不可编辑表单视图之间。记录可以分组在列中，用于工作流可视化或操作(例如任务或工作进度管理)，也可以不分组(仅用于可视化记录)。

看板视图将最多加载和显示10列。之后的任何列都将被关闭(但仍然可以由用户打开)。

它的根标签是`<kanban>`，有以下属性

- `default_group_by` -- 当action或search没有进行分组时，视图是否需要进行分组，取值为用于进行分组的字段名
- `default_order` -- 当用户没有对记录进行排序时卡片中所使用的排序字段
- `class` -- 添加看板视图根html的类属性
- `group_create`--“添加新列”栏是否可见。默认值:true。
- `group_delete`--是否可以通过上下文菜单删除组。默认值:true。
- `group_edit`--是否可以通过上下文菜单编辑组。默认值:true。
- `archivable`--如果在模型上定义了activefield，是否可以存档/恢复属于列的记录。默认值:true。
- `quick_create` -- 是否可以在不切换到表单视图的情况下直接创建记录，当看板视图是经过分组的时候它是启用的，否则不启用，可通过设置True来强制启用，False强制禁用

子元素可以是以下几种

#### field

定义用来集合计算或用在看板视图逻辑中的字段，如果某字段仅用于在看板视图中展示，它不需要预先进行定义，有以下属性：

- name (required) -- 用于获取数据的字段名
- sum, avg, min, max, count -- 在看板视图最上方展示对应的计算后的值，每个字段只支持一个

#### progressbar

声明要放在看板列顶部的progressbar元素。

有以下属性：

- `field` (required) 值用于对progressbar中列的记录进行子组的字段的名称
- `colors` (required) JSON将上述字段值映射为danger”、“warning”或“success”颜色
- `sum_field` (optional)字段的名称，其列的记录值将被汇总并显示在progressbar旁边(如果省略，则显示记录的总数)

#### templates

定义一个QWeb模板列表，卡片可以分割成多个模板，但看板视图至少需要定义一个kanban-box标签，每条记录会执行一次，看板视图用的是严格的qweb javascript，有以下几个环境变量：

- instance -- 当前qweb实例
- widget -- 可用来获取元数据信息，
- record -- 一个带有所有被请求字段的对象，每个字段有value和raw_value两个属性，value遵循当前用户格式，raw_value是直接读取出来的数据
- formats -- 用于操纵和转换值的web.formats()模块
- read_only_mode -- 只读

### 按钮和字段

由于看板模板是标准的qweb，看板视图有特殊的处理field、button、a标签的方式

- 默认情况下字段值显示的是格式化之后的，除非它匹配了对应的视图widget
- 拥有type属性的按钮和链接会转换成odoo相关的操作：

> `action`,`object`  --标准行为的Odoo按钮，大多数属性相关的标准Odoo按钮可以使用
>
> `open` --  在只读模式下打开卡片的视图
>
> `edit` --  在编辑模式下打开卡片视图
>
> `delete` -- 删除卡片的记录且移除卡片

### javascript API

class KanbanRecord()

- Widget() 将单条记录解析到卡片中
- kanban_color(raw_value) 将一个color片段转换成oe_kanban_color_color_index
- kanban_getcolor(raw_value) 将color片段转换为color_index
- kanban_image(model, field, id[, cache][, options]) 将指定字段转换成图片URL

> `model` -- 保存图片的model， field -- 保存图片数据的字段名 ， id -- 需要展示图片的记录id，cache--图片在浏览器的缓存时间（秒），0表示不缓存

- kanban_text_ellipsis(string[, size=160]) 将比较长的内容提取一部分显示

## 日历视图

日历视图按天、周、月来显示数据，根元素是`<calendar>`，有以下属性：

- `date_start` (必选) -- 储存开始时间的字段

- `date_stop` -- 储存结束时间的字段，当提供了该字段时记录可以直接在视图中删除

- `date_delay` -- 与date_stop类似，表示的是该事件的持续时间

- `color` -- 用于定义颜色的字段，颜色字段值相同的记录会在视图中以相同的颜色显

- `readonly_form_view_id`-- 视图以只读模式打开

- `form_view_id`-- 视图在用户创建或编辑事件时打开。注意，如果没有设置此属性，calendar视图将返回到当前操作中form视图的id(如果有的话)。

- `event_open_popup`-- 以弹框代替表单(使用do_action)来打开事件，默认是禁用的

- `quick_add`-- 允许快速添加事件，只需要提供name就行，当创建失败时会转到一个完整的表单弹出框

- `all_day`-- 布尔型，用来定义对应事件是否是全天有效

- `mode`-- 默认的显示模式：day, week, month

- `<field>`

  声明要聚合或在看板逻辑中使用的字段。如果字段只是显示在日历卡中。

  字段可以有额外的属性:

  >`invisible`		使用“True”隐藏卡片中的值
  >
  >`avatar_field`	仅对于x2many字段，在卡片中显示avatar而不是display_name
  >
  >`write_model` ***and*** `write_field` 您可以添加一个过滤器并将结果保存在定义的模型中，过滤器添加在侧栏中

- `templates`

  定义QWeb模板日历框。卡片定义可以被分割成多个模板，以便清晰地呈现每条记录一次。
  
  看板视图使用最标准的javascript qweb，并提供以下上下文变量:
  
  >`widget`--当前的KanbanRecord()可以用来获取一些元信息。这些方法也可以直接在模板上下文中使用，不需要通过小部件getColor来访问，就可以在颜色整数getAvatars中转换，也可以在不可见字段的avatar图像显示字段列表中转换
  >
  >`record`--将所有请求字段作为其属性的对象。每个字段都有两个属性值和raw_value
  >
  >`event`--日历事件对象
  >
  >`format`-- format方法将值转换为具有用户参数的可读字符串
  >
  >`fields`--定义所有模型字段参数
  >
  >`user_context`--不需加以说明的
  >
  >`read_only_mode`--不需加以说明的



## 甘特图

甘特图用于展示甘特图表如流程，根元素是`<gantt>`，没有子元素，但可以有以下属性：

- `date_start` (required)-- 储存开始时间的字段

- `date_stop`-- 提供结束时间的字段，可以用date_delay来实现同样的作用，两者必须提供一个，如果该字段被设置为False，那该事件的开始时间和结束时间是同个时间点

- `date_delay`-- 提供事件持续时间的字段

- `duration_unit`-- 持续时间的单位，minute, hour (默认), day, week, month, year

- `default_group_by`-- 任务分组的依据字段

- `type`-- 

  > `gantt`（默认） 传统甘特图
  >
  > `consolidate` (首个child的值被合并甘特图任务中)
  >
  > `planning` (children会自动显示到甘特图任务中）
  >
  > 

- `consolidation` -- 在记录单元格中用于显示合并值的字段名

- `consolidation_max` -- 数据字典，表示超过一定的值会标红显示 ，如：`{"user_id": 100}`

- `consolidation_exclude`描述如果必须将任务排除在整合之外的字段名(如果设置为true)，它将在整合线中显示一个带条纹的区域，警告词典定义必须使用双引号，{'user_id': 100}不是有效值

- `create`, `edit`--允许通过将相应属性设置为false来禁用视图中相应的操作

- `string` -- 展示在合并值旁边的字符，如果没设置会自动取对应字段的label

- `fold_last_level`-- 如果设置了该属性，最后一个分组级别会被折叠

- `round_dnd_dates`-- 开始和结束时间取整

- `drag_resize`任务调整，默认True

- `progress`为记录事件提供完成率的字段的名称，该字段的完成率介于0到100之间



## Diagram

示意图可用来展示原来就是图表的记录，根元素是`<diagram>`，没有属性，

有几种子元素：

- `node` (必选, 1)

  定义图表的节点，有以下属性：

  > `object`-- 节点对应的model
  >
  > `shape`-- 就像列表视图的颜色、字体一样的形状表示，唯一可选的取值是`rectangle` （长方形），默认无
  >
  > `bgcolor`-- 用来表示节点的背景颜色，默认是白色，可取值grey

- `arrow` (必选, 1)

  用于定义图表的箭头，有以下属性：

  > `object` (required)-- 箭头对应的model
  >
  > `source` (required)-- model的Many2one字段，用于指向箭头的源节点数据
  >
  > `destination` (required)-- model的Many2one字段，指向箭头的目标节点数据
  >
  > `label`-- python格式的属性列表，相应的属性值会用作箭头的label显示

- `label`

  用于解释示意图的节点，string属性定义的是节点的内容，每个label带有编号显示在示意图头部



## 仪表板视图

与pivot和graph视图一样，dashboard视图用于显示聚合数据。然而，仪表板可以嵌入子视图，这使得对给定数据集有更完整和更有趣的查看成为可能。

### Warning

​	仪表板视图只在Odoo企业中可用。

仪表板视图可以显示子视图、某些字段的聚合(在一个域中)，甚至公式(包含一个或多个聚合的表达式)。例如，这里有一个非常简单的仪表盘:

```xml
<dashboard>
    <view type="graph" ref="sale_report.view_order_product_graph"/>
    <group string="Sale">
        <aggregate name="price_total" field="price_total" widget="monetary"/>
        <aggregate name="order_id" field="order_id" string="Orders"/>
        <formula name="price_average" string="Price Average"
            value="record.price_total / record.order_id" widget="percentage"/>
    </group>
    <view type="pivot" ref="sale_report.view_order_product_pivot"/>
</dashboard>
```

Dashboard视图的根元素是< Dashboard >，它不接受任何属性。

在仪表板视图中有5种可能的标签类型:

- `view`

  声明子视图。

  容许属性:

  - `type`(强制)--子视图的类型。例如，图或枢轴。
  - `ref`(可选)--视图的xml id。如果没有给出，则使用模型的默认视图。
  - `name`(可选)--标识此元素的字符串。用作xpath的目标非常有用。

- `group`

  定义列布局。这实际上非常类似于表单视图中的group元素。

  容许属性:

  - `string` (可选)--将显示为组标题的描述。
  - `colspan` (可选)--此组标记中的子列数。默认情况下,6。
  - `col` (可选)--由这个组标记张成的列数(只有在另一个组中才有意义)。默认情况下,6

- `aggregate`

  声明一个聚合。这是给定字段在当前域中的聚合值。

  请注意，聚合应该在组标记中使用(否则样式将无法正确应用)。

  容许属性:

  - `field` (必填)

  用于计算聚合的字段名。可能的字段类型有:

  > `integer` (默认的组操作符是sum)
  >
  > `float` (默认的组操作符是sum)
  >
  > `many2one` (默认的组操作符是count distinct)

  

  - `name` (必填)

  - `string` (可选)

    将在值上方显示的简短描述。如果不给出，它将返回到字段字符串。

  - `domain` (可选)

    对要聚合的记录集的附加限制。此域将与当前域合并。

  - `domain_label` (可选)

    当用户单击带有域的聚合时，它将作为方面添加到搜索视图中。可以使用此属性自定义为此方面显示的字符串。

  - `group_operator` (可选)

    使用WHN聚合值的有效PostgreSQL聚合函数标识符（请参阅https://www.postgresql.org/docs/9.5/static/functions aggregate.html）。如果未提供，默认情况下，将使用字段定义中的group_运算符。请注意，如果组“operator value”为“”，则不会实现字段值的聚合。

    这里还可以使用特殊的聚合函数count_distinct（在odoo中定义）

    ```xml
    <aggregate name="price_total_max" field="price_total" group_operator="max"/>
    ```
    
  - `col` (可选)--由此标记张成的列数(仅在组中有意义)。默认情况下,1。
  
  - `widget` (可选)--格式化值的小部件(类似于字段的小部件属性)。例如,货币。
  
  - `help` (可选)--工具提示中dipkill的帮助消息(相当于python中字段的帮助)
  
  - `measure` (可选)--此属性是描述在单击聚合时必须在图和轴心视图中使用的度量的字段的名称。特殊值_count__可用于计数测度。
  
    ```xml
    <aggregate name="total_ojects" string="Total Objects" field="id" group_operator="count" measure="count"/>
    ```
  
  - `clickable` (optional)--一个布尔值，指示这个聚合是否应该单击(默认为true)。单击可单击聚合将更改子视图使用的度量，并将域属性的值(如果有的话)添加到搜索视图。
  - `value_label` (optional)--放在聚合值右侧的字符串。例如，指示聚合值的度量单位可能很有用。

- `formula`

  声明派生值。公式是由聚合计算得到的值。

  注意，与聚合类似，公式也应该在组标记中使用(否则样式将无法正确应用)。

- `widget`

  声明用于显示信息的专用小部件。这是一种类似于窗体视图中小部件的机制。允许的属性是：name（强制）一个字符串，用于标识应实例化哪个小部件。视图将查看widget_注册表，以获得正确的class.col（可选）这个标记所跨越的列数（只在组内有意义）。默认情况下，1.



## Cohort

队列视图用于显示和理解某些数据在一段时间内的变化方式。例如，假设对于给定的业务，客户机可以订阅某些服务。然后，队列视图可以显示每个月的订阅总数，并研究客户离开服务（流失）的速度。单击单元格时，队列视图将重定向到一个新操作，在该操作中，您将只看到单元格时间间隔中包含的记录；此操作包含列表视图和表单视图。

### Warning

队列视图仅在Odo Enterprise中可用。

默认情况下，队列视图将使用与操作上定义的列表和表单视图相同的列表和表单视图。您可以将列表视图和表单视图传递到操作的上下文，以便设置/重写将要使用的视图（要使用的上下文键是表单视图ID和列表视图ID）

例如，这里有一个非常简单的队列视图：

```
<cohort string="Subscription" date_start="date_start" date_stop="date" interval="month"/>
```

队列视图的根元素是`<cohort>`，它接受以下属性：

- `string` (必填)

  标题，应描述视图

- `date_start` (必填)

  有效的日期或日期时间字段。视图将此字段理解为记录的开始日期。

- `date_stop` (必填)

  有效的日期或日期时间字段。视图将此字段理解为记录的结束日期。这是决定客户流失的字段。

- `mode` (可选)

  描述模式的字符串。它应该是“客户流失”或“保留”（默认）。搅动模式将从0%开始，并随着时间累积，而保留将从100%开始，并随着时间减少。

- `timeline` (可选)

  描述时间线的字符串。它应该是“向后”或“向前”（默认）。前进时间线将显示从“开始”到“停止”的数据，而后退时间线将显示从“停止”到“开始”的数据（当“开始”日期在将来/大于“停止”日期时）。

- `interval` (可选)

  描述时间间隔的字符串。应为“天”、“周”、“月”（默认）或“年”。

- `measure` (可选)

  可以聚合的字段。此字段将用于计算每个单元格的值。如果未设置，队列视图将计算出现的次数。



## Activity

活动视图用于显示链接到记录的活动。数据显示在图表中，其中记录构成行，活动类型为列。当单击一个单元格时，将显示该记录的同一类型的所有活动的详细说明。

### Warning

只有在安装了`mail` 模块以及从`mail.activity.mixin`继承的模型时，“活动”视图才可用。

例如，这里是一个非常简单的活动视图：

```
<activity string="Activities"/>
```

活动视图的根元素是`<activity>`，它接受以下属性：

- `string` (必填)

  标题，应描述视图



## Search

搜索视图自定义与列表视图（以及其他聚合视图）关联的搜索字段。它们的根元素是`<search>`，它们由定义可以搜索哪些字段的字段组成：

如果模型不存在搜索视图，则Odoo会生成仅允许在该`name`字段上搜索的视图。

搜索视图与以前的视图类型不同，因为它们不显示内容：尽管它们应用于特定的模型，但它们用于筛选其他视图的内容（通常是聚合视图，例如列表或图形）。除了用例中的差异之外，它们的定义方式也是一样的。

搜索视图的根元素是`<search>`。它不需要属性。

搜索视图的可能子元素包括：

- `field`

  字段使用用户提供的值domains或contexts。当生成搜索域时，字段域彼此组成，并使用**AND**筛选。

  字段可以具有以下属性：

  `name`要筛选字符串的字段的名称字段的labeloperator默认情况下，字段生成形式为 `[(*name*, *operator*,*provided_value*)]`的域，其中name是字段的名称，provided值是用户提供的值，可能是fil或转换（例如，用户需要提供选择字段值的标签，而不是值本身）。

  `operator`属性允许重写默认运算符，该运算符取决于字段的类型（例如=对于float字段，而ilike对于char字段）`filter_domain` complete域用作字段的搜索域，可以使用自变量将提供的值注入自定义域。可用于生成比单独的运算符更灵活的域（例如，一次搜索多个字段）。如果同时提供运算符和筛选器域，则筛选器域优先。上下文允许添加上下文键，包括用户提供的值（对于域，该值为avai）标记为自变量）。默认情况下，字段不会生成域。域和上下文是包含的，如果指定了上下文，则两者都会生成。若要仅生成上下文值，请将filter_domain设置为空列表：filter_domain=“[]”`` groups使该字段仅对特定用户可用如果该字段可以提供De an auto completion（例如Many2one），过滤可能的完成结果。

  

- `filter`

  过滤器是搜索视图中的预定义切换，只能启用或禁用。其主要目的是将数据添加到搜索上下文（传递给数据视图以进行搜索/筛选的上下文），或将新节附加到搜索筛选器。筛选器可以具有以下属性：string（必需）filter domain（可选）的标签odoo域，将被附加到o操作的域作为搜索域的一部分。日期（可选）日期或日期时间类型的字段的名称。使用此属性可以创建过滤器菜单子菜单中可用的一组过滤器。示例：<filter name=“filter_create_date”date=“create_date”string=“creation date”/>上面的示例允许在其中一个期间中轻松搜索具有创建日期字段值的记录。下面。创建日期>本周，本月，本季度Orites菜单）。默认时间段（可选）仅对具有非空日期属性的筛选器有意义。确定如果筛选器在视图初始化时激活的默认筛选器集中，则激活哪个期间。如果未提供，则默认使用“本月”。要在以下选项中进行选择：今天、本周、本月、本季度、本年、昨天、上周、上月、上季度、去年、上7天、上30天、上365天示例：<filter name=“filter\u create\u date”date=“create_date“string=”creation date“default_period=”this_week/>`` contexta python dictionary，合并到操作的域中以生成搜索域密钥group_by可用于定义“group by”菜单中可用的groupby。“group_by”值可以是有效的字段名或字段名列表。<filter name=“groupby_category”string=“category”context=“group_by”：“category_id”/>上面定义的groupby允许按类别对数据进行分组。当字段类型为日期或日期时间时，筛选器生成子菜单。在“分组依据”菜单中，可以使用以下间隔选项：日、周、月、季度、年。如果筛选器在视图初始化时激活的默认筛选器集中，则默认情况下，记录按月分组。这可以通过使用以下示例中的语法“日期域：间隔”来更改。示例：<filter name=“group by\u create\u date”string=“creation date”context=“group\u by”：“创建日期：周”/>``筛选器的名称逻辑名称，默认情况下可用于启用它，也可用于heritance hookhelp筛选器的较长解释性文本可以显示为工具提示组，就像只有特定用户才能使用的筛选器7.0版一样。筛选器序列（没有将其分隔的非筛选器）被视为包含组合：它们将由或更确切地说是由n通常和，例如<filter domain=“[（'state'，'='，'draft'）”/><filter domain=“[（'state'，'='，'done'）”/>如果同时选择了两个筛选器，将选择状态为draft或done的记录，但<filter domain=“[（'state'，'='，'draft'）”/><separator/><filter domain=“[（'delay'，'<'，15）]“/>如果bot选择H过滤器，将选择状态为草稿且延迟低于15的记录。

- `separator`

  可用于在简单搜索视图中分隔过滤器组

- `group`

  可用于分隔过滤器组，比复杂搜索视图中的分隔符更可读。

### Search defaults

搜索字段和过滤器可以通过操作的上下文使用搜索\u default_*name*键进行配置。对于字段，值应该是要在字段中设置的值，对于筛选器，它是一个布尔值。例如，假设foo是一个字段，而bar是一个筛选器，则操作上下文为：

```
{
  'search_default_foo': 'acro',
  'search_default_bar': 1
}
```

将自动启用栏过滤器，并在foo字段中搜索`acro`。



### widget

| **odoo12** **基础 widget** | **高级 widget，多数为关联型及模块专有** |
| -------------------------- | --------------------------------------- |
| abstract                   | appointment_employee_url                |
| ace                        | asyncwidget                             |
| attachment_image           | barcode_handler                         |
| binary                     | bullet_state                            |
| boolean                    | deprec_lines_toggler                    |
| boolean_button             | field_float_scannable                   |
| boolean_favorite           | field_partner_autocomplete              |
| boolean_toggle             | filters                                 |
| char                       | form.many2many_tags                     |
| CopyClipboardChar          | gauge                                   |
| CopyClipboardText          | hierarchy_kanban                        |
| dashboard_graph            | hr_org_chart                            |
| date                       | html                                    |
| datetime                   | html_frame                              |
| domain                     | inventory_barcode_handler               |
| email                      | iot                                     |
| float                      | iot_picture                             |
| float_factor               | kanban.many2many_tags                   |
| float_time                 | kanban.many2one                         |
| float_toggle               | kanban_activity                         |
| handle                     | list.many2one                           |
| html                       | lot_barcode_handler                     |
| image                      | mail_activity                           |
| input                      | mail_followers                          |
| integer                    | mail_thread                             |
| kanban_state_selection     | many2many                               |
| label_selection            | many2many_binary                        |
| link_button                | many2many_checkboxes                    |
| monetary                   | many2many_select                        |
| pdf_viewer                 | many2many_tags                          |
| percentage                 | many2many_tags_email                    |
| percentpie                 | many2manyattendee                       |
| phone                      | many2one                                |
| priority                   | marketing_activity_graph                |
| progressbar                | mrp_time_coun                           |
| state_selection            | one2many                                |
| statinfo                   | one2many_list                           |
| text                       | pad                                     |
| toggle_button              | password_meter                          |
|                            | payment                                 |
|                            | picking_barcode_handler                 |
|                            | previous_order                          |
|                            | radio                                   |
|                            | reference                               |
|                            | report_layout                           |
|                            | res_partner_many2one                    |
|                            | section_and_note_one2many               |
|                            | section_and_note_text                   |
|                            | selection                               |
|                            | selection_badge                         |
|                            | sms_widget                              |
|                            | statusbar                               |
|                            | tablet_image                            |
|                            | tablet_kanban_view                      |
|                            | tablet_list_view                        |
|                            | terback_arrow                           |
|                            | test                                    |
|                            | test_barcode_handler                    |
|                            | timesheet_uom                           |
|                            | timezone_mismatch                       |
|                            | upgrade_boolean                         |
|                            | upgrade_radio                           |
|                            | url                                     |
|                            | website_button                          |
