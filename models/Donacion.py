from odoo import models, fields, api

class Donacion(models.Model):
     _name = 'llamador.donacion'
     _description = 'Papeleta de sitio de hermandad'

     dFecha = fields.Datetime('Fecha donacion',required=True, autodate = True)
     iCantidad = fields.Float('Cantidad',required=True)