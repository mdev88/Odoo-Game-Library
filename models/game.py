from odoo import models, fields


class Game(models.Model):
    _name = 'game.model'
    _description = 'Game model'

    name = fields.Char('Title', required=True)
    year = fields.Char('Year', help='Release date')
    genre = fields.Selection([('action', 'Action'),
                              ('adventure', 'Adventure'),
                              ('fps', 'FPS'),
                              ('horror', 'Horror'),
                              ('simulation', 'Simulation'),
                              ('strategy', 'Strategy'),
                              ('other', 'Other')])
    completed = fields.Boolean('Completed')
    cover = fields.Binary('Cover')
    wikipedia = fields.Char('Wikipedia')