[TOC]



# 会员



## 会员产品创建

### 模型

`erp\addons\membership\models\product.py`

```python
class Product(models.Model):
    _inherit = 'product.template'
	#是否为会员产品
    membership = fields.Boolean(help='Check if the product is eligible for membership.')
    #会员有效期开始
    membership_date_from = fields.Date(string='Membership Start Date',
        help='Date from which membership becomes active.')
    #会员有效期结束
    membership_date_to = fields.Date(string='Membership End Date',
        help='Date until which membership remains active.')

    _sql_constraints = [
        ('membership_date_greater', 'check(membership_date_to >= membership_date_from)', 'Error ! Ending Date cannot be set before Beginning Date.')
    ]
```

### 视图

`erp\addons\membership\views\product_views.xml`     **tree,search,kanban,form**

menu(name = Members,id = menu_association)   

---> menu(name =Configuration,id = menu_marketing_config_association,action=action_membership_products)

![会员目录](C:\Users\Administrator\Desktop\会员目录.png)

```xml
<record model="ir.ui.view" id="membership_products_form">
```

![会员产品](C:\Users\Administrator\Desktop\会员产品.png)

**产品默认**

```xml
<field name="context">{'membership':True, 'type':'service', 'default_membership': True, 'default_type': 'service'}</field>
```

### 产品发布后在网站 shop中出售



## 会员的产生

会员产品出售时打印发票,同时创建会员记录明细

`addons\membership\models\account_invoice.py`

```python

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'
	def create(self, vals):
		MemberLine.create({
                'partner': invoice_line.invoice_id.partner_id.id,
                'membership_id': invoice_line.product_id.id,
                'member_price': invoice_line.price_unit,
                'date': fields.Date.today(),
                'date_from': date_from,
                'date_to': date_to,
                'account_invoice_line': invoice_line.id,
            })
```





```python
class MembershipLine(models.Model):
    _name = 'membership.membership_line'
#合作伙伴(会员角色)
partner = fields.Many2one('res.partner', string='Partner', ondelete='cascade', index=True)
#产品
membership_id = fields.Many2one('product.product', string="Membership", required=True)
#开始时间
date_from = fields.Date(string='From', readonly=True)
#结束时间
date_to = fields.Date(string='To', readonly=True)
#取消时间
date_cancel = fields.Date(string='Cancel date')
#加入会员时间
date = fields.Date(string='Join Date',help="Date on which member has joined the membership")
#会员价格
member_price = fields.Float(string='Membership Fee',
        digits=dp.get_precision('Product Price'), required=True,
        help='Amount for the membership')
#发票明细
account_invoice_line = fields.Many2one('account.invoice.line', string='Account Invoice line', readonly=True, ondelete='cascade')
#发票
account_invoice_id = fields.Many2one('account.invoice', related='account_invoice_line.invoice_id', string='Invoice', readonly=True)
#公司
company_id = fields.Many2one('res.company', related='account_invoice_line.invoice_id.company_id', string="Company", readonly=True, store=True)
#会员状态，它指示成员身份状态
state = fields.Selection(STATE, compute='_compute_state', string='Membership Status', store=True,
        help="It indicates the membership status.\n"
             "-Non Member: A member who has not applied for any membership.\n"
             "-Cancelled Member: A member who has cancelled his membership.\n"
             "-Old Member: A member whose membership date has expired.\n"
             "-Waiting Member: A member who has applied for the membership and whose invoice is going to be created.\n"
             "-Invoiced Member: A member whose invoice has been created.\n"
             "-Paid Member: A member who has paid the membership amount.")
STATE = [
    #默认
    ('none', 'Non Member'),#非成员：没有申请任何成员资格的成员。
    
    #partner.membership_cancel and today > partner.membership_cancel
    ('canceled', 'Cancelled Member'),#取消成员：取消其成员资格的成员。
    
    #partner.membership_stop and today > partner.membership_stop
    ('old', 'Old Member'),#旧成员：成员资格日期已过期的成员。
    
    ('free', 'Free Member'),#免费会员：当partner.free_member=True时 , 会员不会退化为canceled,old
    
    #根据 account_invoice.state 修改以下状态
    #'draft'
    ('waiting', 'Waiting Member'),#等待成员：已申请成员身份并将要创建其发票的成员。
    #'open'
    ('invoiced', 'Invoiced Member'),#已开票成员：其发票已创建的成员。
    #'paid'
    ('paid', 'Paid Member'),#付费会员：已支付会员金额的会员
    
]
```





```python
class Partner(models.Model):
    _inherit = 'res.partner'
#联合会员
associate_member = fields.Many2one('res.partner', string='Associate Member',
help="A member with whom you want to associate your membership."
"It will consider the membership state of the associated member.")
#要与其关联成员身份的成员。它将考虑关联成员的成员身份状态。

member_lines = fields.One2many('membership.membership_line', 'partner', string='Membership')

#是否是免费会员(如果是，会员到期或取消会成为Free Member)
free_member = fields.Boolean(string='Free Member',
        help="Select if you want to give free membership.")
#会费(未使用)
membership_amount = fields.Float(string='Membership Amount', digits=(16, 2),help='The price negotiated by the partner')

membership_state =
fields.Selection(membership.STATE,compute='_compute_membership_state',
        string='Current Membership Status', store=True,
        help='It indicates the membership state.\n'
             '-Non Member: A partner who has not applied for any membership.\n'
             '-Cancelled Member: A member who has cancelled his membership.\n'
             '-Old Member: A member whose membership date has expired.\n'
             '-Waiting Member: A member who has applied for the membership and whose invoice is going to be created.\n'
             '-Invoiced Member: A member whose invoice has been created.\n'
             '-Paying member: A member who has paid the membership fee.')
membership_start = fields.Date(compute='_compute_membership_start',
        string ='Membership Start Date', store=True,
        help="Date from which membership becomes active.")
membership_stop = fields.Date(compute='_compute_membership_stop',
        string ='Membership End Date', store=True,
        help="Date until which membership remains active.")
membership_cancel = fields.Date(compute='_compute_membership_cancel',
        string ='Cancel Membership Date', store=True,
        help="Date on which membership has been cancelled")
```



### 会员时间状态跟踪

```xml
<record id="ir_cron_update_membership" model="ir.cron">
            <field name="name">Membership: update memberships</field>
            <field name="model_id" ref="base.model_res_partner"/>
            <field name="state">code</field>
            <field name="code">model._cron_update_membership()</field>
            <field name="interval_type">days</field>
            <field name="numbercall">-1</field>
        </record>
```

```python
def _cron_update_membership(self):
        partners = self.search([('membership_state', 'in', ['invoiced', 'paid'])])
        # mark the field to be recomputed, and recompute it
        partners._recompute_todo(self._fields['membership_state'])
        self.recompute()
```





