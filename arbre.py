from state import *

class Arbre():

    def __init__(self, x, y, state:State):
        self.pos = [x, y]
        self.state = state

    def grow(self):
        if (self.state == State.lowTree or self.state == State.midTree):
            self.state += 1

    def growFruits(self):
        if (self.state == State.highTree):
            self.state += 1

    def getPos(self):
        return self.pos

    def setPos(self, x, y): # Peut etre utile mais normalement non
        self.pos = [x, y]

    def getState(self):
        return self.state

    def setState(self, state:State):
        self.state = state
    
