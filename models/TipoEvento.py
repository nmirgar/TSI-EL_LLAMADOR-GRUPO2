from odoo import models, fields

class TipoEvento(models.Model):
    _name = 'llamador.tipoevento'
    _description = 'Modelo para los tipos de eventos de la hermandad de Semana Santa'

    sTipo = fields.Char(string='Tipo de Evento', required=True)
    sColor = fields.Char(string='Color', default='#800080')

    rel_evento = fields.One2many('llamador.evento', 'rel_tipoevento', string='Eventos')