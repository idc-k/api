class Movie(HTTPMethodView): 
    def __init__(self, name, director): 
        self.name = name 
        self.director = director 
        self.movie = {"name" : name, "director": director} 
    #@app.post("/postmovie")
    #def post(request, movie):
    #    r.json().set('movie:1', '$', movie)
        
    @app.get("/savemovie")
    def get(request):
        r.json().set('movie:3', '$', {"director" : "abc", "rating":5})
        result = r.json().get('movie:3')
        r.save()
        return text(str(result))
    
    #@app.delete("/deletemovie")
    #def delete(request, movie):
    #    print("delete movie")