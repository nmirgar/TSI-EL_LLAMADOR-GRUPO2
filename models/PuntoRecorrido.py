from odoo import models, fields, api

class PuntoRecorrido(models.Model):
    #_inherit = 'clase.class'
    _name =  'llamador.puntorecorrido' 
   
    _description = 'Punto de un Recorrido de la Semana Santa'
    
    sUbicacion = fields.Char('Ubicación', required=True)
    sPuntoInteres = fields.Char('Punto Interés')
    rel_paso= fields.Many2many("llamador.paso", string="Pasos")

    # 
    
  

