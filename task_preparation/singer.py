class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello my name is " + self.name)


class Singer(Person):

    def __init__(self, name, age):
        super(Singer, self).__init__(name, age)
        self.songs = ['Unforgettable Day', 'Love of Tired Swans', 'Olympico']
        self.vocal_range = ('A1', 'C8', 'L8', 'D9', 'C9')
        self.perfomances = {'Unforgettable Day': ['Niahoo Square', 'Beijing', 2017],
                            'Love of Tired Swans': ['Kremle Palace', 'Moscow',  2018],
                            'Olympico': ['Dynamo Stadium', 'Minsk', 2019]
                            }

    def print_my_favourite_songs(self):
        for index, song in enumerate(self.songs, start=1):
            print 'My favourite song {}:  "{}".'.format(str(index), song)

    def find_world_highest_note(self):
        if 'D9' in self.vocal_range:
            print True

    def choose_cities(self):
        perfomances = self.perfomances
        for song, information in perfomances.items():
            print 'The song "{}" was performed in {}.'.format(song, information[1])

    def greeting(self):
        print("Hello my name is!!! " + self.name)


dimash = Singer('Dimash', 25)

print(dimash.songs[2])
print(dimash.vocal_range)
print(dimash.perfomances['Olympico'])

dimash.print_my_favourite_songs()
dimash.find_world_highest_note()
dimash.choose_cities()

dimash.greeting()
