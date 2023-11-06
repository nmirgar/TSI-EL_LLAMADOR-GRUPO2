
from odoo import models, fields, api

class Enseres(models.Model):
    _name = 'llamador.enseres' #modulo.modelo
    _description = 'Enseres registrados'
    #con guion bajo no se guarda en la base de datos

    sNombre = fields.Char(string="Nombre del elemento", required=True, help="Nombre del enser")
    #la PK tiene q ser numerica -> tonses q hago xd
    iCantidad=  fields.Integer("Cantidad") 
    sDescripcion = fields.Char(string="Descripcion del elemento", required=True)