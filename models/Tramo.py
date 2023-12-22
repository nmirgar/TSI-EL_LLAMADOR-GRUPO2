from odoo import models, fields

class Tramo(models.Model):
    _name = 'llamador.tramo'
    _description = 'Tramos de la hermandad de Semana Santa'

    iNum_tram = fields.Integer('Número de Tramo', required=True)
    iCap = fields.Integer('Capacidad', required=True)

    rel_papeleta = fields.One2many('llamador.papeleta', 'rel_tramo', string='Papeletas')
    rel_paso = fields.Many2one('llamador.paso', string='Paso', required=True)

    _sql_constraints = [('tramo_iNum_tram_unique','UNIQUE (i_Num_tram)','El numero de tramo debe ser único')]