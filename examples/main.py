from gravity import body, system
import ploter

from planets import *
from stars   import sun

solar = system("solar")

earth.radius   = 6371000

solar.addBody(sun)
solar.addBody(mercury)
solar.addBody(earth)
solar.addBody(venus)
solar.addBody(mars)
#solar.addBody(jupiter)
#solar.addBody(saturn)
#solar.addBody(uranus)

motions = solar.simulate(1000, 20000)

ploter.show2d(motions)

#frames = ploter.framesDropper(motions, tragetFps=30, tragetDuration=10)
#ploter.anim2d(frames, history=20, directory="img", space="static")
#ploter.anim2mp4("img", "test2")