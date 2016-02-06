__author__ = 'Jorian'

def chorus():
    print("Old MacDonald had a farm, ee-igh, ee-igh, oh!")


def animalInSong(animal):
    chorus()
    print("And on that farm he had a", animal + ".")
    print("with a moo moo here and a moo moo there")
    print("Here a moo, there a moo moo moo moo moo")
    chorus()

animalInSong("Cow")
print()
animalInSong("Sheep")
print()
animalInSong("Chicken")