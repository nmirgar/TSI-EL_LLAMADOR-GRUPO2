from odoo import models, fields, api

class Papeleta(models.Model):
     _name = 'llamador.papeleta'
     _description = 'Papeleta de sitio de hermandad'


     sTipo = fields.Selection([('tipo1','Nazareno'),
                                     ('tipo2','Penitente'),
                                     ('tipo3','Costalero'),
                                     ('tipo4','Monaguillo'),
                                     ('tipo5','Portador'),
                                     ('otro','Otros')],
                                     'Tipo de papeleta', default='otro')
     fPrecio = fields.Float('Precio')
     rel_hermano = fields.One2many("llamador.hermano","rel_papeleta", string = "Hermano asociado")
     rel_evento = fields.Many2many('llamador.evento', string='Eventos')
     rel_tramo = fields.Many2one('llamador.tramo', string='Tramo', required=True)
            
     @api.onchange('fPrecio','sTipo')
     def onchange_classes(self):
          resultado = {}
          if self.sTipo == 'tipo1':      
               resultado = {
                    'value': {'fPrecio':30.00},
                    'warning': {
                         'title':'Precio por defecto',
                         'message':'El precio de la papeleta por Nazareno es de 30€.'
                    }
               }
               
          elif self.sTipo == 'tipo2':
               resultado = {
                    'value': {'fPrecio':45.00},
                    'warning': {
                         'title':'Precio por defecto',
                         'message':'El precio de la papeleta por Penitente es de 45€.'
                    }
               }
          elif self.sTipo == 'tipo3':
               resultado = {
                    'value': {'fPrecio':40.00},
                    'warning': {
                         'title':'Precio por defecto',
                         'message':'El precio de la papeleta por Costalero es de 40€.'
                    }
               }
          elif self.sTipo == 'tipo4':
               resultado = {
                    'value': {'fPrecio':50.00},
                    'warning': {
                         'title':'Precio por defecto',
                         'message':'El precio de la papeleta por Monaguillo es de 50€.'
                    }
               }
          elif self.sTipo == 'tipo5':             
               resultado = {
                    'value': {'fPrecio':35.00},
                    'warning': {
                         'title':'Precio por defecto',
                         'message':'El precio de la papeleta por Portador es de 35€.'
                    }
               } 
                
          return resultado
     
     def btn_generate_papeleta_report(self):
          return self.env.ref('el__llamador.report_papeletas').report_action(self)

          
          