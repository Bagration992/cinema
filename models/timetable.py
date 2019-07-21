# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError

class timetable(models.Model):

    _name = 'cinema.timetable'

    date = fields.Datetime(string="Projection time", required=True)

    movie = fields.Many2one(comodel_name="cinema.movie", string="Movie", required=True)

    premiere = fields.Boolean(string="Premiere", required=False, default=False)

    room = fields.Many2one(comodel_name="cinema.room", string="Room", required=False)

    total_seats = fields.Integer(compute="_get_total_seats", store=True, string="Total seats")

    sold_seats = fields.Integer(string="Number of sold seats", store=True, default=0)

    remaining_seats = fields.Integer(compute="_get_remaining_seats", store=True, string="Number of seats remaining")

    # calculating number of seats
    @api.depends('room.capacity')
    def _get_total_seats(self):
        for row in self:
            row.total_seats = row.room.capacity

    # update in case sold seats increase (or total seats change)
    @api.depends('sold_seats', 'total_seats')
    def _get_remaining_seats(self):
        for row in self:
            subtraction = row.total_seats - row.sold_seats
            if subtraction < 0:
                raise UserError("Number of sold seats cannot exceed number of total seats")
            else:
                row.remaining_seats = subtraction



