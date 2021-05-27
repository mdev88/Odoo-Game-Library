from odoo import models, fields


class Tag(models.Model):
    _name = 'game.tag'
    _description = 'Tag model'

    name = fields.Char('Name', required=True)
    color = fields.Integer()
