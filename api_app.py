import os
import asyncio
import tracemalloc
from redis.asyncio import client, from_url
import redis
import datetime
from sanic import Sanic
from sanic.response import json, html, text
from sanic.response import text
from sanic_redis import SanicRedis
from redis_om import HashModel
from sanic import HTTPResponse, Sanic
from redis.commands.json.path import Path
from sanic.views import HTTPMethodView
from sanic.response import text

app = Sanic("SimpleAPI")
rows = []
HOST = "localhost"
PORT = 6379

r = redis.Redis(host = "localhost", port = 6379)

app.config.update(
    {
        'REDIS' : "redis://localhost:6379",
        'REDIS1' : "redis://localhost:6379/1",
        #'REDIS2': "redis://localhost:6379/2",
    }
)

redis = SanicRedis() # default config_name is "REDIS"
redis.init_app(app)

redis1 = SanicRedis(config_name = "REDIS1")
redis1.init_app(app)

@app.route("/")
async def data(request) :
    template = open(os.getcwd() + "\index.html")
    return html(template.read())

@app.route("/apps")
async def data(request) :
    template = open(os.getcwd() + "\apps.html")
    return html(template.read())

@app.get("/data")
async def data(request) :
    template = open(os.getcwd() + "\data.html")
    return html(template.read())

@app.get("apps.imdb.movies")
async def data(request) :
    template = open(os.getcwd() + "\data.html")
    return html(template.read())

class Movie(HTTPMethodView): 
    @app.get("/savemovie")
    def get(request):
        name = "Harry Potter and the philosopher's stone" 
        director = "Chris Columbus"
        movie = {"name" : name, "director": director} 
        r.json().set('movie:3', '$', movie)
        result = r.json().get('movie:3')
        r.save()
        return text(str(result))
    
              
@app.route("apps.spotify.songs")
async def data(request) :
    template = open(os.getcwd() + "\music.html")
    return html(template.read())

class Music(HTTPMethodView): 
    def __init__(self, song, artist): 
        self.song = song 
        self.artist = artist
        self.track = {"song" : song, "artist": artist} 
    
    #@app.post("/postsong")
    #def post(request, track):
    #    r.json().set('movie:1', '$', track)
        
    @app.get("/getsong")
    def get(request, track):
        r.json().set('song:1', '$', track)
        result = r.json().get('song:1')
        r.save()
        return text(str(result))
        #movie = {"name": name, "director": director}
        
    #@app.delete("/deletesong")
    #def delete(request, track):
    #    print("delete song")
        
@app.route("apps.homework.tasks")
async def data(request) :
    template = open(os.getcwd() + "\music.html")
    return html(template.read())
    
class Music(HTTPMethodView): 
    def __init__(self, assignment, due_date): 
        self.assignment = assignment 
        self.due_date = due_date
        self.task = {"song" : assignment, "artist": due_date} 
        
    @app.post("/posttask")
    def post(request, task):
        r.json().set('movie:1', '$', task)
        
    @app.get("/savetask")
    def get(request, task):
        r.json().set('song:1', '$', task)
        result = r.json().get('song:1')
        r.save()
        return text(str(result))
        #movie = {"name": name, "director": director}
        
    @app.delete("/deletetask")
    def delete(request, task):
        print("delete task")
    
if __name__ == "__main__" :
    app.run(debug = True)
    #app.run(host=HOST, port=PORT, debug=True)