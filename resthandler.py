from google.appengine.ext.webapp import RequestHandler
from json_controller import JSONController

class ReSTHandler(RequestHandler):

  def __init__(self, model, controllers=[JSONController]):
    self.controllers = dict( [(controller.MIME_TYPE, controller(model)) for controller in controllers] )

  def get(self, id=None, mime_type=None):  
    if id:
      return self.controllers[mime_type].show(id, self.request, self.response)
    else:
      return self.controllers[mime_type].index(self.request, self.response)

  def post(self, id=None, mime_type=None):
    if id:
      return self.controllers[mime_type].append(id, self.request, self.response)
    else:
      return self.controllers[mime_type].new(self.request, self.response)

  def put(self, id=None, mime_type=None):
    if id:
      return self.controllers[mime_type].update(id, self.request, self.response)
    else:
      return self.controllers[mime_type].batch_replace(self.request, self.response)

  def delete(self, id=None, mime_type=None):
    if id:
      return self.controllers[mime_type].delete(id, self.request, self.response)
    else:
      return self.controllers[mime_type].batch_delete(self.request, self.response)
