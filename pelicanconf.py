#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mike Walton'
SITENAME = "Mike Walton"
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = 'machine learning results and ramblings'
SITELOGO = 'https://avatars0.githubusercontent.com/u/1017968?v=3&u=489ec35a177e0a3d2454fe6699958799c27fab4d&s=400'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'
THEME='./themes/Flex'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MAIN_MENU = True

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/michael-walton-35135438'),
          ('github', 'https://github.com/mwalton'),
          ('google', 'https://plus.google.com/+MykeWalton'),
          ('facebook', 'https://www.facebook.com/myke.walton.3'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IPYNB_IGNORE_CSS=True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
