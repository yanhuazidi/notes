[TOC]



## 创建新的字段小部件

这可能是一个非常常见的用例：我们希望以一种真正特定（可能依赖于业务）的方式在表单视图中显示一些信息。例如，假设我们希望根据某些业务条件更改文本颜色。

这可以通过三个步骤完成：创建一个新的小部件，在字段注册表中注册它，然后在表单视图中将该小部件添加到字段中

1. 创建新的小部件：

   这可以通过扩展一个小部件来实现：

   ```javascript
   var FieldChar = require('web.basic_fields').FieldChar;
   
   var CustomFieldChar = FieldChar.extend({
       _renderReadonly: function () {
           // implement some custom logic here
       },
   });
   ```

2. 在字段注册表中注册它：

   Web客户机需要知道小部件名称与其实际类之间的映射。这是由注册表完成的：

   ```javascript
   var fieldRegistry = require('web.field_registry');
   fieldRegistry.add('my-custom-field', CustomFieldChar);
   ```

3. 在窗体视图中添加小部件

   ```xml
   <field name="somefield" widget="my-custom-field"/>
   ```

请注意，只有表单、列表和看板视图使用此字段小部件注册表。这些视图紧密集成，因为列表和看板视图可以出现在表单视图中）。



## 修改现有字段小部件

另一个用例是我们想要修改现有的字段小部件。例如，odoo中的voip插件需要修改fieldphone小部件，以增加在voip上轻松调用给定号码的可能性。这是通过包含fieldphone小部件来完成的，因此不需要更改任何现有的表单视图。

字段小部件（abstractfield的（子类）实例）与其他所有小部件一样，因此它们可以进行猴修补。如下所示：

```javascript
var basic_fields = require('web.basic_fields');
var Phone = basic_fields.FieldPhone;

Phone.include({
    events: _.extend({}, Phone.prototype.events, {
        'click': '_onClick',
    }),

    _onClick: function (e) {
        if (this.mode === 'readonly') {
            e.preventDefault();
            var phoneNumber = this.value;
            // call the number on voip...
        }
    },
});
```

注意，不需要将小部件添加到注册表中，因为它已经注册了。



## 从界面修改主部件

另一个常见的用例是需要从用户界面定制一些元素。例如，在主菜单中添加消息。在这种情况下，通常的过程是再次包括小部件。这是唯一的方法，因为这些小部件没有注册表。

这通常是通过如下代码完成的：

```javascript
var HomeMenu = require('web_enterprise.HomeMenu');
HomeMenu.include({
    render: function () {
        this._super();
        // do something else here...
    },
});
```



## 创建新视图（从头开始）

创建新视图是一个更高级的主题。此备忘表将只突出显示可能需要执行的步骤（无特定顺序）：

- 向`ir.ui.view`的字段类型添加新的视图类型：

  ```python
  class View(models.Model):
      _inherit = 'ir.ui.view'
      type = fields.Selection(selection_add=[('map', "Map")])
  ```

- 将新视图类型添加到`ir.actions.act_window.view`的字段视图\模式：

  ```python
  class ActWindowView(models.Model):
      _inherit = 'ir.actions.act_window.view'
  
      view_mode = fields.Selection(selection_add=[('map', "Map")])
  ```

- 创建构成视图的四个主要部分（在javascript中）：

  我们需要一个视图（AbstractView的子类，这是工厂）、一个渲染器（AbstractRenderer）、一个控制器（AbstractController）和一个模型（AbstractModel）。我建议从扩展超类开始：

  ```javascript
  var AbstractController = require('web.AbstractController');
  var AbstractModel = require('web.AbstractModel');
  var AbstractRenderer = require('web.AbstractRenderer');
  var AbstractView = require('web.AbstractView');
  
  var MapController = AbstractController.extend({});
  var MapRenderer = AbstractRenderer.extend({});
  var MapModel = AbstractModel.extend({});
  
  var MapView = AbstractView.extend({
      config: {
          Model: MapModel,
          Controller: MapController,
          Renderer: MapRenderer,
      },
  });
  ```

- 将视图添加到注册表：

  和往常一样，需要更新视图类型和实际类之间的映射：

  ```javascript
  var viewRegistry = require('web.view_registry');
  
  viewRegistry.add('map', MapView);
  ```

- 实现四个主要类：

  视图类需要解析arch字段并设置其他三个类。渲染器负责在用户界面中表示数据，模型应该与服务器对话，加载数据并进行处理。控制器在那里协调，和网络客户机交谈……

- 在数据库中创建一些视图：

  ```xml
  <record id="customer_map_view" model="ir.ui.view">
      <field name="name">customer.map.view</field>
      <field name="model">res.partner</field>
      <field name="arch" type="xml">
          <map latitude="partner_latitude" longitude="partner_longitude">
              <field name="name"/>
          </map>
      </field>
  </record>
  ```



## 自定义现有视图

假设我们需要创建一个通用视图的自定义版本。例如，一个看板视图，顶部有一些额外的类似功能区的小部件（显示一些特定的自定义信息）。在这种情况下，这可以通过3个步骤完成：扩展看板视图（也可能意味着扩展控制器/渲染器和/或模型），然后在视图注册表中注册视图，最后使用看板架构中的视图（特定示例是帮助台仪表板）。

- 扩展视图：

  下面是它的样子：

  ```javascript
  var HelpdeskDashboardRenderer = KanbanRenderer.extend({
      ...
  });
  
  var HelpdeskDashboardModel = KanbanModel.extend({
      ...
  });
  
  var HelpdeskDashboardController = KanbanController.extend({
      ...
  });
  
  var HelpdeskDashboardView = KanbanView.extend({
      config: _.extend({}, KanbanView.prototype.config, {
          Model: HelpdeskDashboardModel,
          Renderer: HelpdeskDashboardRenderer,
          Controller: HelpdeskDashboardController,
      }),
  });
  ```

- 将其添加到视图注册表：

  像往常一样，我们需要通知Web客户机视图名称和实际类之间的映射。

  ```javascript
  var viewRegistry = require('web.view_registry');
  viewRegistry.add('helpdesk_dashboard', HelpdeskDashboardView);
  ```

- 在实际视图中使用它：

  现在我们需要通知Web客户机特定的`ir.ui.view`需要使用我们的新类。请注意，这是一个特定于Web客户端的问题。从服务器的角度来看，我们仍然有看板的观点。正确的方法是在arch的根节点上使用一个特殊的属性js_类（它将在某天被重命名为widget，因为这真的不是一个好名字）：

  ```xml
  <record id="helpdesk_team_view_kanban" model="ir.ui.view" >
      ...
      <field name="arch" type="xml">
          <kanban js_class="helpdesk_dashboard">
              ...
          </kanban>
      </field>
  </record>
  ```

注意：您可以更改视图解释拱门结构的方式。但是，从服务器的角度来看，这仍然是一个具有相同基本类型的视图，并遵循相同的规则（例如，RNG验证）。所以，您的视图仍然需要有一个有效的拱门字段。