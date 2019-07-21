from odoo import models, fields, api

class Wizard(models.TransientModel):

    _name = 'cinema.wizard'

    _description = "Wizard: Selling tickets for cinema"

    tickets = fields.Integer(string="Number of tickets (to buy)", store=True, default=0, required=True)

    # returns timetable connected to current wizard
    def _default_timetable(self):
        return self.env['cinema.timetable'].browse(self._context.get('active_id'))

    #
    timetable_id = fields.Many2one(comodel_name="cinema.timetable", string="Timetable",
                                   default=_default_timetable, reqiured=True)

    #
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner", required=True)

    # required=True
    account_id = fields.Many2one(comodel_name='account.account', string='Account')

    # returns default product
    def _default_product(self):
        lst = self.env['product.product']
        return lst

    #
    product_id = fields.Many2one(comodel_name='product.product', string="Product", required=True)

    @api.multi
    def buy(self):

        # part of function incrementing number of seats sold
        for member in self.timetable_id:
            member.sold_seats += self.tickets


        # part of function creating invoice
        invoice_vals = {
            'partner_id': self.partner_id.id,
            'invoice_line_ids': [(0, 0, {'name': 'Myinvoice', 'price_unit': 1, 'product_id': self.product_id.id,
                                         'quantity': self.tickets, 'account_id': self.account_id.id})]
        }

        self.env['account.invoice'].create(invoice_vals)
