
from odoo import models, fields, api

class Enseres(models.Model):
    _name = 'llamador.enseres' #modulo.modelo
    _description = 'Enseres registrados'
    _rec_name = "sNombre" #para visualizar bien en odoo

    #Atributos
    id_enser = fields.Integer(required=True, readonly=True, copy=True, index=True, string="ID Articulo")
    sNombre = fields.Char(string="Nombre del elemento", required=True, help="Nombre del enser")
    iCantidad=  fields.Integer("Cantidad") 
    sDescripcion = fields.Char(string="Descripcion del elemento", required=True)

    #Relaciones
    almacen_id = fields.Many2one("llamador.almacen",string = "Almacen perteneciente")

    #Restriccion funcional
    _sql_constraints = [('enseres_nombre_unique','UNIQUE (sNombre)','El nombre debe ser unico')]