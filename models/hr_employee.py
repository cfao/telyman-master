from odoo import models, fields, api
from datetime import datetime, timedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    supervisor_cliente = fields.Boolean(string='Supervisor:')
    jefe_proyecto_cliente = fields.Boolean(string='Jefe Proyecto Cliente')
    contrata = fields.Boolean('Contrata')

    contrata_inst = fields.Boolean('Contrata Institucion:')

    jefe_cuadrilla = fields.Boolean(string='Jefe de Cuadrilla:')
    jefe_proyecto = fields.Boolean(string='Jefe de Proyecto:')
    sup_telyman = fields.Boolean(string='Sup Telyman:')