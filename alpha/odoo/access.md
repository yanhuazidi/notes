

[TOC]



**除了使用自定义代码手动管理访问外，Odoo还提供了两种主要的数据驱动机制来管理或限制对数据的访问。**
**这两种机制都通过*组*链接到特定用户：用户属于任意数量的组，安全机制与组相关联，从而将安全机制应用于用户。**

Odoo的权限的核心是权限组（res_groups）。对每个权限组，可以设置权限组的菜单表示，对象表示，记录规则表示，字段表示。

**权限管理的四个层次**
    菜单级别：不属于指定菜单所包含组的用户看不到该菜单，不安全，只是隐藏菜单，若知道菜单ID，
						仍然可以通过指定URL访问
    对象级别：对某个对象是否有'创建，读取，修改，删除'的权限，可以简单理解为表对象
    记录级别：对对象表中的数据的访问权限，比如访问“客户”对象，业务员只能对自己创建
              			的客户有访问权限，而经理可以访问其管辖的业务员所有的“客户”对象
   字段级别：一个对象或表上的某些字段的访问权限，比如产品的成本字段只有经理有读权限
       		 'name':fields.char('Name',size=128,required=True,select=True,write=['base.group_admin']
               read=['base.group_admin'])
       定义name字段只能超级用户组可读写

### 建立权限组
     这是我们常说的用户组，会通常放在“模块名_security.xml”这个文件中

```xml
<data noupdate="0">
    <record id="module_category_test" model="ir.module.category">
        <field name="name">测试</field>
    </record>
    
    <record id="group_test_user" model="res.groups">
        <field name="name">测试用户</field>
        <field name="category_id" ref="module_category_test"/>
    </record>
    
    <record id="group_test_manager" model="res.groups">
        <field name="name">测试管理</field>
        <field name="implied_ids" eval="[(4, ref('group_test_user'))]"/>
        <field name="category_id" ref="module_category_test"/>
    </record>
    
    <record id="base.group_hr_manager" model="res.groups">
        <field name="name">Manager</field>
        <field name="comment">the user will have an access to the human resources configuration as well as statistic reports.</field>
        <field name="category_id" ref="base.module_category_human_resources"/>
        <field name="implied_ids" eval="[(4, ref('base.group_hr_user'))]"/>
        <field name="users" eval="[(4, ref('base.user_root'))]"/>
     </record>
</data>
```

Noupdate 表示，当模块升级时是否更新本条数据。
对于demo 数据，通常设置成noupdate=”1”，即不更新，不指定noupdate 的话，默认值是noupdate=”0”。
name:用户组名，这个或以翻译的
comment:用户组的注释
category_id 用户组所属的模块名
implied_ids 基于哪个用户组，这个层级关系

```xml
<field name="implied_ids" eval="[(4, ref('base.group_user'))]"/>
```

是最基础的用户名，最初是基于这个，后面一层一层递增，像上面 base.group_hr_user 定义时就是基于最基础
users 预设用户属于这个用户组



### 权限组
​    权限管理核心是权限组，每个权限组，可以设置权限组的 Menus,Access Right, Record Rule

**Menus:**
​        定义该权限组可以访问哪些菜单，若该权限组可以访问某父菜单，父菜单对应的子菜单会显示出来
​        若不想显示其子菜单，可以把其子菜单加入 "Useablity/No One" 权限组。

 **Access Right:**
​        定义该权限组可以访问哪些对象，以及拥有 增、查、改、删的哪个权限    (create,read,write,unlink)

**​Record Rule:**
​        定义该权限组可以访问对象中的哪些记录，以及拥有 增、查、改、删的哪个权限，Access Right是
​        对对象中的所有记录赋权限，Record Rule 则通过定义domain过滤指定某些记录赋权限
​        ['&',('department','=',user.context_department_id.id),('state','=','pr_draft')]
​        申购单的部门等于当前用户的部门，且申购单的状态是草稿状态



## 基于组的访问控制

### 视图中

**运用group_id**

```xml
<record id="view_order_form_editable_list" model="ir.ui.view">
    <field name="name">sale.order.form.editable.list</field>
    <field name="model">sale.order</field>
    <field name="inherit_id" ref="sale.view_order_form" />
    <field name="group_id" eval="[(6,0,[ref('product.group.uos'),
         							ref('product.group_stock_packaging'),
         							ref('sale.group_mrp_properties')])]" />
    <field name="arch" type="xml">
        <xpath expr="//field[@name='order_line]/tree" position="before"
            <attribute name="editable" />
        </xpath>    
    </field>
</record>
```

