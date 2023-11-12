
from odoo import models, fields, api

class Enseres(models.Model):
    _name = 'llamador.enseres' #modulo.modelo
    _description = 'Enseres registrados'
<<<<<<< HEAD
=======
    _rec_name = "sNombre" #para visualizar bien en odoo
>>>>>>> nuria

    #Atributos
    sNombre = fields.Char(string="Nombre del elemento", required=True, help="Nombre del enser")
    iCantidad=  fields.Integer("Cantidad") 
    sDescripcion = fields.Char(string="Descripcion del elemento", required=True)

    #Relaciones
    rel_almacen = fields.Many2one("llamador.almacen",string = "Almacen perteneciente")