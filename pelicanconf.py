#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = 'Geoffrey Guéret'
SITENAME = 'Geoffrey Guéret'
SITEURL = ''
SITEDESC = "Site personnel d'un codeur autrefois devops."
# ensure correct length of the site description meta for mobile devices
assert len(SITEDESC) <= 120

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/ggueret', open('content/extras/social/github.svg').read()),
    ('LinkedIn', 'https://www.linkedin.com/in/ggueret/', open('content/extras/social/linkedin.svg').read()),
    ('Malt', 'https://www.malt.fr/profile/geoffreygueret', open('content/extras/social/malt.svg').read()),
)

# Hosting widget
HOSTING_NAME = "localhost"

COPYRIGHT_YEAR = datetime.date.today().year

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
        "markdown.extensions.toc": {"permalink": "", "permalink_class": "headerlink"}
    },
    "output_format": "html5",
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["assets", "sitemap"]

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = ARTICLE_URL + "index.html"
DRAFT_URL = "drafts/{slug}/"
DRAFT_SAVE_AS = DRAFT_URL + "index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
DRAFT_PAGE_URL = "drafts/pages/{slug}/"
DRAFT_PAGE_SAVE_AS = DRAFT_PAGE_URL + "index.html"
AUTHOR_SAVE_AS = CATEGORY_SAVE_AS = ""
TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = ARCHIVES_URL + "index.html"
TAGS_URL = "tags/"
TAGS_SAVE_AS = TAGS_URL + "index.html"

SITEMAP = {
    "format": "xml",
    "changefreqs": {
        "articles": "weekly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

# Disable "authors" and "categories" pages
DIRECT_TEMPLATES = ["index", "tags", "archives"]
DELETE_OUTPUT_DIRECTORY = True
