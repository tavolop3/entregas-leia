class Agent(object):
    def __init__(self, environment):
        self.environment = environment
        self.step = 0

    def suck(self):
        self.environment.clean(self.room)

    def noOp(self):
        pass

    def moveRight(self):

        self.step += 1

    def moveLeft(self):
        self.step += 1

    def __str__(self):
        return 'El agente está en el cuarto {}'.format(self.room)
