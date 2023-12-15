
from odoo import models, fields, api

class Hermandad(models.Model):
    _name = 'llamador.hermandad' #modulo.modelo
    _description = 'Hermandad registrada'
    _rec_name = "sNombre" #para visualizar bien en odoo

    #Atributos
    sNombre = fields.Char(string="Nombre Hermandad", required=True, help="Nombre de la hermandad")
    iTlf_cont = fields.Integer('Telefono de contacto',required=True,store=True)
    sEmail_cont = fields.Char(string="Email de contacto", required=True)
    dFecha_fundacion = fields.Datetime('Fecha fundacion',required=True, autodate = False)
    sDescripcion = fields.Char(string="Descripcion Hermandad", required=True)
    sDia_procesion = fields.Selection([('vierD','Viernes de Dolores'),
                                     ('sabP','Sábado de Pasión'),
                                     ('domRa','Domingo de Ramos'),
                                     ('lun','Lunes Santo'),
                                     ('mar','Martes Santo'),
                                     ('mier','Miércoles Santo'),
                                     ('juev','Jueves Santo'),
                                     ('mad','Madrugada'),
                                     ('vier','Viernes Santo'),
                                     ('sab','Sábado Santo'),],
                                     'Dia de la semana que le toca salir')
    
    #Atributo para poder asignarle el escudo a cada hermandad
    escudo = fields.Binary('Escudo')

    #Relaciones
    hermanos_ids = fields.Many2many("llamador.hermano", string = "Hermanos pertenecientes")
    almacenes_ids = fields.Many2many("llamador.almacen",string = "Almacenes pertenecientes")

    #Restriccion
    _sql_constraints = [('hermandad_nombre_unique', 'UNIQUE(sNombre)', 'El nombre debe ser unico')]