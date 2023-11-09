# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hermano(models.Model):
    #_inherit = 'clase.class'
    _name =  'llamador.hermano' 
   
    _description = 'Hermanos de los SS'
    
    sNombre = fields.Char('Nombre', required=True)
    sApellidos = fields.Char('Apellidos', required=True)
    sDNI = fields.Char('DNI', required=True)
    sTlfn = fields.Char('Telefono', required=True)
    sEmail = fields.Char('Email', required=True)
    sDireccion = fields.Char('Direccion', required=True)
    fPeso = fields.Float('Peso', required=True)
    fAltura = fields.Float('Altura', required=True)
    # rel_hermandad = fields.Many2many("llamador.hermandad",string="Hermandad perteneciente")
    #rel_rol = fields.Many2many()
    #rel_papeletaSitio= fields.

