# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hermanos(models.Model):
    #_inherit = 'clase.class'
    _name =  'llamador.hermanos' 
   
    _description = 'Hermanos de los SS'
    
    namxe = fields.Char('Titulo', required=True, help='Dame el Nombre del Brother')
    start = fields.Datetime('Hora Inicio', required=True, autoDate=True)
    end = fields.Datetime('Hora Finalización', required=True, autoDate=True)
    capacity = fields.Integer('Capacity')
    
  

