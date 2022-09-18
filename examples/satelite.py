from gravity import body, system
import ploter
import numpy as np

from planets import earth

solar = system()

earth.radius   = 6371000
earth.color    = "blue"
earth.velocity = np.array([0,0,0], dtype=float)

satellite        = body(position=earth.position + np.array([0,earth.radius + 850000,0], dtype=float), mass=144, velocity=np.array([9000,1000,3000], dtype=float), name="Satellite")
satellite.color  = "red"
satellite.radius = 25

solar.addBody(earth)
solar.addBody(satellite)


motions = solar.simulate(10, 20000)

ploter.show2d(motions)
ploter.show3d(motions)

frames = ploter.framesDropper(motions, tragetFps=30, tragetDuration=30)
ploter.anim2d(frames, history=10, directory="img", space="static")
ploter.anim2mp4("img", "test2")