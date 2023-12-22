# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hermano(models.Model):
    #_inherit = 'clase.class'
    _name =  'llamador.hermano' 
   
    _description = 'Hermanos de los SS'
    _rec_name="sDNI"
    sNombre = fields.Char('Nombre', required=True)
    sApellidos = fields.Char('Apellidos', required=True)
    sDNI = fields.Char('DNI', size=9,required=True,)
    sTlfn = fields.Char('Telefono', size=9,required=True)
    sEmail = fields.Char('Email', required=True)
    sDireccion = fields.Char('Direccion', required=True)
    foto=fields.Binary('Foto')    
    fPeso = fields.Float('Peso', required=True)
    fAltura = fields.Float('Altura', required=True)

    #Relaciones
    rel_hermandad = fields.Many2many("llamador.hermandad",string="Hermandad perteneciente")
    rel_rol = fields.Many2many("llamador.rol", string="Rol Hermano")
    rel_donacion = fields.One2many("llamador.donacion","rel_hermano", string="Donacion Hermano")
    rel_papeleta= fields.Many2one("llamador.papeleta", string="Papeleta de Sitio")

    #orm - compute
    iNumHermandadesPertenecientes = fields.Integer(compute='_iNumeroHermandadesPertenecientes',string="Numero de Hermandades a las que pertenece",store=True)

    @api.depends('rel_hermandad')
    def _iNumeroHermandadesPertenecientes(self):
        for record in self:
            record.iNumHermandadesPertenecientes = len(record.rel_hermandad)

    #orm - on change
            
    @api.onchange('sTlfn')
    def onchange_tlfn(self):
          if self.sTlfn and len(self.sTlfn) != 9     : # el false de idcard sirve para que no se ejecute el onchange al pulsar el boton "Create"
               raise models.ValidationError('El teléfono debe contener 9 dígitos.')
    @api.onchange('fPeso')
    def onchange_peso(self):
          if self.fPeso <0 and self.sDNI != False    : # el false de dni sirve para que no se ejecute el onchange al pulsar el boton "Create"
               raise models.ValidationError('El peso debe ser positivo.')
    @api.onchange('fAltura')
    def onchange_altura(self):
          if self.fAltura <0 and self.sDNI != False    : # el false de dni sirve para que no se ejecute el onchange al pulsar el boton "Create"
               raise models.ValidationError('La altura debe ser positiva.')

    #Report
    def btn_generate_report(self):
          return self.env.ref('el__llamador.report_hermano').report_action(self)