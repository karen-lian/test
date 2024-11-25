from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_centralized = fields.Boolean(string="團購", default=False)
