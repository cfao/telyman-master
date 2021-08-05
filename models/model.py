# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import pytz

from odoo import models, fields, api
from datetime import datetime, timedelta
from pytz import timezone

formatoFecha = '%Y-%m-%d'


# ****************************************  Instalaciones   ************************************************************
# ****************************************  Instalaciones   ************************************************************
# ****************************************  Instalaciones   ************************************************************
# ****************************************  Instalaciones   ************************************************************
# ****************************************  Instalaciones   ************************************************************

# class ControlInstalacioneswizard(models.TransientModel):
#     _name = "control_instalaciones.wizard"
#
#     def _get_default_proyecto(self):
#         return self.env['control_instalaciones.control_instalaciones'].browse(self.env.context.get('active_ids'))
#
#     wiz_proyecto = fields.Many2one('control_instalaciones.control_instalaciones', string='proyectos',
#                                    default=_get_default_proyecto)
#     wiz_cod_Proyecto = fields.Char('Instalacion', related='wiz_proyecto.name', store=False)
#     wiz_cod_sitio = fields.Char('Cod Sitio', related='wiz_proyecto.cod_sitio', store=False)
#     wiz_nombre_sitio = fields.Char('Nombre Sitio', related='wiz_proyecto.nombre_sitio', store=False)
#     wiz_nombre_proyecto = fields.Char('Nombre Proyecto', related='wiz_proyecto.nombre_proyecto', store=False)
#     wiz_contrata_ids = fields.One2many('contrata.item', 'telyman_core_id', 'Contratas', store=True)
#     wiz_contrata_id = fields.Many2one('res.partner', 'Contrata', store=True)
#     wiz_po_contrata = fields.Char('Cod Sitio', related='wiz_contrata_ids.po_contrata', store=True)
#     active = fields.Boolean('Activo', default=True)
#
#     def unlink(self):
#         for obj in self:
#             obj.write({'active': False})
#         return True
#
#     @api.onchange('wiz_proyecto')
#     def obtener(self):
#         return {'domain': {'contrata_id': [('id', 'in', self.wiz_proyecto.contrata_ids.mapped('contrata_id').ids)]}}
#
#
#     def imprimir_reporte(self):
#
#         print('A++++++++++++++++++++++++++++++++++++++' + str(self.wiz_po_contrata) + ' ' + str(
#             self.wiz_contrata_id.name))
#         for contratas in self.wiz_proyecto.contrata_ids:
#             if (self.wiz_po_contrata == contratas.po_contrata) | (
#                     self.wiz_contrata_id.name == contratas.contrata_id.name):
#                 print('---' + contratas.po_contrata + '  cont:' + contratas.contrata_id.name + '' + str(
#                     contratas.ud_contrata) + '  ' + str(contratas.precio_unitario) + ' ' + str(
#                     contratas.precio_total) + '   ' + contratas.name + '  +++ ')
#         print('B++++++++++++++++++++++++++++++++++++++')
#
#         result = self.env['report'].get_action(self, 'telyman.action_reporte6')
#         print('C++++++++++++++++++++++++++++++++++++++' + str(result))
#         return result
#


