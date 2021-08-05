from odoo import models, fields, api
from datetime import datetime, timedelta


class ContrataTelyman(models.Model):
    _name = 'contrata.telyman'

    @api.depends('precio_unitario', 'ud_contrata', 'po_contrata')
    def _compute_total_contratas(self):
        for contrata in self:
            contrata.precio_total = contrata.precio_unitario * contrata.ud_contrata

    name = fields.Char('Nombre')
    contrata_id = fields.Many2one('hr.employee', 'Contrata')

    po_contrata = fields.Char('PO Contrata')  # cambio Juliana5-4-2019

    ud_contrata = fields.Float('Ud Contrata')
    precio_unitario = fields.Float('Precio Unitario')
    precio_total = fields.Float('P. Total Contrato', compute='_compute_total_contratas', store=True)

    aceptado = fields.Boolean('Aceptado')
    fecha_fact_contrata = fields.Date('Fec. Fact. Contrato')
    num_contrato = fields.Char('Num. Contrato')
    fecha_pago_contrata = fields.Date('Fec. Pago. Contrata')
    attachment_id = fields.Binary('Adjunto')
    telyman_core_id = fields.Many2one('telyman.control_instalaciones', string='Instalacion')

    telyman_core_id_cod_sitio = fields.Many2one('sites.telyman','Cod Sitio', related='telyman_core_id.cod_sitio', store=True)
    telyman_core_id_fecha_inic_inst = fields.Date('Fecha Instal', related='telyman_core_id.fecha_inic_inst')

    codigo = fields.Char('Código')
    item_id = fields.Many2one('telyman.item', 'Item ID')

    carga_actualizadocontrata = fields.Char('Car-Actual')
    contratas_observaciones = fields.Char('Observaciones')
    active = fields.Boolean('Activo', default=True)

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True

