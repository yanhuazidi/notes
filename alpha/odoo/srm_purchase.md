

[TOC]



# purchase_requisition采购协议

此模块允许您管理采购协议。

管理投标招募以及一揽子订单。招标用于从不同的供应商中获取 竞争报价，并选择最合适的供应商。

总括订单是您与供应商达成的协议，可以从预定的价格中受益。

## models

```python
class PurchaseRequisitionType(models.Model):
    _name = "purchase.requisition.type"
    _description = "Purchase Requisition Type"
    _order = "sequence"

    name = fields.Char(string='Agreement Type', required=True, translate=True)
    sequence = fields.Integer(default=1)
    exclusive = fields.Selection([
        ('exclusive独家', 'Select only one RFQ (exclusive)'), ('multiple多个', 'Select multiple RFQ')],
        string='Agreement协议 Selection Type', required=True, default='multiple',
            help="""只选择一个RFQ (exclusive):当一个采购订单被确认时，取消剩余的采购订单
选择多个RFQ:允许多个购买订单。在确认购买订单时，它不会取消剩余的订单""")
    quantity_copy = fields.Selection([
        ('copy', 'Use quantities of agreement使用协议数量'), ('none', 'Set quantities manually手动设置数量')],string='Quantities', required=True, default='none')
    line_copy = fields.Selection([
        ('copy', 'Use lines of agreement使用协议条款'), ('none', 'Do not create RfQ lines automatically不自动创建RfQ行')],
        string='Lines', required=True, default='copy')
```



