class Room(object):
    def __init__(self, name):
        self.name = name
        self.dirt = 0
        self.right = self
        self.left = self

    def __str__(self):
        return self.name
    
    def clean(self):
        self.dirt = 0

    def isDirty(self):
        return self.dirt == 1