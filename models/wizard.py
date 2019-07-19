from odoo import models, fields, api

class Wizard(models.TransientModel):

    _name = 'cinema.wizard'

    _description = "Wizard: Selling tickets for cinema"

    # treba li store=True i required=True ?
    tickets = fields.Integer(string="Number of tickets (to buy)", store=True, default=0, required=True)

    # vraca sa trenutnim wizardom povezani timetable
    def _default_session(self):
        return self.env['cinema.timetable'].browse(self._context.get('active_id'))

    # treba li reqiured=True ?
    timetable_id = fields.Many2one(comodel_name="cinema.timetable", string="Timetable", default=_default_session)

    @api.multi
    def buy(self):
        for member in self.timetable_id:
            member.sold_seats += self.tickets



