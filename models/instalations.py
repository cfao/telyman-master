from odoo import models, fields, api
from datetime import datetime, timedelta

formatoFecha = '%Y-%m-%d'


class ControlInstalaciones(models.Model):
    _name = "telyman.control_instalaciones"
    _description = "Instalaciones"
    _inherit = ['mail.thread']

    @api.model
    def _get_next_sequence(self):
        seq_id = self.env.ref('telyman.seq_control_instacion')
        new_num = seq_id.number_next_actual

        return '%%0%sd' % seq_id.padding % new_num

    @api.model
    def create(self, vals):

        seq_id = self.env.ref('telyman.seq_control_instacion')
        new_seq = self._get_next_sequence()
        if True:  # vals['name'] == new_seq:
            self._cr.execute("SELECT nextval('ir_sequence_%03d')" % seq_id.id)
        result = super(ControlInstalaciones, self).create(vals)
        print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP ' + str(new_seq))
        return result

    def copy(self, default=None):
        self.ensure_one()
        if not default:
            default = {}
        seq_id = self.env.ref('telyman.seq_control_instacion')
        new_seq = self._get_next_sequence()
        default['name'] = new_seq
        self._cr.execute("SELECT nextval('ir_sequence_%03d')" % seq_id.id)
        return super(ControlInstalaciones, self).copy(default)

    # *******************************  Datos Generales  ****************************************

    name = fields.Char(string='Instalacion', required=True, default=_get_next_sequence, index=True)
    cod_project = fields.Many2one('project.telyman', string='Proyecto:', required=True)
    project_id = fields.Many2one('product.category', related='cod_project.proyecto_id')
    client = fields.Char( string='Cliente:',related='cod_project.client.name', readonly=True)
    cod_sitio = fields.Many2one('sites.telyman', string='Sitio:', required=True)
    tipo_trabajo = fields.Many2one('tipo_trabajo.tipo_trabajo', 'Tipo Trabajo', required=True, ondelete='cascade')

    modificar_fecha_proyecto = fields.Boolean('Modificar fechas proyectos')
    # *****************************   Datos del Cliente  *****************************************
    jefe_proyecto = fields.Many2one('hr.employee', string='Jefe Proyecto:')
    currency_id = fields.Many2one('res.currency', 'Moneda del proyecto')

    # ******************************  Datos  del Instalador*****************************************
    # fields.Many2one('operadora.operadora', 'Operadora', required=True, ondelete='cascade')
    contrata_inst = fields.Many2one('hr.employee', 'Contrata:', ondelete='cascade')
    jefe_cuadrilla_inst = fields.Many2one('hr.employee', string='Jefe de Cuadrilla:')
    sup_telyman_inst = fields.Many2one('hr.employee', string='Sup Telyman:')
    fecha_planific_inst = fields.Date(string="Fecha Planif.:")

    fecha_inic_inst = fields.Date(string="Fecha Inicio Inst:")
    fecha_fin_inst = fields.Date(string="Fecha Fin Inst:")
    fecha_produccion_inst = fields.Date(string="Fecha de Producción")
    quickbook = fields.Boolean(default=False, string="Creado en QuickBook?")

    # ******************************  Seguimiento  *****************************************
    seg_administrativo = fields.Many2one('tipo.seguimiento.administrativo', string='Seg Administrativo',
                                         track_visibility='onchange', index=True,
                                         default=lambda self: self.env.ref('telyman.seguimiento01').id,
                                         group_expand='_read_group_stage_ids',
                                         copy=False)

    seg_tecnico = fields.Many2one('tipo.seguimiento.tecnico', string='Seg Tecnico', track_visibility='onchange',
                                  index=True,
                                  default=lambda self: self.env.ref('telyman.seguimiento_tecnico01').id,
                                  group_expand='_read_group_stage_ids',
                                  copy=False)

    # ******************************  Item  *****************************************
    items_relacionados = fields.One2many('telyman.item', 'control_instalaciones_relacionado', 'Items')

    # ******************************  Documentacion  *****************************************
    doc_estado = fields.Selection([('P', 'Pendiente'), ('E', 'Enviado'), ('R', 'Rechazar'), ('A', 'Aprobado')],
                                  string='Seg Tecnico:')

    planos_docu = fields.Boolean(default=False, string='Planos')
    planos_fecha_recibido_docu = fields.Date()
    planos_realizado_aprob_docu = fields.Boolean(default=False)
    planos_fecha_envio_cliente_docu = fields.Date()
    planos_envio_cliente_aprobado_docu = fields.Boolean(default=False)
    planos_observacion_docu = fields.Char()  # fields.One2many('product.category', 'parent_id', 'Child Categories')

    foto_docu = fields.Boolean(default=False, string='Fotografia')
    foto_fecha_recibido_docu = fields.Date()
    foto_realizado_aprob_docu = fields.Boolean(default=False)
    foto_fecha_envio_cliente_docu = fields.Date()
    foto_envio_cliente_aprobado_docu = fields.Boolean(default=False)
    foto_observacion_docu = fields.Char()

    AS_build_docu = fields.Boolean(default=False, string='AS Build')
    AS_build_fecha_recibido_docu = fields.Date()
    AS_build_realizado_aprob_docu = fields.Boolean(default=False)
    AS_build_fecha_envio_cliente_docu = fields.Date()
    AS_build_envio_cliente_aprobado_docu = fields.Boolean(default=False)
    AS_build_observacion_docu = fields.Char()

    ATP_docu = fields.Boolean(default=False, string='APT/Check List')
    ATP_fecha_recibido_docu = fields.Date()
    ATP_realizado_aprob_docu = fields.Boolean(default=False)
    ATP_fecha_envio_cliente_docu = fields.Date()
    ATP_envio_cliente_aprobado_docu = fields.Boolean(default=False)
    ATP_observacion_docu = fields.Char()

    EHS_docu = fields.Boolean(default=False, string='EHS')
    EHS_fecha_recibido_docu = fields.Date()
    EHS_realizado_aprob_docu = fields.Boolean(default=False)
    EHS_fecha_envio_cliente_docu = fields.Date()
    EHS_envio_cliente_aprobado_docu = fields.Boolean(default=False)
    EHS_observacion_docu = fields.Char()

    doc_observaciones = fields.Char(string='Observaciones:')

    # ******************************  Check List  *****************************************
    fecha_chck = fields.Date()
    estado_chck = fields.Selection(
        [('No', 'No Establecido'), ('Po', 'Postpuesto'), ('P', 'Programado'), ('R', 'Rechazado'), ('A', 'Aceptado'),
         ('A', 'Enviado')], string='Estado:')
    realizado_chck = fields.Char()
    fecha_enviado_chck = fields.Date()
    chck_observaciones = fields.Text(string='Observaciones:')

    # ******************************  Contratas *****************************************
    contrata_ids = fields.One2many('contrata.telyman', 'telyman_core_id', 'Contratas')

    items_relacionados_precio_total_aprobado = fields.Float('Total Items Aprobados', compute='_compute_total_Items',
                                                            store=True)
    items_relacionados_precio_total_solicitado = fields.Float('Total Items Solicitados', compute='_compute_total_Items',
                                                              store=True)
    items_relacionados_pac_facturado = fields.Float('PAC Facturado', compute='_compute_total_Items', store=True)
    items_relacionados_fac_facturado = fields.Float('FAC Facturado', compute='_compute_total_Items', store=True)
    items_relacionados_pac_fecha = fields.Date('PAC Fecha', compute='_compute_total_Items', store=True)
    items_relacionados_fac_fecha = fields.Date('PAC Fecha', compute='_compute_total_Items', store=True)

    tipo_cambio = fields.Float('Tipo Cambio')

    cliente_orden_compra = fields.Many2one('res.partner', 'Cliente Orden Compra', ondelete='cascade', store=False)

    fecha_alerta1 = fields.Date(string="Fecha de Alerta", compute='_compute_Fecha_Alerta1', store=True)

    alerta1 = fields.Boolean(default=False, store=True)
    contador_Alerta = fields.Integer('Días Alerta', default=0)
    alerta_observaciones = fields.Text('Alerta Observaciones')

    #  observaciones alerta   vista Gam Rural

    historial_relacionado = fields.One2many('telyman.historial', 'historial_proyecto_asociado', 'Historial')

    items_precio_total_instalacion = fields.Float('Valor Total', compute='_compute_total_Items', store=True)
    active = fields.Boolean('Activo', default=True)

    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'No puede tener dos instalaciones con el mismo cod. proyecto!')
    ]

    def modificar_fecha(self):
        self.modificar_fecha_proyecto = True

    def bloquear_fecha(self):
        self.modificar_fecha_proyecto = False

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True

    # PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
    @api.depends()
    def compute_Fecha_Alerta(self):
        fechaAhora = datetime.now()
        fechaActual = fechaAhora.strftime(formatoFecha)

        if str(fechaActual) == str(self.fecha_alerta1):
            print('TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')

    # PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
    def actualizar_Alertas(self):

        fechaAhora = datetime.now()
        fechaActual = fechaAhora.strftime(formatoFecha)

        dia = fechaAhora.strptime(fechaActual, formatoFecha).strftime('%A')

        # print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQ  Actualizando Alerta : ' + str(self.fecha_alerta1)+' ---- '+dia)

        for instalacion in self.search([('id', '!=', self.id)]):
            # print('WWWW:'+ instalacion.name + ' ---- '+str(instalacion.alerta1)+'---- ' + str(instalacion.fecha_inic_inst)+' --- '+str(instalacion.fecha_alerta1))

            if instalacion.fecha_alerta1 == fechaActual:

                fecha_alerta_temp = datetime.strptime(instalacion.fecha_alerta1, '%Y-%m-%d')

                if dia == 'Sunday':
                    instalacion.fecha_alerta1 = fecha_alerta_temp + timedelta(days=1)

                if dia == 'Saturday':
                    instalacion.fecha_alerta1 = fecha_alerta_temp + timedelta(days=2)

                instalacion.contador_Alerta = 1
                instalacion.alerta1 = True

            else:
                # print('********************Alerta ************' + str(instalacion.fecha_alerta1))

                if instalacion.alerta1 == True:

                    if instalacion.contador_Alerta < 3:
                        instalacion.contador_Alerta = instalacion.contador_Alerta + 1

        print('********************Alerta ********************************************')

        return True


    # Esta función revisa cada uno de los items relacionados de una instalación y asigna los precios totales correspondientes al Estado del Item
    @api.depends('items_relacionados')
    def _compute_total_Items(self):

        item_precio_global_aceptado = 0
        item_precio_global_solicitado = 0
        item_precio_total = 0
        item_precio_global_pac_facturado = 0
        item_precio_global_fac_facturado = 0

        for instalacion_Item in self.items_relacionados:

            if instalacion_Item.state == 'aprobado':
                item_precio_global_aceptado = item_precio_global_aceptado + instalacion_Item.precio_total

                if instalacion_Item.fecha_pac != False:
                    self.items_relacionados_pac_facturado = item_precio_global_aceptado * 0.7
                    self.items_relacionados_pac_fecha = instalacion_Item.fecha_pac
                    # print "--- item_precio_global_PAC: " + str(item_precio_global_pac_facturado)

                if instalacion_Item.fecha_fac != False:
                    self.items_relacionados_fac_facturado = item_precio_global_aceptado * 0.3
                    self.items_relacionados_fac_fecha = instalacion_Item.fecha_fac
                    # print "--- item_precio_global_FAC: " + str(item_precio_global_fac_facturado)

            if instalacion_Item.state == 'solicitado':
                item_precio_global_solicitado = item_precio_global_solicitado + instalacion_Item.precio_total

            item_precio_total = item_precio_total + instalacion_Item.precio_total

        self.items_relacionados_precio_total_aprobado = item_precio_global_aceptado
        self.items_relacionados_precio_total_solicitado = item_precio_global_solicitado
        self.items_precio_total_instalacion = item_precio_total

        # print '-------------------_compute_total_Items------------------------'

    def incrementar_orden_compra(self):
        # print '*************************************'
        self.cliente_ordenCompra
        Cliente_clase = Cliente()

    def generar_linea(self):
        item_precio_global_aceptado = 0
        item_precio_global_solicitado = 0
        item_precio_global_pac_facturado = 0
        item_precio_global_fac_facturado = 0
        item_precio_total = 0
        # if item_precio_global_aceptado == 1:
        for instalacion_Item in self.items_relacionados:

            if instalacion_Item.state == 'aprobado':
                item_precio_global_aceptado = item_precio_global_aceptado + instalacion_Item.precio_total

                if instalacion_Item.fecha_pac != False:
                    self.items_relacionados_pac_facturado = item_precio_global_aceptado * 0.7
                    self.items_relacionados_pac_fecha = instalacion_Item.fecha_pac
                    # print "--- item_precio_global_PAC: " + str(item_precio_global_pac_facturado)

                if instalacion_Item.fecha_fac != False:
                    self.items_relacionados_fac_facturado = item_precio_global_aceptado * 0.3
                    self.items_relacionados_fac_fecha = instalacion_Item.fecha_fac
                    # print "--- item_precio_global_FAC: " + str(item_precio_global_fac_facturado)

            if instalacion_Item.state == 'solicitado':
                item_precio_global_solicitado = item_precio_global_solicitado + instalacion_Item.precio_total
            item_precio_total = item_precio_total + instalacion_Item.precio_total
        self.items_relacionados_precio_total_aprobado = item_precio_global_aceptado
        self.items_relacionados_precio_total_solicitado = item_precio_global_solicitado
        # print '-------------------_compute_total_Items------------------------'
        self.items_precio_total_instalacion = item_precio_total