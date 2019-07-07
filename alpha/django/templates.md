[TOC]



## Django模板语言

## Templates

模板只是一个文本文件。它可以生成任何基于文本的格式（HTML、XML、CSV等）

模板包含变量（在评估模板时用值替换）和标记（控制模板的逻辑）。

```html
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}
```



## 变量

变量如下：**{{** **variable** **}}**

当模板引擎遇到变量时，它将评估该变量并用结果替换它。变量名由字母数字字符和下划线（“_”）的任意组合组成，但不能以下划线开头。点（“.”）也出现在变量部分，尽管它有特殊的含义，如下所示。重要的是，变量名中不能有空格或标点符号。

使用点（.）访问变量的属性。

从技术上讲，当模板系统遇到一个点时，它会按以下顺序尝试查找：

- 词典查找

- 属性或方法查找

- 数字索引查找

如果结果值是可调用的，则不使用参数调用它。调用的结果将成为模板值。

此查找顺序可能会导致覆盖字典查找的对象出现一些意外行为。例如，考虑以下代码段，这些代码段试图循环访问collections.defaultdict：

```
{% for k, v in defaultdict.items %}
    Do something with k and v here...
{% endfor %}
```

因为字典查找首先发生，所以该行为开始并提供默认值，而不是使用预期的.items（）方法。在这种情况下，首先考虑转换为字典。

在上面的示例中，**{{** **section.title** **}}**将替换为section对象的title属性。

如果使用不存在的变量，模板系统将插入`string_if_invalid` 选项的值，默认情况下该选项设置为“ ”（空字符串）。

请注意，**{{** **foo.bar** **}}**等模板表达式中的“bar”将被解释为文本字符串，如果模板上下文中存在变量“bar”，则不使用变量“bar”的值。

不能访问以下划线开头的变量属性，因为它们通常被视为私有属性。



## 过滤器

您可以使用过滤器修改要显示的变量。

过滤器如下：`{{ name|lower }}`.。这将显示 `{{ name }}` 变量通过下面的过滤器过滤后的值，该过滤器将文本转换为小写。使用管道 (`|`) 应用过滤器。

过滤器可以“链接”。一个过滤器的输出应用于下一个。{{ **text|escape|linebreaks** **}}**是用于转义文本内容，然后将换行符转换为<p>标记的常见习惯用法。

有些筛选器接受参数。筛选器参数如下所示：`{{ bio|truncatewords:30 }}`.。这将显示前面变量的前30个字。

包含空格的筛选参数必须引号括起来；例如，要用逗号和空格联接列表，必须使用**{{** **list|join:", " }}**。



Django提供了大约60个内置模板过滤器。您可以在内置的过滤器引用中阅读关于它们的所有信息。为了让您了解可用的内容，以下是一些更常用的模板过滤器：

`default`

如果变量为假或空，请使用给定的默认值。否则，使用变量的值。例如：

```
{{ value|default:"nothing" }}
```



`length`

返回值的长度。这对字符串和列表都有效。例如：

```
{{ value|length }}
```



`filesizeformat`

将值格式化为“可读”文件大小（即“13KB”、“4.1MB”、“102字节”等）。例如：

```
{{ value|filesizeformat }}
```

如果值为123456789，则输出将为117.7 MB。

同样，这些只是几个例子；有关完整列表，请参见内置过滤器参考。

您还可以创建自己的自定义模板过滤器；请参见自定义模板（template）的标签（tags）和过滤器（filters）。



## 标签

标签如下：**{%** **tag** **%}**。标记比变量更复杂：一些在输出中创建文本，一些通过执行循环或逻辑来控制流，还有一些将外部信息加载到模板中以供以后的变量使用。

Django提供了大约20个内置模板标签。您可以在内置的标记引用中阅读关于它们的所有信息。为了让您了解可用的标签，以下是一些更常用的标签：

### for

循环数组中的每个项，使该项在上下文变量中可用。例如，要显示运动员列表中提供的运动员列表，请执行以下操作：

```
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```

您可以通过`reversed`**{%** **for** **obj** **in** **list** **reversed** **%}**来反向循环一个列表。

如果需要循环遍历列表，可以将每个子列表中的值解包为单独的变量。例如，如果您的上下文包含一个被称为点的（x，y）坐标列表，则可以使用以下命令输出点列表：

```
{% for x, y in points %}
    There is a point at {{ x }},{{ y }}
{% endfor %}
```

如果需要访问字典中的项目，这也很有用。例如，如果上下文包含字典数据，则以下内容将显示字典的键和值：

