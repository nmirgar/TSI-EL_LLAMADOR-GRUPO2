
from odoo import models, fields, api

class Hermandad(models.Model):
    _name = 'llamador.hermandad' #modulo.modelo
    _description = 'Hermandad registrada'
    _rec_name = "sNombre" #para visualizar bien en odoo

    #Atributos
    sNombre = fields.Char(string="Nombre Hermandad", required=True, help="Nombre de la hermandad")
    iTlf_cont = fields.Char('Telefono de contacto',required=True,store=True)
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
                                     ('sab','Sábado Santo'),
                                     ('domRe','Domingo de Resurrección'),],
                                     'Dia de la semana que le toca salir')
    escudo = fields.Binary('Escudo')

    #Relaciones
    hermanos_ids = fields.Many2many("llamador.hermano", string = "Hermanos pertenecientes")
    almacenes_ids = fields.Many2many("llamador.almacen",string = "Almacenes pertenecientes")

    #Restriccion
    _sql_constraints = [('hermandad_nombre_unique', 'UNIQUE(sNombre)', 'El nombre debe ser unico')]



    #Funciones
    iNumHermanos = fields.Integer(compute='_numeroHermanos', string='Numero de Hermanos pertenecienets', store = True)
    iNumAlmacenes = fields.Integer(compute='_numeroAlmacenes',string='Numero de Almacenes pertenecientes',store=True)
    
    @api.depends('hermanos_ids')
    def _numeroHermanos(self):
        for record in self:
            record.iNumHermanos = len(record.hermanos_ids)
    
    @api.depends('almacenes_ids')
    def _numeroAlmacenes(self):
        for record in self:
            record.iNumAlmacenes = len(record.almacenes_ids)



    @api.constrains('sNombre')
    def _check_nombre(self):
        if len(self.sNombre) > 60:
           raise models.ValidationError("La longitud de la cadena no puede ser superior a 60 caracteres")
    
    @api.constrains('sEmail_cont')
    def _check_email(self):
        if len(self.sEmail_cont) > 100:
           raise models.ValidationError("La longitud de la cadena Email no puede ser superior a 100 caracteres")
        
    @api.constrains("iTlf_cont")
    def _check_tlfn(self):
        if len(self.iTlf_cont) < 0 or len(self.iTlf_cont) > 9:
            raise models.ValidationError("El número de teléfono debe tener como máximo 9 digitos")
    
    @api.constrains('sDescripcion')
    def _check_descripcion(self):
        if len(self.sDescripcion) > 250:
           raise models.ValidationError("La longitud de la cadena Descripcion no puede ser superior a 250 caracteres")
    
    @api.constrains('dFecha_fundacion')
    def _check_diaFundacion(self):
        if self.dFecha_fundacion > fields.Datetime.now():
            raise models.ValidationError("La fecha no puede ser superior a la fecha actual")

  

    def btn_desapuntarHermanos(self):
        self.write({'hermanos_ids': [(5,)]})

    def btn_generate_report(self):
          return self.env.ref('llamador.report_hermandad').report_action(self)