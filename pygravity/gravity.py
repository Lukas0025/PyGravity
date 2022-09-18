import numpy as np
import copy

class body:
    def __init__(self, position, mass, velocity, name = ""):
        self.position     = position
        self.mass         = mass
        self.velocity     = velocity
        self.acceleration = np.zeros(1, dtype=float)
        self.name         = name
        self.color        = None
        self.radius       = None

class system:
    def __init__(self, name="", dimensions=3):
        self.name   = name
        self.bodies = []
        self.dimensions = dimensions
        self.G = 6.67408e-11 #m3 kg-1 s-2

    def addBody(self, body):
        self.bodies.append(body)

    def getBody(self, name):
        for body in self.bodies:
            if body.name == name:
                return body

        return none

    def __updateBodyAcceleration(self, body):
        body.acceleration = np.zeros(self.dimensions, dtype=float)
        for otherBody in self.bodies:
            if not(otherBody is body):
                r = np.sqrt(np.sum(np.power(body.position - otherBody.position, 2)))
                globalAcceleration = (self.G * otherBody.mass) / (r ** 3)
                
                body.acceleration += (otherBody.position - body.position) * globalAcceleration


    def simulate(self, step, steps):
        pos = []
        for stepIndex in range(steps):

            for body in self.bodies:
                self.__updateBodyAcceleration(body)
                body.velocity += body.acceleration * step

            for body in self.bodies:
                body.position += body.velocity * step

            pos.append(copy.deepcopy(self))

        return pos