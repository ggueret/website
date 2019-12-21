#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Geoffrey Guéret'
SITENAME = 'Geoffrey Guéret'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# CUSTOMS
THEME = "themes/third"

STATIC_PATHS = ("extras",)
EXTRA_PATH_METADATA = {
    "extras/robots.txt": {"path": "robots.txt"},
    "extras/favicon.ico": {"path": "favicon.ico"},
    "extras/favicon.svg": {"path": "favicon.svg"},
    "extras/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "extras/android-chrome-256x256.png": {"path": "android-chrome-256x256.png"},
    "extras/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "extras/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extras/browserconfig.xml": {"path": "browserconfig.xml"},
    "extras/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extras/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extras/mstile-150x150.png": {"path": "mstile-150x150.png"},
    "extras/safari-pinned-tab.svg": {"path": "safari-pinned-tab.svg"},
    "extras/site.webmanifest": {"path": "site.webmanifest"}
}

DEFAULT_CATEGORY = "misc"
USE_FOLDER_AS_CATEGORY = False

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": "", "permalink_class": "headerlink fas fa-link"}
    },
    "output_format": "html5",
}

PLUGINS = ["plugins.assets"]

ARTICLE_URL = ARTICLE_SAVE_AS = "{slug}.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