eval :  把eval的值通过作为python运算返回该属性
    	ref:视图的方法，根据 module_name.xml_id 返回数据库id
    	[(6,0,[xx,yy])]
      	(0,_ ,{’field’: value}) 这将创建一个新的记录并连接它
     	 (1,id,{’field’: value}): 这是更新一个已经连接了的记录的值
      	(2,id,_) 这是删除或取消连接某个已经连接了的记录
      	(3,id,_) 这是取消连接但不删除一个已经连接了的记录
      	(4,id,_) 连接一个已经存在的记录
      	(5,_,_) 取消连接但不删除所有已经连接了的记录
      	(6,_,[ids]) 用给出的列表替换掉已经连接了的记录
      		这里的下划线一般是0或False

**运用groups**

```xml
<button name="invoice_pay_customer" type="object" string="Register Payment"
                    attrs="{'invisible': ['|', ('state','!=','open'), ('sent','=',True)]}" groups="base.group_user"/>
<field name="invoice_line_ids" groups="account.group_account_invoice"/>
<menuitem name="China Account" id="menu_china_account" parent="account.menu_finance" sequence="4" groups="account.group_account_user"/>
```


### 在模型中

```python
package_id = fields.Many2one(comodel_name='stock.quant.package', string='Package',
			related='quant.package_id', readonly=True, groups="stock.group_tracking_lot")
```


   要有多个用户组时，用户组之间用逗号隔开

小结
	只有在视图中有完整标签时，会用group_id,其它都用groups



##  访问权限管理：
**对于其内的数据访问权限管理有两种机制:** 

- 第一种是模型访问权限管理 (access rule)；
- 第二种是记录规则管理 (record rule)。

record rule 是对access rule的细化 ，带条件，比如记录是什么状态的可以访问
如果不为模块设置规则，默认只有Administator才能访问这个模型的数据
record rule 对 Administator 用户是无效的，而access rule还是有效

### access rule
  	权限对象模型是 ir.model.access.csv 一般是放在security 文件夹下的 ir.model.access.csv 文件来管理的
**文件表头如下：**

```python
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
```

来一个例子：

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
   access_payment_notice_account_user,payment.notice.account.user,model_payment_notice,account.group_account_user,1,1,1,1
   access_payment_notice_sale_user,payment.notice.sale.user,model_payment_notice,base.group_sale_salesman,1,1,0,0
```

分析这个是针对 payment.notice 这个模型做访问权限设置
可以看一下对应模型定义的代码：

```python
class PaymentNotice(models.Model):
    _name = "payment.notice"
```

`id:`权限的ID不可重复 一般取名为 access_模型名_特定用户组名（用下划线连起来）
`name:` 描述 一般命名沿用模型名用“.”连接加 用户组名
`model_id:id：`对象，命名是model_模型名（用下划线连起来）
`group_id:id  `组名称 （模块.用户组名）
**下面的，0 表示无权限， 1 表示有权限**
`perm_read `           只读
`perm_write`         修改
`perm_create`        创建
`perm_unlink `        删除
       

###  record rule     

     一般是放在security 文件夹下的 模块名_record_rules.xml 文件来管理的 
     对于模型权限的补充

```xml
<?xml version="1.0" encoding="utf-8”?>
<openerp>
     <record model="ir.rule" id="payment_notice_personal_rule">
           <field name="name">Personal Payment Notice</field>
           <field name="model_id" ref="model_payment_notice"/>
           <field name="domain_force">['|',('claimed_user_id','=',user.id),('claimed_user_id','=',False)]</field>
           <field name="groups" eval="[(4, ref('base.group_sale_salesman'))]"/>
      </record>
            
      <record model="ir.rule" id="payment_notice_see_all">
           <field name="name">All Payment Notice</field>
           <field name="model_id" ref="model_payment_notice"/>
           <field name="domain_force">[(1,'=',1)]</field>
           <field name="groups" eval="[(4, ref('account.group_account_user'))]"/>
           <field name="perm_read" eval="1" />
           <field name="perm_write" eval="1" />
           <field name="perm_create" eval="1" />
           <field name="perm_unlink" eval="1" />
      </record>
