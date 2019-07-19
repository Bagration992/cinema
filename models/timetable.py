# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class timetable(models.Model):

    _name = 'cinema.timetable'

    date = fields.Datetime(string="Projection time", required=True)

    movie = fields.Many2one(comodel_name="cinema.movie", string="Movie", required=True)

    premiere = fields.Boolean(string="Premiere", required=False, default=False)

    room = fields.Many2one(comodel_name="cinema.room", string="Room", required=False)

    total_seats = fields.Integer(compute="_get_total_seats", store=True, string="Total seats")

    sold_seats = fields.Integer(string="Number of sold seats", store=True, default=1)

    remaining_seats = fields.Integer(compute="_get_remaining_seats", store=True, string="Number of seats remaining")

    @api.depends('room')
    def _get_total_seats(self):
        for row in self:
            row.total_seats = row.room.capacity

    @api.depends('sold_seats', 'total_seats')
    def _get_remaining_seats(self):
        for row in self:
            row.remaining_seats = row.total_seats - row.sold_seats