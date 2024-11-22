import random

class Room(object):
    def __init__(self, name):
        self.name = name
        self.dirty = False
        self.neighbour = self

    def __str__(self):
        return self.name
    
    def clean(self):
        self.dirty = False

    def is_dirty(self):
        return self.dirty

    def random_dirty(self):
        self.dirty = bool(random.getrandbits(1))


class Environment(object):
    def __init__(self):
        self.squares = []
        self.A, self.B = Room('A'), Room('B')
        self.squares.append(self.A)
        self.squares.append(self.B)
        self.A.neighbour = self.B
        self.B.neighbour = self.A
        
        for s in self.squares:
            s.dirty = bool(random.getrandbits(1))
        
    def __str__(self):
        return '[({},{}),({},{})]'.format(self.A, self.A.dirty, self.B, self.B.dirty) 
    
    def random_room(self) -> Room:
        return random.choice(self.squares)