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

    #Restriccion
    _sql_constraints = [('almacen_localizacion_unique', 'UNIQUE(geo_localizacion_almacen)', 'La localizacion debe ser unica')]

    #Funciones
    iNumEnseres = fields.Integer(compute='_numeroEnseres',string='Numero de Enseres que almacena',store=True)
    iNumHermandades = fields.Integer(compute='_numeroHermandades',string='Numero de Hermandades pertenecientes',store=True)

    @api.depends('enseres_ids')
    def _numeroEnseres(self):
        for record in self:
            record.iNumEnseres = len(record.enseres_ids)
    
    @api.depends('hermandades_ids')
    def _numeroHermandades(self):
        for record in self:
            record.iNumHermandades = len(record.hermandades_ids)



    @api.constrains("iCapacidad_max")
    def _check_capacidad(self):
        if self.iCapacidad_max < 0:
            raise models.ValidationError("La capacidad debe ser un valor positivo")
        
    @api.constrains('sLocalizacion')
    def _check_localizacion(self):
        if len(self.sLocalizacion) > 100:
           raise models.ValidationError("La longitud de la cadena Localizacion no puede ser superior a 100 caracteres")

    @api.constrains('iNumEnseres')
    def _check_cantidad(self):
        for record in self:
            if record.iNumEnseres > record.iCapacidad_max:
                raise models.ValidationError('No se pueden añadir más enseres, la capacidad máxima es {}'.format(record.iCapacidad_max))



    def btn_vaciarAlmacen(self):
        self.write({'enseres_ids': [(5,)]})
    
    def btn_desasociarHermandades(self):
        self.write({'hermandades_ids': [(5,)]})
    
    def btn_generate_report(self):
        return self.env.ref('el__llamador.report_almacen').report_action(self)