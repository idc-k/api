class MyClass:
    def __init__(self, name):
        self.name = name 
        self.accessories = []
    def add_accessory(self, accessory):
        self.accessories.append(accessory)

katy = MyClass('katy')
katy.add_accessory('handbag')
print(katy.accessories)

class Movie:
    def __init__(self, name, director):
        self.name = name 
        self.director = director 
        self.cast = []
    def add_cast(self, person):
        self.cast.append(person)
        
movie = Movie('Pirates of the Caribbean', 'Bro')
movie.add_cast('johnny depp')
print(movie.cast)

movie.add_cast('whagter')
print(movie.cast)
