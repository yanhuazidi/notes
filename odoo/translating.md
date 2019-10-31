[TOC]





## 处理翻译文本

### python

```python
from odoo import _
_('To send the goods')
```

### JavaScript

```javascript
var core = require('web.core');
var _t = core._t;
var _lt = core._lt;
title = _t("Bank Accounts");
```

只有文本字符串可以标记为导出，而不是表达式或变量。对于格式化字符串的情况，这意味着必须标记格式化字符串，而不是格式化字符串



### 变量

错误

```python
_("Scheduled meeting with %s" % invitee.name)
```

正确

```python
_("Scheduled meeting with %s") % invitee.name
```



### 块

不要将翻译拆分为多个块或多行

```python
# bad, trailing spaces, blocks out of context
_("You have ") + len(invoices) + _(" invoices waiting")
_t("You have ") + invoices.length + _t(" invoices waiting");

# bad, multiple small translations
_("Reference of the document that generated ") + \
_("this sales order request.")
```

一定要保留在一个块中，为翻译人员提供完整的上下文

```python
# good, allow to change position of the number in the translation
_("You have %s invoices wainting") % len(invoices)
_.str.sprintf(_t("You have %s invoices wainting"), invoices.length);

# good, full sentence is understandable
_("Reference of the document that generated " + \
  "this sales order request.")
```



### 复数

不要用英语的方式复数

```python
msg = _("You have %s invoice") % invoice_count
if invoice_count > 1:
  msg += _("s")
```

请记住，每种语言都有不同的复数形式：

```python
if invoice_count > 1:
  msg = _("You have %s invoices") % invoice_count
else:
  msg = _("You have %s invoice") % invoice_count
```



### 读取与运行时间

不要在服务器启动时调用翻译查找，在服务器启动时评估，没有用户语言

```python
ERROR_MESSAGE = {
  # bad, evaluated at server launch with no user language
  access_error: _('Access Error'),
  missing_error: _('Missing Record'),
}

class Record(models.Model):

  def _raise_error(self, code):
    raise UserError(ERROR_MESSAGE[code])
```

读取javascript文件时不要调用翻译查找，js _t过早评估,应使用  \_lt

```js
// bad, js _t is evaluated too early
var core = require('web.core');
var _t = core._t;
var map_title = {
    access_error: _t('Access Error'),
    missing_error: _t('Missing Record'),
};
```

在读取JS文件时执行翻译查找完成的情况下，使用时使用\_lt而不是\_t来翻译该术语

```js
// good, js _lt is evaluated lazily    js-lt的评估比较迟缓
var core = require('web.core');
var _lt = core._lt;
var map_title = {
    access_error: _lt('Access Error'),
    missing_error: _lt('Missing Record'),
};
```



## 导出可翻译术语

通过管理界面执行翻译导出，登录后端界面并打开**设置‣翻译‣导入/导出‣导出翻译**

- 将语言保留为默认值（新语言/空模板）,设置为翻译的目标语言

- 选择翻译文件格式   .po

- 选择要翻译的模块

- 单击导出`Export`并下载文件

  该文件是一个翻译模板，它只列出可翻译字符串，并从中创建实际翻译（翻译文件）。

- 可以使用msginit、Poedit等专用翻译工具或将模板复制到名为language.po的新文件中来创建翻译文件。翻译文件应放在yourmodule/i18n/中yourmodule.pot旁边，并在安装相应语言时由odoo自动加载（通过设置翻译加载翻译）

- 在要翻译的模块下创建**i18n**文件夹

- 将翻译好的翻译模板文件， PO 翻译文件 放入**i18n**文件夹

可以直接在**设置‣翻译‣导入/导出‣导入翻译**中导入 PO翻译文件

安装或更新模块时，也会安装或更新所有加载语言的翻译。











