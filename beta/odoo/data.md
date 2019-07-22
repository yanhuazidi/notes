[TOC]



odoo是一个很大的数据驱动的系统，模块定义的很大一部分就是它所管理的各种记录的定义：用户界面（菜单和视图）、安全性（访问权限和访问规则）、报表和普通数据都是通过记录来定义的。



## 结构

在odoo中定义数据的主要方法是通过XML数据文件：XML数据文件的广泛结构如下：

根元素odoo中任意数量的操作元素:

```xml
<!-- the root elements of the data file -->
<odoo>
	<data noupdate="1">
        <!-- noupdate="1" 只创建记录，存在则不更新-->
        <!-- noupdate="0" 模块升级时更新记录-->
        <record id="action_client_pos_menu" model="ir.actions.client">
            <field name="name">Open POS Menu</field>
            <field name="tag">reload</field>
            <field name="params" eval="{'menu_id': ref('menu_point_root')}"/>
        </record>
	</data>
</odoo>
```

**数据文件按顺序执行，操作只能引用前面定义的操作结果**





## 核心操作

### `record`

`record` 适当地定义或更新数据库记录

它具有以下属性：

- `model` **(required)**	--要创建（或更新）的模型的名称
- `id`   此记录的外部标识符。强烈建议提供一个
  - 对于记录创建，允许后续定义修改或引用此记录
  - 对于记录修改，要修改的记录

- `context `    创建记录时要使用的上下文

- `forcecreate`在更新模式下，如果记录不存在，是否应创建它,需要外部ID，默认为true。



### `field`

每个记录可以由`field` 标记组成，定义创建记录时要设置的值。没有`field`的`record`将使用所有默认值（创建）或不执行任何操作（更新）。

`field`具有强制的`name` 属性、要设置的字段的名称以及定义值本身的各种方法：

如果没有为字段提供值，则将在字段上设置隐式false。可用于清除字段，或避免使用字段的默认值。

- `search`对于关系字段，应该是字段模型上的域。

  将评估域，使用该域的模型搜索该域，并将搜索结果设置为该域的值。仅当字段为`Many2one`时使用第一个结果

  ```xml
  <field search="[('code','=','PL')]" model='res.country' name='country_id'/> 
  <field name="journal_id" model="account.journal" search="[
                  ('type', '=', 'bank'),
                  ('company_id', '=', obj().env['res.company']._company_default_get('account.journal').id)]"/>
  ```

- `ref`如果提供了ref属性，则其值必须是有效的外部ID，该ID将被查找并设置为字段的值。

  主要用于Many2one和Reference字段

  ```xml
  <field name="categ_id" ref="point_of_sale.product_category_pos"/>
  <field name="uom_id" ref="uom.product_uom_unit"/>
  ```

- `type`

  如果提供了`type`属性，则用于解释和转换字段的内容。字段的内容可以通过使用文件属性的外部`file` 属性提供，也可以通过节点的主体提供

  可用类型包括：

  - `xml`**,** `html`

    将字段的子级提取为单个文档，计算用形式`%（external_id）s`指定的任何外部ID。可以使用.%来输出实际的%符号。

  - `file`

    确保字段内容是当前模型中的有效文件路径，并将pair模块path保存为字段值

  - `char`

    直接将字段内容设置为字段的值，而不进行更改

  - `base64`

    base64对字段内容进行编码，与`file`属性结合使用可将图像数据加载到附件中。

    ```xml
    <field name="image" type="base64" file="point_of_sale/static/img/product_product_49-image.jpg"/>
    ```

  - `int`

    将字段的内容转换为整数并将其设置为字段的值

  - `float`

    将字段的内容转换为float并将其设置为字段的值

  - `list`**,** `tuple`

    应包含任意数量的与字段属性相同的值元素，每个元素解析为生成的元组或列表的项，生成的集合设置为字段的值。

- `eval`

  对于前面的方法不适用的情况，eval属性只评估提供的任何python表达式，并将结果设置为字段的值。

  评估上下文包含各种模块（`time`, `datetime`, `timedelta`, `relativedelta`）、用于解析外部标识符（`ref`）的函数以及当前字段的模型对象（如果适用）（`obj`）