```
{% for key, value in data.items %}
    {{ key }}: {{ value }}
{% endfor %}
```

请记住，对于点运算符，字典键查找优先于方法查找。因此，如果数据字典包含名为“items”的键，data.items将返回数据[“items”]，而不是data.items（）。如果要在模板中使用这些方法（项、值、键等），请避免添加类似字典方法的键。

for循环设置循环中可用的变量数：

| Variable              | Description                          |
| --------------------- | ------------------------------------ |
| `forloop.counter`     | 循环的当前迭代（1个索引）            |
| `forloop.counter0`    | 循环的当前迭代（0-索引）             |
| `forloop.revcounter`  | 循环结束时的迭代次数（1个索引）      |
| `forloop.revcounter0` | 循环结束时的迭代次数（0-索引）       |
| `forloop.first`       | 如果这是第一次通过循环               |
| `forloop.last`        | 如果这是最后一次通过循环，则为真     |
| `forloop.parentloop`  | 对于嵌套循环，这是围绕当前循环的循环 |



### for` ... `empty

for标记可以采用可选的`{% empty %}` 子句，如果给定的数组为空或找不到该子句，则会显示其文本：

```
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
```



### if

```
{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
```

```
{% if athlete_list|length > 1 %}
   Team: {% for athlete in athlete_list %} ... {% endfor %}
{% else %}
   Athlete: {{ athlete_list.0.name }}
{% endif %}
```

虽然上面的示例有效，但是请注意大多数模板过滤器都返回字符串，因此使用过滤器进行数学比较通常不会像您期望的那样有效。长度是一个例外。

在上面，如果运动员列表不为空，运动员数量将由运动员列表长度变量显示。



#### 布尔运算符

`if`标记可以使用`and`, `or` or `not`测试多个变量，或对给定变量求反：

```
{% if athlete_list and coach_list %}
    Both athletes and coaches are available.
{% endif %}

{% if not athlete_list %}
    There are no athletes.
{% endif %}

{% if athlete_list or coach_list %}
    There are some athletes or some coaches.
{% endif %}

{% if not athlete_list or coach_list %}
    There are no athletes or there are some coaches.
{% endif %}

{% if athlete_list and not coach_list %}
    There are some athletes and absolutely no coaches.
{% endif %}
```

允许在同一标记内同时使用和或子句，其优先级高于或，例如：

```
{% if athlete_list and coach_list or cheerleader_list %}
```

`if`标记中使用的实际括号是无效语法。如果需要它们指示优先级，则应使用嵌套的if标记。

`if`标记也可以使用运算符==，！=，<，>，<=，>=，in，not in，is，is not 

```
{% if somevar == "x" %}
  This appears if variable somevar equals the string "x"
{% endif %}
{% if somevar != "x" %}
  This appears if variable somevar does not equal the string "x",
  or if somevar is not found in the context
{% endif %}
{% if somevar < 100 %}
  This appears if variable somevar is less than 100.
{% endif %}
{% if "bc" in "abcdef" %}
  This appears since "bc" is a substring of "abcdef"
{% endif %}
{% if "hello" in greetings %}
  If greetings is a list or set, one element of which is the string
  "hello", this will appear.
{% endif %}
{% if user in users %}
  If users is a QuerySet, this will appear if user is an
  instance that belongs to the QuerySet.
{% endif %}
{% if somevar is True %}
  This appears if and only if somevar is True.
{% endif %}
{% if somevar is not True %}
  This appears if somevar is not True, or if somevar is not found in the
  context.
{% endif %}
```

也可以在if表达式中使用过滤器。例如：

```
{% if messages|length >= 100 %}
   You have lots of messages today!
{% endif %}
```

所有这些都可以组合成复杂的表达式。对于此类表达式，在计算表达式（即优先级规则）时，了解如何对运算符进行分组是很重要的。运算符的优先级从低到高如下：

- `or`
- `and`
- `not`
- `in`
- `==`, `!=`, `<`, `>`, `<=`, `>=`

（这完全遵循Python）。例如，下面的复杂if标记：

```
{% if a == b or c == d and e %}
```

如果需要不同的优先级，则需要使用嵌套的if标记。有时，为了那些不知道优先规则的人，这样做更清楚。

比较运算符不能像在python或数学符号中那样“链接”。例如，不要使用：

```
{% if a > b > c %}  (WRONG)
```

您应该使用：

```
{% if a > b and b > c %}
```



### include

