from django.utils import simplejson
from controller import Controller
from google.appengine.ext import db

class JSONController(Controller):
  MIME_TYPE = "json"

  def __init__(self, model):
    self.model = model
    self.model_name = model.__class__.__name__
    
  def index(self, request, response):
    model = self.model.all().get()
    self._dump(model, request, response)

  def new(self, request, response):
    pass

  def update(self, id, request, response):
    pass
  
  def delete(self, id, request, response):
    model.get(self._build_key(id)).delete

  def show(self, id, request, response):
    model = db.get(self._build_key(id))
    self._dump(model, request, response)

  def _build_key(self, id):
    return db.Key.from_path(self.model_name, id)