```xml
<field name="date" eval="time.strftime('%Y')+'-01-01'"/>
<field name="name" eval="'BNK/%s/0001' % time.strftime('%Y')"/>
<field name="payment_icon_ids" eval="[(6,0,[ref('website_payment_alipay.payment_icon_cc_alipay')])]"/>

```



### `delete`

 `delete` 标记可以删除以前定义的任何数量的记录。它具有以下属性：

- `model` **(required)**

  应在其中删除指定记录的模型

- `id ` 要删除的记录的外部ID

- `search`要查找要删除的模型记录的域

`id` 和`search`是只填一个的



### `function`

`function`标记使用提供的参数调用模型上的方法。它有两个强制参数`model`和`name`，分别指定要调用的方法的模型和名称。

可以使用`eval`（应计算为调用方法的参数序列）或`value`元素（请参见`list`值）提供参数。



## 快捷方式

由于odoo的一些重要结构模型很复杂且涉及到，数据文件提供了使用记录标记定义它们的较短替代方法：

### `menuitem`

定义具有多个默认值和回退的ir.ui.menu记录：

#### 父菜单

- 如果设置了`parent`属性，则它应该是其他菜单项的外部ID，用作新项的父项
- 如果没有提供`parent`，则尝试将name属性解释为一个/分隔的菜单名称序列，并在菜单层次结构中找到一个位置。在这种解释中，中间菜单是自动创建的
- 否则，菜单被定义为“顶级”菜单项（不是没有父菜单的菜单）

#### 菜单名称

如果未指定`name`属性，则尝试从链接操作（如果有）中获取菜单名称。否则使用记录的ID

#### 组

`groups`属性被解释为`res.groups`模型外部标识符的逗号分隔序列。如果外部标识符的前缀是减号（-），则该组将从菜单的组中删除。

#### `action`  

如果指定，则action属性应为打开菜单时要执行的操作的外部ID。

#### `id`

菜单项的外部ID



### `template`

创建仅需要视图的 `arch` 部分并允许一些可选属性的QWeb视图：

- `id`视图的外部标识符

- `name`**,** `inherit_id`**,** `priority`

  与`ir.ui.view`上的相应字段相同（注意：`inherit_id`应为外部标识符）

- `primary`

  如果设置为`true`并与`inherit_id`组合，则将视图定义为主视图

- `groups`

  以逗号分隔的组外部标识符列表

- `page`

  如果设置为"True"，模板是一个网站页面（可链接到，可删除）

- `optional`

  已启用`enabled` 或已禁用`disabled`，视图是否可以禁用（在网站界面中）及其默认状态。如果不设置，则始终启用视图。



### `report`

用几个默认值创建一个`ir.actions.report`记录。

大多数情况下，只将属性代理到`ir.actions.report`上的相应字段，但也会自动在报表模型的“更多”菜单中创建该项。



## CSV数据文件

XML数据文件具有灵活性和自描述性，但在批量创建同一模型的多个简单记录时非常冗长。

对于这种情况，数据文件也可以使用csv，这通常是访问权限的情况：

- 文件名为`model_name.csv`
- 第一行列出要写入的字段，外部标识符的特殊字段ID（用于创建或更新）
- 此后每行都创建一个新记录

以下是定义us states `res.country.state.csv`的数据文件的第一行

```
"id","country_id:id","name","code"
state_au_1,au,"Australian Capital Territory","ACT"
state_au_2,au,"New South Wales","NSW"
state_au_3,au,"Northern Territory","NT"
state_au_4,au,"Queensland","QLD"
state_au_5,au,"South Australia","SA"
state_au_6,au,"Tasmania","TAS"
state_au_7,au,"Victoria","VIC"
state_au_8,au,"Western Australia","WA"
state_us_1,us,"Alabama","AL"
state_us_2,us,"Alaska","AK"
state_us_3,us,"Arizona","AZ"
state_us_4,us,"Arkansas","AR"
state_us_5,us,"California","CA"
state_us_6,us,"Colorado","CO"
```

对于每一行（记录）：

- 第一列是要创建或更新的记录的外部ID
- 第二列是要链接到的Country对象的外部ID（Country对象必须事先定义）
- 第三列是res.country.state的名称字段
- 第四列是res.country.state的代码字段