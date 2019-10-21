# -*- coding: utf-8 -*-
from odoo import models, fields, api

class NextProPeCatalogTmpl(models.Model):
    _name = 'nextpro_pe.catalogo.tmpl'
    _description = 'Catalog Template'

    code = fields.Char(string='Code', size=4, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)

    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result

class NextProPeCatalog01(models.Model):
    _name = 'nextpro_pe.catalogo.01'
    _description = 'Codigo de Tipo de documento'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    label = fields.Char(string='Label to print', size=256)

class NextProPeCatalog05(models.Model):
    _name = "nextpro_pe.catalogo.05"
    _description = 'Codigo de Tipo de tributo'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    un_5153 = fields.Char(string='UN/ECE 5153-Duty or tax or fee type name code', size=5)
    un_5103 = fields.Char(string='UN/ECE 5305-Duty or tax or fee category code', size=1)

class NextProPeCatalog06(models.Model):
    _name = "nextpro_pe.catalogo.06"
    _description = 'Tipo de documento de Identidad'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=4, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)
    default = fields.Char(string='Valor por defecto', size=128)
    
    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result
               
class NextProPeCatalog07(models.Model):
    _name = "nextpro_pe.catalogo.07"
    _description = 'Codigos de Tipo de Afectacion del IGV'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    no_onerosa = fields.Boolean(string='No onerosa')
    type = fields.Selection([('gravado','Gravado'),('exonerado','Exonerado'),('inafecto','Inafecto')],string='Tipo')
    
class NextProPeCatalog08(models.Model):
    _name = "nextpro_pe.catalogo.08"
    _description = 'Codigos de Tipo de Afectacion del IGV'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog09(models.Model):
    _name = "nextpro_pe.catalogo.09"
    _description = 'Codigos de Tipo de Nota de Credito Electronica'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog10(models.Model):
    _name = "nextpro_pe.catalogo.10"
    _description = 'Codigos de Tipo de Nota de Debito Electronica'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog11(models.Model):
    _name = "nextpro_pe.catalogo.11"
    _description = 'Codigo de Tipo de Valor de Venta'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog12(models.Model):
    _name = "nextpro_pe.catalogo.12"
    _description = 'Codigos -Documentos Relacionados Tributarios'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog14(models.Model):
    _name = "nextpro_pe.catalogo.14"
    _description = 'Codigos - Otros Conceptos Tributarios'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog15(models.Model):
    _name = "nextpro_pe.catalogo.15"
    _description = 'Codigos-Elementos Adicionales en la Factura Electrónica '
    _inherit = 'nextpro_pe.catalogo.tmpl'

    name = fields.Char(string='Value', size=256, index=True, required=True)

class NextProPeCatalog16(models.Model):
    _name = "nextpro_pe.catalogo.16"
    _description = 'Codigos - Tipo de Precio de Venta Unitario'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog17(models.Model):
    _name = "nextpro_pe.catalogo.17"
    _description = 'Codigos -Tipo de Operacion'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog18(models.Model):
    _name = "nextpro_pe.catalogo.18"
    _description = 'Codigos - Modalidad de  Traslado'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog19(models.Model):
    _name = "nextpro_pe.catalogo.19"
    _description = 'Codigos de Estado de Item'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog20(models.Model):
    _name = "nextpro_pe.catalogo.20"
    _description = 'Codigos - Motivo de Traslado'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog21(models.Model):
    _name = "nextpro_pe.catalogo.21"
    _description = 'Codigos-Documentos Relacionados '
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog22(models.Model):
    _name = "nextpro_pe.catalogo.22"
    _description = 'Codigos- Regimenes de Percepcion'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    rate = fields.Char(string='Tasa', size=10, index=True, required=True)

class NextProPeCatalog23(models.Model):
    _name = "nextpro_pe.catalogo.23"
    _description = 'Codigos- Regimenes de Retencion'
    _inherit = 'nextpro_pe.catalogo.tmpl'

class NextProPeCatalog24(models.Model):
    _name = "nextpro_pe.catalogo.24"
    _description = 'Codigos- Recibo Electronico por Servicios Publicos'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    name = fields.Char(string='Service', size=128, index=True, required=True)
    rate_code = fields.Char(string='Rate code', size=4, index=True, required=True)
    
class NextProPeCatalog25(models.Model):
    _name = "nextpro_pe.catalogo.25"
    _description = 'Codigos - Producto SUNAT'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=12, index=True, required=True)

class NextProPeCatalog51(models.Model):
    _name = "nextpro_pe.catalogo.51"
    _description = 'Codigo de  Tipo de Factura'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=12, index=True, required=True)

class NextProPeCatalog52(models.Model):
    _name = "nextpro_pe.catalogo.52"
    _description = 'Codigos de Leyendas'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=12, index=True, required=True)

class NextProPeCatalog53(models.Model):
    _name = "nextpro_pe.catalogo.53"
    _description = 'Codigos de Cargos o Descuentos'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=12, index=True, required=True)

class NextProPeCatalog54(models.Model):
    _name = "nextpro_pe.catalogo.54"
    _description = 'Codigos de Bienes y Servicio Sujetos a Detraccion'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=12, index=True, required=True)

class NextProPeCatalog55(models.Model):
    _name = "nextpro_pe.catalogo.55"
    _description = 'Codigo de identificacion del Item'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=12, index=True, required=True)

class NextProPeCatalog56(models.Model):
    _name = "nextpro_pe.catalogo.56"
    _description = 'Codigo de Tipo de Servicio Publico'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=12, index=True, required=True)

class NextProPeCatalog57(models.Model):
    _name = "nextpro_pe.catalogo.57"
    _description = 'Codigo de Tipo de Servicio Publicos-Telecomunicaciones'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=12, index=True, required=True)
    
class NextProPeCatalog58(models.Model):
    _name = "nextpro_pe.catalogo.58"
    _description = 'Codigo de Tipo de Medidor-Recibo de Luz'
    _inherit = 'nextpro_pe.catalogo.tmpl'

    code = fields.Char(string='Code', size=12, index=True, required=True)