</openerp>   
```

​    record rule    记录是 ir.rule 模型， 存在public.ir_rule 表格中
​    model_id 作用于哪个模型 值为 model_模型名
​    domain_force 对该模型中所有记录进行某种过滤操作
​    常用的 ['|',('user_id','=',user.id),('user_id','=',False)] 表示是自己的单 
​    user_id是记录的字段，这个看实际情况改变， user.id 代表当前登录用户的id
​    [(1,'=',1)] 表示所有的单
​    noupdate 值为1 表示升级模块不会更新本数据
​    base.group_user 是人力资源 / 雇员
​    perm_read 这些后面，是对 前面模型权限组设定的覆盖

**来一个完整的例子解说：**

建立组

```xml
<record id="group_department_project_admin" model="res.groups">
    <field name="name">A</field>
    <field name="category_id" ref="B"/>
    <field name="users" eval="[(4, ref('base.user_root'))]"/> //把admin用户加入该组中
</record>
```

​    @ name 组名称
​    @ category_id 属于哪个应用程序，或者哪个模块，为了方便管理
​    @ users 组里面的用户
这样B应用程序就建立了一个名叫A的组。并且初始化了A组的一个用户admin组控制菜单显示

```xml
<record model="ir.ui.menu" id=" memu_id1">
    <field name="name" >menu1</field>
    <field name="groups_id" eval="[(6,0,[ref('A'),ref('B')]),]"/>           
    <field name="sequence">1</field>
</record>
```

    @ name 菜单名称
    @ groups_id 哪些组可以访问该菜单
    @ sequence 该菜单的序号
    这样A组与B组的成员都可以访问menu1菜单，menu1菜单的显示顺序为1 
    注：eval 后面解释，多个组访问用“，”隔开

```xml
<menuitem id="menu_id2 " name="menu2" parent="menu_id1" sequence="1" groups="A,B "/>
```


    @ name 菜单名称
    @ parent 父类菜单 如果没有可以不写parent
    @ groups哪些组可以访问该菜单
    这样menu1的子菜单menu2可以被A组合B组的成员访问
    

权限规则

```xml
<record model="ir.rule" id="rule1">
     <field name="name">rule1</field>
     <field name="model_id" ref="model_model1"/>
     <field name="global" eval="True"/>
     <field name="domain_force">[1,’=’,1]</field>
     <field name="groups" eval="[(4,ref('A'))]"/>
</record>
```

​    @ name 规则名称
​    @ model_id 依赖的模块
​    @ global 是否是全局
​    @ domain_force 过滤条件
​    @ groups 属于哪个组

​    这样A组的成员就可以取到model_model1的所有数据

ir.model.access.csv
​    @id 随便取
​    @name 随便取
​    @model_id:id 这个就是你所定义的对象了
​    @group_id:哪个组
​    @perm_read","perm_write","perm_create","perm_unlink" 增删改查权限了。1代表有权限
​ 
Eval

​    many2many
​    (0,0,{values}) 根据values里面的信息新建一个记录。
​    (1,ID,{values})更新id=ID的记录（写入values里面的数据）
​    (2,ID) 删除id=ID的数据（调用unlink方法，删除数据以及整个主从数据链接关系）
​    (3,ID) 切断主从数据的链接关系但是不删除这个数据
​    (4,ID) 为id=ID的数据添加主从链接关系。
​    (5) 删除所有的从数据的链接关系就是向所有的从数据调用(3,ID)
​    (6,0,[IDs]) 用IDs里面的记录替换原来的记录（就是先执行(5)再执行循环IDs执行（4,ID））

​    例子[(6, 0, [8, 5, 6, 4])] 设置 many2many to ids [8, 5, 6, 4]
​    one2many
​    (0, 0,{ values })根据values里面的信息新建一个记录。
​    (1,ID,{values}) 更新id=ID的记录（对id=ID的执行write 写入values里面的数据）
​    (2,ID) 删除id=ID的数据（调用unlink方法，删除数据以及整个主从数据链接关系）
​    例子：
​    [(0,0,{'field_name':field_value_record1,...}),(0,0,{'field_name':field_value_record})]
​    many2one的字段比较简单，直接填入已经存在的数据的id或者填入False删除原来的记录。

隐藏的常用技巧

直接隐藏

```xml
<group name="owner" position="attributes">
     <attribute name="invisible">True</attribute>
</group>
```

满足某些条件的隐藏

```xml
<xpath expr="//field[@name='parent_id']" position='attributes'>
     <attribute name="attrs">{'invisible': [('passenger','=', True)]}</attribute>
</xpath>
<group col="4" string='旅客信息' attrs="{'invisible': [('supplier','=', True)]}"></group>

