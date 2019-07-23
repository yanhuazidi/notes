[TOC]



## 常见的结构

视图对象公开许多字段，除非另有指定，否则它们是可选的。

- `name` (必选) 用于通过名字查找

- `model `与view相关联的model

- `priority` 当搜索查找view时，优先级最低的view会被返回

- `arch` 视图layout的描述

- `groups_id` 指定可查看、使用视图的用户组id，many2many关系

- `inherit_id` 当前视图的父级视图

- `mode` 继承模式，当inherit_id没有设置时，它的值是primary,当设置了inherit_id后，它默认值是extension，可手动设置为primary

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

- 带有expr属性的xpath元素 ，expr是一个用在arch中的xpath表达式，找到的第一个节点就是匹配结果
- 带有name属性的field元素，匹配第一个一样name的field元素，其他的属性在匹配时被忽略
- 其他的元素：匹配第一个拥有一样的name及其他属性的元素（忽略position,version属性）

继承规范通过可选的position属性来指定如何修改匹配的节点

- `inside`（默认） - 添加到匹配的节点前
- `replace` - 替换匹配的节点
- `after `- 添加到匹配的节点的父节点之后
- `before `- 添加到匹配的节点的父节点之前
- `attributes` - 继承的内容是一系列拥有name属性的attribute 元素，且有可选的内容主体
   1.如果attribute有内容主体，就在匹配的节点上添加以name命名的、以内容主体为值的属性
   2.如果attribute没有内容主体，就将匹配节点上名字为name的属性删除，如果没有对应的属性，抛出一个错误

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

## 列表视图

列表视图的根元素是`<tree>`,它可以有以下几种属性：

### editable

默认情况下选择单行记录时会打开对应记录的表单，该属性让数据可以在列表内进行编辑，有效的值是top和bottom，可让新的记录出现在列表的顶部或底部

### default_order

重定义视图的排序规则，以逗号分隔多个字段，可使用desc来进行倒序

```xml
<tree default_order="sequence,name desc">
```

### decoration-{$name}

允许基于相应记录的属性更改行文本的样式。

值是Python表达式。对于每个记录，表达式都使用记录的属性作为上下文值进行计算，如果为真，则将相应的样式应用于行。其他上下文值是uid(当前用户的id)和current_date(当前日期作为yyyy-MM-dd格式的字符串)。

