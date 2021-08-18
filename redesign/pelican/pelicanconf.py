#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'marvic'
SITENAME = 'NAUFIP'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Bratislava'

DEFAULT_LANG = u'sk'

# Set custom theme
THEME = 'themes/naufip'

# Main menu
MENUITEMS = [
    ('Domov','/'),
    ('O projekte','/pages/o-projekte.html'),
    ('Riešiteľský kolektív','/pages/riesitelsky-kolektiv.html'),
    ('Aktivity', '/category/activities.html'),
    ('Výstupy','/pages/vystupy.html'),
    ('Médiá','/category/media.html')
]

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Plugins settings
PLUGIN_PATHS = ["./plugins/"]
PLUGINS = ['i18n_subsites', 'gallery']

# Gallery plugin config
GALLERY_PATH = "./images/gallery"
IMAGE_PATH = "./images"
THUMBNAIL_DIR = "./images"
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_KEEP_TREE = True

# Translation settings
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

I18N_SUBSITES = {
    'en': {
        'THEME': 'themes/naufip-en',
	    'SITENAME': 'NAUFIP',
        'GALLERY_PATH': "./images/gallery",
        'MENUITEMS': [
            ('Home', '/en'),
            ('About', '/en/pages/about-the-project.html'),
            ('Researchers', '/en/pages/researchers.html'),
            ('Activities', '/en/category/activities.html'),
            ('Publications', '/en/pages/publications.html'),
            ('Media', '/en/category/media.html')
        ]
    }
#         'MENUITEMS': [('Home','/en'),
#                       ('About','/en/pages/about-the-project.html'),
#                       ('Researchers','/en/pages/researchers.html'),
#                       ('Activities', '/en/category/activities.html'),
#                       ('Publications','/en/pages/publications.html'),
#                       ('Media','/en/category/media.html'),
#         ]
#     }
}

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
