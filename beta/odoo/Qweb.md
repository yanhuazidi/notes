[TOC]



## 简介

- QWeb是被Odoo使用的主要的模版引擎。它是一个XML模板引擎，主要用于生成HTML片段和页面。

- 模板指令指定的XML属性的前缀 t-，例如t-if 为条件，与元素和其他属性被直接渲染。

  ```xml
  <p><t t-esc="value"/></p>
  ```

- 为了避免元素渲染，占位符元素<t>也可用，它执行指令，但本身并不会产生任何输出

  ```xml
  <t t-if="condition">
      <p>Test</p>
  </t>
  ```

  

## 数据输出

### t-esc="value"

它自动转义HTML，当显示用户提供的内容esc时，其内容限制XSS风险

esc 获取表达式，计算并打印内容

### t-raw="value"

行为与esc相同，但HTML没有转义输出。它可以显示分别标记有用（例如功能）或已消毒的用户提供的标记。



## 条件

### t-if="value"

它评估作为属性值的表达式,如果条件为`true`，则渲染元素.但如果条件为`false`，则从结果中删除

```xml
<div>
    <t t-if="condition">
        <p>ok</p>
    </t>
</div>
或
<div>
    <p t-if="condition">ok</p>
</div>
```

附加条件分支指令` t-elif` 和`t-else` 也是可用的

```xml
<div>
    <p t-if="user.birthday == today()">Happy birthday!</p>
    <p t-elif="user.login == 'root'">Welcome master!</p>
    <p t-else="">Welcome!</p>
</div>
```



## 循环

### t-foreach="[1, 2, 3]" t-as="i"

它获取返回集合迭代的表达式，第二参数`t-as`提供要使用的名称为“当前项”的迭代：

foreach 可以迭代数组（当前项将是当前值）、映射（当前项将是当前键）或整数（相当于迭代这包含0而不包含提供证书区间的数组上）。

`$as` 将被传递给t-as的名称替换 	如:   `i_all`,   `i_value`

**$as_all**

正在迭代的对象

**$as_value**

当前迭代值，对于列表和整数与$as相同的，但是对于映射它提供了一个值($as 提供键)

**$as_index**

当前迭代索引（迭代的第一项索引为0）

**$as_size**

集合的大小，如果可用的话

**$as_first**

当前项目是否是迭代的第一个项(相当于$as_index == 0)

**$as_last**

当前项目是否是迭代的最后一个(相当于 $as_index + 1 == $as_size)，要求迭代（如数组）大小是可用的

**$as_parity**

要么是"even" 要么是 "odd"，当前迭代循环的奇偶性

**$as_even**

指示当前迭代在偶数索引上的布尔标志

**$as_odd**

指示当前迭代在奇数索引上的布尔标志

这些提供的额外的变量和所有在foreach中创建的新变量，仅仅在`foreach`范围内是可用的。如果变量存在与`foreach`的上下文之外， 在`foreach`循环的最后，值将复制到全局上下文中。

```xml
<t t-set="existing_variable" t-value="False"/>
<!-- existing_variable now False -->

<p t-foreach="[1, 2, 3]" t-as="i">
    <t t-set="existing_variable" t-value="True"/>
    <t t-set="new_variable" t-value="True"/>
    <!-- existing_variable and new_variable now True -->
</p>

<!-- existing_variable always True -->
<!-- new_variable undefined -->
```



## 属性

QWeb可以在传输过程中计算属性并在设置输出节点上的计算结果。这是通过`t-att` (属性) 指令完成，它存在3种不同的形式：

### t-att-$name

一个叫 $name 的属性被创建，属性值被求值，结果被设置为属性值：

```xml
<div t-att-a="42"/>
<div a="42"></div>
```



### t-attf-$name

与`t-att-`相同，但参数是一个格式字符串，而不是表达式，通常用于混合文字和非文字字符串（例如类）：

```xml
<t t-foreach="[1, 2, 3]" t-as="item">
    <li t-attf-class="row {{ item_parity }}"><t t-esc="item"/></li>
</t>
```



### t-att=mapping

如果参数是一个映射，每个（key，value）对生成一个新属性及其值：

```xml
<div t-att="{'a': 1, 'b': 2}"/>
<div a="1" b="2"></div>
```



### t-att=pair

如果参数是一对（元组或2元素数组），这对的第一项是属性的名称，第二项是值：

```xml
<div t-att="['a', 'b']"/>
<div a="b"></div>
```



## 设置变量

QWeb允许从模板中创建变量，记忆计算(多次使用)，给数据块一个更清晰的名称，…

