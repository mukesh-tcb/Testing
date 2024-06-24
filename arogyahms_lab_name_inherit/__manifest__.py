# -*- coding: utf-8 -*-

{
    'name': "Arogyahms Addons Lab Name",
    'summary': """
        arogyahms app changes and custimizations
        """,
    'description': """ """,
    'author': "Mukesh Kumar",
    'website': "",

    'category': 'healthcare',
    'version': '0.1',

    'depends': ['sysadmin','hospital_mgmt','base','sale','hr','mail','purchase','account'],

    'data': [
        'security/ir.model.access.csv',
        # 'views/sale_order_inherit_view.xml',
        'views/lab_name_inherit_view.xml',
        'views/medical_lab_test_inherit_view.xml',
        'views/x-ray_size_master_view.xml',
       
        'views/direct_invoice_view.xml',
        'views/patient_group_inherit_view.xml',
        'views/account_move_inherit_view.xml',
        
        'views/medical_lab_list_inherit_view.xml',
        'views/res_partner_inherit_view.xml',
        # 'views/account_move_line_inherit_view.xml'
        'views/Hospital_menus_inherit.xml',
        
    ]
}