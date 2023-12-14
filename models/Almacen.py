from odoo import models, fields, api

class Almacen(models.Model):
    _name = 'llamador.almacen' #modulo.modelo
    _description = 'Almacenes registrados'
    _rec_name = "sLocalizacion" #para visualizar bien en odoo

    #Atributos
    iCapacidad_max=  fields.Integer("Capacidad Maxima") 
    sLocalizacion = fields.Char(string="Localizacion", required=True)
    geo_localizacion_almacen = fields.Char(string="Ubicación Geoespacial", help = "Coordenadas")

    #Relaciones
    enseres_ids = fields.One2many("llamador.enseres", "almacen_id",string = "Enseres pertenecientes")
    hermandades_ids = fields.Many2many("llamador.hermandad", string = "Hermandades pertenecientes")