from odoo import models, fields


class Genre(models.Model):
    _name = 'game.genre'
    _description = 'Genre model'

    name = fields.Char('Name', required=True)
