from sanic.views import HTTPMethodView
from sanic.response import text

class SimpleView(HTTPMethodView):

  def get(self, request):
      return text("I am get method")

  # You can also use async syntax
  async def post(self, request):
      return text("I am post method")

  def put(self, request):
      return text("I am put method")

  def patch(self, request):
      return text("I am patch method")

  def delete(self, request):
      return text("I am delete method")
app.add_route(SimpleView.as_view(), "/bru")
  
class SimpleView(HTTPMethodView):
    #def __init__(self, name = "name", director = "director"):
    #    self.name = name
    #    self.director = director
    #def get(self, request):
        #return print(self.name)
    def __init__(self,  name):
        self.name = "yo"
    async def get(self, request):
        async with redis.conn as r :
            await r.set("bro", "yo")
            result = await r.get("bro")
            r.save()
        return text(str(result))
app.add_route(SimpleView.as_view(), "/")



 