``{$name}` 可为 `bf` (`font-weight: bold`), `it` (`font-style: italic`),或其他 bootstrap样式如(`danger`, `info`, `muted`, `primary`, `success` or `warning`).

### create, edit, delete

可以通过将它们设置为false来禁用视图中的对应操作

### on_write

只当启用editable时有用，在调用时会传给函数新增或修改后的记录，该函数需要返回一个用于更新列表的记录id列表

### button

在一个列表单元格中显示按钮

>**属性列表：**
>
>1. `icon` -- 用来展示按钮的图标
>2. `string` -- 当没有icon的时候，button显示的文字，有icon的时候、相当于alt属性值
>3. `type` -- 按钮类型，表示点击它之后如何影响系统
>
>>1)`workflow`（默认）：将按钮name作为信号发送给工作流，记录的内容作为参数
>> 2)`object `： 调用当前数据列表模型的方法，方法名是按钮的name，调用时带有记录id和当前上下文环境
>> 3)`action` ： 加载ir.actions，按钮name是该action在数据库的id，上下文环境扩展到列表的model(作为active_model)、当前记录(active_id)、所有当前加载记录的id(active_ids)
>
>4. `name`,`args` 与type一样
>5. `attrs` 基于记录值的动态属性，将domain表达式应用在记录上，当返回值为True的时候设置相应的属性，一般用于invisible （隐藏按钮）、readonly （禁用按钮但显示）这两种属性
>6. `states`   `invisible`属性的简写，`attrs`给出一个以逗号分隔的state列表，需要模型有一个对应的state属性，可以将不在state列表中的记录的按钮隐藏
>7. context` 当响应odoo的调用时，合并到视图的上下文环境中
>8. confirm` 当点击按钮时给出的确认消息

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
>6. `sum`, `avg` 在底部显示基于当前页面数据的计算
>7. `attrs` 基于记录值的动态属性，只对当前栏有效，即可以第一条记录中该字段显示，第二条隐藏

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



## 表单

表单视图用于展示单条数据，根元素是form，由常规html和构造部分、语义部分组成

### 构造部分

构造部分提供了结构和可视特性，以元素或者元素的子元素的形式应用到表单视图的元素中

#### notebook

定义一个tab块，每一个tab通过一个page子元素定义，每个page可以有以下属性：

- string (required) --tab标签的名称
- accesskey --html accesskey
- attrs --基于记录值的动态属性

#### group

用于定义栏目在表单中布局，默认情况下一个group定义两个列，并且每个最直接的子元素占用一个列，field类型的元素默认显示一个标签
 group占用的列数是可以通过col属性自定义的，默认2个；其他元素可以通过**colspan**属性来定义占的列数，子元素是横向布局的，可以通过设置string 属性来定义group所展示的标题

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

>`special`
>
>对于对话框中打开的窗体视图:保存以保存记录并关闭对话框，取消以不保存而关闭对话框。

#### field

展示当前记录的某个字段，有以下属性：
- `name` (必选) -- 用于展示字段名
- `widget` -- 每个字段根据其数据类型有一个默认的展示方式，widget属性可指定用一个别的方式来展示
- `options` -- 用于指定widget字段配置的json对象
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
- `group_create`--“添加新列”栏是否可见。默认值:真的。
- `group_delete`--是否可以通过上下文菜单删除组。默认值:真的。
- `group_edit`--是否可以通过上下文菜单编辑组。默认值:真的。
- `archivable`--如果在模型上定义了activefield，是否可以存档/恢复属于列的记录。默认值:真的。
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

  - `field` (强制性)

  用于计算聚合的字段名。可能的字段类型有:

  > `integer` (默认的组操作符是sum)
  >
  > `float` (默认的组操作符是sum)
  >
  > `many2one` (默认的组操作符是count distinct)

  

  - `name` **(强制性)**

  - `string` (optional)

    A short description that will be displayed above the value. If not given, it will fall back to the field string.

  - `domain` (optional)

    An additional restriction on the set of records that we want to aggregate. This domain will be combined with the current domain.

  - `domain_label` (optional)

    When the user clicks on an aggregate with a domain, it will be added to the search view as a facet. The string displayed for this facet can be customized with this attribute.

  - `group_operator` (optional)

    A valid postgreSQL aggregate function identifier to use whn aggregating values (see <https://www.postgresql.org/docs/9.5/static/functions-aggregate.html>). If not provided, By default, the group_operator from the field definition is used. Note that no aggregation of field values is achieved if the group_operator value is “”.

    The special aggregate function `count_distinct` (defined in odoo) can also be used here

    ```xml
    <aggregate name="price_total_max" field="price_total" group_operator="max"/>
    ```
    
  - `col` (optional)--由此标记张成的列数(仅在组中有意义)。默认情况下,1。
  
  - `widget` (optional)--格式化值的小部件(类似于字段的小部件属性)。例如,货币。
  
  - `help` (optional)--工具提示中dipkill的帮助消息(相当于python中字段的帮助)
  
  - `measure` (optional)--此属性是描述在单击聚合时必须在图和轴心视图中使用的度量的字段的名称。特殊值_count__可用于计数测度。
  
    ```xml
    <aggregate name="total_ojects" string="Total Objects" field="id" group_operator="count" measure="count"/>
    ```
  
  - `clickable` (optional)--一个布尔值，指示这个聚合是否应该单击(默认为true)。单击可单击聚合将更改子视图使用的度量，并将域属性的值(如果有的话)添加到搜索视图。
  - `value_label` (optional)--放在聚合值右侧的字符串。例如，指示聚合值的度量单位可能很有用。

- `formula`

  声明派生值。公式是由聚合计算得到的值。

  注意，与聚合类似，公式也应该在组标记中使用(否则样式将无法正确应用)。









- `widget`

  Declares a specialized widget to be used to display the information. This is a mechanism similar to the widgets in the form view.Admissible attributes are:`name` (mandatory)A string to identify which widget should be instantiated. The view will look into the `widget_registry` to get the proper class.`col` (optional)The number of columns spanned by this tag (only makes sense inside a group). By default, 1.



## Cohort

The cohort view is used to display and understand the way some data changes over a period of time. For example, imagine that for a given business, clients can subscribe to some service. The cohort view can then display the total number of subscriptions each month, and study the rate at which client leave the service (churn). When clicking on a cell, the cohort view will redirect you to a new action in which you will only see the records contained in the cell’s time interval; this action contains a list view and a form view.

### Warning

The Cohort view is only available in Odoo Enterprise.

By default the cohort view will use the same list and form views as those defined on the action. You can pass a list view and a form view to the context of the action in order to set/override the views that will be used (the context keys to use being `form_view_id` and `list_view_id`)

For example, here is a very simple cohort view:

```
<cohort string="Subscription" date_start="date_start" date_stop="date" interval="month"/>
```

The root element of the Cohort view is <cohort>, it accepts the following attributes:

- - `string` (mandatory)

    A title, which should describe the view

- - `date_start` (mandatory)

    A valid date or datetime field. This field is understood by the view as the beginning date of a record

- - `date_stop` (mandatory)

    A valid date or datetime field. This field is understood by the view as the end date of a record. This is the field that will determine the churn.

- - `mode` (optional)

    A string to describe the mode. It should be either ‘churn’ or ‘retention’ (default). Churn mode will start at 0% and accumulate over time whereas retention will start at 100% and decrease over time.

- - `timeline` (optional)

    A string to describe the timeline. It should be either ‘backward’ or ‘forward’ (default). Forward timeline will display data from date_start to date_stop, whereas backward timeline will display data from date_stop to date_start (when the date_start is in future / greater than date_stop).

- - `interval` (optional)

    A string to describe a time interval. It should be ‘day’, ‘week’, ‘month’’ (default) or ‘year’.

- - `measure` (optional)

    A field that can be aggregated. This field will be used to compute the values for each cell. If not set, the cohort view will count the number of occurrences.



## Activity

The Activity view is used to display the activities linked to the records. The data are displayed in a chart with the records forming the rows and the activity types the columns. When clicking on a cell, a detailed description of all activities of the same type for the record is displayed.

### Warning

The Activity view is only available when the `mail` module is installed, and for the models that inherit from the `mail.activity.mixin`.

For example, here is a very simple Activity view:

```
<activity string="Activities"/>
```

The root element of the Activity view is <activity>, it accepts the following attributes:

- - `string` (mandatory)

    A title, which should describe the view



## Search

Search views are a break from previous view types in that they don’t display*content*: although they apply to a specific model, they are used to filter other view’s content (generally aggregated views e.g. [Lists](https://www.odoo.com/documentation/12.0/reference/views.html#reference-views-list) or [Graphs](https://www.odoo.com/documentation/12.0/reference/views.html#reference-views-graph)). Beyond that difference in use case, they are defined the same way.

The root element of search views is `<search>`. It takes no attributes.

Possible children elements of the search view are:

- `field`

  fields define domains or contexts with user-provided values. When search domains are generated, field domains are composed with one another and with filters using **AND**.Fields can have the following attributes:`name`the name of the field to filter on`string`the field’s label`operator`by default, fields generate domains of the form `[(*name*, *operator*,*provided_value*)]` where `name` is the field’s name and `provided_value` is the value provided by the user, possibly filtered or transformed (e.g. a user is expected to provide the *label* of a selection field’s value, not the value itself).The `operator` attribute allows overriding the default operator, which depends on the field’s type (e.g. `=` for float fields but `ilike` for char fields)`filter_domain`complete domain to use as the field’s search domain, can use a `self` variable to inject the provided value in the custom domain. Can be used to generate significantly more flexible domains than `operator` alone (e.g. searches on multiple fields at once)If both `operator` and `filter_domain` are provided, `filter_domain` takes precedence.`context`allows adding context keys, including the user-provided value (which as for `domain` is available as a `self` variable). By default, fields don’t generate domains.the domain and context are inclusive and both are generated if a `context` is specified. To only generate context values, set `filter_domain` to an empty list: `filter_domain="[]"``groups`make the field only available to specific users`widget`use specific search widget for the field (the only use case in standard Odoo 8.0 is a `selection` widget for [`Many2one`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Many2one) fields)`domain`if the field can provide an auto-completion (e.g. [`Many2one`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Many2one)), filters the possible completion results.

- `filter`

  a filter is a predefined toggle in the search view, it can only be enabled or disabled. Its main purposes are to add data to the search context (the context passed to the data view for searching/filtering), or to append new sections to the search filter.Filters can have the following attributes:`string` (required)the label of the filter`domain` (optional)an Odoo [domain](https://www.odoo.com/documentation/12.0/reference/orm.html#reference-orm-domains), will be appended to the action’s domain as part of the search domain.`date` (optional)the name of a field of type `date` or `datetime`. Using this attribute has the effect to create a set of filters available in a submenu of the filters menu.Example:`<filter name="filter_create_date" date="create_date" string="Creation Date"/> `The example above allows to easily search for records with creation date field values in one of the periods below.`Create Date >   Today   This Week   This Month   This Quarter   This Year --------------   Yesterday   Last Week   Last Month   Last Quarter   Last Year --------------   Last 7 Days   Last 30 Days   Last 365 Days `Note that the generated domains are dynamic and can be saved as such (via the favorites menu).`default_period` (optional)only makes sense for a filter with non empty `date` attribute. determines which period is activated if the filter is in the default set of filters activated at the view initialization. If not provided, ‘this_month’ is used by default.To choose among the following options: today, this_week, this_month, this_quarter, this_year, yesterday, last_week, last_month, last_quarter, last_year, last_7_days, last_30_days, last_365_daysExample:`<filter name="filter_create_date" date="create_date" string="Creation Date" default_period="this_week"/> ``context`a Python dictionary, merged into the action’s domain to generate the search domainThe key `group_by` can be used to define a groupby available in the ‘Group By’ menu. The ‘group_by’ value can be a valid field name or a list of field names.`<filter name="groupby_category" string="Category" context = {'group_by': 'category_id'}/> `The groupby defined above allows to group data by category.When the field is of type `date` or `datetime`, the filter generates a submenu of the Group By menu in which the following interval options are available: day, week, month, quarter, year.In case the filter is in the default set of filters activated at the view initialization, the records are grouped by month by default. This can be changed by using the syntax ‘date_field:interval’ as in the following example.Example:`<filter name="groupby_create_date" string="Creation Date" context = {'group_by': 'create_date:week'}/> ``name`logical name for the filter, can be used to [enable it by default](https://www.odoo.com/documentation/12.0/reference/views.html#reference-views-search-defaults), can also be used as [inheritance hook](https://www.odoo.com/documentation/12.0/reference/views.html#reference-views-inheritance)`help`a longer explanatory text for the filter, may be displayed as a tooltip`groups`makes a filter only available to specific usersNew in version 7.0.Sequences of filters (without non-filters separating them) are treated as inclusively composited: they will be composed with `OR` rather than the usual `AND`, e.g.`<filter domain="[('state', '=', 'draft')]"/> <filter domain="[('state', '=', 'done')]"/> `if both filters are selected, will select the records whose `state` is `draft` or `done`, but`<filter domain="[('state', '=', 'draft')]"/> <separator/> <filter domain="[('delay', '<', 15)]"/> `if both filters are selected, will select the records whose `state` is `draft` **and** `delay` is below 15.

- `separator`

  can be used to separates groups of filters in simple search views

- `group`

  can be used to separate groups of filters, more readable than `separator` in complex search views



### Search defaults

Search fields and filters can be configured through the action’s `context` using `search_default_*name*` keys. For fields, the value should be the value to set in the field, for filters it’s a boolean value. For instance, assuming `foo` is a field and `bar` is a filter an action context of:

```
{
  'search_default_foo': 'acro',
  'search_default_bar': 1
}
```

will automatically enable the `bar` filter and search the `foo` field for *acro*.









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











## 视图

- 菜单视图：把   数据模型—— 菜单 —— 视图（tree、form）连接起来

- 表单视图：创建、编辑数据模型所用视图。

- 列表视图：展示数据模型（显示数据）时使用。

- 搜索视图：制定odoo右上角对于当前数据模型的可搜索字段以及可用过滤器。




## 菜单视图

在定义了数据模型之后，我们要操作该模型。就需要把模型——菜单——视图 连接起来。这可以通过act_window+menuitem来实现。

<act_window>元素定义了一个客户端窗口动作，该动作将以列表和表单视图的顺序打开todo.task模型.

 <menuitem>定义了一个顶级菜单项，调用前面定义的action_todo_task动作。

两个元素都包含了id属性。 此id属性也称为XML ID，它用于唯一标识模块内的每个数据元素，并且可以由其他元素使用来引用它。

```
<!-- 视图动作 -->
<act_window id="action_qingjia_qingjiadan"  //该标签的id
               name="请假单"    //视图名
               res_model="qingjia.qingjiadan"  //视图要操作哪个数据模型：模块.数据模型
               view_mode="tree,form" />   //依次用什么视图来打开这个数据模型

