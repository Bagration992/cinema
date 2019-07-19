from odoo import api, fields, models

class Room(models.Model):

    _name = 'cinema.room'

    timetable_id = fields.One2many('cinema.timetable', 'room', string="Timetable")

    capacity = fields.Integer(string="Capacity", store=True, default=100, required=True)

