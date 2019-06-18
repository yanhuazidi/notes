# -*- coding: utf-8 -*-

{
    'name': '微信支付',
    'category': 'Website',
    'summary': '微信支付',
    'version': '1.1.27',
    'description': """商城微信支付""",
    'author': "Gavin Gu",
    'website': "",
    'depends': ['website', 'payment'],
    'data': [
        'templates/payment_weixin_templates.xml',
        'data/weixin.xml',
        'views/payment_acquirer.xml',
        'views/action_confirm_template.xml',
        # error page
        'views/payment_error_template.xml',

    ],
    'installable': True,
}
