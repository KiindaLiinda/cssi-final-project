import json
import jinja2
import datetime
import os
import webapp2

from datetime import datetime
from datetime import timedelta
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
        start_template = jinja_current_dir.get_template("html/index.html")
        self.response.write(start_template.render())

#Embedding Google Calendar
class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("html/newevent.html")
        self.response.write(start_template.render())
    def post(self):
        event_name = self.request.get('event-name')
        start_string = self.request.get('start-time')
        end_string = self.request.get('end-time')
        if start_string and end_string and event_name:
            start_date = datetime.strptime(start_string, "%Y-%m-%dT%H:%M")
            end_utc = datetime.strptime(end_string, "%Y-%m-%dT%H:%M")
            start_utc = start_date + timedelta(hours=7)

            calendar_url = "http://www.google.com/calendar/event?action=TEMPLATE&text=%s&dates=%s/%s"
            calendar_start = start_utc.strftime("%Y%m%dT%H%M00Z")
            calendar_end = end_utc.strftime("%Y%m%dT%H%M00Z")

            calendar_link = calendar_url % (event_name, calendar_start, calendar_end)
            calendar_html = "<HTML><BODY><A href='%s' target='_blank'>~View Event~</A></BODY></HTML>"
            self.response.write(calendar_html % calendar_link)
        else:
            self.redirect('/newevent')

#class AllEventsHandler(webapp2.RequestHandler):
#    def get(self):
#        all_events_url: "https://www.googleapis.com/calendar/v3/calendars/calendarId/events"

app = webapp2.WSGIApplication([
    ('/', HomepageHandler),
    ('/newevent', NewEventHandler),
], debug=True)
