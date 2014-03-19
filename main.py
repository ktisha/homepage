#!/usr/bin/env python

from bottle import Bottle, template, static_file

# Run the Bottle wsgi application. We don't need to call run() since our
# application is embedded within an App Engine WSGI application server.
bottle = Bottle()

@bottle.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@bottle.route('/')
def home():
  return template("home")

@bottle.route('/contact')
def contact():
  return template("contact_me")

@bottle.route('/projects')
def contact():
  return template("projects")


@bottle.error(404)
def error_404(error):
  """Return a custom 404 error."""
  return 'Sorry, Nothing at this URL.'