```python
PURCHASE_REQUISITION_STATES = [
    ('draft', 'Draft'),#草稿
    ('ongoing', 'Ongoing'),#正在进行
    ('in_progress', 'Confirmed'),#已确认
    ('open', 'Bid Selection'),#比价选择
    ('done', 'Closed'),#关闭
    ('cancel', 'Cancelled')#取消
]
class PurchaseRequisition(models.Model):
    _name = "purchase.requisition"
    _description = "Purchase Requisition"
    _inherit = ['mail.thread']
    _order = "id desc"

    def _get_picking_in(self):#picking_type_id 
        pick_in = self.env.ref('stock.picking_type_in', raise_if_not_found=False)
        company = self.env['res.company']._company_default_get('purchase.requisition')
        if not pick_in or pick_in.sudo().warehouse_id.company_id.id != company.id:
            pick_in = self.env['stock.picking.type'].search(
                [('warehouse_id.company_id', '=', company.id), ('code', '=', 'incoming')],
                limit=1,
            )
        return pick_in

    def _get_type_id(self):#获取采购协议的类型对象type_id
        return self.env['purchase.requisition.type'].search([], limit=1)

    name = fields.Char(string='Agreement Reference', required=True, copy=False, default='New', readonly=True)
    #原单据
    origin = fields.Char(string='Source Document')
    #订单数量
    order_count = fields.Integer(compute='_compute_orders_number', string='Number of Orders')
    #供应商
    vendor_id = fields.Many2one('res.partner', string="Vendor")
    #采购协议类型
    type_id = fields.Many2one('purchase.requisition.type', string="Agreement Type", required=True, default=_get_type_id)
    #订单日期
    ordering_date = fields.Date(string="Ordering Date", track_visibility='onchange')
    #协议截止日期
    date_end = fields.Datetime(string='Agreement Deadline', track_visibility='onchange')
    #发货日期
    schedule_date = fields.Date(string='Delivery Date', index=True, help="The expected and scheduled delivery date where all the products are received", track_visibility='onchange')
    #销售代表
    user_id = fields.Many2one('res.users', string='Purchase Representative', default= lambda self: self.env.user)
    #内容
    description = fields.Text()
    #公司
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env['res.company']._company_default_get('purchase.requisition'))
    #采购订单s
    purchase_ids = fields.One2many('purchase.order', 'requisition_id', string='Purchase Orders', states={'done': [('readonly', True)]})
    #协议明细行s
    line_ids = fields.One2many('purchase.requisition.line', 'requisition_id', string='Products to Purchase', states={'done': [('readonly', True)]}, copy=True)
    #仓库
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
    #协议状态
    state = fields.Selection(PURCHASE_REQUISITION_STATES,
                              'Status', track_visibility='onchange', required=True,
                              copy=False, default='draft')
    #总括订单状态
    state_blanket_order = fields.Selection(PURCHASE_REQUISITION_STATES, compute='_set_state')
    #入库物流类型
    picking_type_id = fields.Many2one('stock.picking.type', 'Operation Type', required=True, default=_get_picking_in)
    #数量拷贝
    is_quantity_copy = fields.Selection(related='type_id.quantity_copy', readonly=True)
    #货币
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id.id)

    @api.depends('state')
    def _set_state(self):#state_blanket_order
        self.state_blanket_order = self.state

    @api.onchange('vendor_id')
    def _onchange_vendor(self):#改变供应商时检查此供应商是否有在进行的总括协议
        requisitions = self.env['purchase.requisition'].search([
            ('vendor_id', '=', self.vendor_id.id),
            ('state', '=', 'ongoing'),
            ('type_id.quantity_copy', '=', 'none'),
        ])
        if any(requisitions):
            title = _("Warning for %s") % self.vendor_id.name
            message = _("There is already an open blanket order for this supplier. We suggest you to use to complete this open blanket order instead of creating a new one.")
            warning = {
                'title': title,
                'message': message
            }
            return {'warning': warning}

    @api.multi
    @api.depends('purchase_ids')
    def _compute_orders_number(self):
        for requisition in self:#order_count
            requisition.order_count = len(requisition.purchase_ids)

    @api.multi
    def action_cancel(self):#取消此协议
        # try to set all associated quotations to cancel state
        for requisition in self:
            for requisition_line in requisition.line_ids:
                requisition_line.supplier_info_ids.unlink()
            requisition.purchase_ids.button_cancel()
            for po in requisition.purchase_ids:
                po.message_post(body=_('Cancelled by the agreement associated to this quotation.'))
        self.write({'state': 'cancel'})

    @api.multi
    def action_in_progress(self):#确认按钮
        self.ensure_one()
        if not all(obj.line_ids for obj in self):#产品明细行为空
            raise UserError(_("You cannot confirm agreement '%s' because there is no product line.") % self.name)
        if self.type_id.quantity_copy == 'none' and self.vendor_id:
            for requisition_line in self.line_ids:
                if requisition_line.price_unit <= 0.0:
                    raise UserError(_('You cannot confirm the blanket order without price.'))
                if requisition_line.product_qty <= 0.0:
                    raise UserError(_('You cannot confirm the blanket order without quantity.'))
                requisition_line.create_supplier_info()
            self.write({'state': 'ongoing'})
        else:
            self.write({'state': 'in_progress'})
        # Set the sequence number regarding the requisition type
        if self.name == 'New':
            if self.is_quantity_copy != 'none':
                self.name = self.env['ir.sequence'].next_by_code('purchase.requisition.purchase.tender')
            else:
                self.name = self.env['ir.sequence'].next_by_code('purchase.requisition.blanket.order')

    @api.multi
    def action_open(self):
        self.write({'state': 'open'})

    def action_draft(self):#置为草稿
        self.ensure_one()
        self.name = 'New'
        self.write({'state': 'draft'})

    @api.multi
    def action_done(self):
        """
        Generate all purchase order based on selected lines, should only be called on one agreement at a time
        """
        if any(purchase_order.state in ['draft', 'sent', 'to approve'] for purchase_order in self.mapped('purchase_ids')):
            raise UserError(_('You have to cancel or validate every RfQ before closing the purchase requisition.'))
        for requisition in self:
            for requisition_line in requisition.line_ids:
                requisition_line.supplier_info_ids.unlink()
        self.write({'state': 'done'})

    def _prepare_tender_values(self, product_id, product_qty, product_uom, location_id, name, origin, values):
        return{
            'origin': origin,
            'date_end': values['date_planned'],
            'warehouse_id': values.get('warehouse_id') and values['warehouse_id'].id or False,
            'company_id': values['company_id'].id,
            'line_ids': [(0, 0, {
                'product_id': product_id.id,
                'product_uom_id': product_uom.id,
                'product_qty': product_qty,
                'move_dest_id': values.get('move_dest_ids') and values['move_dest_ids'][0].id or False,
            })],
        }

    def unlink(self):
        if any(requisition.state not in ('draft', 'cancel') for requisition in self):
            raise UserError(_('You can only delete draft requisitions.'))
        # Draft requisitions could have some requisition lines.
        self.mapped('line_ids').unlink()
        return super(PurchaseRequisition, self).unlink()
```

```python
class SupplierInfo(models.Model):#产品供应商信息表
    _inherit = "product.supplierinfo"
    _order = 'sequence, purchase_requisition_id desc, min_qty desc, price'
	#总括订单协议
    purchase_requisition_id = fields.Many2one('purchase.requisition', related='purchase_requisition_line_id.requisition_id', string='Blanket order', readonly=False)
    #采购招标协议明细行
    purchase_requisition_line_id = fields.Many2one('purchase.requisition.line')

```



