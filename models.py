from google.appengine.ext import ndb

class Event(ndb.Model):
    name = ndb.StringProperty(required=True)
    start_time = ndb.DateTimeProperty(required=True)
    end_time = ndb.DateTimeProperty(required=True)
    owner_id = ndb.StringProperty(required=True)
