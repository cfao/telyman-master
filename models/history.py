from odoo import models, fields, api
from datetime import datetime, timedelta


class HistorialInstalacion(models.Model):
    _name = 'telyman.historial'

    historial_proyecto_asociado = fields.Many2one('telyman.control_instalaciones', 'Instalacion',
                                                  ondelete='cascade')
    historial_fecha = fields.Date(string="Fecha:")
    historial_descripcion = fields.Char(string='Descipcion:')
    historial_fecha_entrega_materiales = fields.Date(string="Fecha Materiales:")
    historial_materiales = fields.Char(string='Materiales:')
    historial_porcentaje_avance = fields.Integer(string='Avance %', size=2)
    tipo_tecnologia = fields.Char(string='Tipo Tecnología:')
    tipo_partner = fields.Selection([("telyman", "Telyman")])
    historial_observaciones = fields.Text(string='Observaciones:')

    historial_PO = fields.Selection([("pendiente", "Pendiente"), ("ok", "OK")], 'PO')

    historial_cod_sitio = fields.Many2one('sites.telyman','Cod Sitio', related='historial_proyecto_asociado.cod_sitio')
    historial_fecha_planific_inst = fields.Date('Fecha Planificación',
                                                related='historial_proyecto_asociado.fecha_planific_inst')
    historial_fecha_inic_inst = fields.Date('Fecha Inicio Inst', related='historial_proyecto_asociado.fecha_inic_inst')
    historial_fecha_fin_inst = fields.Date('Fecha Fin Inst', related='historial_proyecto_asociado.fecha_fin_inst')
    historial_DU = fields.Char(string='DU:')
    active = fields.Boolean('Activo', default=True)

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True
