from odoo import models, fields, api
from datetime import datetime, timedelta


class ProjectTelyman(models.Model):
    _name = 'project.telyman'

    name = fields.Char(string='Nombre del Proyecto:', required=True)
    client = fields.Many2one('res.partner', 'Cliente', required=True, ondelete='cascade')
    project_description = fields.Char(string='Descripcion del Proyecto:', required=True)
    supervisor = fields.Many2one('hr.employee', string='Supervisor:')
    project_manager = fields.Many2one('hr.employee', string='Jefe Proyecto:')
    proyecto_id = fields.Many2one('product.category', 'Contrato')







