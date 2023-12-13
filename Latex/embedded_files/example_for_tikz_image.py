import numpy as np
import matplotlib.pyplot as plt
import tikzplotlib
import os

x = np.arange(100)
y = x**0.5

plt.figure()
plt.plot(x,y,'k')
plt.xlabel('x [-]')
plt.ylabel('y [-]')

tikzplotlib.save('simple_example.tex')