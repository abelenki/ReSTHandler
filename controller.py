from django.utils import simplejson

class Controller(object):
  """The following should all be made to set the response to 404"""

  MIME_TYPES = {"json" : "application/json", "html": "text/html"}

  def index(self, request, response):
  	pass

  def new(self, request, response):
    pass

  def update(self, id, request, response):
    pass
  
  def delete(self, id, request, response):
    pass
  
  def append(self, id, request, response):
    pass

  def show(self, id, request, response):
  	pass

  def batch_replace(self, request, response):
    pass
  
  def batch_delete(self, request, response):
    pass

  def _dump(self, model, request, response):
    callback = request.get("callback")
    json = simplejson.dumps(model)
    if callback:
      json = "%s( %s );" % (callback, json)
    
    response.headers.add_header('Content-type', self.MIME_TYPES[self.MIME_TYPE])
    return response.out.write( json )
