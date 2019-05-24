"""Practice: write a dog class
props: name, breed, (anything else you want)
methods: bark (anything else you want)"""

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.trick = []

    def add_trick(self, methods):
        self.trick.append(methods)

d = Dog('Rex, doberman')
e = Dog('spot, jack russell')
d.add_trick('roll over')
e.add_trick('play dead')
d.trick
e.trick
