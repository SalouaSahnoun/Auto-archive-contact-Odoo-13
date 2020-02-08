# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = "Res partner inherit"

    # Check if the related client/company is archived

    if_archived = fields.Selection([('yes', "Yes"),
                                    ('no', "No")], string="If archived", compute='get_if_archived')

    def get_if_archived(self):

        # Check if archived

        for active in self:
            if active.active is True:
                active.if_archived = 'no'
            else:
                active.if_archived = 'yes'

        # Auto-archive contact if related_company archived

        for parent_id in self.search([('is_company', '=', True), ('active', '=', False)]):

            if parent_id.is_company is True and parent_id.active is False:

                for child_id in self.search([('is_company', '=', False), ('parent_id', 'in', parent_id.name)]):

                    if child_id.is_company is False and child_id.parent_id in parent_id:

                        child_id.active = False

