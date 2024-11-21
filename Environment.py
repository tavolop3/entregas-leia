import random
import Room


class Environment(object):
    def __init__(self):
        self.squares = []
        self.A, self.B = Room('A'), Room('B')
        self.squares.append(self.A)
        self.squares.append(self.B)
        self.A.right = self.B
        self.B.left = self.A
        self.points = 0
        
        for s in self.squares:
            s.dirt = random.randint(0,1)
        
    def __str__(self):
        return '[({},{}),({},{})]'.format(self.A, self.A.dirt, self.B, self.B.dirt) 
    
    def clean(self, room):
        if room.isDirty():
            room.clean()
            self.points += 1
            print('Limpieza en {}'.format(room))