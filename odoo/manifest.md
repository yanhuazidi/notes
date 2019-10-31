

清单文件用于将python包声明为odoo模块，并指定模块元数据。

它是一个名为`__manifest__.py`的文件，包含一个单独的python字典，其中每个键指定模块元数据。

```python
{
    'name': "A Module",
    'version': '1.0',
    'depends': ['base'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/mymodule_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',
    ],
}
```

可用的清单字段包括：

- `name` **(**`str`**, required)**

  模块的可读名称

- `version` **(**`str`**)**

  此模块的版本应遵循语义版本控制规则。

- `description` **(**`str`**)**

  重构文本中模块的扩展描述

- `author` **(**`str`**)**

  模块作者姓名

- `website` **(**`str`**)**

  模块作者的网站URL

- `license` **(**`str`**, defaults:** `LGPL-3`**)**

  模块的分发许可证

- `category` **(**`str`**, default:** `Uncategorized`**)**

  在odoo中的分类类别，模块的粗略业务域。

  尽管建议使用现有类别，但该字段是自由形式的，并且动态创建未知类别。可以使用分隔符创建类别层次结构/例如，foo/bar将创建类别foo，类别栏作为foo的子类别，并将bar设置为模块的类别。

- `depends` **(**`list(str)`**)**

  必须在这个模块之前加载的odoo模块，要么是因为这个模块使用了它们创建的特性，要么是因为它改变了它们定义的资源。

  安装模块后，所有依赖项都将安装在模块之前。同样，在加载模块之前加载依赖项。

- `data` **(**`list(str)`**)**

  必须始终使用模块安装或更新的数据文件列表。模块根目录中的路径列表

- `demo` **(**`list(str)`**)**

  仅在演示模式下安装或更新的数据文件列表

- `auto_install` **(**`bool`**, default:** `False`**)**

  如果为true，则在安装了此模块的所有依赖项时，将自动安装此模块。

  它通常用于实现两个独立模块之间的协同集成的“链接模块”。

  例如，sale_crm依赖sale和crm，并设置为自动安装。当同时安装了sale和crm时，它会自动将crm活动跟踪添加到销售订单中，而不需要sale或crm相互了解。

- `external_dependencies` **(**`dict(key=list(str))`**)**

  包含python和/或二进制依赖项的字典。

  对于python依赖项，必须为此字典定义`python`键，并且应该为其分配要导入的python模块列表。

  对于二进制依赖项，必须为此字典定义`bin`键，并应为其分配二进制可执行文件名列表。

  如果主机中没有安装python模块，或者在主机的path环境变量中找不到二进制可执行文件，则不会安装该模块。

- `application` **(**`bool`**, default:** `False`**)**

  模块是应该被视为完全成熟的应用程序（true），还是仅仅是为现有应用程序模块提供一些额外功能的技术模块（false）。

- `css` **(**`list(str)`**)**

  使用要导入的自定义规则指定CSS文件，这些文件应位于模块内的static/src/css中。

- `images` **(**`list(str)`**)**

  指定模块要使用的图像文件。

- `installable` **(**`bool` **default:** `False`**)**

  用户是否应该能够从Web UI安装模块。

- `maintainer` **(**`str`**)**

  负责维护此模块的人员或实体，默认情况下假定作者是维护者。

- `{pre_init, post_init, uninstall}_hook` **(**`str`**)**

  模块安装/卸载的回调函数，它们的值应该是一个字符串，表示在模块的`__init__.py`中定义的函数名。

  - `pre_init_hook` 将光标作为唯一的参数，此函数在模块安装之前执行。

  - `post_init_hook` 以一个光标和一个注册表作为参数，此函数在模块安装后立即执行。

  - `uninstall_hook`以光标和注册表作为参数，此函数在模块卸载后执行。

  仅当此模块所需的设置/清理非常困难或无法通过API进行时，才应使用这些挂钩。



```python
# -*- coding: utf-8 -*-
{
    'name': "om_payment_alipay",
    'summary': 'Payment Acquirer: Alipay Implementation',
    'description': """Alipay Payment Acquirer""",

    'author': "Wei Tianhua",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','payment'],

    'external_dependencies': {
        'python': [
            'Cryptodome',
        ],
    },
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/alipay_views.xml',
        'views/payment_alipay_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'post_init_hook': 'create_missing_journal_for_acquirers',
    'images': ['static/description/banner.png'],
}
```



