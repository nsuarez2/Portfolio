import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("GET HOME")
    	template = JINJA_ENVIRONMENT.get_template('templates/home.html')
    	self.response.write(template.render({'page': 'Home'}))

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/home.html', HomeHandler)
], debug=True)