<!-- 顶级菜单 -->
<menuitem name="请假" id="menu_qingjia"/> //顶级菜单：出现在导航栏上

<!-- 二级菜单 -->  //二级菜单：点击顶级菜单跳转到请假模块后，出现在左侧边栏。
<menuitem name="请假单" id="menu_qingjia_qingjiadan" parent="menu_qingjia" action="action_qingjia_qingjiadan"/>  //指定菜单的响应动作：依次用什么视图来操作数据模型
```

最后，把视图文件所在路径注册到manifest的data中：

 'data': [
        'views/views.xml',  //注意：路径要全。
    ],
2）表单视图

 所有的视图都存储在数据库中。我们在XML文件中声明一个描述视图的<record>元素，该模块在安装模块时将被加载到数据库中。

<record id="view_form_模块名" model="ir.ui.view"> 
   <field name="name">表单名</field> 
   <field name="model">数据模型（模块.模型）</field> 
   <field name="arch" type="xml"> //重点：视图类型定义 
     <form> 
       <group> //表单中一列
         <field name="name"/> //字段为数据模型中的字段内容
         <field name="is_done"/> 
         <field name="active"/> 
       </group> 
     </form> 
   </field> 
 </record> 
业务凭证窗体视图（仿纸页风格）

此表单包含两个元素：<header>包含操作按钮，<sheet>包含数据字段。

Form视图可以添加按钮以完成特定动作。这些按钮可以打开一个新的包含Form表单的窗口或运行定义在模块中的Python函数。

它们可以定义在Form视图内的任意位置，但是对于文档形式的窗体，建议把它们放在<header>标签中。

```
   <form>
      <header> //操作按钮所在区域
        <button name="按钮响应事件（定义在数据模型中）" type="动作的类型（执行的操作）" string="按钮显示文本" class="按钮样式" />
      </header>
      <sheet> //数据字段操作区域
        <group name="group_top" string="请假单"> 
          <field name="name"/> //数据模型中的字段们
          <field name="days"/>
          <field name="startdate"/>
          <field name="reason"/>
        </group>
      </sheet>
    </form>
