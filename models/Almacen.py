from odoo import models, fields, api

class Almacen(models.Model):
    _name = 'llamador.almacen' #modulo.modelo
    _description = 'Almacenes registrados'
    _rec_name = "sLocalizacion" #para visualizar bien en odoo

    #Atributos
    iCapacidad_max=  fields.Integer("Capacidad Maxima") 
    sLocalizacion = fields.Char(string="Localizacion", required=True)

    #Atributo necesario para la implementación de la vista mapa
    geo_localizacion_almacen = fields.Char(string="Ubicación Geoespacial", help = "Coordenadas")

    #Relaciones
    rel_enseres = fields.One2many("llamador.enseres", "rel_almacen",string = "Enseres pertenecientes")
    rel_hermandad = fields.Many2many("llamador.hermandad", string = "Hermandades pertenecientes")