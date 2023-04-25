import numpy as np
temps = np.array([25, 30. 35, 40])
temps_f = (temps * 9/5) + 32

print(temps_f)

#[77. 86. 95. 104.]


## 
from unyt import degC, degF
#array temp in Celcius degree
temps = np.array([25, 30. 35, 40]) * degC
#Convert to Fahrenheit degree
temps_f = temps.to(degF)

print(temps_f)

##[77. 86. 95. 104.] Fahrenheit degree
