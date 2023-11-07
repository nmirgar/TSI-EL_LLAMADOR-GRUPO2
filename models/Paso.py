# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Paso(models.Model):
    #_inherit = 'clase.class'
    _name =  'llamador.paso' 
   
    _description = 'Paso de Semana Santa'
    
    sNombre = fields.Char('Nombre', required=True)
    iNumeroTramos = fields.Integer('Numero de Tramos',required=True)
    iFilasCuadrilla = fields.Integer('Filas Cuadrilla',required=True)
    iColumnasCuadrilla = fields.Integer('Columnas Cuadrilla',required=True)
    iNumeroCuadrillas = fields.Integer('Numero de Cuadrillas',required=True)
    fPeso = fields.Float('Peso', required=True)
    
    
  

