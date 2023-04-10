AUTHOR = 'Helder Oliveira'
SITENAME = "Helder's Home Page"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'MST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

OUTPUT_PATH = 'output'

# static paths will be copied under the same name
STATIC_PATHS = ['img', 'src']

THEME = "themes/blue-penguin"

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SUPPRESS_CATEGORIES_ON_MENU = True
SUPPRESS_ITEM_CATEGORIES = True
DISPLAY_PAGES_ON_MENU = True
DELETE_OUTPUT_DIRECTORY = True