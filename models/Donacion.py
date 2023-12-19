from odoo import models, fields, api

class Donacion(models.Model):
     _name = 'llamador.donacion'
     _description = 'Papeleta de sitio de hermandad'

     dFecha = fields.Datetime('Fecha donacion',required=True, readonly = True)
     iCantidad = fields.Float('Cantidad',required=True, default=0.01)
     rel_hermano = fields.Many2one("llamador.hermano", string="Hermano donante", required= True)
          
     @api.onchange('iCantidad')
     def onchange_cantidad(self):
          if self.iCantidad <= 0:
               raise models.ValidationError('Introduzca una cantidad válida para registrar el donativo. ¡Gracias! ')
     
     @api.onchange('dFecha')
     def onchange_fecha(self):
          self.write({'dFecha': fields.Datetime.now()})
     
     
     