```

通过组来隐藏

```xml
<xpath expr="//field[@name='type']" position="attributes">
     <attribute name="groups">base.group_no_one</attribute>
</xpath>
```

菜单的隐藏

```xml
<record model="ir.ui.menu" id="crm.menu_crm_opportunities">
      <field eval="[(6,0, [ref('base.group_no_one'),])]" name="groups_id"/>
</record>
```

代码分析中的运用

字段显示权限

```xml
<field name="company_id" groups="base.group_multi_company" widget="selection"/>
```

在model中判断

```python
self.pool.get('res.users').has_group(cr, uid, 'sale.group_discount_per_so_line')
```



## 访问控制

由`ir.model.access`记录管理，定义对整个模型的访问。

每个访问控制都有一个模型，它授予权限，授予权限以及可选的组。

访问控制是附加的，对于给定的模型，用户可以访问授予其任何组的所有权限：如果用户属于允许写入的一个组而另一个允许删除的组，则它们都可以写入和删除。

如果未指定组，则访问控制适用于所有用户，否则仅适用于给定组的成员。

可用权限是creation（`perm_create`），search and reading（`perm_read`），更新现有记录（`perm_write`）和删除现有记录（`perm_unlink`）

security/ir.model.access.csv

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_purchase_requisition_type,purchase.requisition.type,model_purchase_requisition_type,purchase.group_purchase_user,1,0,0,0
access_purchase_requisition_type_manager,purchase.requisition.type,model_purchase_requisition_type,purchase.group_purchase_manager,1,1,1,1
access_purchase_requisition,purchase.requisition,model_purchase_requisition,purchase.group_purchase_user,1,1,1,1
access_purchase_requisition_line_purchase_user,purchase.requisition.line,model_purchase_requisition_line,purchase.group_purchase_user,1,1,1,1
access_purchase_requisition_manager,purchase.requisition manager,model_purchase_requisition,purchase.group_purchase_manager,1,0,0,0
access_purchase_requisition_line_manager,purchase.requisition.line manager,model_purchase_requisition_line,purchase.group_purchase_manager,1,0,0,0
access_purchase_requisition_stock_manager,purchase.requisition,model_purchase_requisition,stock.group_stock_manager,1,0,1,0
access_purchase_requisition_line_stock_manager,purchase.requisition.line,model_purchase_requisition_line,stock.group_stock_manager,1,0,1,0
```

ir.model.access.csv 文件：
示例：
id					name	model_id:id					group_id:id		perm_read	perm_write	perm_create	perm_unlink
access_xxx	xxxxx	model_website_menu	base.group_website_designer	1	1	1	1
model_id:id 对应的对象模型，
写法示例：website.model_website_config_settings
如果内容本身在website模块中则可以省略website.
后面则为模型的name将”.”替换成”-“的结果，在前面加model_
group_id:id 哪个组
perm_read、perm_write、perm_create、perm_unlink 增删改查权限。1 有权限 0 无权限



## 记录规则

记录规则是记录必须满足的条件，允许操作（创建，读取，更新或删除）。在应用访问控制之后，它将逐个记录地应用。

记录规则是一个记录模型”ir.rule”，关联到一个模型。

记录规则有：

