import base64

import requests

from odoo import models, fields, api


class Game(models.Model):
    _name = 'game.model'
    _description = 'Game model'
    _order = 'name'

    @staticmethod
    def load_image_from_url(url):
        data = base64.b64encode(requests.get(url.strip()).content).replace(b'\n', b'')
        return data

    @api.depends('completed')
    def get_status(self):
        for rec in self:
            if rec.completed:
                rec.status = 'Completed'
            else:
                rec.status = 'Not completed'

    @api.depends('cover_url')
    def _compute_image(self):
        print('_compute_image called')
        for record in self:
            cover = None
            if record.cover_url:
                cover = self.load_image_from_url(record.cover_url)
            record.update({'cover': cover, })

    name = fields.Char('Title', required=True)
    year = fields.Char('Year', help='Release date')
    # genre = fields.Selection([('action', 'Action'),
    #                           ('adventure', 'Adventure'),
    #                           ('fps', 'FPS'),
    #                           ('horror', 'Horror'),
    #                           ('simulation', 'Simulation'),
    #                           ('strategy', 'Strategy'),
    #                           ('other', 'Other')])
    genre = fields.Many2one('game.genre', 'Genre')
    tags = fields.Many2many('game.tag')
    completed = fields.Boolean('Completed')
    status = fields.Char('Status', compute='get_status')
    wikipedia = fields.Char('Wikipedia')
    cover = fields.Binary('Cover', compute='_compute_image', store=True, attachment=False)
    cover_url = fields.Char('Cover URL')
