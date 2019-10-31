[TOC]



本文介绍了odoo javascript框架。从代码行的角度来看，这个框架不是一个大的应用程序，但它是非常通用的，因为它基本上是一个将声明性接口描述转换为活动应用程序的机器，能够与数据库中的每个模型和记录交互。甚至可以使用Web客户端修改Web客户端的接口。

Odoo中所有DocStrings的HTML版本可从以下网址获得：

- [Javascript API](https://www.odoo.com/documentation/12.0/reference/javascript_api.html)



## 概述

JavaScript框架设计用于三个主要用例：

- Web客户机：这是一个私有的Web应用程序，可以在其中查看和编辑业务数据。这是一个单页应用程序（永远不会重新加载页面，只有在需要时才从服务器提取新数据）
- 网站：这是odoo的公共部分。它允许身份不明的用户作为客户机浏览某些内容、购物或执行许多操作。这是一个经典的网站：各种各样的带有控制器的路由和一些让它工作的javascript。
- 销售点：这是销售点的接口。它是一个专门的单页应用程序

一些JavaScript代码对于这三个用例来说是通用的，并且捆绑在一起（请参见下面的资产部分）。本文档主要关注Web客户端设计。



## Web client

### 单页应用程序

简而言之，webclient实例是整个用户界面的根组件。它的职责是协调所有的子组件，并提供服务，如RPC、本地存储等等。

在运行时，Web客户端是单页应用程序。每次用户执行操作时，它不需要从服务器请求整页。相反，它只请求它所需要的，然后替换/更新视图。此外，它还管理URL：它与Web客户机状态保持同步。

这意味着，当用户在处理odoo时，Web客户机类（和操作管理器）实际上创建并销毁了许多子组件。状态是高度动态的，每个小部件都可以随时销毁。



### Web客户端JS代码概述

这里，我们在web/static/src/js插件中快速概述了web客户机代码。请注意，这是故意不详尽的。我们只涉及最重要的文件/文件夹。

- boot.js：这是定义模块系统的文件。它需要先加载。
- core/：这是较低级别的构建基块的集合。值得注意的是，它包含类系统、小部件系统、并发实用程序和许多其他类/函数。
- chrome/：在这个文件夹中，我们有大多数大型小部件，它们构成了大部分用户界面。
- chrome/abstract_web_client.js和chrome/web_client.js：这些文件一起定义了webclient小部件，它是web客户端的根小部件。
- chrome/action_manager.js：这是将操作转换为小部件（例如看板或窗体视图）的代码。
- chrome/search_x.js所有这些文件都定义了搜索视图（它不是Web客户机视图中的视图，仅从服务器视图中）
- fields : 所有主视图字段小部件都在此处定义
- views: 这是视图所在的位置



## 资产管理Assets Management

在Odoo中管理资产并不像在其他应用程序中那样简单。其中一个原因是，我们有各种各样的情况，其中一些，但不是所有的资产都是必需的。例如，Web客户端、销售点、网站甚至移动应用程序的需求是不同的。此外，有些资产可能很大，但很少需要。在这种情况下，我们有时希望它们被懒惰地加载。

主要的想法是我们用XML定义一组包。捆绑包在这里定义为一组文件（javascript、css、scss）。在odoo中，最重要的包在addons/web/views/webclient_templates.xml文件中定义。看起来是这样的：

**addons/web/views/webclient_templates.xml**

```xml
<template id="web.assets_common" name="Common Assets (used in backend interface and website)">
    <link rel="stylesheet" type="text/css" href="/web/static/lib/jquery.ui/jquery-ui.css"/>
    ...
    <script type="text/javascript" src="/web/static/src/js/boot.js"></script>
    ...
</template>
```

然后，可以使用t-call-assets指令将捆绑包中的文件插入到模板中：

```python
<t t-call-assets="web.assets_common" t-js="false"/>
<t t-call-assets="web.assets_common" t-css="false"/>
```

下面是当服务器使用以下指令呈现模板时会发生的情况：

- 包中描述的所有SCSS文件都编译为CSS文件。名为file.scss的文件将编译在名为file.scss.css的文件中。
- **如果我们处于`debug=assets`模式**

>- t-js属性设置为false的t-call-assets指令将替换为指向css文件的样式表标记列表。
>
>- t-css属性设置为false的t-call-assets指令将替换为指向JS文件的脚本标记列表。

- **如果我们不处于`debug=assets`模式**

>- CSS文件将被连接并缩小，然后拆分为不超过4096个规则的文件（以绕过IE9的旧限制）。然后，我们根据需要生成尽可能多的样式表标签
>
>- JS文件被连接并缩小，然后生成一个脚本标记。

请注意，资产文件是缓存的，因此理论上，浏览器只应加载一次。



## 主捆Main bundles

当odoo服务器启动时，它检查包中每个文件的时间戳，如果需要，它将创建/重新创建相应的包。

以下是大多数开发人员需要知道的一些重要捆绑包：

- web.assets_common：此捆绑包包含Web客户端、网站以及销售点所共有的大多数资产。这应该包含用于ODO框架的较低级别的构建块。注意，它包含boot.js文件，它定义了odoo模块系统。

- web.assets_backend：这个包包含特定于web客户机的代码（特别是web客户机/操作管理器/视图）

- web.assets_frontend : 这个包是关于所有特定于公共网站的内容：电子商务、论坛、博客、事件管理……



### 在资产包中添加文件

将位于addons/web中的文件添加到bundle的正确方法很简单：只需将脚本或样式表标记添加到文件webclient_templates.xml中的bundle即可。但是当我们使用不同的插件时，我们需要从该插件添加一个文件。在这种情况下，应分三步进行：

1. 在视图/文件夹中添加assets.xml文件

2. 在清单文件的“data”键中添加字符串“views/assets.xml”

3. 创建所需包的继承视图，并使用xpath表达式添加文件。例如

   ```xml
   <template id="assets_backend" name="helpdesk assets" inherit_id="web.assets_backend">
       <xpath expr="//script[last()]" position="after">
           <link rel="stylesheet" type="text/scss" href="/helpdesk/static/src/scss/helpdesk.scss"/>
           <script type="text/javascript" src="/helpdesk/static/src/js/helpdesk_dashboard.js"></script>
       </xpath>
   </template>
   ```

   请注意，当用户加载odoo web客户机时，包中的文件都会立即加载。这意味着每次通过网络传输文件（浏览器缓存处于活动状态时除外）。在某些情况下，最好使用Lazyload的一些资产。例如，如果一个小部件需要一个大的库，而这个小部件不是体验的核心部分，那么在实际创建小部件时，最好只加载库。widget类实际上只为这个用例提供了内置支持。（请参见QWeb模板引擎一节）

### 如果文件未加载/更新，该怎么办？

文件可能无法正确加载有许多不同的原因。您可以尝试以下几点来解决此问题：

- 一旦服务器启动，它就不知道资产文件是否已被修改。因此，您可以简单地重新启动服务器来重新生成资产。


- 检查控制台（在dev工具中，通常用f12打开）以确保没有明显的错误


- 尝试在文件的开头添加console.log（在任何模块定义之前），这样您就可以查看文件是否已加载。


- 在用户界面中，在调试模式下（在此处插入链接到调试模式），有一个选项可以强制服务器更新其资产文件。


- 使用debug=assets模式。这实际上会绕过资产捆绑包（请注意，它实际上并不能解决问题）。服务器仍然使用过时的捆绑包）


- 最后，对于开发人员来说，最方便的方法是使用`–dev=all`选项启动服务器。这将激活文件监视程序选项，必要时将自动使资产无效。请注意，如果操作系统是Windows，它就不能很好地工作。


- 记住刷新页面！


- 或者保存代码文件…

重新创建资产文件后，需要刷新页面，重新加载正确的文件（如果不起作用，则可以缓存文件）。



## javascript模块系统

一旦我们能够将我们的javascript文件加载到浏览器中，我们就需要确保以正确的顺序加载它们。为了实现这一点，odoo定义了一个小模块系统（位于addons/web/static/src/js/boot.js文件中，需要先加载该文件）。

在AMD的启发下，odoo模块系统通过在全局odoo对象上定义函数define来工作。然后我们通过调用该函数来定义每个javascript模块。在odoo框架中，模块是一段将尽快执行的代码。它有一个名称，可能还有一些依赖项。当它的依赖项被加载时，模块也将被加载。模块的值就是定义模块的函数的返回值。

作为一个例子，它可能如下所示：

```javascript
// in file a.js
odoo.define('module.A', function (require) {
    "use strict";
    var A = ...;
    return A;
});
// in file b.js
odoo.define('module.B', function (require) {
    "use strict";
    var A = require('module.A');
    var B = ...; // something that involves A
    return B;
});
```

定义模块的另一种方法是在第二个参数中显式地给出依赖项列表。

```javascript
odoo.define('module.Something', ['module.A', 'module.B'], function (require) {
    "use strict";
    var A = require('module.A');
    var B = require('module.B');
    // some code
});
```

如果某些依赖项丢失/未就绪，那么模块将不会被加载。几秒钟后控制台中将出现警告。

请注意，不支持循环依赖项。这是有道理的，但这意味着一个人需要小心。



### 定义模块

`odoo.define`方法有三个参数：

- module name：javascript模块的名称。它应该是一个唯一的字符串。惯例是在odoo模块的名字后面加上一个具体的描述。例如，“web.widget”描述在web插件中定义的模块，该模块导出一个widget类（因为第一个字母大写）。如果名称不唯一，将引发异常并显示在控制台中。
- 依赖项：第二个参数是可选的。如果给定，它应该是一个字符串列表，每个字符串对应一个JavaScript模块。这描述了在执行模块之前需要加载的依赖项。如果这里没有显式地给出依赖项，那么模块系统将通过对其调用ToString从函数中提取它们，然后使用regexp查找所有Require语句。
- 最后一个参数是定义模块的函数。它的返回值是模块的值，可以传递给其他需要它的模块。注意，异步模块有一个小的异常，请参见下一节。

如果发生错误，将在控制台中记录（在调试模式下）：

- `Missing dependencies`: 这些模块不会出现在页面中。可能是javascript文件不在页面中或模块名称错误。
- `Failed modules`: 检测到一个javascript错误
- `Rejected modules`: 模块返回拒绝的延迟。它（及其相关模块）未加载。
- `Rejected linked modules`: 依赖被拒绝模块的模块
- `Non loaded modules`: 依赖丢失或故障模块的模块

### 异步模块

模块可能需要在准备就绪之前执行一些工作。例如，它可以做一个RPC来加载一些数据。在这种情况下，模块只需返回一个延迟（promise）。在这种情况下，模块系统只需等待延迟完成，然后注册模块。

```javascript
odoo.define('module.Something', ['web.ajax'], function (require) {
    "use strict";

    var ajax = require('web.ajax');

    return ajax.rpc(...).then(function (result) {
        // some code here
        return something;
    });
});
```



### 最佳实践

- 记住模块名的约定：以模块名后缀的加载项名。
- 在模块顶部声明所有依赖项。此外，它们应该按模块名称的字母顺序排序。这样更容易理解您的模块。
- 在末尾声明所有导出的值
- 尽量避免从一个模块导出过多的内容。通常最好在一个（小/小）模块中简单地导出一件事情。
- 异步模块可以用来简化一些用例。例如，web.dom_ready模块返回一个延迟的，当dom实际就绪时，这个延迟将被解决。因此，另一个需要dom的模块可以在某个地方简单地有一个require（“web.dom_ready”）语句，并且只有当dom准备好时才会执行代码。
- 尽量避免在一个文件中定义多个模块。这在短期内可能很方便，但实际上很难维持。



## Class System

Odoo是在EcmaScript 6类可用之前开发的。在ECMAScript 5中，定义类的标准方法是定义一个函数并在其原型对象上添加方法。这很好，但是当我们想要使用继承、混合时，它稍微复杂一些。

出于这些原因，Odoo决定使用自己的class system，这是受到John Resig的启发。基类位于web.class文件class.js中。



### 创建类

让我们讨论如何创建类。主要机制是使用扩展方法（这或多或少相当于ES6类中的扩展）。

```javascript
var Class = require('web.Class');
var Animal = Class.extend({
    init: function () {
        this.x = 0;
        this.hunger = 0;
    },
    move: function () {
        this.x = this.x + 1;
        this.hunger = this.hunger + 1;
    },
    eat: function () {
        this.hunger = 0;
    },
});
```

在本例中，init函数是构造函数。它将在创建实例时调用。通过使用new关键字创建实例。



### 继承

可以方便地继承现有的类。这只需在超类上使用extend方法即可完成。当调用一个方法时，框架会秘密地将一个特殊的方法重新绑定到当前调用的方法中。这允许我们在需要调用父方法时使用它。

```javascript
var Animal = require('web.Animal');
var Dog = Animal.extend({
    move: function () {
        this.bark();
        this._super.apply(this, arguments);
    },
    bark: function () {
        console.log('woof');
    },
});
var dog = new Dog();
dog.move()
```



### 混合多个类

odoo类系统不支持多重继承，但是对于那些需要共享某些行为的情况，我们有一个混合系统：extend方法实际上可以接受任意数量的参数，并将它们组合到新的类中。

```javascript
var Animal = require('web.Animal');
var DanceMixin = {
    dance: function () {
        console.log('dancing...');
    },
};

var Hamster = Animal.extend(DanceMixin, {
    sleep: function () {
        console.log('sleeping');
    },
});
```

在本例中，仓鼠类是动物的一个子类，但它也混合了DanceMixin。



### 覆盖现有类方法

这并不常见，但有时我们需要在适当的位置修改另一个类。目标是有一个机制来改变一个类和所有未来/现在的实例。这是通过使用include方法完成的：

```javascript
var Hamster = require('web.Hamster');

Hamster.include({
    sleep: function () {
        this._super.apply(this, arguments);
        console.log('zzzz');
    },
});
```

这显然是一个危险的操作，应该小心操作。但是，按照odoo的结构，有时需要在一个插件中修改在另一个插件中定义的小部件/类的行为。请注意，它将修改类的所有实例，即使它们已经创建。



## Widgets

*Widget* class 实际上是用户界面的一个重要构建块。几乎用户界面中的所有内容都在小部件的控制之下。Widget class在module *web.Widget*和widget.js中定义。

简而言之，widget类提供的特性包括：

- 小部件之间的父/子关系（propertiesmixin）

- 具有安全功能的广泛生命周期管理(e.g. 在销毁父级期间自动销毁子窗口小部件)

- 使用[qweb]自动呈现

- 帮助与外部环境交互的各种实用功能。

下面是一个基本计数器小部件的示例：

```javascript
var Widget = require('web.Widget');

var Counter = Widget.extend({
    template: 'some.template',
    events: {
        'click button': '_onClick',
    },
    init: function (parent, value) {
        this._super(parent);
        this.count = value;
    },
    _onClick: function () {
        this.count++;
        this.$('.val').text(this.count);
    },
});
```

对于本例，假设模板some.template（并且正确加载：模板位于一个文件中，该文件在模块清单中的qweb键中正确定义）由以下公式给出：

```xml
<div t-name="some.template">
    <span class="val"><t t-esc="widget.count"/></span>
    <button>Increment</button>
</div>
```

这个例子说明了小部件类的一些特性，包括事件系统、模板系统、带有初始父参数的构造函数。



### 小部件生命周期

与许多组件系统一样，widget类有一个定义良好的生命周期。通常的生命周期如下：调用init，然后启动，然后渲染，然后启动，最后销毁。



**Widget.init(*parent*)**

这是构造函数。init方法应该初始化小部件的基本状态。它是同步的，可以被重写以从小部件的创建者/父对象获取更多参数。

>Arguments   :  **parent** ([`Widget()`](https://www.odoo.com/documentation/12.0/reference/javascript_api.html#Widget)) – 新小部件的父级，用于处理自动销毁和事件传播。对于没有父级的小部件，可以为null。

**Widget.willStart()**

当一个小部件被创建并被附加到DOM的过程中，框架将调用这个方法一次。`willstart`方法是一个钩子，它应该返回一个延迟的。JS框架将等待这个延迟完成，然后再继续渲染步骤。注意，此时小部件没有dom根元素。`willstart`钩子主要用于执行一些异步工作，例如从服务器获取数据。

**Rendering()**

此步骤由框架自动完成。框架会检查小部件上是否定义了模板键。如果是这种情况，那么它将在呈现上下文中使用绑定到小部件的小部件键呈现该模板（请参见上面的示例：我们在QWeb模板中使用widget.count来读取小部件的值）。如果没有定义模板，则读取标记名键并创建相应的DOM元素。渲染完成后，我们将结果设置为小部件的`$el`属性。在此之后，我们将自动绑定事件和自定义事件键中的所有事件。

**Widget.start()**

渲染完成后，框架将自动调用Start方法。这对于执行一些特殊的后期渲染工作很有用。例如，设置库。

必须返回延迟以指示其工作何时完成。

>**Returns**	: deferred object

**Widget.destroy()**

这始终是小部件生命周期中的最后一步。当小部件被破坏时，我们基本上执行所有必要的清理操作：从组件树中删除小部件，取消绑定所有事件，…

当小部件的父级被销毁时自动调用，如果小部件没有父级，或者如果它被删除但父级仍然存在，则必须显式调用。



请注意，不必调用willstart和start方法。可以创建一个小部件（将调用init方法），然后销毁（destroy方法），而不需要附加到DOM。如果是这种情况，将不会调用will start和start。



### Widget API

**Widget.tagName**

如果小部件没有定义模板，则使用。默认为DIV，将用作标记名来创建要设置为小部件的dom根的dom元素。可以使用以下属性进一步自定义生成的dom根目录：

**Widget.id**

用于在生成的dom根上生成id属性。请注意，这是很少需要的，如果一个小部件可以多次使用，这可能不是一个好主意。

**Widget.className**

用于在生成的dom根上生成类属性。注意，它实际上可以包含多个css类：“some class other class”

**Widget.attributes**

属性名到属性值的映射（对象文本）。这些k:v对中的每一个都将设置为生成的dom根上的dom属性。

**Widget.el**

将原始DOM元素设置为小部件的根（仅在StartLifecycle方法之后可用）

**Widget.$el**

jquery围绕el的包装。（仅在Start Lifecycle方法之后可用）

**Widget.template**

应设置为QWeb模板的名称。如果设置了，模板将在小部件初始化之后但在其启动之前呈现。模板生成的根元素将被设置为小部件的dom根。

**Widget.xmlDependencies**

呈现小部件之前需要加载的XML文件的路径列表。这不会导致加载已加载的任何内容。如果您想延迟加载模板，或者想要在网站和Web客户机界面之间共享一个小部件，这很有用。

```javascript
var EditorMenuBar = Widget.extend({
    xmlDependencies: ['/web_editor/static/src/xml/editor.xml'],
    ...
```

**Widget.events**

事件是事件选择器（由空格分隔的事件名称和可选CSS选择器）到回调的映射。回调可以是小部件方法或函数对象的名称。在任何一种情况下，这都将设置为小部件：

```javascript
events: {
    'click p.oe_some_class a': 'some_method',
    'change input': function (e) {
        e.stopPropagation();
    }
},
```

选择器用于jquery的事件委托，回调仅对与选择器匹配的dom根的后代触发。如果选择器被省略（只指定了一个事件名），那么事件将直接设置在小部件的dom根上。

注意：不鼓励使用内联函数，将来可能会删除它。

**Widget.custom_events**

这几乎与事件属性相同，但键是任意字符串。它们表示由一些子小部件触发的业务事件。当一个事件被触发时，它将“冒泡”小部件树（有关更多详细信息，请参阅组件通信部分）。

**Widget.isDestroyed()**

Returns    `true` if the widget is being or has been destroyed, `false` otherwise

**Widget.$(*selector*)**

将指定为参数的CSS选择器应用于小部件的dom根目录：

```javascript
this.$(selector);
```

功能上与以下相同：

```javascript
this.$el.find(selector);
```

>Arguments    **selector** (`String`) – CSS selector
>
>Returns    jQuery object

​	此助手方法类似于 Backbone.View.$

**Widget.setElement(*element*)**

将小部件的dom根重新设置为提供的元素，还处理重新设置dom根的各种别名以及取消设置和重新设置委托事件。

>Arguments
>
>- **element** (`Element`) – 要设置为小部件的dom根的dom元素或jquery对象



### 在DOM中插入小部件

**Widget.appendTo(*element*)**

呈现小部件并将其作为目标的最后一个子项插入，使用[.appendTo()](http://api.jquery.com/appendTo/)

**Widget.prependTo(*element*)**

呈现小部件并将其作为目标的第一个子项插入，使用[.prependTo()](http://api.jquery.com/prependTo/)

**Widget.insertAfter(*element*)**

呈现小部件并将其作为目标的前一个同级插入，使用[.insertAfter()](http://api.jquery.com/insertAfter/)

**Widget.insertBefore(*element*)**

呈现小部件并将其作为目标的以下同级插入，使用[.insertBefore()](http://api.jquery.com/insertBefore/)

所有这些方法都接受相应jquery方法接受的任何内容（css选择器、dom节点或jquery对象）。他们都会返回一个延迟的任务，并承担三个任务：

- 通过以下方式呈现小部件的根元素：`renderElement()`
- 使用与其匹配的jquery方法在DOM中插入小部件的根元素
- 启动小部件并返回启动结果



### 小部件指南

- 应避免使用标识符（id属性）。在一般应用中而模块、ID限制了组件的可重用性，并往往使代码更加脆弱。大多数情况下，它们可以替换为Nothing、Classes或保留对dom节点或jquery元素的引用。如果ID是绝对必要的（因为第三方库需要一个），则应使用_.uniqueid（）部分生成ID，例如：

```javascript
this.id = _.uniqueId('my-widget-');
```

- 避免使用可预测/通用的CSS类名。类名称（如“content”或“navigation”）可能与所需的含义/语义匹配，但很可能其他开发人员也会有相同的需求，从而造成命名冲突和意外行为。通用类名的前缀应该是它们所属组件的名称（创建“非正式”名称空间，就像在C或Objective-C中那样）。
- 应避免使用全局选择器。因为一个组件可以在一个页面中多次使用（ODoo中的一个例子是仪表板），所以查询应该限制在给定组件的范围内。未筛选的选择（如\$（选择器）或document.querySelectorAll（选择器））通常会导致意外或错误的行为。odoo web的widget（）有一个属性，提供了它的dom根（$el），以及直接选择节点的快捷方式（$（））。
- 更一般地说，不要假设您的组件拥有或控制任何超出其个人$el的东西（因此，避免使用对父窗口小部件的引用）。
- HTML模板/呈现应该使用QWeb，除非非常简单。
- 所有交互组件（向屏幕显示信息或截取DOM事件的组件）必须继承自widget（），并正确实现和使用其API和生命周期。



## QWeb Template Engine

Web客户端使用QWeb模板引擎来呈现小部件（除非它们重写renderelement方法来执行其他操作）。QWebJS模板引擎基于XML，主要与Python实现兼容。

现在，让我们解释如何加载模板。每当Web客户端启动时，都会对/web/web client/qweb路由进行RPC。然后，服务器将返回在每个已安装模块的数据文件中定义的所有模板的列表。正确的文件列在每个模块清单的QWeb条目中。

在启动第一个小部件之前，Web客户机将等待加载该模板列表。

这个机制可以很好地满足我们的需求，但有时我们希望延迟加载模板。例如，假设我们有一个很少使用的小部件。在这种情况下，我们可能不希望将其模板加载到主文件中，以便使Web客户机稍微轻一些。在这种情况下，我们可以使用小部件的xmlpendencies键：

```javascript
var Widget = require('web.Widget');

var Counter = Widget.extend({
    template: 'some.template',
    xmlDependencies: ['/myaddon/path/to/my/file.xml'],

    ...

});
```

有了这个，计数器小部件将以willstart方法加载xmlpendencies文件，这样在执行呈现时模板将准备就绪。



## 事件系统

目前，odoo支持两个事件系统：一个允许添加侦听器和触发事件的简单系统，以及一个更完整的系统，它还可以使事件“冒泡”。

这两个事件系统都在文件`mixins.js`的`eventspatchemixin`中实现。这个`mixin`包含在`widget`类中。

### 基本事件系统

这是历史上第一个事件系统。它实现了一个简单的总线模式。我们有4种主要方法：

- *on*: 这用于在事件上注册侦听器。
- *off*: 用于删除事件侦听器。
- *once*: 这用于注册只调用一次的侦听器。
- *trigger*: 触发事件。这将导致调用每个侦听器。

以下是如何使用此事件系统的示例：

```javascript
var Widget = require('web.Widget');
var Counter = require('myModule.Counter');

var MyWidget = Widget.extend({
    start: function () {
        this.counter = new Counter(this);
        this.counter.on('valuechange', this, this._onValueChange);
        var def = this.counter.appendTo(this.$el);
        return $.when(def, this._super.apply(this, arguments);
    },
    _onValueChange: function (val) {
        // do something with val
    },
});

// in Counter widget, we need to call the trigger method:

... this.trigger('valuechange', someValue);
```

警告

不鼓励使用此事件系统，我们计划用扩展事件系统中的trigger-up方法替换每个trigger方法。

### 扩展事件系统

自定义事件小部件是一个更高级的系统，它模拟DOM事件API。每当一个事件被触发时，它将“冒泡”组件树，直到它到达根小部件，或者停止。

触发**trigger_up**:：这是一个方法，将创建一个小的odooEvent并在组件树中调度它。请注意，它将从触发事件的组件开始

自定义事件 **custom_events**:：这相当于事件字典，但对于odoo事件。

OdoEvent类非常简单。它有三个公共属性：目标（触发事件的小部件）、名称（事件名称）和数据（有效负载）。它还有两种方法：停止传播和停止。

上一个示例可以更新为使用自定义事件系统：

```javascript
var Widget = require('web.Widget');
var Counter = require('myModule.Counter');

var MyWidget = Widget.extend({
    custom_events: {
        valuechange: '_onValueChange'
    },
    start: function () {
        this.counter = new Counter(this);
        var def = this.counter.appendTo(this.$el);
        return $.when(def, this._super.apply(this, arguments);
    },
    _onValueChange: function(event) {
        // do something with event.data.val
    },
});

// in Counter widget, we need to call the trigger_up method:

... this.trigger_up('valuechange', {value: someValue});
```



## Registries

Odoo生态系统的一个常见需求是从外部扩展/更改基本系统的行为（通过安装应用程序，即不同的模块）。例如，可能需要在某些视图中添加新的小部件类型。在这种情况下，以及其他许多情况下，通常的过程是创建所需的组件，然后将其添加到注册表（注册步骤），以使Web客户机的其余部分知道它的存在。

系统中有几个注册表可用：

- 系统中有几个注册表可用：字段注册表（由“web.field_registry”导出）。字段注册表包含Web客户端已知的所有字段小部件。每当视图（通常是表单或列表/看板）需要字段小部件时，这就是它将要查找的地方。典型的用例如下所示：

  ```javascript
  var fieldRegistry = require('web.field_registry');
  
  var FieldPad = ...;
  
  fieldRegistry.add('pad', FieldPad);
  ```

  注意，每个值都应该是AbstractField的子类

- 视图注册表：此注册表包含Web客户端已知的所有JS视图（尤其是视图管理器）。此注册表的每个值都应该是AbstractView的子类


- 操作注册表：我们跟踪此注册表中的所有客户端操作。这个是操作管理器在需要创建客户端操作时查找的位置。在版本11中，每个值应该只是小部件的一个子类。但是，在版本12中，值必须是abstractAction。




## 小部件之间的通信

组件之间有许多通信方式。

- 从**parent**到**child**：

  这是一个简单的例子。父窗口小部件可以简单地对其子窗口调用方法：

  ```javascript
  this.someWidget.update(someInfo);
  ```

- 从一个小部件到它的父/某些祖先：

  在这种情况下，小部件的工作只是通知其环境发生了什么事情。由于我们不希望小部件具有对其父部件的引用（这将使小部件与其父部件的实现相结合），因此继续操作的最佳方法通常是触发一个事件，该事件将通过使用trigger-up方法在组件树中冒泡：

  ```javascript
  this.trigger_up('open_record', { record: record, id: id});
  ```

  此事件将在小部件上触发，然后将冒泡并最终被某些上游小部件捕获：

  ```javascript
  var SomeAncestor = Widget.extend({
      custom_events: {
          'open_record': '_onOpenRecord',
      },
      _onOpenRecord: function (event) {
          var record = event.data.record;
          var id = event.data.id;
          // do something with the event.
      },
  });
  ```

- 交叉分量：

  通过总线可以实现跨组件通信。这不是首选的通信形式，因为它有使代码难以维护的缺点。但是，它具有分离组件的优势。在这种情况下，这只是通过触发和监听总线上的事件来完成的。例如：

  ```javascript
  // in WidgetA
  var core = require('web.core');
  
  var WidgetA = Widget.extend({
      ...
      start: function () {
          core.bus.on('barcode_scanned', this, this._onBarcodeScanned);
      },
  });
  
  // in WidgetB
  var WidgetB = Widget.extend({
      ...
      someFunction: function (barcode) {
          core.bus.trigger('barcode_scanned', barcode);
      },
  });
  ```

  在本例中，我们使用web.core导出的总线，但这不是必需的。可以为特定目的创建总线。



## 服务

在11.0版中，我们引入了服务的概念。主要的想法是给子组件一种受控制的方式来访问它们的环境，这种方式允许框架进行足够的控制，并且是可测试的。

服务系统围绕三个理念进行组织：服务、服务提供商和小部件。它的工作方式是小部件触发（触发）事件，这些事件冒泡到服务提供者，服务提供者将要求服务执行任务，然后可能返回一个答案。

### 服务

服务是AbstractService类的实例。它基本上只有一个名称和一些方法。它的工作是执行一些工作，通常是一些依赖于环境的工作。

例如，我们有Ajax服务（任务是执行RPC）、本地存储（与浏览器本地存储交互）和许多其他服务。

以下是有关如何实现Ajax服务的简化示例：

```javascript
var AbstractService = require('web.AbstractService');

var AjaxService = AbstractService.extend({
    name: 'ajax',
    rpc: function (...) {
        return ...;
    },
});
```

此服务名为“ajax”，并定义一个方法rpc。

### 服务提供商

为了使服务正常工作，有必要让一个服务提供者准备好分派定制事件。在后端（Web客户端），这是由主Web客户端实例完成的。请注意，服务提供程序的代码来自ServiceProviderMin。

### Widget

小部件是请求服务的部分。为了做到这一点，它只需触发一个事件调用服务（通常通过使用helper函数调用）。此事件将冒泡并将意图传达给系统的其余部分。

在实践中，有些函数被频繁地调用，以至于我们有一些帮助器函数使它们更容易使用。例如，rpc方法是帮助生成rpc的助手。

```javascript
var SomeWidget = Widget.extend({
    _getActivityModelViewID: function (model) {
        return this._rpc({
            model: model,
            method: 'get_activity_view_id'
        });
    },
});
```

警告

如果一个小部件被破坏，它将从主组件树中分离出来，并且没有父组件。在这种情况下，事件不会冒泡，这意味着工作不会完成。这通常正是我们从一个被破坏的小部件中想要的。



### RPCs

RPC功能由Ajax服务提供。但大多数人可能只会与_rpc助手进行交互。

在处理odoo时，通常有两个用例：一个需要在（python）模型上调用方法（这需要通过控制器调用_kw），或者一个需要直接调用控制器（在某些路由上可用）。

- 在Python模型上调用方法：

  ```javascript
  return this._rpc({
      model: 'some.model',
      method: 'some_method',
      args: [some, args],
  });
  ```

- 直接呼叫控制器:

  ```javascript
  return this._rpc({
      route: '/some/route/',
      params: { some: kwargs},
  });
  ```



## 通知

odoo框架有一种标准的方式来向用户传递各种信息：通知，它显示在用户界面的右上角。

通知有两种类型：

- 通知*notification*: 有助于显示一些反馈。例如，每当用户取消订阅某个频道时。
- *warning*: useful to display some important/urgent information. Typically most kind of (recoverable) errors in the system.

此外，通知还可以用于向用户询问问题，而不会干扰其工作流。想象一下通过VoIP接收到的电话：一个粘性的通知可以显示为两个按钮：接受和拒绝。

### 通知系统

Odoo中的通知系统设计有以下组件：

- 通知小部件：这是一个简单的小部件，用于创建和显示所需的信息。
- 通知服务：一种服务，其职责是在请求完成时（使用自定义事件）创建和销毁通知。请注意，Web客户端是一个服务提供者。
- ServiceMixin中的两个助手功能：do_notify和do_warn

### 显示通知

显示通知的最常见方法是使用来自ServiceMixin的两种方法：

- **do_notify(title, message, sticky, className):**

  显示通知类型的通知。

  - *title*: string. 这将作为标题显示在顶部
  - *message*: string, 通知的内容
  - *sticky*: boolean, optional.如果为真，通知将一直保留，直到用户解除通知。否则，通知将在短时间延迟后自动关闭。
  - *className*: string, optional. 这是一个将自动添加到通知中的CSS类名。尽管不鼓励使用它，但这对于设计用途可能很有用。

- **do_warn(title, message, sticky, className):**

  显示警告类型的通知。

  - title*: string. 这将作为标题显示在顶部
  - *message*: string, 通知的内容
  - *sticky*: boolean, optional.如果为真，通知将一直保留，直到用户解除通知。否则，通知将在短时间延迟后自动关闭。
  - *className*: string, optional. 这是一个将自动添加到通知中的CSS类名。尽管不鼓励使用它，但这对于设计用途可能很有用。

以下是关于如何使用这些方法的两个示例：

```javascript
// note that we call _t on the text to make sure it is properly translated.
this.do_notify(_t("Success"), _t("Your signature request has been sent."));

this.do_warn(_t("Error"), _t("Filter name is required."));
```



## 任务栏

Systray是界面菜单栏的右侧部分，Web客户端在其中显示一些小部件，如消息菜单。

当菜单创建SystrayMenu时，它将查找所有已注册的小部件，并将它们作为子小部件添加到适当的位置。

目前没有针对Systray小工具的特定API。它们应该是简单的小部件，并且可以像使用trigger-up方法的其他小部件一样与环境通信。

### 添加新的Systray项目

没有Systray注册表。添加小部件的正确方法是将其添加到类变量systraymenu.items中。

```javascript
var SystrayMenu = require('web.SystrayMenu');

var MySystrayWidget = Widget.extend({
    ...
});

SystrayMenu.Items.push(MySystrayWidget);
```

### 订购

在向自己添加小部件之前，Systray菜单将按Sequence属性对项目进行排序。如果原型上不存在该属性，则将使用50。因此，要将Systray项目定位在右侧，可以设置一个非常高的序列号（反之，将其放在左侧的是一个较低的序列号）。

### 翻译管理

有些翻译是在服务器端进行的（基本上是由服务器呈现或处理的所有文本字符串），但是静态文件中有需要翻译的字符串。它目前的工作方式如下：

- 每个可翻译字符串都带有特殊的函数_t（可在js模块web.core中找到）
- 服务器使用这些字符串生成正确的采购订单文件。
- 每当加载Web客户端时，它都将调用route/web/web client/translations，它返回所有可翻译术语的列表。
- 在运行时，每当调用函数时，它都会在该列表中查找以查找转换，如果找不到转换，则返回它或原始字符串。

请注意，在文档翻译模块中，从服务器的角度对翻译进行了更详细的解释。

javascript中的翻译有两个重要功能：\_t和\_lt。区别在于\_lt的评估比较慢。

```javascript
var core = require('web.core');

var _t = core._t;
var _lt = core._lt;

var SomeWidget = Widget.extend({
    exampleString: _lt('this should be translated'),
    ...
    someMethod: function () {
        var str = _t('some text');
        ...
    },
});
```

在本例中，由于加载模块时翻译尚未就绪，因此必须使用\_lt。

注意，翻译功能需要注意。参数中给定的字符串不应是动态的。



## Session

Web客户端提供了一个特定的模块，其中包含一些特定于用户当前会话的信息。一些著名的钥匙是

- uid: 当前用户ID（作为res.users的ID）
- user_name: 用户名，作为字符串
- 用户上下文（用户ID、语言和时区）
- partner_id: 与当前用户关联的合作伙伴的ID
- db: 当前正在使用的数据库的名称

### 向会话添加信息

加载/web路由后，服务器将在模板中插入一些会话信息和脚本标记。信息将从模型ir.http的方法会话_信息中读取。因此，如果要添加特定信息，可以通过重写session_info方法并将其添加到字典中来完成。

```python
from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        result['some_key'] = get_some_value_from_db()
        return result
```

现在，可以通过在会话中读取javascript来获取该值：

```javascript
var session = require('web.session');
var myValue = session.some_key;
...
```

请注意，此机制旨在减少Web客户端准备就绪所需的通信量。它更适合于计算成本较低的数据（缓慢的会话信息调用将延迟为每个人加载Web客户端），以及在初始化过程早期需要的数据。



## Views

视图”一词有多种含义。本节是关于视图的JavaScript代码的设计，而不是Arch的结构或其他任何内容。

2017年，Odoo用一个新的架构替换了以前的视图代码。主要需要将呈现逻辑与模型逻辑分开。

视图（一般意义上）现在用4个部分描述：视图、控制器、渲染器和模型。这4个部分的API在AbstractView、AbstractController、AbstractRenderer和AbstractModel类中进行了描述。

- 这里是工厂。它的工作是获取一组字段、arch、上下文和其他一些参数，然后构造一个控制器/渲染器/模型三元组。

  视图的作用是用正确的信息正确地设置MVC模式的每一部分。通常，它必须处理arch字符串，并提取视图中每个其他部分所需的数据。

  请注意，视图是一个类，而不是一个小部件。一旦它的工作完成，它就可以被丢弃。

- 渲染器有一个任务：表示在DOM元素中查看的数据。每个视图可以以不同的方式呈现数据。此外，它还应该听取适当的用户操作，并在必要时通知其父（控制器）。

  渲染器是MVC模式中的V。

- 模型：它的任务是获取并保持视图的状态。通常，它以某种方式表示数据库中的一组记录。模型是“业务数据”的所有者。它是MVC模式中的M。

- 控制器：它的工作是协调渲染器和模型。此外，它是Web客户机其余部分的主要入口点。例如，当用户在搜索视图中更改某些内容时，将使用适当的信息调用控制器的更新方法。

  它是MVC模式中的C。

视图的JS代码设计为在视图管理器/操作管理器上下文之外可用。它们可以用于客户端操作，也可以显示在公共网站上（对资产进行了一些工作）。



## Field Widgets

Web客户端体验的一个很好的部分是关于编辑和创建数据。大部分工作都是在字段小部件的帮助下完成的，这些小部件了解字段类型以及有关如何显示和编辑值的具体细节。

### AbstractField

AbstractField类是视图中所有小部件的基类，用于支持它们的所有视图（当前为：窗体、列表、看板）。

v11字段小部件与以前的版本有很多不同。最重要的是：

- 小部件在所有视图之间共享(well, Form/List/Kanban).不再需要复制实现。请注意，通过在视图注册表中为其添加视图名称：*list.many2one*将优先于*many2one*选择，可以为视图提供专门版本的小部件。
- 小部件不再是字段值的所有者。它们只表示数据并与视图的其余部分通信。
- 小部件不再需要能够在编辑和只读模式之间切换。现在，当需要这样的更改时，小部件将被销毁并重新发送。这不是问题，因为他们不拥有自己的价值
- 字段小部件可以在视图外部使用。他们的API有点笨拙，但设计为独立的。



### 装饰品Decorations

与列表视图一样，字段小部件对装饰有一个简单的支持。装饰的目标是有一个简单的方法来根据记录的当前状态指定文本颜色。例如，

```xml
<field name="state" decoration-danger="amount &lt; 10000"/>
```

有效装修名称为：

- decoration-bf
- decoration-it
- decoration-danger
- decoration-info
- decoration-muted
- decoration-primary
- decoration-success
- decoration-warning

每个装饰装修x将映射到一个CSS类text-x，这是一个标准的引导CSS类（除了文本it和文本bf，分别由odoo处理并对应于斜体和粗体）。注意，decoration属性的值应该是一个有效的python表达式，它将以记录作为评估上下文进行评估。

### 非关系字段

我们在这里记录所有默认情况下可用的非关系字段，没有特定的顺序。

- **integer (FieldInteger)**

  这是integer类型字段的默认字段类型。

  - 支持的字段类型：integer 

  Options:

  - type:设置输入类型（默认情况下，文本可以设置为数字）

  在编辑模式下，该字段呈现为输入，HTML属性类型设置为“数字”（以便用户可以受益于本机支持，特别是在移动设备上）。在这种情况下，将禁用默认格式以避免不兼容。

  ```xml
  <field name="int_value" options='{"type": "number"}'/>
  ```

  **step: 当用户单击按钮时，将步骤设置为上下值**

  （仅用于输入类型编号，默认为1）

  ```xml
  <field name="int_value" options='{"type": "number", "step": 100}'/>
  ```

- **float (FieldFloat)**

  这是浮动类型字段的默认字段类型。

  - 支持的字段类型：*float*

  Attributes:

  - digits:显示精度

    ```xml
    <field name="factor" digits="[42,5]"/>
    ```

  Options:

  - type: 设置输入类型（默认情况下，文本可以设置为数字）

  在编辑模式下，该字段呈现为输入，HTML属性类型设置为“数字”（以便用户可以受益于本机支持，特别是在移动设备上）。在这种情况下，将禁用默认格式以避免不兼容。

  ```xml
  <field name="int_value" options='{"type": "number"}'/>
  ```

  **step: 当用户单击按钮时，将步骤设置为上下值**

  （仅用于输入类型编号，默认为1）

  ```xml
  <field name="int_value" options='{"type": "number", "step": 0.1}'/>
  ```

- **float_time (FieldFloatTime)**

  这个小部件的目标是正确显示一个表示时间间隔（以小时为单位）的浮点值。例如，0.5的格式应该是0:30，或者4.75对应于4:45。

  - 支持的字段类型：*float*

- **float_factor (FieldFloatFactor)**

  这个小部件的目标是正确显示一个浮动值，该值使用其选项中给定的系数进行转换。因此，例如，保存在数据库中的值是0.5，系数是3，小部件值应该格式化为1.5。

  - 支持的字段类型：*float

- **float_toggle (FieldFloatToggle)**

  这个小部件的目标是用包含一系列可能值（在选项中给出）的按钮替换输入字段。每次单击都允许用户在该范围内循环。这里的目的是将字段值限制为预定义的选择。此外，小部件支持将因子转换为浮点因子小部件（范围值应该是转换的结果）。

  - 支持的字段类型：float

  ```xml
  <field name="days_to_close" widget="float_toggle" options='{"factor": 2, "range": [0, 4, 8]}'/>
  ```

- **boolean (FieldBoolean)**

  这是布尔型字段的默认字段类型。

  - 支持的字段类型：boolean

- **char (FieldChar)**

  这是char类型字段的默认字段类型。

  - 支持的字段类型： char

- **date (FieldDate)**

  这是日期类型字段的默认字段类型。请注意，它也适用于日期时间字段。它在格式化日期时使用会话时区。

  - 支持的字段类型： *date*, *datetime*

  Options:

  ​	datepicker：datepicker小部件的额外设置。

  ```xml
  <field name="datefield" options='{"datepicker": {"daysOfWeekDisabled": [0, 6]}}'/>
  ```

- **datetime (FieldDateTime)**

  这是日期时间类型字段的默认字段类型。

  - 支持的字段类型： *date*, *datetime*

  Options:

  - datepicker: datepicker小部件的额外设置。

  ```xml
  <field name="datetimefield" options='{"datepicker": {"daysOfWeekDisabled": [0, 6]}}'/>
  ```

- **monetary (FieldMonetary)**

  这是“货币”类型字段的默认字段类型。它用于显示货币。如果在选项中给定了货币字段，它将使用该字段，否则将返回默认货币（在会话中）

  - 支持的字段类型： *monetary*, *float*

  Options:

  - currency_field: 另一个字段名应该是货币上的many2one。

  ```xml
  <field name="value" widget="monetary" options="{'currency_field': 'currency_id'}"/>
  ```

- **text (FieldText)**

  这是文本类型字段的默认字段类型。

  支持的字段类型： *text*

- **handle (HandleWidget)**

  此字段的作业将在列表视图中显示为句柄，并允许通过拖放行重新排序各种记录。

  警告

  不支持在同一列表上具有多个句柄小部件的字段。

  - 支持的字段类型： integer

- **email (FieldEmail)**

  此字段显示电子邮件地址。使用它的主要原因是，在只读模式下，它被呈现为具有正确href的锚标记。

  - 支持的字段类型： char

- **phone (FieldPhone)**

  此字段显示电话号码。使用它的主要原因是，它以只读模式呈现为具有正确的Href的锚标记，但仅在某些情况下：我们只希望在设备可以调用此特定号码时使其可单击。

  - 支持的字段类型： char

- **url (UrlWidget)**

  此字段显示一个URL（处于只读模式）。使用它的主要原因是，它被呈现为带有适当的css类和href的锚标记。

  - 支持的字段类型： char

  此外，锚定标记的文本可以使用文本属性进行自定义（它不会更改href值）。

  ```xml
  <field name="foo" widget="url" text="Some URL"/>
  ```

- **domain (FieldDomain)**

  "domain”字段允许用户通过类似树的界面构建技术前缀域，并实时查看所选记录。在调试模式下，输入还可以直接输入前缀char域（或者构建树型接口不允许的高级域）。

  请注意，这仅限于“静态”域（没有动态表达式或对上下文变量的访问）。

  - 支持的字段类型： char

- **link_button (LinkButton)**

  LinkButton小部件实际上只显示一个带有图标和文本值的范围作为内容。链接是可点击的，将打开一个新的浏览器窗口，其值为url。

  - 支持的字段类型： char

- **image (FieldBinaryImage)**

  此小部件用于将二进制值表示为图像。在某些情况下，服务器返回的是“bin_大小”而不是实际图像（bin_大小是表示文件大小的字符串，如6.5kb）。在这种情况下，小部件将生成一个具有与服务器上的图像对应的源属性的图像。

  - 支持的字段类型： *binary*

  Options:

  - preview_image: 如果图像仅加载为“bin_size”，则此选项有助于通知Web客户端默认字段名不是当前字段的名称，而是另一个字段的名称。

  ```xml
  <field name="image" widget='image' options='{"preview_image":"image_medium"}'/>
  ```

- **binary (FieldBinaryFile)**

  允许保存/下载二进制文件的通用小部件。

  - 支持的字段类型： binary

  Attribute:

  - filename: 保存二进制文件将丢失其文件名，因为它只保存二进制值。文件名可以保存在另一个字段中。为此，应将属性文件名设置为视图中存在的字段。

  ```xml
  <field name="datas" filename="datas_fname"/>
  ```

- **priority (PriorityWidget)**

  这个小部件呈现为一组星，允许用户单击它来选择一个值或不选择一个值。这对于将任务标记为高优先级很有用。

  注意这个小部件也在“只读”模式下工作，这是不寻常的。

  - 支持的字段类型： *selection*

- **attachment_image (AttachmentImage)**

  用于many2one字段的图像小部件。如果设置了该字段，则该小部件将呈现为具有正确SRC URL的图像。这个小部件在编辑或只读模式下没有不同的行为，它只用于查看图像。

  - 支持的字段类型： *many2one*

  ```xml
  <field name="displayed_image_id" widget="attachment_image"/>
  ```

- **image_selection (ImageSelection)**

  允许用户通过单击图像来选择值。

  - 支持的字段类型： selection

  Options:

  - 具有从选择值到具有图像URL（图像链接）和预览图像（预览链接）的对象的映射的字典。

    请注意，此选项不是可选的！

  ```xml
  <field name="external_report_layout" widget="image_selection" options="{
      'background': {
          'image_link': '/base/static/img/preview_background.png',
          'preview_link': '/base/static/pdf/preview_background.pdf'
      },
      'standard': {
          'image_link': '/base/static/img/preview_standard.png',
          'preview_link': '/base/static/pdf/preview_standard.pdf'
      }
  }"/>
  ```

- **label_selection (LabelSelection)**

  这个小部件呈现一个简单的不可编辑标签。这只对显示一些信息有用，而不是编辑它。

  - 支持的字段类型： selection

  Options:

  - classes:从选择值到CSS类的映射

  ```xml
  <field name="state" widget="label_selection" options="{
      'classes': {'draft': 'default', 'cancel': 'default', 'none': 'danger'}
  }"/>
  ```

- **state_selection (StateSelectionWidget)**

  这是一个专门的选择小部件。它假设记录有一些硬编码字段，显示在视图中：*stage_id*, *legend_normal*,*legend_blocked*, *legend_done*. 。这主要用于显示和更改项目中任务的状态，并在下拉列表中显示其他信息。

  - 支持的字段类型： selection

  ```xml
  <field name="kanban_state" widget="state_selection"/>
  ```

- **kanban_state_selection (StateSelectionWidget)**

  这与状态选择完全相同

  - 支持的字段类型： selection

- **boolean_favorite (FavoriteWidget)**

  根据布尔值的不同，这个小部件显示为空（或非）星。请注意，它也可以在只读模式下进行编辑。

  - 支持的字段类型： boolean

- **boolean_button (FieldBooleanButton)**

  布尔按钮小部件用于表单视图中的stat按钮。目标是显示一个具有布尔字段当前状态的漂亮按钮（例如，“active”），并允许用户在单击该字段时更改该字段。

  请注意，它也可以在只读模式下进行编辑。

  - 支持的字段类型： boolean

  Options:

  - terminology: 它可以是 ‘active’, ‘archive’, ‘close’ 或者使用键string_true*, *string_false*, *hover_true*, *hover_false*自定义映射

  ```xml
  <field name="active" widget="boolean_button" options='{"terminology": "archive"}'/>
  ```

- **boolean_toggle (BooleanToggle)**

  显示用于表示布尔值的切换开关。这是FieldBoolean的一个子字段，主要用于具有不同的外观。

- **statinfo (StatInfo)**

  这个小部件用于在stat按钮中表示统计信息。它基本上只是一个带有数字的标签。

  - 支持的字段类型： *integer, float*

  Options:

  - label_field: 如果给定，小部件将使用标签字段的值作为文本。

  ```xml
  <button name="%(act_payslip_lines)d"
      icon="fa-money"
      type="action">
      <field name="payslip_count" widget="statinfo"
          string="Payslip"
          options="{'label_field': 'label_tasks'}"/>
  </button>
  ```

- **percentpie (FieldPercentPie)**

  这个小部件用于在stat按钮中表示统计信息。这类似于statinfo小部件，但信息在饼图中表示（从空到满）。请注意，该值被解释为一个百分比（介于0和100之间的数字）。

  - 支持的字段类型： integer, float

  ```xml
  <field name="replied_ratio" string="Replied" widget="percentpie"/>
  ```

- **progressbar (FieldProgressBar)**

  将值表示为进度条（从0到某个值）

  - 支持的字段类型： integer, float

  Options:

  - title: 栏的标题，显示在栏选项的顶部
  - editable: 布尔值（如果值可编辑）
  - current_value: 从视图中必须存在的字段中获取当前值
  - max_value: 从视图中必须存在的字段中获取最大值
  - edit_max_value: 布尔值（如果最大值可编辑）
  - title: 条标题，显示在条顶部–>未翻译，请使用参数（非选项）“标题”代替

  ```xml
  <field name="absence_of_today" widget="progressbar"
      options="{'current_value': 'absence_of_today', 'max_value': 'total_employee', 'editable': false}"/>
  ```

- **toggle_button (FieldToggleBoolean)**

  此小部件用于布尔字段。它在绿色项目符号/灰色项目符号之间切换按钮。它还根据值和某些选项设置工具提示。

  - 支持的字段类型： *boolean*

  Options:

  - active: 布尔值为真时应设置的工具提示字符串
  - inactive: 布尔值为假时应设置的工具提示

  ```xml
  <field name="payslip_status" widget="toggle_button"
      options='{"active": "Reported in last payslips", "inactive": "To Report in Payslip"}'
  />
  ```

- **dashboard_graph (JournalDashboardGraph)**

  这是一个更专门化的小部件，用于显示表示一组数据的图形。例如，它在会计仪表板看板视图中使用。

  它假定该字段是一组数据的JSON序列化

  - 支持的字段类型：char

  Attribute

  - graph_type:字符串，可以是“line”或“bar”

  ```xml
  <field name="dashboard_graph_data" widget="dashboard_graph" graph_type="line"/>
  ```

- **ace (AceEditor)**

  此小部件用于文本字段。它提供了用于编辑XML和Python的ACE编辑器。

  - 支持的字段类型：*char, text*

### 关系字段

***class* FieldSelection()**

​		Extends :   AbstractField

FieldSelection小部件是一个带有下拉菜单的简单选择标记，允许选择一系列值。它设计用于处理类型为的字段 ‘selection’ and ‘many2one’.

支持的字段类型：*selection*, *many2one*

`placeholder`     一个字符串，用于在未选择值时显示某些信息。

```xml
<field name="tax_id" widget="selection" placeholder="Select a tax"/>
```

- **radio (FieldRadio)**

  这是字段选择的子字段，但专门用于将所有有效选项显示为单选按钮。

  请注意，如果在many2one记录上使用，那么将执行更多的RPC来获取相关记录的name_gets。

  - 支持的字段类型：*selection*, *many2one*

  Options:

  - horizontal:如果为真，将水平显示单选按钮

  ```xml
  <field name="recommended_activity_type_id" widget="radio"
      options="{'horizontal':true}"/>
  ```

- **selection_badge (FieldSelectionBadge)**

  这是FieldSelection的子字段，但专门用于将所有有效选项显示为矩形徽章。

  - 支持的字段类型：*selection*, *many2one*

  ```xml
  <field name="recommended_activity_type_id" widget="selection_badge"/>
  ```

- **many2one (FieldMany2One)**

  many2one字段的默认小部件。

  - 支持的字段类型：*selection*, *many2one*

  Attributes:

  - can_create:允许创建相关记录（优先于无创建选项）
  - can_write: 允许编辑相关记录的（默认值：真）

  Options:

  - no_create: 防止创建相关记录
  - quick_create: 允许快速创建相关记录（默认值：真）
  - no_quick_create: 阻止快速创建相关记录（不要问我）
  - no_create_edit: 和不创造一样，也许…
  - create_name_field: 创建相关记录时，如果设置了此选项，则“创建名称”字段的值将填充输入值（默认值：名称）。
  - always_reload: boolean, 默认为false。如果为真，该小部件将始终执行附加名称获取其名称值。这用于重写名称get方法的情况（请不要这样做）
  - no_open: boolean, 默认为false。如果设置为“真”，则在单击记录时（在只读模式下），many2one不会重定向该记录。

  ```xml
  <field name="currency_id" options="{'no_create': True, 'no_open': True}"/>
  ```

- **list.many2one (ListFieldMany2One)**

  many2one字段的默认小部件（在列表视图中）。

  列表视图的many2one字段的专门化。主要原因是我们需要将many2one字段（以只读模式）呈现为文本，这不允许打开相关记录。

  - Supported field types: *many2one*

- **kanban.many2one (KanbanFieldMany2One)**

  many2one字段的默认小部件（在看板视图中）。我们需要禁用看板视图中的所有版本。

  - Supported field types: *many2one*

- **many2many (FieldMany2Many)**

  many2many字段的默认小部件

  - Supported field types: *many2many*

  Attributes:

  - mode: string, 要显示的默认视图
  - domain: 将数据限制到特定域

  Options:

  - create_text: 允许自定义添加新记录时显示的文本

- **many2many_binary (FieldMany2ManyBinaryMultiFiles)**

  这个小部件帮助用户同时上载或删除一个或多个文件。

  注意这个小部件是特定于模型的‘ir.attachment’.

  - Supported field types: many2many

- **many2many_tags (FieldMany2ManyTags)**

  将many2many显示为标记列表。

  - Supported field types: many2many

  Options:

  - color_field:数值字段的名称，应出现在视图中。将根据其值选择颜色。

  ```xml
  <field name="category_id" widget="many2many_tags" options="{'color_field': 'color'}"/>
  ```

- **form.many2many_tags (FormFieldMany2ManyTags)**

  表单视图的many2many_tags小部件的专门化。它有一些额外的代码来允许编辑标签的颜色。

  - Supported field types: many2many

- **kanban.many2many_tags (KanbanFieldMany2ManyTags)**

  针对看板视图的many2many_tags小部件的专门化。

  - Supported field types: many2many

- **many2many_checkboxes (FieldMany2ManyCheckBoxes)**

  此字段显示复选框列表，并允许用户选择选项的子集。

  - Supported field types: many2many

- **one2many (FieldOne2Many)**

   one2many 字段的默认小部件。

  它通常在子列表视图或子看板视图中显示数据。

  - Supported field types: *one2many*

  Options:

  - create_text: 用于自定义“添加”标签/文本的字符串。

  ```xml
  <field name="turtles" options="{\'create_text\': \'Add turtle\'}">
  ```

- **statusbar (FieldStatus)**

  这是一个专门针对表单视图的小部件。它是许多表示流的窗体顶部的条，允许选择特定状态。

  - Supported field types: *selection, many2one*

- **reference (FieldReference)**

  FieldReference是select（用于模型）和FieldMany2One（用于其值）的组合。它允许在任意模型上选择记录。

  - Supported field types: *char, reference*

- **one2many_list (FieldOne2Many**

  这个小部件与FieldOne2Many完全相同。它在这个密钥上注册只是为了向后兼容。请不要使用这个。



## Client actions

客户机操作的想法是一个定制的小部件，它集成在Web客户机界面中，就像一个*act_window_action*一样。当需要与现有视图或特定模型没有紧密链接的组件时，此功能非常有用。例如，讨论应用程序实际上是一个客户机操作。

客户行为是一个具有不同含义的术语，具体取决于上下文：

- 从服务器的角度来看，它是模型*ir_action*的记录，字段标记类型为char
- 从Web客户机的角度来看，它是一个小部件，继承自类AbstractAction，并且应该在操作注册表中的相应键（从字段char）下注册。

每当菜单项与客户机操作相关联时，打开它只需从服务器获取操作定义，然后查找到其操作注册表中以获取相应键处的小部件定义，最后，它将实例化小部件并将其附加到DOM中的适当位置。



### 添加客户端操作Adding a client action

客户机操作是一个小部件，它将控制菜单栏下面的屏幕部分。如有必要，它可以有一个控制面板。定义客户机操作可以分为两个步骤：实现一个新的小部件，并在操作注册表中注册该小部件。

- **实施新的客户端操作:**

  这是通过创建一个小部件来完成的：

  ```javascript
  var ControlPanelMixin = require('web.ControlPanelMixin');
  var AbstractAction = require('web.AbstractAction');
  
  var ClientAction = AbstractAction.extend(ControlPanelMixin, {
      ...
  });
  ```

  如果不需要，不要添加控制面板混音器。注意，需要一些代码来与控制面板交互（通过mixin提供的update_control_panel方法）。

- **Registering the client action:**

  像往常一样，我们需要让Web客户机知道客户机操作和实际类之间的映射：

  ```javascript
  var core = require('web.core');
  
  core.action_registry.add('my-custom-action', ClientAction);
  ```

  然后，要在Web客户机中使用客户机操作，我们需要创建一个具有适当`tag`属性的客户机操作记录（模型ir.actions.client的记录）：

  ```xml
  <record id="my_client_action" model="ir.actions.client">
      <field name="name">Some Name</field>
      <field name="tag">my-custom-action</field>
  </record>
  ```

### 使用控制面板混合类型

默认情况下，abstractAction类不包括控制面板mixin。这意味着客户端操作不显示控制面板。要做到这一点，需要执行几个步骤。

- 在小部件中添加ControlPanelMixin：

  ```javascript
  var ControlPanelMixin = require('web.ControlPanelMixin');
  
  var MyClientAction = AbstractAction.extend(ControlPanelMixin, {
      ...
  });
  ```

- 每当需要更新控制面板时，调用方法update_control_panel。例如：

  ```javascript
  var SomeClientAction = Widget.extend(ControlPanelMixin, {
      ...
      start: function () {
          this._renderButtons();
          this._updateControlPanel();
          ...
      },
      do_show: function () {
           ...
           this._updateControlPanel();
      },
      _renderButtons: function () {
          this.$buttons = $(QWeb.render('SomeTemplate.Buttons'));
          this.$buttons.on('click', ...);
      },
      _updateControlPanel: function () {
          this.update_control_panel({
              cp_content: {
                 $buttons: this.$buttons,
              },
       });
  ```

有关更多信息，请查看control_panel.js文件。