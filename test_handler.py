from django.utils import simplejson
from controller import Controller
from resthandler import ReSTHandler
import logging

class TestHandler(ReSTHandler):
  def __init__(self):
    super(TestHandler, self).__init__({}, [TestController])

class TestController(Controller):
  MIME_TYPE = "json"

  def __init__(self, model):
    self.model = model
    self.model_name = model.__class__.__name__
    logging.info(self.model_name)

  def index(self, request, response):
    logging.info("Response class: %s" % response.__class__.__name__)
    model = [ 1, 2, 3, 4, 5]
    self._dump(model, request, response)

  def new(self, request, response):
    logging.info("Response class: %s" % response.__class__.__name__)
    self._dump("this should be a url", request, response)

  def update(self, id, request, response):
    logging.info("Data: %s" % request.body)
    self._dump("this should also be a 200", request, response)
  
  def delete(self, id, request, response):
    logging.info("Trying to delete: %s" % id )
  
  def append(self, id, request, response):
    self._dump("this should add something to entry if it is a list", request, response)

  def show(self, id, request, response):
    self._dump("this should be the contents of an entity", request, response)

  def batch_replace(self, request, response):
    self._dump("this should replace the entire list of stuff", request, response)
  
  def batch_delete(self, request, response):
      logging.info("Trying to delete everything")
