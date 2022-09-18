from gravity import body
import numpy as np

mercury = body(position=np.array([0,5.7e10,0], dtype=float), mass=3.285e23, velocity=np.array([47000,0,0], dtype=float), name="Mercury")
venus   = body(position=np.array([0,1.1e11,0], dtype=float), mass=4.8e24,   velocity=np.array([35000,0,0], dtype=float), name="Venus")
earth   = body(position=np.array([0,1.5e11,0], dtype=float), mass=6e24,     velocity=np.array([30000,0,0], dtype=float), name="Earth")
mars    = body(position=np.array([0,2.2e11,0], dtype=float), mass=2.4e24,   velocity=np.array([24000,0,0], dtype=float), name="Mars")
jupiter = body(position=np.array([0,7.7e11,0], dtype=float), mass=1e28,     velocity=np.array([13000,0,0], dtype=float), name="Jupiter")
saturn  = body(position=np.array([0,1.4e12,0], dtype=float), mass=5.7e26,   velocity=np.array([9000,0,0], dtype=float),  name="Saturn")
uranus  = body(position=np.array([0,2.8e12,0], dtype=float), mass=8.7e25,   velocity=np.array([6835,0,0], dtype=float),  name="Uranus")
neptune = body(position=np.array([0,4.5e12,0], dtype=float), mass=1e26,     velocity=np.array([5477,0,0], dtype=float),  name="Neptune")
pluto   = body(position=np.array([0,3.7e12,0], dtype=float), mass=1.3e22,   velocity=np.array([4748,0,0], dtype=float),  name="Pluto")
