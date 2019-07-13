

```
1.options = options || {};
2.!(models instanceof Array)
3.
```

```javascript
this.getSession() 当前session
```





## POS组件定义

### PosBaseWidget

抽象组件

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



## 一级组件

实体组件

```javascript
var UsernameWidget = PosBaseWidget.extend({
    template: 'UsernameWidget',
    init: function(parent, options){
        options = options || {};
        this._super(parent,options);
    },
    renderElement: function(){
        var self = this;
        this._super();

        this.$el.click(function(){
            self.click_username();
        });
    },
    click_username: function(){
        var self = this;
        this.gui.select_user({
            'security':     true,
            'current_user': this.pos.get_cashier(),
            'title':      _t('Change Cashier'),
        }).then(function(user){
            self.pos.set_cashier(user);
            self.renderElement();
        });
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
```













