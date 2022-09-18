# PyGravity (WIP)

Simple python gravitation simulator with real stars and planets dataset.

### Exmaple

```python
from gravity import body, system
import ploter
import numpy as np

from planets import earth

solar = system()

satellite = body(
		position=earth.position + np.array([0,earth.radius + 850000,0], dtype=float),
		mass=144,
		velocity=np.array([9000,1000,3000], dtype=float), 
		name="Satellite"
	    )

solar.addBody(earth)
solar.addBody(satellite)


motions = solar.simulate(10, 20000)

ploter.show2d(motions)
```