加载模板并用当前上下文呈现。这是一种在模板中“包括”其他模板的方法。

```
{% include "foo/bar.html" %}
{% include template_name %}
```

可以使用关键字参数将其他上下文传递给模板：

```
{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
```

如果只想使用提供的变量（甚至根本没有变量）呈现上下文，请使用唯一的选项。所包含的模板没有其他可用变量：

```
{% include "name_snippet.html" with greeting="Hi" only %}
```

include标记应被视为“呈现此子模板并包含HTML”的实现，而不是“解析此子模板并将其内容包含为父模板的一部分”。这意味着包含的模板之间没有共享状态——每个包含都是一个完全独立的呈现过程。

在包含块之前对其进行评估。这意味着包含来自另一个的块的模板将包含已评估和呈现的块，而不是可被扩展模板（例如，扩展模板）覆盖的块。



### now

根据给定字符串使用格式显示当前日期和/或时间。这样的字符串可以包含格式说明符字符，如日期筛选部分所述。

```
It is {% now "jS F Y H:i" %}
```

请注意，如果要使用“原始”值，可以反斜杠转义格式字符串。在本例中，“o”和“f”都是反斜杠转义的，因为否则每一个都是分别显示年份和时间的格式字符串：

```
It is the {% now "jS \o\f F" %}
```



### url

返回与给定视图和可选参数匹配的绝对路径引用（没有域名的URL）。结果路径中的任何特殊字符都将使用iri_to_uri（）进行编码。

这是一种在不违反dry原则的情况下输出链接的方法，即在模板中硬编码URL：

```
{% url 'some-url-name' v1 v2 %}
```

第一个参数是URL模式名。它可以是带引号的文字或任何其他上下文变量。其他参数是可选的，应该是空格分隔的值，这些值将用作URL中的参数。上面的示例显示传递位置参数。或者，您可以使用关键字语法：

```
{% url 'some-url-name' arg1=v1 arg2=v2 %}
```

不要在单个调用中混合使用位置语法和关键字语法。urlconf所需的所有参数都应存在。

```
path('client/<int:id>/', app_views.client, name='app-views-client')
```

```
{% url 'app-views-client' client.id %}
```

…然后，在模板中，可以创建指向此视图的链接，如下所示：

```
{% url 'app-views-client' client.id %}
```

模板标记将输出字符串/clients/client/123/



如果要检索一个URL而不显示它，可以使用稍微不同的调用：

```
{% url 'some-url-name' arg arg2 as the_url %}

<a href="{{ the_url }}">I'm linking to {{ the_url }}</a>
```

**as** **var**语法创建的变量范围是**{%** **block** **%}**，其中出现`{% url %}` 标记。

此**{%** **url** **...** **as** **var** **%}**如果视图丢失，语法不会导致错误。在实践中，您将使用此链接到可选视图：

```
{% url 'some-url-name' as the_url %}
{% if the_url %}
  <a href="{{ the_url }}">Link to optional stuff</a>
{% endif %}
```

如果要检索命名空间URL，请指定完全限定名：

```
{% url 'myapp:view-name' %}
```

这将遵循正常的名称空间URL解析策略，包括使用上下文提供的关于当前应用程序的任何提示。

不要忘记在url模式名周围加引号，否则该值将被解释为上下文变量！



### block

```
<title>{% block title %}My amazing site{% endblock %}</title>
```



### extends

表示此模板扩展父模板。

此标记可通过两种方式使用：

- **{%** **extends** **"base.html"** **%}**（带引号）使用文字值“base.html”作为要扩展的父模板的名称。
- **{%** **extends** **variable** **%}**使用变量的值。如果变量的计算结果为字符串，Django将使用该字符串作为父模板的名称。如果变量的计算结果为模板对象，Django将使用该对象作为父模板。

通常，模板名是相对于模板加载器的根目录的。字符串参数也可以是以./或../开头的相对路径。例如，假设以下目录结构：

```
dir1/
    template.html
    base2.html
    my/
        base3.html
base1.html

在template.html中，以下路径有效：
{% extends "./base2.html" %}
{% extends "../base1.html" %}
{% extends "./my/base3.html" %}
{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
    <h2>{{ entry.title }}</h2>
    <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}
```



### autoescape

控制当前的自动转义行为。此标记接受开或关作为参数，并确定自动转义是否在块内有效。块用EndAutoEscape结束标记关闭。

当自动转义生效时，在将结果放入输出之前（但在应用了任何过滤器之后），所有变量内容都应用了HTML转义。这相当于手动对每个变量应用转义过滤器。

