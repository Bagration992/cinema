from odoo import api, fields, models

class Merchandise(models.Model):

    # is it needed?
    #_name ='product.product'

    _inherit = "product.product"

    # named merch because class name is Merchandise
    merch = fields.Boolean(string="Merchandise", required=False, default=False)

