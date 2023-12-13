import numpy as np
import matplotlib.pyplot as plt
import tikzplotlib   #install by 'conda install matplotlib=3.7 tikzplotlib'  , unfortunately newer matplotlib is currently not compatible with tikzplotlib, use virt env if necessary
import os

x = np.arange(100)
y = x**0.5

plt.figure()
plt.plot(x,y,'k')
plt.xlabel('x [-]')
plt.ylabel('y [-]')

tikzplotlib.save('simple_example.tex')