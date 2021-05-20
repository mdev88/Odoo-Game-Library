from odoo import models, fields


class GameModel(models.Model):
    _name = 'game.model'
    _description = 'Game model'

    name = fields.Char(string='Title', required=True)
    year = fields.Integer('Year')
    genre = fields.Selection([('action', 'Action'),
                              ('adventure', 'Adventure'),
                              ('fps', 'FPS'),
                              ('simulation', 'Simulation'),
                              ('strategy', 'Strategy'),
                              ('other', 'Other')])
    completed = fields.Boolean('Completed')
    cover = fields.Binary('Cover')
