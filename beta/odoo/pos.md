[TOC]



## POS组件定义

### PosBaseWidget

### 抽象组件

```javascript
var Widget = require('web.Widget');
var PosBaseWidget = Widget.extend({
    init:function(parent,options){
        this._super(parent);
        options = options || {};
        this.pos    = options.pos    || (parent ? parent.pos : undefined);
        this.chrome = options.chrome || (parent ? parent.chrome : undefined);
        this.gui    = options.gui    || (parent ? parent.gui : undefined); 
        // the widget class does not support anymore using $el/el before the
        // 'start' lifecycle method, but point of sale actually needs it.
        this.setElement(this._makeDescriptive());
    },
    show()
    hide()
    return PosBaseWidget
```



### 实体组件

#### 组件模板

```xml
<t t-name="PopupWidget">模板名称
     <div role="dialog" class="modal-dialog">
          <div class="popup popup-alert">
              <p class="title"><t t-esc=" widget.options.title || 'Alert' " /></p>
              <p class="body"><t t-esc=" widget.options.body || '' "/></p>
              <div class="footer">
                   <div class="button cancel">Ok</div>
              </div>
        </div>
    </div>
</t>
```



```javascript
var UsernameWidget = PosBaseWidget.extend({
    template: 'UsernameWidget',//模板名称
    init: function(parent, options){
        options = options || {};
        this._super(parent,options);
    },

    get_name: function(){
        var user = this.pos.get_cashier();
        if(user){
            return user.name;
        }else{
            return "";
        }
    },
});
//重写 weiget 渲染方法
renderElement: function(){
        var self = this;
        // cleanup table widgets from previous renders
        for (var i = 0; i < this.table_widgets.length; i++) {
            this.table_widgets[i].destroy();
        }
        this.table_widgets = [];

        this._super();
}
//内部 $el = $(core.qweb.render(this.template, {widget: this}).trim());
```





### 渲染XML

```js
var QWeb = core.qweb;
rendered_order_lines = QWeb.render('CustomerFacingDisplayOrderLines', {
                    'orderlines': order.get_orderlines(),
                    'widget': self.chrome,
                });
rendered_payment_lines = QWeb.render('CustomerFacingDisplayPaymentLines', {
                    'order': order,
                    'widget': self.chrome,
                });
$rendered_html.find('.pos_orderlines_list').html(rendered_order_lines);
$rendered_html.find('.pos-paymentlines').html(rendered_payment_lines);
//CustomerFacingDisplayOrderLines  为模板名称，不是组件名称
```





## POS添加js/css

```xml
<template id="assets" inherit_id="point_of_sale.assets">
    <xpath expr="." position="inside">
        <script type="text/javascript" src="/pos_restaurant/static/src/js/notes.js"></script>
    </xpath>
    <xpath expr="//link[@id='pos-stylesheet']" position="after">
        <link rel="stylesheet" href="/pos_restaurant/static/src/css/restaurant.css"/>
     </xpath>
</template>

```

img

```xml
<img class="pos-logo" src="/point_of_sale/static/src/img/logo.png" alt="Logo"/>
```





## MODELS

在销售点启动时加载openerp模型。加载模型接受模型加载程序声明数组。模型将按数组顺序加载。如果没有提供openerp模型名称，则不会加载任何服务器数据，但可以使用系统在加载前对数据进行预处理。加载器参数可以是返回动态值的函数。函数将posmodel作为第一个参数和一个临时对象，由所有模型共享，可用于存储模型加载之间的临时信息，不进行依赖关系管理。必须按正确的顺序加载模型。新添加的模型将在末尾加载，但可以使用“后/前”选项直接在另一个模型之前/之后加载。

