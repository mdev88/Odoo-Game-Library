from odoo import models, fields, api


class Game(models.Model):
    _name = 'game.model'
    _description = 'Game model'
    _order = 'name'

    @api.depends('completed')
    def get_status(self):
        for rec in self:
            if rec.completed:
                rec.status = 'Completed'
            else:
                rec.status = 'Not completed'

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
    status = fields.Char('', compute='get_status')
    cover = fields.Binary('Cover')
    wikipedia = fields.Char('Wikipedia')