唯一的例外是那些已经被标记为“安全”的变量，它们不会被转义，要么被填充该变量的代码标记，要么因为它已经应用了安全或转义过滤器。

```
{% autoescape on %}
    {{ body }}
{% endautoescape %}
```



### comment

忽略`{% comment %}`  `{% endcomment %}`.之间的所有内容。可在第一个标记中插入可选注释。例如，在注释代码以记录代码被禁用的原因时，这很有用。

```
<p>Rendered text with {{ pub_date|date:"c" }}</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
```

注释标记不能嵌套。



### csrf_token

此标签用于CSRF保护，如跨站点请求伪造文档中所述。



### cycle

每次遇到此标记时都生成其参数之一。第一个'row1'是在第一次相遇时产生的，'row2' 第二次相遇时产生的，等等。一旦所有参数都用完了，标记就循环到第一个参数并再次生成它。

```
{% for o in some_list %}
    <tr class="{% cycle 'row1' 'row2' %}">
        ...
    </tr>
{% endfor %}
```

第一次迭代为循环的每次迭代生成引用类row1、第二次引用row2、第三次引用row1，依此类推。

你也可以使用变量。例如，如果有两个模板变量rowvalue1和rowvalue2，则可以在它们的值之间进行如下交替

```
{% for o in some_list %}
    <tr class="{% cycle rowvalue1 rowvalue2 %}">
        ...
    </tr>
{% endfor %}
```

循环中包含的变量将被转义。您可以使用以下命令禁用自动转义：

```
{% for o in some_list %}
    <tr class="{% autoescape off %}{% cycle rowvalue1 rowvalue2 %}{% endautoescape %}">
        ...
    </tr>
{% endfor %}
```

您可以混合变量和字符串：

```
{% for o in some_list %}
    <tr class="{% cycle 'row1' rowvalue2 'row3' %}">
        ...
    </tr>
{% endfor %}
```



在某些情况下，您可能希望引用循环的当前值，而不前进到下一个值。为此，只需给**{%** **cycle** **%}**标记一个名称，使用“as”，如下所示：

```
{% cycle 'row1' 'row2' as rowcolors %}
```

从那时起，您可以通过将循环名称作为上下文变量引用，在模板中任意位置插入循环的当前值。如果要将循环移动到与原始循环标记无关的下一个值，可以使用另一个循环标记并指定变量的名称。因此，以下模板：

```
<tr>
    <td class="{% cycle 'row1' 'row2' as rowcolors %}">...</td>
    <td class="{{ rowcolors }}">...</td>
</tr>
<tr>
    <td class="{% cycle rowcolors %}">...</td>
    <td class="{{ rowcolors }}">...</td>
</tr>
```

将输出：

```
<tr>
    <td class="row1">...</td>
    <td class="row1">...</td>
</tr>
<tr>
    <td class="row2">...</td>
    <td class="row2">...</td>
</tr>
```



### firstof

输出非假的第一个参数变量。如果所有传递的变量都为假，则不输出任何内容。

```
{% firstof var1 var2 var3 %}
```

如果所有传递的变量都为假，还可以使用文本字符串作为输出值：

```
{% firstof var1 var2 var3 "fallback value" %}
```

此标记自动转义变量值。您可以使用以下命令禁用自动转义：

```
{% autoescape off %}
    {% firstof var1 var2 var3 "<strong>fallback value</strong>" %}
{% endautoescape %}
```

或者，如果只应转义某些变量，则可以使用：

```
{% firstof var1 var2|safe var3 "<strong>fallback value</strong>"|safe %}
```

您可以使用语法**{%** **firstof** **var1** **var2** **var3** **as** **value** **%}**将输出存储在变量中。



### widthratio

对于创建条形图等，此标记计算给定值与最大值的比率，然后将该比率应用于常量。

```
<img src="bar.png" alt="Bar"
     height="10" width="{% widthratio this_value max_value max_width %}">
```

如果`this_value` 为175，最大_值为200，最大_宽度为100，则上述示例中的图像将为88像素宽（因为175/200=0.875；.875*100=87.5，四舍五入为88）。

在某些情况下，您可能希望捕获变量中widthraio的结果。例如，在这样的BlockTrans中，它可能很有用：

```
{% widthratio this_value max_value max_width as width %}
{% blocktrans %}The width is: {{ width }}{% endblocktrans %}
```



### static

