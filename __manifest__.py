# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Telyman Control de Instalaciones',
    'version': '1.0',
    'summary': 'Control de Instalaciones',
    'description': """
   
    Control de Instalaciones para proyectos
    
    """,
    'category': 'tools',
    'website': 'https://www.Telyman.com',
    'depends': ['product','sale'],
    'data': [
        
        'reporte1.xml',
        'report/reporte1_lista.xml',
        'reporte2.xml',
        'report/reporte2_lista.xml',
        'reporte4.xml',
        'report/reporte_orden_compra4.xml',
        'reporte5.xml',
        'report/reporte_orden_compra5.xml',
        'reporte6.xml',
        'report/reporte_orden_compra6.xml',
        'reporte7.xml',
        'report/reporte_cotizaciones_1.xml',
        'reporte8.xml',
        'report/reporte_cotizaciones_2.xml',
        'grafico/graficoTrabajo1.xml',
        'data/tipo.seguimiento.administrativo.csv',
        'data/tipo.seguimiento.tecnico.csv',
        'data/sequence.xml',
        'security/gruposTelyman.xml',
        "security/ir.model.access.csv",
        #'views/contratas_wizard_view.xml',
         'views/reportes.xml',
        'views/project_view.xml',
        'views/hr_employee.xml',
        'views/sites.xml',
         'views/view.xml',
        'views/instalations.xml',
        'views/items.xml',
        'views/contractors.xml',
        'views/history.xml',
        'views/menu.ir.xml'



    ],
    'demo': [],
    'installable': True,
    'auto_install': False
}
