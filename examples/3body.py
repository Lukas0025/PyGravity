from gravity import body, system
import ploter

from planets import *
from stars   import sun

AU = 1.5e11

solar = system("trisolaris", dimensions=2)

a = body(position=np.array([-2*AU,0],    dtype=float), mass=3.0e30,     velocity=np.array([10000,-10000], dtype=float), name="A")
b = body(position=np.array([0,2*AU],     dtype=float), mass=2.0e30,     velocity=np.array([-10000,-10000],dtype=float), name="B")
c = body(position=np.array([3*AU,0],     dtype=float), mass=3.0e30,     velocity=np.array([-10000,10000], dtype=float), name="C")
d = body(position=np.array([-2*AU,-1*AU], dtype=float), mass=earth.mass,velocity=np.array([1000,10000],   dtype=float), name="Trisolaris")

solar.addBody(a)
solar.addBody(b)
solar.addBody(c)
solar.addBody(d)

motions = solar.simulate(1, 1000000)

frames = ploter.framesDropper(motions, tragetFps=60, tragetDuration=10)
ploter.anim2d(frames, history=20, directory="img", space="dynamic")
ploter.anim2mp4("img", "test", fps=60)