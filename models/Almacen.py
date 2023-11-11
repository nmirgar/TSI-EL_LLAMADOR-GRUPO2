from odoo import models, fields, api

class Almacen(models.Model):
    _name = 'llamador.almacen' #modulo.modelo
    _description = 'Almacenes registrados'
    #con guion bajo no se guarda en la base de datos

    iCapacidad_max=  fields.Integer("Capacidad Maxima") 
    sLocalizacion = fields.Char(string="Localizacion", required=True)
    geo_localizacion_almacen = fields.Char(string="Ubicación Geoespacial", help = "Coordenadas")

    #Relaciones
    rel_enseres = fields.One2many("llamador.enseres", "rel_almacen",string = "Enseres pertenecientes")
    rel_hermandad = fields.Many2many("llamador.hermandad", string = "Hermandades pertenecientes")