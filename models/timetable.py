# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class timetable(models.Model):

    _name = 'cinema.timetable'

    date = fields.Datetime(string="Projection starting date", required=True)

    movie = fields.Many2one(comodel_name="cinema.movie", string="Movie", required=True)

    premiere = fields.Boolean(string="Premiere", required=False, default=False)

