from odoo import models, fields, api

class Papeleta(models.Model):
     _name = 'llamador.papeleta'
     _description = 'Papeleta de sitio de hermandad'

     dFecha = fields.Datetime('Fecha evento',required=True, autodate = True)
     sTipo = fields.Selection([('tipo1','Tipo 1'),
                                     ('tipo2','Tipo 2'),
                                     ('otros','Otros'),],
                                     'Tipo de papeleta', default='tipo1')
     fPrecio = fields.Float('Precio')
     rel_hermano = fields.One2many("llamador.hermano","rel_papeleta", string = "Hermano asociado")