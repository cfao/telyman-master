from odoo import models, fields, api
from datetime import datetime, timedelta


class SitesTelyman(models.Model):
    _name = 'sites.telyman'

    name = fields.Char(string='Nombre de Sitio:',  required=True,)
    cod_sitio = fields.Char(string='Referencia Interna:')
    site_client = fields.Many2one('res.partner','Cliente', required=True)
    #tipo_trabajo = fields.Many2one('tipo_trabajo.tipo_trabajo', 'Tipo Trabajo', required=True, ondelete='cascade')
    ubicacion_Gam_rural = fields.Selection([("gam", "GAM"), ("rural", "Rural")], 'Ubicación')
    ubicacion = fields.Char(string='Dirección:')
    provincia = fields.Selection(
        [('No Especificada', 'NO ESPECIFICADA'), ('san_jose', 'San Jose'), ('alajuela', 'Alajuela'),
         ('cartago', 'Cartago'), ('heredia', 'Heredia'), ('guanacaste', 'Guanacaste'), ('puntarenas', 'Puntarenas'),
         ('limon', 'Limón')], string='Provincia:', required=True)
    coord_x = fields.Float(string='Coord(x):')
    coord_y = fields.Float(string='Coord(y):')