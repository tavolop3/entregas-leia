from environment import Environment
from environment import Room

class Agent(object):
    def __init__(self, environment: Environment):
        self.environment = environment
        self.location = environment.random_room()
        self.points = 0
        self.steps = 0

    def start(self, steps):
        for i in range(steps):
            #Limpiar o no
            print (
                f"======Paso:{i}======\n"
                f"Estoy parado en {self.location}"
            )
            if self.location.is_dirty():
                self.clean()
            else:
                self.move()
            print(self.environment)
        self.steps = steps
            
    def suck(self):
        self.environment.clean(self.room)

    def clean(self):
        self.location.clean()
        self.points += 10
        print("Estoy limpiando")

    def move(self):
        print(f"Estoy parado en {self.location}")
        self.location.random_dirty()
        self.location = self.location.neighbour
        self.points -= 1

    def noOp(self):
        pass

    def get_performance(self):
        print(f"Puntos: {self.points}")
        print(f"Pasos: {self.steps}")
        return self.points / self.steps

    def __str__(self):
        return 'El agente está en el cuarto {}'.format(self.room)