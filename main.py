import json
import jinja2
import datetime
import os

from google.appengine.api import users
from google.appengine.ext import ndb
#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#Google Login API

#Google Calendar API

#Embedding Google Calendar
def add_event(self):
    event_name = self.request.get('event-name')
    event_time_start = self.request.get('event-time-start')
    event_time_end = self.request.get('event-time-end')
    event_cat = self.request.get('event-cat')

def remove_event(self):
    pass 
