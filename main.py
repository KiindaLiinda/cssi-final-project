import json
import jinja2
import datetime
import os
import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb
#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#Homepage Handler
class HomepageHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("html-css/index.html")
        self.response.write(start_template.render())

#Embedding Google Calendar
class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        start_string = self.request.get('starttime')
        start_date = datetime.strptime(start_string, "%Y-%m-%dT%H:%M")
        start_utc = start_date + timedelta(hours=7)
        end_utc = start_utc + timedelta(hours=1)

        calendar_url = "http://www.google.com/calendar/event?action=TEMPLATE&text=%s&dates=%s/%s"
        calendar_start = start_utc.strftime("%Y%m%dT%H%M00Z")
        calendar_end = end_utc.strftime("%Y%m%dT%H%M00Z")

        calendar_link = calendar_url % ("TestEvent",calendar_start, calendar_end)
        calendar_html = "<html><body><a target='_blank' href='%s'>Test Event Link</a></body></html>"
        self.response.write(calendar_html % calendar_link)

app = webapp2.WSGIApplication([
    ('/', HomepageHandler),
    ('/newevent', NewEventHandler),
], debug=True)