```python
class PurchaseRequisitionLine(models.Model):#明细行
    _name = "purchase.requisition.line"
    _description = "Purchase Requisition Line"
    _rec_name = 'product_id'
	#产品
	product_id = fields.Many2one('product.product', string='Product', domain=[('purchase_ok', '=', 		True)], required=True)
    #计量单位
    product_uom_id = fields.Many2one('uom.uom', string='Product Unit of Measure')
    #数量
    product_qty = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of 		Measure'))
    #单价
    price_unit = fields.Float(string='Unit Price', digits=dp.get_precision('Product Price'))
    #已购数量
    qty_ordered = fields.Float(compute='_compute_ordered_qty', string='Ordered Quantities')
    #采购协议
    requisition_id = fields.Many2one('purchase.requisition', required=True, string='Purchase Agreement', ondelete='cascade')
    #采购公司
    company_id = fields.Many2one('res.company', related='requisition_id.company_id', string='Company', store=True, readonly=True, default= lambda self: self.env['res.company']._company_default_get('purchase.requisition.line'))
    #分析账号
    account_analytic_id = fields.Many2one('account.analytic.account', string='Analytic Account')
    #分析标签
    analytic_tag_ids = fields.Many2many('account.analytic.tag', string='Analytic Tags')
    #计划日期
    schedule_date = fields.Date(string='Scheduled Date')
    #下游库存移动
    move_dest_id = fields.Many2one('stock.move', 'Downstream Move')
    #产品供应商信息表
    supplier_info_ids = fields.One2many('product.supplierinfo', 'purchase_requisition_line_id')
```



# purchase采购管理

采购单、入库单、采购发票

# purchase_stock采购库存

采购订单, 入库单, 库存的供应商订单



# account_payment_purchase账户付款购买

为采购订单添加银行账户和支付模式

该模块为采购订单添加了两个字段:银行账户和支付模式。这些字段从合作伙伴复制到采购订单，然后从采购订单复制到供应商发票。

这个模块类似于purchase_payment模块;主要区别在于它不依赖于account_payment_extension模块(它不是惟一一个与account_payment_extension冲突的模块;银行插件中的所有SEPA模块都与account_payment_extension冲突)。

# procurement_mto_analytic采购分析(MTO)

该模块考虑了从销售订单到创建的采购订单行之间的分析值。

该模块从销售订单分析账户中设置采购订单行分析账户



# purchase_mrp销售与 MRP 管理

此模块为用户提供了同时安装 mrp 和购买模块的功能。

通常在我们想要跟踪从采购订单中生成的生产订单时使用。



# sale_purchase销售采购

允许外包服务。该模块允许销售提供的服务 并自动生成给供应商的采购订单。



# purchase_delivery_split_date

采购交货日期

当安装此模块时，您确认的每个采购订单将为采购订单行中指示的每个进料日期生成一个传入发货。

一旦订单被确认,后续更改预定日期的订单行相应的股票走势会产生重组传入的出货量,在需要的时候创建/删除新传入的出货,确保每个传入的货物包含移动接收相同的日期。

此模块还设计用于可扩展性，以便您可以在其他模块中定义拆分交付的新标准。

允许您确认的采购订单为采购订单行中指定的每个预期日期生成一个进货装运

# srm_purchasseSRM采购协同

扩展Odoo官方的采购模块，提供一个供应商门户，让您可以与您的供应商在线协同报价、订单、发货。

1. 邀请供应商注册供应商门户账号。
2. 供应商门户提供的功能： - 采购员“通过EMAIL发送”询价单后，供应商可在线查看询价单并提交报价，不再需要采购员手动录入价格到询价单。 - 采购员“确认订单”后，供应商可在线查看订单并发货，系统自动生成一张待入库的入库单。

这是知链SRM采购模块的开源社区版。您可以联系我们以获取功能更强大的商业版本。下面列出了一部分商业版提供的功能特性。

1. 更强大的供应商门户： - 发货前，供应商可以提交预估的发货计划。 - 发货后，供应商可以查看采购方是否已经收货入库。 - 支持分批发货。 - 支持订单自定义审批流。
2. 单独的且功能更强大的在线询报价/招标模块。 - 采购招标一次邀请多家供应商在线询比价。 - 支持多轮次报价。 - 在线报价分析。 - 询比价结果自动导入供应商价格表。

## controllers



## models

### purchase_order.py



### purchase_order_line.py

### product_product.py



## views













