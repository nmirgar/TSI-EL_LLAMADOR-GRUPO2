
from odoo import models, fields, api

class Hermandad(models.Model):
    _name = 'llamador.hermandad' #modulo.modelo
    _description = 'Hermandad registrada'
    #con guion bajo no se guarda en la base de datos

    sNombre = fields.Char(string="Nombre Hermandad", required=True, help="Nombre de la hermandad")
    

    iTlf_cont = fields.Integer('Telefono de contacto',required=True, autodate = True)
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
    escudo = fields.Binary('Escudo')

    #Relaciones
    rel_hermanos = fields.Many2many("llamador.hermano", string = "Hermanos pertenecientes")
    rel_almacen = fields.Many2many("llamador.almacen",string = "Almacenes pertenecientes")