# def test(self):
#  print ('*************************************')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class AlertasInstalacion(models.Model):
    _name = 'alerta.proyecto'

    alerta_proyecto_relacionado = fields.Many2one('control_instalaciones.control_instalaciones', 'Instalacion',
                                                  ondelete='cascade')
    fecha_alerta1 = fields.Date(string="Fecha de Alerta")
    alerta1 = fields.Boolean(default=False, store=True)
    active = fields.Boolean('Activo', default=True)

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ------------------------  historial Instalaciones  -------------------------------
class HistorialInstalacion(models.Model):
    _name = 'historial.instalacion'

    historial_proyecto_asociado = fields.Many2one('control_instalaciones.control_instalaciones', 'Instalacion',
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

    historial_cod_sitio = fields.Char('Cod Sitio', related='historial_proyecto_asociado.cod_sitio')
    historial_nombre_sitio = fields.Char('Nombre Sitio', related='historial_proyecto_asociado.nombre_sitio')
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


# DU = cod de sistema de huawei

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class PreInstalacion(models.Model):
    _name = 'pre.instalacion'
    _description = "preinstalaciones"
    _inherit = ['mail.thread']

    preInstal_cod_sitio = fields.Char(string='Cod Sitio:', required=True)
    preInstal_nombre_sitio = fields.Char(string='Nombre Sitio:', required=True)
    preInstal_provincia = fields.Selection(
        [('No Especificada', 'NO ESPECIFICADA'), ('san_jose', 'San Jose'), ('alajuela', 'Alajuela'),
         ('cartago', 'Cartago'),
         ('heredia', 'Heredia'), ('guanacaste', 'Guanacaste'), ('puntarenas', 'Puntarenas'), ('limon', 'Limón')],
        string='Provincia:')
    preInstal_ubicacion_Gam_rural = fields.Selection([("gam", "GAM"), ("rural", "Rural")], 'Ubicación')

    preInstal_descripcion_trabajo = fields.Char(string='Descripción del Trabajo:', required=True)

    preInstal_fecha_planificacion = fields.Date(string="Fecha de Plan:")
    preInstal_fecha_planificacion_final = fields.Date(string="Fecha de Plan Final:")

    preInstal_cliente_Solicitante = fields.Char(string='Cliente Solicitante:')
    preInstal_cliente = fields.Many2one('res.partner', 'Cliente', ondelete='cascade')
    preInstal_jefe_cuadrilla_responsable = fields.Many2one('hr.employee', string='Jefe de Cuadrilla:')
    preInstal_jefe_proyecto = fields.Many2one('hr.employee', string='Jefe Proyecto:')
    preInstal_status_sitio = fields.Selection(
        [("por ejecutar", "Por Ejecutar"), ("ejecutando", "Ejecutando"), ("terminado", "Terminado")], 'Estado',
        required=True)
    preInstal_observaciones = fields.Text(string='Observaciones:')

    preInstal_calendarizado = fields.Boolean(default=False, string="En Calendario?")
    preInstal_instalacion_creada = fields.Boolean(default=False, string="Instalacion?")

    # -----------------------------------------------------------------------------------------------------------------
    preInstal_operador = fields.Selection(
        [("ice", "ICE"), ("claro", "CLARO"), ("Entreprise", "ENTERPRICE"), ("jasec", "JASEC"), ("otro", "OTRO"),
         ("Telefonica", "TELEFONICA")], 'Operadora')

    preInstal_tipo_trabajo = fields.Many2one('tipo_trabajo.tipo_trabajo', 'Tipo Trabajo', ondelete='cascade')

    preInstal_nombre_proyecto = fields.Char(string='Nombre Proyecto:')
    active = fields.Boolean('Activo', default=True)

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True

    def crear_cita_calendario(self):

        jefeCuadrilla = self.preInstal_jefe_cuadrilla_responsable.name
        nombre = 'Pre Instalacion Sitio:' + self.preInstal_cod_sitio + ' - ' + self.preInstal_nombre_sitio + ' -Cliente:' + self.preInstal_cliente_Solicitante + ' -Jefe:' + jefeCuadrilla
        locacion = str(self.preInstal_provincia) + ' ' + str(self.preInstal_ubicacion_Gam_rural)
        locacion = locacion.replace("false", "")
        fechaInicio = self.preInstal_fecha_planificacion
        fechaFinal = self.preInstal_fecha_planificacion_final
        user_tz = self.env.context['tz']
        if fechaInicio:
            fecha_alerta_temp = datetime.strptime(fechaInicio, '%Y-%m-%d')

            # pst = pytz.timezone(user_tz)
            # fechaInicio = pst.localize(fecha_alerta_temp)
            fechaInicio = fecha_alerta_temp + timedelta(hours=6)

            if fechaFinal:
                fecha_alerta_temp = datetime.strptime(fechaFinal, '%Y-%m-%d')

                fechaFinal = fecha_alerta_temp + timedelta(hours=29)

                if self.preInstal_calendarizado == False:
                    self.env['calendar.event'].create({'name': nombre,
                                                       'location': locacion,
                                                       'duration': 0,
                                                       'start': fechaInicio,
                                                       'stop': fechaFinal
                                                       })
                    self.preInstal_calendarizado = True

    def crear_instalacion(self):
        if not self.preInstal_instalacion_creada:
            control_instalaciones_env = self.env['control_instalaciones.control_instalaciones']
            instalacion_vals = control_instalaciones_env.default_get(['name'])

            instalacion_vals.update({'cod_sitio': self.preInstal_cod_sitio, 'nombre_sitio': self.preInstal_nombre_sitio,
                                     'operador': self.preInstal_operador, 'provincia': self.preInstal_provincia,
                                     'nombre_proyecto': self.preInstal_nombre_proyecto,
                                     'tipo_trabajo': self.preInstal_tipo_trabajo.id,
                                     'cliente': self.preInstal_cliente.id})

            control_instalaciones_env.create(instalacion_vals)

            self.preInstal_instalacion_creada = True
        else:
            print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')


class PreInstalacioneswizard(models.TransientModel):
    _name = "pre_instalaciones.wizard"

    def _get_default_pre_instalacion(self):
        return self.env['pre.instalacion'].browse(self.env.context.get('active_ids'))

    wiz_proyecto = fields.Many2one('pre.instalacion', string='proyectos', default=_get_default_pre_instalacion)
    wiz_cod_sitio = fields.Char('Instalacion', related='wiz_proyecto.preInstal_cod_sitio', store=False)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class ControlInstalaciones(models.Model):
    _name = "control_instalaciones.control_instalaciones"
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
    name = fields.Char(string='Cod Proyecto:', required=True, default=_get_next_sequence, index=True)
    cod_sitio = fields.Char(string='Cod Sitio:', required=True)
    nombre_sitio = fields.Char(string='Nombre Sitio:', required=True)
    operador = fields.Selection(
        [("ice", "ICE"), ("claro", "CLARO"), ("Entreprise", "ENTERPRICE"), ("jasec", "JASEC"), ("otro", "OTRO"),
         ("Telefonica", "TELEFONICA")], 'Operadora', required=True)
    tipo_trabajo = fields.Many2one('tipo_trabajo.tipo_trabajo', 'Tipo Trabajo', required=True, ondelete='cascade')
    operador = fields.Selection(
        [("ice", "ICE"), ("claro", "CLARO"), ("Entreprise", "ENTERPRICE"), ("jasec", "JASEC"), ("otro", "OTRO"),
         ("Telefonica", "TELEFONICA")], 'Operadora', required=True)
    ubicacion_Gam_rural = fields.Selection([("gam", "GAM"), ("rural", "Rural")], 'Ubicación')
    ubicacion = fields.Char(string='Dirección:')
    provincia = fields.Selection(
        [('No Especificada', 'NO ESPECIFICADA'), ('san_jose', 'San Jose'), ('alajuela', 'Alajuela'),
         ('cartago', 'Cartago'), ('heredia', 'Heredia'), ('guanacaste', 'Guanacaste'), ('puntarenas', 'Puntarenas'),
         ('limon', 'Limón')], string='Provincia:', required=True)
    nombre_proyecto = fields.Char(string='Nombre Proyecto:', required=True)
    coord_x = fields.Float(string='Coord(x):')
    coord_y = fields.Float(string='Coord(y):')
    proyecto_id = fields.Many2one('product.category', 'Contrato')
    modificar_fecha_proyecto = fields.Boolean('Modificar fechas proyectos')
    # *****************************   Datos del Cliente  *****************************************
    cliente = fields.Many2one('res.partner', 'Cliente', required=True, ondelete='cascade')
    supervisor_cliente = fields.Many2one('hr.employee', string='Supervisor:')
    jefe_proyecto_cliente = fields.Many2one('hr.employee', string='Jefe Proyecto:')
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
    items_relacionados = fields.One2many('item.item', 'control_instalaciones_relacionado', 'Items')
    item_observaciones = fields.Text(string='Observaciones:')

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
    contrata_ids = fields.One2many('contrata.item', 'telyman_core_id', 'Contratas')

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

    historial_relacionado = fields.One2many('historial.instalacion', 'historial_proyecto_asociado', 'Historial')

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

    # PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
    @api.depends('fecha_inic_inst', 'ubicacion_Gam_rural')
    def _compute_Fecha_Alerta1(self):

        if self.ubicacion_Gam_rural:
            try:
                fecha_instalacion = datetime.strptime(self.fecha_inic_inst, '%Y-%m-%d')

                if self.ubicacion_Gam_rural == 'gam':
                    self.fecha_alerta1 = fecha_instalacion + timedelta(days=3)
                else:
                    self.fecha_alerta1 = fecha_instalacion + timedelta(days=6)
            except:
                print('++++++++++++++++++++++EEEEEEEEEEEEEEEEEEEEEEEEEEE     ++++  ')

        a = datetime.now()
        s = a.strftime(formatoFecha)

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


class button_action_demo(models.Model):
    _name = 'boton.actualizar'
    name = fields.Char(required=True, default='Click on generate name!')
    password = fields.Char()


# ****************************************  Contrata Item   ************************************************************
# ****************************************  Contrata Item   ************************************************************
# ****************************************  Contrata Item   ************************************************************
# ****************************************  Contrata Item   ************************************************************
# ****************************************  Contrata Item   ************************************************************
# ****************************************  Contrata Item   ************************************************************
# ****************************************  Contrata Item   ************************************************************


class ContrataItem(models.Model):
    _name = 'contrata.item'

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
    telyman_core_id = fields.Many2one('control_instalaciones.control_instalaciones', string='Instalacion')

    telyman_core_id_cod_sitio = fields.Char('Cod Sitio', related='telyman_core_id.cod_sitio', store=True)
    telyman_core_id_fecha_inic_inst = fields.Date('Fecha Instal', related='telyman_core_id.fecha_inic_inst')

    codigo = fields.Char('Código')
    item_id = fields.Many2one('item.item', 'Item ID')

    carga_actualizadocontrata = fields.Char('Car-Actual')
    contratas_observaciones = fields.Char('Observaciones')
    active = fields.Boolean('Activo', default=True)

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True


# ********************************************  Items   ****************************************************************
# ********************************************  Items   ****************************************************************
# ********************************************  Items   ****************************************************************
# ********************************************  Items   ****************************************************************
# ********************************************  Items   ****************************************************************
# ********************************************  Items   ****************************************************************

class Items(models.Model):
    _name = "item.item"

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

    contrata_ids = fields.One2many('contrata.item', 'item_id', 'Contratas')
    control_instalaciones_relacionado = fields.Many2one('control_instalaciones.control_instalaciones', 'Instalacion',
                                                        ondelete='cascade')

    item_utilizado_contratas = fields.Boolean(default=False, string="Contratas Item")
    control_instalaciones_relacionado_cod_Proyecto = fields.Char('Instalacion',
                                                                 related='control_instalaciones_relacionado.name',
                                                                 store=True)
    control_instalaciones_relacionado_cod_sitio = fields.Char('Cod Sitio',
                                                              related='control_instalaciones_relacionado.cod_sitio',
                                                              store=True)
    control_instalaciones_relacionado_nombre_sitio = fields.Char('Sitio',
                                                                 related='control_instalaciones_relacionado.nombre_sitio',
                                                                 store=True)
    control_instalaciones_relacionado_nombre_proyecto = fields.Char('Nombre Proyecto',
                                                                    related='control_instalaciones_relacionado.nombre_proyecto',
                                                                    store=True)
    control_instalaciones_relacionado_cliente = fields.Char('Cliente',
                                                            related='control_instalaciones_relacionado.cliente.name',
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

    control_instalaciones_relacionado_duplicar = fields.Many2one('control_instalaciones.control_instalaciones',
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
        self.env['item.item'].create({'name': self.name.id,
                                      'control_instalaciones_relacionado': self.control_instalaciones_relacionado_duplicar.id,
                                      'precio_unitario': self.precio_unitario})

        print('++++++++++++++++  Duplicando Item 2++++++++++++++++++++++++')

        self.control_instalaciones_relacionado_duplicar = False



class ControlOperadoras(models.Model):
    _name = "operadora.operadora"

    # ****************************  Datos Generales  *****************************************
    operadora_cod = fields.Char(string='Cod Operadora:', required=True)
    name = fields.Char('Name', index=True, required=True, translate=True)
    operadora_nombre = fields.Char(string='Nombre Operadora:', required=True)
    operadora_descripcion = fields.Char(string='Descripción Operadora:')
    active = fields.Boolean('Activo', default=True)

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True


class TipoTrabajo(models.Model):
    _name = "tipo_trabajo.tipo_trabajo"
    name = fields.Char('Nombre', index=True, required=True, translate=True)
    trabajo_descripcion = fields.Char(string='Descripción Trabajo:')
    active = fields.Boolean('Activo', default=True)

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True


class Contratista(models.Model):
    _name = "contratista.contratista"
    name = fields.Char('Nombre', index=True, required=True, translate=True)
    contratista_descripcion = fields.Char(string='Descripción Contratista:')
    contratista_telefono = fields.Char(string='Teléfono:')
    contratista_contacto = fields.Char(string='Contacto:')
    active = fields.Boolean('Activo', default=True)

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True


class NumeroOrdenCompra():
    _name = "orden_compra.orden_compra"
    name = fields.Char('Nombre', index=True, required=True, translate=True)
    num_orden_compra = fields.Integer('Num Orden Compra')


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends('order_line.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """

        # print "Entrando Herencia"
        total = super(SaleOrder, self)._amount_all()
        # print "Resultado=  "+ str(total)


class TipoSeguimientoAdministrativo(models.Model):
    _name = 'tipo.seguimiento.administrativo'

    _order = 'sequence'

    name = fields.Char('Nombre')
    sequence = fields.Char('Secuencia')
    fold = fields.Boolean(string='Doblar en vista Kanban',
                          help='This stage is folded in the kanban view when there are no records in that stage to display.')


class TipoSeguimientoTecnico(models.Model):
    _name = 'tipo.seguimiento.tecnico'

    _order = 'sequence'

    name = fields.Char('Nombre')
    sequence = fields.Char('Secuencia')
    fold = fields.Boolean(string='Doblar en vista Kanban',
                          help='This stage is folded in the kanban view when there are no records in that stage to display.')


# /////////////////////////////////////////////////////////////////////////////////////////////////////
class CotizacionesInstalaciones(models.Model):
    _name = "cotizaciones_instalaciones.cotizaciones_instalaciones"
    _description = "Cotizaciones"
    _inherit = ['mail.thread']

    @api.model
    def _get_next_sequence(self):
        seq_id = self.env.ref('telyman.seq_control_cotizacion')
        new_num = seq_id.number_next_actual
        return '%%0%sd' % seq_id.padding % new_num

    @api.model
    def create(self, vals):

        seq_id = self.env.ref('telyman.seq_control_cotizacion')
        new_seq = self._get_next_sequence()
        if vals['codigo'] == new_seq:
            self._cr.execute("SELECT nextval('ir_sequence_%03d')" % seq_id.id)
        result = super(CotizacionesInstalaciones, self).create(vals)
        return result

    def copy(self, default=None):
        self.ensure_one()
        if not default:
            default = {}
        seq_id = self.env.ref('telyman.seq_control_instacion')
        new_seq = self._get_next_sequence()
        default['codigo'] = new_seq
        self._cr.execute("SELECT nextval('ir_sequence_%03d')" % seq_id.id)
        return super(CotizacionesInstalaciones, self).copy(default)

    codigo = fields.Char(string='Código:', required=True, default=_get_next_sequence)
    cotizacion_cod_sitio = fields.Char(string='Cod Sitio:', required=True)
    cotizacion_cliente = fields.Many2one('res.partner', 'Cliente', required=True, ondelete='cascade')
    cotizacion_fecha_emision = fields.Date('Fecha')
    cotizacion_observaciones = fields.Text('Cotización Observaciones')

    producto_contrato = fields.Many2one('product.category', 'Categoría')
    productos_relacionados = fields.One2many('producto.producto', 'cotizacion_relacionado', 'Producto')
    cotizacion_instalacion_creada = fields.Boolean('Instalación creada', default=False)

    # ------------------------------------------------------------------------------------------

    cotizacion_nombre_sitio = fields.Char(string='Nombre Sitio:')
    cotizacion_operador = fields.Selection([("ice", "ICE"), ("claro", "CLARO"), ("Entreprise", "ENTERPRICE"),
                                            ("jasec", "JASEC"), ("otro", "OTRO"), ("Telefonica", "TELEFONICA")],
                                           'Operadora')
    cotizacion_tipo_trabajo = fields.Many2one('tipo_trabajo.tipo_trabajo', 'Tipo Trabajo', required=True,
                                              ondelete='cascade')
    cotizacion_operador = fields.Selection(
        [("ice", "ICE"), ("claro", "CLARO"), ("Entreprise", "ENTERPRICE"), ("jasec", "JASEC"), ("otro", "OTRO"),
         ("Telefonica", "TELEFONICA")], 'Operadora')
    cotizacion_ubicacion_Gam_rural = fields.Selection([("gam", "GAM"), ("rural", "Rural")], 'Ubicación')
    cotizacion_ubicacion = fields.Char(string='Dirección:')
    cotizacion_provincia = fields.Selection(
        [('No Especificada', 'NO ESPECIFICADA'), ('san_jose', 'San Jose'), ('alajuela', 'Alajuela'),
         ('cartago', 'Cartago'), ('heredia', 'Heredia'), ('guanacaste', 'Guanacaste'), ('puntarenas', 'Puntarenas'),
         ('limon', 'Limón')], string='Provincia:')
    cotizacion_nombre_proyecto = fields.Char(string='Nombre Proyecto:')
    active = fields.Boolean('Activo', default=True)

    def unlink(self):
        for obj in self:
            obj.write({'active': False})
        return True

    def crear_instalacion_cotizacion(self, vals):

        if self.cotizacion_instalacion_creada == False:

            control_instalaciones_env = self.env['control_instalaciones.control_instalaciones']
            instalacion_vals = control_instalaciones_env.default_get(['name'])

            instalacion_vals.update({'cod_sitio': self.cotizacion_cod_sitio,
                                     'nombre_sitio': self.cotizacion_nombre_sitio,
                                     'nombre_proyecto': self.cotizacion_nombre_proyecto,
                                     'operador': self.cotizacion_operador, 'provincia': self.cotizacion_provincia,
                                     'tipo_trabajo': self.cotizacion_tipo_trabajo.id,
                                     'cliente': self.cotizacion_cliente.id})

            codProyecto = control_instalaciones_env.create(instalacion_vals)

            for cotizacion_productos in self.productos_relacionados:
                print('WWWWWWWWWWWWWWW:' + str(cotizacion_productos.producto_name.id) + '   ud:' + str(
                    cotizacion_productos.producto_ud) + '  precio:' + str(cotizacion_productos.producto_precio_unitario)
                      + '  total:' + str(cotizacion_productos.producto_precio_total) + ' asociado' + instalacion_vals[
                          'name'])

                self.env['item.item'].create({'name': cotizacion_productos.producto_name.id,
                                              'precio_unitario': cotizacion_productos.producto_precio_unitario,
                                              'ud': cotizacion_productos.producto_ud,
                                              'control_instalaciones_relacionado_cod_Proyecto': instalacion_vals[
                                                  'name'], 'control_instalaciones_relacionado': codProyecto.id

                                              })

            self.cotizacion_instalacion_creada = True

        print('++++++++++++++++  Duplicando Item 2++++++++++++++++++++++++')


# //////////////////////////////////////////////////////////////////////////////////////////////

class Cotizacioneswizard(models.TransientModel):
    _name = "cotizaciones.wizard"

    def _get_default_cotizacion(self):
        return self.env['cotizaciones_instalaciones.cotizaciones_instalaciones'].browse(
            self.env.context.get('active_ids'))

    wiz_cotizacion = fields.Many2one('cotizaciones_instalaciones.cotizaciones_instalaciones', string='proyectos',
                                     default=_get_default_cotizacion)
    wiz_cod_cotizacion = fields.Char('Cotización', related='wiz_cotizacion.codigo', store=False)
    wiz_cod_sitio = fields.Char('Cod Sitio', related='wiz_cotizacion.cotizacion_cod_sitio', store=False)


# //////////////////////////////////////////////////////////////////////////////////////////////

class Producto(models.Model):
    _name = "producto.producto"
    producto_name = fields.Many2one('product.product', 'Producto')

    producto_ud = fields.Float('Ud')
    producto_precio_unitario = fields.Float('Precio Unitario')
    producto_precio_total = fields.Float('Precio Total', compute='_compute_totall', store=True)
    cotizacion_relacionado = fields.Many2one('cotizaciones_instalaciones.cotizaciones_instalaciones', 'Cotización',
                                             ondelete='cascade')
    cotizacion_relacionado_id = fields.Char('cod Cotización', related='cotizacion_relacionado.codigo')

    @api.onchange('producto_name')
    def obtener_Precio_item_Onchange(
            self):  # Onchange para obtener el precio del producto seleccionado en el tab Item de proyectos
        self.producto_precio_unitario = self.producto_name.list_price

    @api.depends('producto_ud', 'producto_precio_unitario')
    def _compute_totall(self):
        for producto in self:
            producto.producto_precio_total = producto.producto_precio_unitario * producto.producto_ud




    # ************************************************************************************************************************
    # ************************************************************************************************************************
    # ************************************************************************************************************************
    # ************************************************************************************************************************
    # ************************************************************************************************************************
    # ************************************************************************************************************************

    """
    alter table add column supervisor_cliente boolean;
    alter table add column jefe_proyecto_cliente boolean;
    alter table add column jefe_proyecto boolean;
    alter table add column contrata boolean;
    alter table add column contrata_inst boolean;
    alter table add column jefe_cuadrilla boolean;
    alter table add column sup_telyman boolean;
    """