`models`：[{

`model`:[string]要加载的openerp模型的名称。

`label`:[string]加载期间显示的标签。

`fields`：[[string]|function]要加载的字段列表。空数组/空加载所有字段。

`order`：[[string]|function]模型将按提供的字段排序

`domain`：[domain|function]决定需要加载哪些模型的域。空加载所有内容

`ids`: [[id]|function]必须加载的模型的ID列表。覆盖域。

`context`:[Dict|function] 模型读取的openerp上下文

`condition`：[function] 如果计算结果为“其他”，则不加载模型。

`loaded`:[function(self,model)]加载模型后调用此函数，将数据作为第二个参数。如果函数返回延迟，则下一个模型将等待直到它在加载前解决。

}]

`options`:

`before`: [string] 模型将在命名模型之前加载（同时适用于模型名称和标签）

`after`:  [string] 模型将加载到（上次加载的）命名模型之后。（适用于型号名称和标签）

```js
var models = require('point_of_sale.models');
models.load_models(models,options)
```

**eg:**

```js
models.load_models({
    model: 'restaurant.floor',
    fields: ['name','background_color','table_ids','sequence'],
    domain: function(self){ return [['pos_config_id','=',self.config.id]]; },
    loaded: function(self,floors){
        self.floors = floors;
        self.floors_by_id = {};
        for (var i = 0; i < floors.length; i++) {
            floors[i].tables = [];
            self.floors_by_id[floors[i].id] = floors[i];
        }
        // Make sure they display in the correct order
        self.floors = self.floors.sort(function(a,b){ return a.sequence - b.sequence; });

        // Ignore floorplan features if no floor specified.
        self.config.iface_floorplan = !!self.floors.length;
    },
});
```





## 支付

```xml
PaymentScreenWidget
PaymentScreen-Paymentlines
PaymentScreen-Numpad
PaymentScreen-Paymentmethods
```





```js
render_paymentmethods: function() {
        var self = this;
        var methods = $(QWeb.render('PaymentScreen-Paymentmethods', { widget:this }));
            methods.on('click','.paymentmethod',function(){
                self.click_paymentmethods($(this).data('id'));
            });
        return methods;
    },
        
click_paymentmethods: function(id) {
        var cashregister = null;
        for ( var i = 0; i < this.pos.cashregisters.length; i++ ) {
            if ( this.pos.cashregisters[i].journal_id[0] === id ){
                cashregister = this.pos.cashregisters[i];
                break;
            }
        }
        this.pos.get_order().add_paymentline( cashregister );
        this.reset_input();
        this.render_paymentlines();
    },

```



## 付款对象

```js
add_paymentline: function(cashregister) {
        this.assert_editable();
        var newPaymentline = new exports.Paymentline({},{order: this, cashregister:cashregister, pos: this.pos});
        if(cashregister.journal.type !== 'cash' || this.pos.config.iface_precompute_cash){
            newPaymentline.set_amount( this.get_due() );
        }
        this.paymentlines.add(newPaymentline);
        this.select_paymentline(newPaymentline);

    },
```

**确认订单**

```js
this.$('.next').click(function(){
      self.validate_order();
});

//确认支付订单
validate_order: function(force_validation) {
      if (this.order_is_valid(force_validation)) {
          this.finalize_validation();
    }
},
  
//支付方法
finalize_validation: function() {
        var self = this;
        var order = this.pos.get_order();
		//钱箱付款
        if (order.is_paid_with_cash() && this.pos.config.iface_cashdrawer) { 
                this.pos.proxy.open_cashbox();
        }
		//付款时间
        order.initialize_validation_date();
    	//订单已付款
        order.finalized = true;
    	//打印发票
        if (order.is_to_invoice()) {
            var invoiced = this.pos.push_and_invoice_order(order);
            this.invoicing = true;

            invoiced.fail(this._handleFailedPushForInvoice.bind(this, order, false));

            invoiced.done(function(){
                self.invoicing = false;
                self.gui.show_screen('receipt');
            });
        } else {
            this.pos.push_order(order);
            this.gui.show_screen('receipt');
        }

    },
```









## 打印小票

```js
this.$('.button.print').click(function(){
      if (!self._locked) {
            self.print();
      }
});
```

