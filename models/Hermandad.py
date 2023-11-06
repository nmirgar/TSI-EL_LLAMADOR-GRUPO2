
from odoo import models, fields, api

class Hermandad(models.Model):
    _name = 'llamador.hermandad' #modulo.modelo
    _description = 'Hermandad registrada'
    #con guion bajo no se guarda en la base de datos

    sNombre = fields.Char(string="Nombre Hermandad", required=True, help="Nombre de la hermandad")
    #la PK tiene q ser numerica -> tonses q hago xd

    iTlf_cont = fields.Integer('Telefono de contacto',required=True, autodate = True)
    sEmail_cont = fields.Char(string="Email de contacto", required=True)
    dFecha_fundacion = fields.Datetime('Fecha fundacion',required=True, autodate = False)
    sDescripcion = fields.Char(string="Descripcion Hermandad", required=True)
    sDia_procesion = fields.Char(string="Dia de la semana que le toca salir", required=True)
