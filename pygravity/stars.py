from gravity import body
import numpy as np

sun = body(position=np.array([0,0,0], dtype=float), mass=2e30, velocity=np.array([0,0,0], dtype=float), name="sun")