这是通过set指令完成的，该指令接受要创建的变量的名称。要设置的值可以通过两种方式提供:

包含表达式的`t-value`属性，其计算结果将被设置

```xml
<t t-set="foo" t-value="2 + 1"/>
<t t-esc="foo"/>
```

如果没有t-value属性，则渲染节点的body并将其设置为变量的值:

```xml
<t t-set="foo">
    <li>ok</li>
</t>
<t t-esc="foo"/>
```

将生成&lt;li&gt;ok&lt;/li&gt;(当我们使用esc指令时，内容被转义)

使用这个操作的结果是raw指令的一个重要用例。



## 调用sub-templates

QWeb模板可以用于顶层渲染，但也可以使用`t-call`指令从另一个模板中使用(以避免重复或给模板的部分命名):

```xml
<t t-call="other-template"/>
```

如果other_template定义为:

```xml
<p><t t-value="var"/></p>
```

上述调用将呈现为(无内容)，但是:

```xml
<t t-set="var" t-value="1"/>
<t t-call="other-template"/>
```

将呈现为`<p>1</p>`.



然而，这有一个从`t-call`外部可见的问题。或者，在调用子模板之前，将对call指令体中的内容集进行评估，并可以更改本地上下文:

```xml
<t t-call="other-template">
    <t t-set="var" t-value="1"/>
</t>
<!-- "var" does not exist here -->
```

call指令的主体可以是任意复杂的(不仅仅是set指令)，它的呈现形式可以在被调用的模板中作为一个神奇的0变量:

```xml
<div>
    This template was called with content:
    <t t-raw="0"/>
</div>
```

被称为:

```xml
<t t-call="other-template">
    <em>content</em>
</t>
```

将导致:

```xml
<div>
    This template was called with content:
    <em>content</em>
</div>
```





## Python

独家指令

资产组合

"智能记录  smart records"字段格式化

`t-field`指令只能在对“智能”记录(`browse`方法的结果)执行字段访问(a.b)时使用。它能够根据字段类型自动格式化，并集成在网站的富文本版本中。

`t-options`可用于自定义字段，最常见的选项是`widget`，其他选项依赖于 `field- `or `widget-dependent`.。



## 调试

### t-debug

使用PDB的set_trace API调用调试器。参数应该是模块的名称，在模块上调用set_trace方法:

```xml
<t t-debug="pdb"/>
```

是非常重要的	`importlib.import_module("pdb").set_trace()`



## 助手

#### Request-based