要链接到保存在`STATIC_ROOT`Django中的静态文件，请使用静态模板标记。如果安装了django.contrib.staticfiles应用程序，则标记将使用staticfiles_storage指定的存储的url（）方法提供文件。例如：

```
{% load static %}
<link rel="stylesheet" href="{% static user_stylesheet %}" type="text/css" media="screen">
```

```
{% load static %}
<img src="{% static "images/hi.jpg" %}" alt="Hi!">
```

如果要检索静态URL而不显示它，可以使用稍微不同的调用：

```
{% load static %}
{% static "images/hi.jpg" as myphoto %}
<img src="{{ myphoto }}">
```



#### get_static_prefix

您应该更喜欢静态模板标记，但是如果您需要更多控制静态URL注入模板的确切位置和方式，可以使用get-static-prefix模板标记：

```
{% load static %}
<img src="{% get_static_prefix %}images/hi.jpg" alt="Hi!">
```

如果您多次需要该值，还可以使用第二个表单来避免额外的处理：

```
{% load static %}
{% get_static_prefix as STATIC_PREFIX %}

<img src="{{ STATIC_PREFIX }}images/hi.jpg" alt="Hi!">
<img src="{{ STATIC_PREFIX }}images/hi2.jpg" alt="Hello!">
```



#### get_media_prefix

与get_static_prefix类似，get_media_prefix使用media prefix media_url填充模板变量。

```
{% load static %}
<body data-media-url="{% get_media_prefix %}">
```

通过将值存储在一个数据属性中，我们可以确保如果要在JavaScript上下文中使用该值，可以对其进行适当的转义。







## Built-in filter reference

### add

```
{{ value|add:"2" }}
```

If `value` is `4`, then the output will be `6`.

此筛选器将首先尝试将两个值强制为整数。如果失败，它将尝试将这些值相加。这将在某些数据类型（字符串、列表等）上工作，而在其他数据类型上失败。如果失败，结果将是一个空字符串。

```
{{ first|add:second }}
```

and `first` is `[1, 2, 3]` and `second` is `[4, 5, 6]`, then the output will be `[1, 2, 3, 4, 5, 6]`.

可以强制为整数的字符串将被求和，而不是像上面的第一个示例中那样连接起来。



### capfirst

```
{{ value|capfirst }}
```

If `value` is `"django"`, the output will be `"Django"`.

将值的第一个字符大写。如果第一个字符不是字母，则此筛选器无效。



### center

```
"{{ value|center:"15" }}"
```

If `value` is `"Django"`, the output will be `"     Django    "`.

### ljust

```
"{{ value|ljust:"10" }}"
```

If `value` is `Django`, the output will be `"Django    "`.

### rjust



### cut

从给定字符串中删除arg的所有值。

```
{{ value|cut:" " }}
```

If `value` is `"String with spaces"`, the output will be `"Stringwithspaces"`.



### `date`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/templates/builtins/#date)

```
{{ value|date:"D d M Y" }}
```

the result of `datetime.datetime.now()`), the output will be the string `'Wed09 Jan 2008'`.



### join

```
{{ value|join:" // " }}
```

If `value` is the list `['a', 'b', 'c']`, the output will be the string `"a // b // c"`.



### linenumbers

```
{{ value|linenumbers }}
```

If `value` is:

```
one
two
three
```

the output will be:

```
1. one
2. two
3. three
```



### safe

将字符串标记为在输出前不需要进一步的HTML转义。当自动转义关闭时，此筛选器没有效果。



### slice

```
{{ some_list|slice:":2" }}
```

If `some_list` is `['a', 'b', 'c']`, the output will be `['a', 'b']`.



### time

```
{{ value|time:"H:i" }}
```

If `value` is equivalent to `datetime.datetime.now()`, the output will be the string `"01:23"`.



### title

```
{{ value|title }}
```

If `value` is `"my FIRST post"`, the output will be `"My First Post"`.



### truncatechars

```
{{ value|truncatechars:7 }}
```

If `value` is `"Joel is a slug"`, the output will be `"Joel i…"`.

### truncatechars_html

```
{{ value|truncatechars_html:7 }}
```

If `value` is `"<p>Joel is a slug</p>"`, the output will be `"<p>Joel i…</p>"`.

将保留HTML内容中的换行符。

### truncatewords

```
{{ value|truncatewords:2 }}
```

If `value` is `"Joel is a slug"`, the output will be `"Joel is …"`.

### truncatewords_html



### upper

```
{{ value|upper }}
```

If `value` is `"Joel is a slug"`, the output will be `"JOEL IS A SLUG"`.





