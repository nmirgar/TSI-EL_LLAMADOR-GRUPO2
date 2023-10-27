# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hermanos(models.Model):
    #_inherit = 'clase.class'
    _name =  'llamador.hermanos' #guion bajo sirve pa conectar la base de datos?
    #para poner el nombre es nombreModulo.nombreModelo(clase)
    _description = 'Hermanos de los SS'
    
    namxe = fields.Char('Titulo', required=True, help='Dame el Nombre del Brother')# la PK debe ser numerica asi que lo haremos con field.Char() ya que no es numero
    start = fields.Datetime('Hora Inicio', required=True, autoDate=True)
    end = fields.Datetime('Hora Finalización', required=True, autoDate=True)
    capacity = fields.Integer('Capacity')
    
    #ya estaría el modulo
    #falta hacer la vista
    # ahora toca instalar el modulito jijiJA 

