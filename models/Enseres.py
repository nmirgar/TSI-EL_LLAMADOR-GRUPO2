
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

    #Funciones
    @api.constrains('sNombre')
    def _check_nombre(self):
        if len(self.sNombre) > 60:
           raise models.ValidationError("La longitud de la cadena Nombre no puede ser superior a 60 caracteres")
    
    @api.constrains("iCantidad")
    def _check_cantidad(self):
        if self.iCantidad < 0:
            raise models.ValidationError("La cantidad debe ser un valor positivo")
        
    @api.constrains('sDescripcion')
    def _check_descripcion(self):
        if len(self.sDescripcion) > 250:
           raise models.ValidationError("La longitud de la cadena Descripcion no puede ser superior a 250 caracteres")