QWeb的大多数python端使用都在控制器中(以及HTTP请求期间)，在这种情况下，可以通过调用简单地呈现存储在数据库中的模板(作为视图[`odoo.http.HttpRequest.render()`](https://www.odoo.com/documentation/12.0/reference/http.html#odoo.http.HttpRequest.render):

```python
response = http.request.render('my-template', {
    'context_value': 42
})
```

这将自动创建一个响应对象，该对象可以从控制器返回(或进一步定制以适应)。



#### View-based

在比上一个助手更深的层次上，是ir.ui.view上的呈现方法：

```python
render(cr, uid, id[, values][, engine='ir.qweb'][, context])
#按数据库ID或外部ID呈现QWeb视图/模板。模板自动从ir.ui.view记录加载。
```

在渲染上下文中设置一些默认值:

`request`		当前WebRequest对象(如果有的话)

`debug`			当前请求(如果有)是否处于调试模式

[`quote_plus`](https://werkzeug.palletsprojects.com/en/0.15.x/urls/#werkzeug.urls.url_quote_plus)		url编码效用函数

[`json`](https://docs.python.org/3/library/json.html#module-json)			对应的标准库模块

[`time`](https://docs.python.org/3/library/time.html#module-time)				对应的标准库模块

[`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime)		对应的标准库模块

[relativedelta](https://labix.org/python-dateutil#head-ba5ffd4df8111d1b83fc194b97ebecf837add454)    参见模块

`keep_query`	keep_query帮助函数

参数:

- **values** – 要传递给QWeb进行呈现的上下文值
- **engine** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 要用于渲染的odoo模型的名称，可用于在本地扩展或自定义qweb（通过创建基于ir.qweb的“新”qweb，并进行修改）



## Javascript

独家指令

定义模板

`t-name`指令只能放在模板文件的顶层（将子级指向文档根目录）：

```xml
<templates>
    <t t-name="template-name">
        <!-- template code -->
    </t>
</templates>
```

它不需要其他参数，但可以与<t>元素或任何其他元素一起使用。对于<t>元素，<t>应该有一个子元素。

模板名称是一个任意字符串，尽管当多个模板相关时（例如，称为sub-templates），通常使用点分隔名称来表示层次关系。



## 模板继承

模板继承用于修改现有的模板，例如将信息添加到由其他模块创建的模板中。

模板继承是通过`t-extend`指令执行的，该指令接受要更改的模板的名称作为参数。

然后使用任意数量的`t-jquery`子指令执行修改:

```xml
<t t-extend="base.template">
    <t t-jquery="ul" t-operation="append">
        <li>new element</li>
    </t>
</t>
```

`t-jquery`指令接受一个CSS选择器。此选择器用于扩展模板，以选择应用指定`t-operation`的上下文节点:

`append`

节点的主体附加在上下文节点的末尾(在上下文节点的最后一个子节点之后)

`prepend`

节点的主体被前缀到上下文节点(插入到上下文节点的第一个子节点之前)

`before`

节点的主体正好插入到上下文节点之前

`after`

节点的主体被插入到上下文节点之后

`inner`

节点的主体替换上下文节点的子节点

`replace`

节点的主体用于替换上下文节点本身

**没有操作**

如果没有指定t-operation，则将模板体解释为javascript代码并使用上下文节点执行，如下所示

警告

虽然这种模式比其他操作强大得多，但调试和维护起来也要困难得多，建议避免使用这种模式



## 调试

javascript QWeb实现提供了一些调试挂钩:

`t-log`

获取表达式参数，在呈现过程中对表达式求值，并使用`console.log`记录其结果。

```xml
<t t-set="foo" t-value="42"/>
<t t-log="foo"/>
```

将打印42到控制台吗

`t-debug`

在模板呈现期间触发调试器断点:

```xml
<t t-if="a_test">
    <t t-debug="">
</t>
```

果调试处于活动状态，将停止执行(具体情况取决于浏览器及其开发工具)

`t-js`

节点的主体是在模板呈现期间执行的javascript代码。获取上下文参数，该参数是`t-js`主体中呈现上下文可用的名称:

```xml
<t t-set="foo" t-value="42"/>
<t t-js="ctx">
    console.log("Foo is", ctx.foo);
</t>
```



## 助手



`core.qweb`

(core 是`web.core` 模块)QWeb2.Engine()的一个实例,加载了所有模块定义的模板文件，以及对标准helper对象`_(underscore)`,`_t (translation function) `和JSON的引用。

`core.qweb.render`可以用来轻松渲染基本模块模板



### API

### class QWeb2.Engine()

QWeb“render”处理QWeb的大部分逻辑(加载、解析、编译和呈现模板)。

Odoo Web在核心模块中为用户实例化一个，并将其导出到core.qweb。它还将各个模块的所有模板文件加载到该QWeb实例中。

QWeb2.Engine()还充当“模板名称空间”。

QWeb2.Engine.render(模板(、上下文))

将先前加载的模板呈现为字符串，使用上下文(如果提供的话)查找模板呈现期间访问的变量(例如要显示的字符串)。

Arguments

- **template** (`String`) – 要呈现的模板的名称

- **context** (`Object`) – 用于模板呈现的基本名称空间

Returns	String

该引擎公开了另一种方法，在某些情况下可能有用(例如，如果你需要一个单独的模板名称空间，在Odoo Web中，看板视图会得到它们自己的QWeb2.Engine()实例，这样它们的模板就不会与更通用的“模块”模板发生冲突):

`QWeb2.Engine.add_template(templates)`

在QWeb实例中加载一个模板文件(模板的集合)。模板可以指定为:

**An XML string**

QWeb将尝试将其解析为XML文档，然后加载它。

**A URL**

QWeb将尝试下载URL内容，然后加载生成的XML字符串。

**A** `Document` **or** `Node`

QWeb将遍历文档的第一层(所提供根的子节点)并加载任何命名模板或模板覆盖。



**QWeb2.Engine()还为行为定制公开了各种属性:**

`QWeb2.Engine.prefix`

用于在解析过程中识别指令的前缀。一个字符串。默认情况下,t。

`QWeb2.Engine.debug`

布尔标志将引擎置于“调试模式”。通常，QWeb拦截模板执行过程中产生的任何错误。在调试模式下，它将保留所有异常，而不拦截它们

`QWeb2.Engine.jQuery`

模板继承处理期间使用的jQuery实例。默认为`window.jQuery`.

`QWeb2.Engine.preprocess_node`

一个函数。如果存在，则在将每个DOM节点编译为模板代码之前调用。在Odoo Web中，这用于自动翻译文本内容和模板中的一些属性。默认为空。

