#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Author
AUTHOR = "Rick Bryce"
AUTHOR_EMAIL = "dev.null@dicbo.bz"
AUTHOR_COUNTRY = "U.S.A."
AUTHOR_REGION = "CA"
AUTHOR_LOCALITY = "San Francisco"

SITENAME = "dicbo.bz"
SITEURL = 'https://dicbo.bz'

# Settings
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 15
#DEFAULT_METADATA = ("don't", "panic")
DEFAULT_DATE = (2013, 01, 01, 14, 01, 01)

DEFAULT_CATEGORY = ('Misc')
# REVERSE_CATEGORY_ORDER = True
NEWEST_FIRST_ARCHIVES = True
DISPLAY_PAGES_ON_MENU = True
#PAGES = ('resume', 'about me')
#MENUITEMS = (('Mirwin','http://mirwin.net/'),
#        ('Cernio','http://cernio.coop/'))

SUMMARY_MAX_LENGTH = 135

#TYPOGRIFY = True
RELATIVE_URLS = True

# PDF_GENERATOR = False
OUTPUT_SOURCES = False

THEME = "bootstrap"
#STATIC_PATHS = (['images'])
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
THEME_STATIC_PATHS = (['static'])

FILES_TO_COPY = (('webroot/robots.txt', 'robots.txt'),
                 ('webroot/humans.txt', 'humans.txt'),
                 ('webroot/favicon.ico', 'favicon.ico'),)

CSS_FILE = "main.css"
COMMENTS_DIR = ['comments']

MARKUP = (('md', 'markdown'))
MD_EXTENSIONS = (['codehilite','extra'])

# Blogroll
LINKS =  (('jirwin', 'http://jirwin.net', 'friend met'),
          ('Mike Burns', 'http://unemployeable.me/', 'friend met'),
          ('bkero', 'http://bke.ro/', 'friend co-worker met'),
          ('Mozilla', 'http://mozilla.org', ''),)

# Social widget
# FACEBOOK_APPID
TWITTER_USERNAME = "djdicbob"
SOCIAL = (('@djdicbob', 'https://twitter.com/djdicbob'),
#      ('Google', 'https://plus.google.com/107225813711437200584/'),
#      ('Facebook', 'https://www.facebook.com/michael.andrew.burns'),
#      ('YouTube', 'https://www.youtube.com/user/maburns210'),
#      ('LinkedIn', 'http://www.linkedin.com/in/maburns/'),
      ('Last.fm', 'http://www.last.fm/user/djdicbob'),)

# Plugins
# PLUGINS_PATH = ""
#PLUGINS=['pelican.plugins.gravatar','pelican.plugins.sitemap',]
#'pelican.plugins.related_posts',]

# Github
GITHUB_URL = "https://github.com/dicbob/"
GITHUB_USER = "dicbob"
GITHUB_ACTIVITY_FEED = 'https://github.com/dicbob.atom'


SITEMAP_SAVE_AS = 'sitemap.xml'
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
