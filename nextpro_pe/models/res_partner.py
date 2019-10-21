# -*- coding: utf-8 -*-
import logging
import datetime
from lxml import etree
import math
import pytz
import requests
from PIL import Image
from odoo import models, fields, api
from odoo.exceptions import Warning

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    nxt_registration_name = fields.Char('Registration Name', size=128, index=True, )
    nxt_catalog_06_id = fields.Many2one('nextpro_pe.catalog.06','Tipo Doc.', index=True)
    nxt_state = fields.Selection([('habido','Habido'),('nhabido','No Habido')],'State')
    
    state_id = fields.Many2one('res.country.state', 'Departamento')#Se reutiliza campo existen
    nxt_province_id = fields.Many2one('res.country.state', 'Provincia')
    nxt_district_id = fields.Many2one('res.country.state', 'Distrito')

    # Funcion reemplazada para considerar los nuevos campos en el onchange
    @api.model
    def _address_fields(self):
        """ Returns the list of address fields that are synced from the parent
        when the `use_parent_address` flag is set. """
        #~ return list(ADDRESS_FIELDS)
        address_fields = ('street', 'street2', 'zip', 'city', 'state_id', 'country_id','nxt_province_id','nxt_district_id')
        return list(address_fields)


    # Onchange para actualizar el codigo de distrito
    @api.onchange('nxt_district_id')
    def onchange_district(self):
        if self.nxt_district_id:
            state = self.nxt_district_id.code
            self.zip = state
    
    def _display_address(self, without_company=False):

        '''
        The purpose of this function is to build and return an address formatted accordingly to the
        standards of the country where it belongs.

        :param address: browse record of the res.partner to format
        :returns: the address formatted in a display that fit its country habits (or the default ones
            if not country is specified)
        :rtype: string
        '''
        # get the information that will be injected into the display format
        # get the address format
        address_format = self.country_id.address_format or \
              "%(street)s\n%(street2)s\n%(state_name)s-%(nxt_province_name)s-%(nxt_district_code)s %(zip)s\n%(country_name)s"
        args = {
            'district_code': self.nxt_district_id.code or '',
            'district_name': self.nxt_district_id.name or '',
            'province_code': self.nxt_province_id.code or '',
            'province_name': self.nxt_province_id.name or '',
            'state_code': self.state_id.code or '',
            'state_name': self.state_id.name or '',
            'country_code': self.country_id.code or '',
            'country_name': self.country_id.name or '',
            'company_name': self.parent_name or '',
        }
        for field in self._address_fields():
            args[field] = getattr(self, field) or ''
        if without_company:
            args['company_name'] = ''
        elif self.commercial_company_name:
            address_format = '%(company_name)s\n' + address_format
        return address_format % args

    @api.onchange('nxt_catalog_06_id','vat')
    def vat_change(self):
        self.update_document()
        
    def update_document(self):
        if not self.vat:
            return False
        if self.nxt_catalog_06_id and self.nxt_catalog_06_id.code == '1':
           #Valida DNI
            if self.vat and len(self.vat) != 8:
                raise Warning('El Dni debe tener 8 caracteres')
            else:
                d = get_data_doc_number(
                    'dni', self.vat, format='json')
                if not d['error']:
                    d = d['data']
                    self.name = '%s %s %s' % (d['nombres'],
                                               d['ape_paterno'],
                                               d['ape_materno'])

        elif self.nxt_catalog_06_id and self.nxt_catalog_06_id.code == '6':
            # Valida RUC
            if self.vat and len(self.vat) != 11:
                raise Warning('El Ruc debe tener 11 caracteres')
            else:
                d = get_data_doc_number(
                    'ruc', self.vat, format='json')
                if d['error']:
                    return True
                d = d['data']
                #~ Busca el distrito
                ditrict_obj = self.env['res.country.state']
                prov_ids = ditrict_obj.search([('name', '=', d['provincia']),
                                               ('nxt_province_id', '=', False),
                                               ('state_id', '!=', False)])
                dist_id = ditrict_obj.search([('name', '=', d['distrito']),
                                              ('nxt_province_id', '!=', False),
                                              ('state_id', '!=', False),
                                              ('nxt_province_id', 'in', [x.id for x in prov_ids])], limit=1)
                if dist_id:
                    self.district_id = dist_id.id
                    self.province_id = dist_id.province_id.id
                    self.state_id = dist_id.state_id.id
                    self.country_id = dist_id.country_id.id

                # Si es HABIDO, caso contrario es NO HABIDO
                tstate = d['condicion_contribuyente']
                if tstate == 'HABIDO':
                    tstate = 'habido'
                else:
                    tstate = 'nhabido'
                self.state = tstate
            
                self.name = d['nombre_comercial'] != '-' and d['nombre_comercial'] or d['nombre']
                self.registration_name = d['nombre']
                self.street = d['domicilio_fiscal']
                self.vat_subjected = True
                self.is_company = True
        else:
            True

    #funcion para obter información del contribuyente desde la sunat
    def get_data_doc_number(tipo_doc, numero_doc, format='json'):
        url = 'https://api.sunat.cloud/ruc/'
        url = '%s/%s' % (url, str(numero_doc))
        res = {'error': True, 'message': None, 'data': {}}
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            res['message'] = 'Error en la conexion'
            return res

        if response.status_code == 200:
            res['error'] = False
            res['data'] = response.json()
        else:
            try:
                res['message'] = response.json()['detail']
            except Exception as e:
                res['error'] = True
        return res

    
    