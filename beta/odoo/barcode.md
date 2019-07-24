





### 在模型中

```python
class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order', 'barcodes.barcode_events_mixin']
    #继承'barcodes.barcode_events_mixin'

    def _add_product(self, product, qty=1.0):
		pass
    def on_barcode_scanned(self, barcode):
        product = self.env['product.product'].search(['|', ('barcode', '=', barcode)])
        if product:
            self._add_product(product)
```



### xml表单

```xml
<form position="inside">
    <field name="_barcode_scanned" widget="barcode_handler"/>
</form>
```



