# -*- coding: utf-8 -*-
{
    'name':'Real Estate',
    'version':'1.0',
    'category':'Real Estate',
    'sequence':14,
    'summary':'',
    'description':""" Real Estate Management
      Properties 
      
      """,
    'author':'Yousef',
    'website':'https://www.syscorp.com',
    'depends':['base','theme_real_estate',],
    'data':[
        'security/real_estate_security.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.xml',
              
    ],
    'images': ['static/description/images/splash-screen.jpg'],
    'installable':True,
    'auto_install':False,
    'application':True,
    'qweb': ['static/src/xml/*.xml'],
}