```

group标签（相当于div）

<group>标签允许组织Form表单里的内容。在<group>中放置<group>，可以创建一个两列的列表。Group标签使用时，建议定义它的name属性，这样可以更方便的让其它模块扩展它或者用于标识该列内容的显示位置。

使用group方便地安排内容的分布显示：

   <sheet>
       <group name="group_top">
           <group name="group_left">//左边列
               <field name="name"/>
           </group>
           <group name="group_right">//右边列
               <field name="is_done"/>
               <field name="active" readonly="1"/>
           </group>
       </group>
   </sheet>
所以一个完整的form视图如下：

```
<form>
       <header>//操作按钮区域
           <button name="数据模型中定义的按钮事件" type="操作类型" string="按钮显示文本" class="按钮样式" />
       </header>
       <sheet>//数据字段区域
           <group name="group_top">//使用group进行布局
               <group name="group_left">
                   <field name="name"/>
               </group>
               <group name="group_right">
                   <field name="is_done"/>
                   <field name="active" readonly="1" />
               </group>
           </group>
       </sheet>
   </form>
```




Tab 分页效果：notebook标签

<form>
        ......
        <notebook>
            <page string="页名">
                <field name="显示内容" nolabel="页号"/>
            </page>
        </notebook>
</form>

3）列表视图

查看模型时，将使用<tree>视图。 树视图能够显示按层级结构组织的行，但大多数时候，它们用于显示简单列表。

<record id="view_tree_数据模型名" model="ir.ui.view"> 
 <field name="name">列表名</field> 
 <field name="model">模块.数据模型</field> 
 <field name="arch" type="xml"> //指明视图类型
   <tree colors="可以指明下面字段值为何值时，对应行使用什么背景颜色（这是通过bootstrap来实现的）"> 
     <field name="字段.."/> 
     <field name="字段.."/> 
   </tree> 
 </field> 
</record>
4）搜索视图

在列表的右上角，Odoo显示一个搜索框。 它搜索的字段和可用的过滤器是由<search>视图定义的。

<record id="view_filter_数据模型名" model="ir.ui.view"> 
 <field name="name">过滤器名</field> 
 <field name="model">模块.数据模型</field> 
 <field name="arch" type="xml"> //视图类型 
   <search>  //搜索视图定义
     <field name="可搜索字段"/>  //可搜索字段定义
     <filter string="过滤条件名"  domain="[('字段','操作符',值)]"/>  //过滤条件定义
   </search> 
 </field> 
</record> 

https://blog.csdn.net/miantian180/article/details/81698120