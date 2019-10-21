# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    nxt_razon_social = fields.Char(string="Razon social")
    nxt_ruc = fields.Char(string="R.U.C.")
    nxt_agente_retencion = fields.Boolean(string="Agente de retencion")
    nxt_buen_contribuyente = fields.Boolean(string="Buen contribuyente")
    nxt_plan_contable = fields.Selection(
        string = "Plan contable",    
        selection = [("01", "01. General empresarial"), 
                    ("02", "02. Por definir")],
        default = "01"
    )
    
# FIN ResCompany
