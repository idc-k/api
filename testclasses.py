from api_app import Movie, Music
import asyncio 


sv = Movie("yo", "man")
print(sv.name)
#sv.add_movie("wonderwall", "mania")
movie = sv.movie
asyncio.run(sv.get())

music = Music("bro", "nice")
print(music.artist)



