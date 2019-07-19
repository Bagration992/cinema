from odoo import api, fields, models

class Movie(models.Model):

    _name = 'cinema.movie'

    name = fields.Char(string="Title of the movie", required=True)

    genre = fields.Selection([
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('scifi', 'SciFi'),
        ('other', 'Other'),
        ('not_specified', 'Not specified')
    ], string="Genre", required=False, default="not_specified")

    description = fields.Text(string="Description", required=False)

    image = fields.Binary(string="Image", attachment=True, required=False, help="Image of the movie")