- 适用的模型
- 它应用的一组权限（例如，如果`perm_read`设置，则仅在读取记录时检查规则）
- 应用规则的一组用户组，如果未指定组，则规则为*全局*
- 一个[domain](https://www.odoo.com/documentation/12.0/reference/orm.html#reference-orm-domains)用来检查一个给定的记录是否符合规则（和访问）或没有（和无法访问）。在上下文中使用两个变量评估域：`user`是当前用户的记录，`time`是[time module](https://docs.python.org/2/library/time.html)

全局规则和组规则（限于特定组的规则与适用于所有用户的组的规则）使用方式完全不同：

- 全局规则是减法的，它们*必须全部*匹配才能访问记录
- 组规则是附加的，如果它们中的*任何*一个匹配（并且所有全局规则都匹配），则可以访问该记录

这意味着第一个*组规则*限制访问，但任何进一步的 *组规则都会*扩展它，而*全局规则*只能限制访问（或不起作用）。

####警告

​	记录规则不适用于管理员用户

security/*.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
<data noupdate="1">
    <record model="ir.rule" id="purchase_requisition_comp_rule">
        <field name="name">Purchase Requisition multi-company</field>
        <field name="model_id" ref="model_purchase_requisition"/>
        <field name="global" eval="True"/>
        <field name="domain_force">['|',('company_id','=',False),('company_id','child_of',[user.company_id.id])]</field>
    </record>
    <record model="ir.rule" id="purchase_requisition_line_comp_rule">
        <field name="name">Purchase requisition Line multi-company</field>
        <field name="model_id" ref="model_purchase_requisition_line"/>
        <field name="global" eval="True"/>
        <field name="domain_force">['|',('company_id','=',False),('company_id','child_of',[user.company_id.id])]</field>
    </record>
<record id="stock_picking_multi_company_rule" model="ir.rule">
    <field name="name">stock.picking multi-company</field>
    <field name="model_id" ref="stock.model_stock_picking"/>
    <field name="global" eval="True"/>
    <field name="active" eval="False"/>
    <field name="domain_force">['|', '|', ('company_id', '=', False), ('company_id','child_of',[user.company_id.id]),('company_id','in',[c.id for c in user.company_ids])]</field>
</record>
<record id="product_template_public" model="ir.rule">
    <field name="name">Public product template</field>
    <field name="model_id" ref="product.model_product_template"/>
    <field name="domain_force">[('website_published', '=', True), ("sale_ok", "=", True)]</field>
    <field name="groups" eval="[(4, ref('base.group_public')), (4, ref('base.group_portal'))]"/>
    <field name="perm_read" eval="True"/>
    <field name="perm_write" eval="False"/>
    <field name="perm_create" eval="False"/>
    <field name="perm_unlink" eval="False"/>
</record>
</data>
</odoo>
```

Domain_force表示自定义Domain 表达式，用于过滤条件，含义是只能访问符合本过滤条件的记录。这里过滤条件是操作人必须是当前用户。

## 字段表示
字段表示权限可以指定权限组能访问记录里的哪个字段，可以在视图和对象上指定字段访问权限。

在视图上指定字段访问权限：

```xml
<field name="arch" type="xml">
    <form string="Scheduled Products">
        <group col="4">
            <field name="name"/>
            <field name="product_id"/>
            <field name="product_qty"/>
            <field name="product_uom" groups="product.group_uom"/>
            <field name="product_uos_qty" groups="product.group_uos"/>
            <field name="product_uos" groups="product.group_uos"/>
        </group>
    </form>
</field>
```

在字段对象定义时指定字段访问权限：

```python
_columns = {
       "gengo_private_key": fields.text("Gengo Private Key", copy=False, groups="base.group_system"),
       "gengo_public_key": fields.text("Gengo Public Key", copy=False, groups="base.group_user"),
       "gengo_comment": fields.text("Comments", help="This comment will be automatically be enclosed in each an every request sent to Gengo", groups="base.group_user"),
       "gengo_auto_approve": fields.boolean("Auto Approve Translation ?", help="Jobs are Automatically Approved by Gengo.", groups="base.group_user"),
       "gengo_sandbox": fields.boolean("Sandbox Mode", help="Check this box if you're using the sandbox mode of Gengo, mainly used for testing purpose."),
}
```

隐藏的常用技巧:

```xml
* 直接隐藏
    <group name="owner" position="attributes">
            <attribute name="invisible">True</attribute>
    </group>
 
* 满足某些条件的隐藏
         <xpath expr="//field[@name='parent_id']" position='attributes'>
             <attribute name="attrs">{'invisible': [('passenger','=', True)]}</attribute>
         </xpath>
    <group col="4" string='旅客信息' attrs="{'invisible': [('supplier','=', True)]}"></group>
 * 通过组来隐藏
    <xpath expr="//field[@name='type']" position="attributes">
                <attribute name="groups">base.group_no_one</attribute>
         </xpath>
* 菜单的隐藏
    <record model="ir.ui.menu" id="crm.menu_crm_opportunities">
            <field eval="[(6,0, [ref('base.group_no_one'),])]" name="groups_id"/>
    </record>
```



## 现场访问

7.0版中的新功能。

ORM [`Field`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Field)可以具有`groups`提供组列表的属性（作为逗号分隔的[外部标识符](https://www.odoo.com/documentation/12.0/glossary.html#term-external-identifiers)串 ）。

如果当前用户不在列出的某个组中，则他将无法访问该字段：

- 受限制的字段会自动从请求的视图中删除
- 受限制的字段将从[`fields_get()`](https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.models.Model.fields_get) 响应中删除
- 尝试（显式地）读取或写入受限制的字段会导致访问错误