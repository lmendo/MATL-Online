"""Javascript and CSS assets for the application."""

from flask_assets import Bundle, Environment

css = Bundle(
    'css/style.css',
    'lib/bootstrap-drawer.min.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'js/main.js',
    'lib/drawer.min.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
