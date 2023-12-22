from datetime import timedelta
from odoo import models, fields, api

class Evento(models.Model):
    _name = 'llamador.evento'
    _description = 'Modelo para los eventos de la hermandad de Semana Santa'

    sName = fields.Char(string='Nombre del Evento', required=True)
    sFechaHora = fields.Datetime(string='Fecha y Hora del Evento', required=True)
    #sEstado = fields.Char(compute='_estadoEvento', string='Estado', store=True)

    #Relaciones
    rel_tipoevento = fields.Many2one('llamador.tipoevento', string='Tipo de Evento')
    rel_papeleta = fields.One2many('llamador.papeleta', 'rel_evento', string='Papeletas') 
    rel_puntorecorrido = fields.Many2many('llamador.puntorecorrido', string='Puntos de Recorrido')

    _sql_constraints = [('evento_sName_unique','UNIQUE (sName)','El nombre debe ser único')]

    def btn_marcar_completado(self):
          self.write({'sEstado':"Completado"})
    
    """@api.constrains('sFechaHora')
    def _estadoEvento(self):
        for x in self:
            if x.sFechaHora < fields.Datetime.now() + timedelta(days=7):
                x.sEstado = 'Proximo'
            else:
                x.evento.sEstado = 'Futuro'"""
    
    @api.constrains('sFechaHora')
    def _check_fechahora(self):
        for x in self:
            if x.sFechaHora < fields.Datetime.now():
                raise models.ValidationError('La fecha no puede ser de un dia ya pasado.')