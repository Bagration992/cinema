from odoo import api, fields, models

class Merchandise(models.Model):

    # is it needed?
    #_name ='product.product'

    _inherit = "product.product"

    merch = fields.Boolean(string="Merchandise", required=False, default=False)

