from odoo import models, fields, api
from datetime import datetime, timedelta

class Items(models.Model):
    _name = "telyman.item"

    @api.depends('precio_unitario', 'ud')
    def _compute_total(self):
        funcionar = 0
        for item in self:
            if item.control_instalaciones_relacionado_tipo_cambio == 0:
                item.control_instalaciones_relacionado_tipo_cambio = 600

            # if funcionar == 1:
            # if self.control_instalaciones_relacionado_currency_id == 'USD':
            # item.precio_unitario = item.precio_unitario / item.control_instalaciones_relacionado_tipo_cambio

            # print '+++++++++++++++++        USD     ++++++++++++++++++++++++++++++++'
            # print '\n\n ' + '\n\n'
            # else:
            # precio unitario se conserva
            # print '++++++++++++++++++       CRC     +++++++++++++++++++++++++++++++'
            # print '\n\n ' + '\n\n'

            item.precio_total = item.precio_unitario * item.ud

            item.precio_unitario_dollar = item.precio_unitario / item.control_instalaciones_relacionado_tipo_cambio
            item.precio_total_dollar = item.precio_unitario / item.control_instalaciones_relacionado_tipo_cambio * item.ud

            print('+++++++++++++++++++++++++++++++++++++++++++++++++')
            # print '\n\n ' + '\n\n'

    def generar_precio(self):

        for item in self:
            if item.control_instalaciones_relacionado_tipo_cambio == 0:
                item.control_instalaciones_relacionado_tipo_cambio = 600

            item.precio_total = item.precio_unitario * item.ud
            item.precio_unitario_dollar = item.precio_unitario / item.control_instalaciones_relacionado_tipo_cambio
            item.precio_total_dollar = item.precio_unitario / item.control_instalaciones_relacionado_tipo_cambio * item.ud

    @api.depends('precio_total')
    def _compute_total_pac(self):
        for item in self:
            item.total_pac = item.precio_total * 0.70

    @api.depends('precio_total')
    def _compute_total_fac(self):
        for item in self:
            item.total_fac = item.precio_total * 0.30

    @api.onchange('name')
    def obtener_Precio_item_Onchange(
            self):  # Onchange para obtener el precio del producto seleccionado en el tab Item de proyectos
        self.precio_unitario = self.name.list_price

    name = fields.Many2one('product.product', 'Item')
    state = fields.Selection(
        [('solicitado', 'Solicitado'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado'), ('interna', 'Interna'),
         ('cancelado', 'Cancelado')], 'Estado')
    fecha_estado_po = fields.Date('Fecha estado PO')
    n_po = fields.Char('Num PO')
    ud = fields.Float('Ud')
    precio_unitario = fields.Float('Precio Unitario')
    precio_total = fields.Float('Precio Total', compute='_compute_total', store=True)

    total_pac = fields.Float('Total PAC', compute='_compute_total_pac', store=True)
    total_fac = fields.Float('Total FAC', compute='_compute_total_fac', store=True)

    pac_enviado = fields.Date('PAC enviado')
    fac_enviado = fields.Date('FAC enviado')
    fecha_pac = fields.Date('Fecha PAC')
    fecha_fac = fields.Date('Fecha FAC')
    facturacion_pac = fields.Boolean('Facturar PAC', default=False)
    facturacion_fac = fields.Boolean('Facturar FAC', default=False)

    item_observaciones = fields.Char('Observaciones')

    contrata_ids = fields.One2many('contrata.telyman', 'item_id', 'Contratas')
    control_instalaciones_relacionado = fields.Many2one('telyman.control_instalaciones', 'Instalacion',
                                                        ondelete='cascade')

    item_utilizado_contratas = fields.Boolean(default=False, string="Contratas Item")
    control_instalaciones_relacionado_cod_Proyecto = fields.Char('Instalacion',
                                                                 related='control_instalaciones_relacionado.name',
                                                                 store=True)
    control_instalaciones_relacionado_cod_sitio = fields.Char('Cod Sitio',
                                                              related='control_instalaciones_relacionado.cod_sitio.name',
                                                              store=True)
    control_instalaciones_relacionado_nombre_proyecto = fields.Char('Nombre Proyecto',
                                                                    related='control_instalaciones_relacionado.cod_project.name',
                                                                    store=True)
    control_instalaciones_relacionado_cliente = fields.Char('Cliente',
                                                            related='control_instalaciones_relacionado.cod_project.client.name',
                                                            store=True)
    control_instalaciones_relacionado_seg_tecnico = fields.Char('Seg Tecnico',
                                                                related='control_instalaciones_relacionado.seg_tecnico.name',
                                                                store=True)
    control_instalaciones_relacionado_seg_administrativo = fields.Char('Seg Administrativo',
                                                                       related='control_instalaciones_relacionado.seg_administrativo.name',
                                                                       store=True)
    control_instalaciones_relacionado_fecha_fin_inst = fields.Date('Fecha Final Instalación',
                                                                   related='control_instalaciones_relacionado.fecha_fin_inst')
    control_instalaciones_relacionado_fecha_produccion_inst = fields.Date('Fecha Final Producción',
                                                                          related='control_instalaciones_relacionado.fecha_produccion_inst')

    control_instalaciones_relacionado_currency_id = fields.Many2one('res.currency', 'Tipo de Moneda',
                                                                    related='control_instalaciones_relacionado.currency_id')

    contratas_asociado = fields.Many2one('contrata.item', 'Contratas Relacionado', ondelete='cascade')
    control_instalaciones_relacionado_tipo_cambio = fields.Float('Tipo Cambio',
                                                                 related='control_instalaciones_relacionado.tipo_cambio')

    precio_unitario_dollar = fields.Float('Precio Unitario $')
    precio_total_dollar = fields.Float('Precio Total $')

    carga_actualizado = fields.Char('Car-Actual')

    control_instalaciones_relacionado_duplicar = fields.Many2one('telyman.control_instalaciones',
                                                                 'Item duplicado en Instalacion', ondelete='cascade',
                                                                 store=True)

    def write(self, vals):
        super(Items, self).write(vals)
        # print "Salida Contratas vals" + str(vals)
        vals.get('item_utilizado_contratas')

        if vals.get('item_utilizado_contratas', 'N/A') != 'N/A':
            if vals['item_utilizado_contratas']:
                contrata_objeto = self.env['contrata.item'].create(
                    {'name': self.name.name, 'telyman_core_id': self.control_instalaciones_relacionado.id,
                     'po_contrata': self.control_instalaciones_relacionado_cod_Proyecto})
                self.contratas_asociado = contrata_objeto.id

                # self.env['calendar']

            else:
                # print "Eliminar Contrata"
                pass  # super(ContrataItem,self.contratas_asociado).unlink()
                # print "Eliminar Contrata"

    # +++++++++++++++++++++++++++++++++++++++++++++  Juliana 5-4-2019  +++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++  al seleccionar un item, duplicarlo en un proyecto existente


    def duplicarItem(self, vals):
        print('++++++++++++++++  Duplicando Item ++++++++++++++++++++++++' + str(self.name.id))

        self.precio_unitario = self.name.list_price
        self.env['telyman.item'].create({'name': self.name.id,
                                      'control_instalaciones_relacionado': self.control_instalaciones_relacionado_duplicar.id,
                                      'precio_unitario': self.precio_unitario})

        print('++++++++++++++++  Duplicando Item 2++++++++++++++++++++++++')

        self.control_instalaciones_relacionado_duplicar = False