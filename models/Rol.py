from odoo import models, fields, api


class Rol(models.Model):
     _name = 'llamador.rol'
     _description = 'Rol dentro de la hermandad'

     cTipo = fields.Char('Nombre del Rol',required=True)
     cDescripcion = fields.Char('Description', size=240)
     rel_hermano = fields.One2many("llamador.hermano", string="Hermanos con este rol", inverse_name='rel_rol')
