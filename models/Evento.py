from odoo import models, fields

class Evento(models.Model):
    _name = 'llamador.evento'
    _description = 'Modelo para los eventos de la hermandad de Semana Santa'

    sName = fields.Char(string='Nombre del Evento', required=True)
    sFecha = fields.Date(string='Fecha del Evento', required=True)
    sHora = fields.Datetime(string='Hora del Evento', required=True)

    #Relaciones
    rel_tipoevento = fields.Many2one('llamador.tipoevento', string='Tipo de Evento')
    rel_papeleta = fields.One2many('llamador.papeleta', 'rel_evento', string='Papeletas') 
    rel_puntorecorrido = fields.Many2many('llamador.puntorecorrido', string='Puntos de Recorrido')