from odoo import api, fields, models, _
from odoo.exceptions import UserError
class GroupBuying(models.Model):
    _name = 'group.buying'
    _description = '團購表單'

    name = fields.Char(string='開團單號', required=True, copy=False, default='New')
    open_date = fields.Date(string='開團日期', required=True, tracking=True)
    close_date = fields.Date(string='結單日期', required=True)
    user_id = fields.Many2one('res.users', string='開團人員', default=lambda self: self.env.user)
    active = fields.Boolean(string='Active', default=True)

    group_buying_ids = fields.One2many('group.buying.line', 'group_buying_id', string='團購明細')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('group.buying') or '/'
        res = super(GroupBuying, self).create(vals)
        return res

    @api.constrains('open_date', 'close_date')
    def _check_date(self):
        if self.open_date and self.close_date and self.close_date < self.open_date:
            raise UserError(_("開團日期需早於結單日期!"))


class GroupBuyingLine(models.Model):
    _name = 'group.buying.line'
    _description = '團購表單明細'

    group_buying_id = fields.Many2one('group.buying', string='開團單號', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='跟團人員')
    product_id = fields.Many2one('product.product', string='商品')
    qty = fields.Integer(string='數量', default=1.0)