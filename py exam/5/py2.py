import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-5,5,0.1)
y=x**2
plt.xlim(-5,5)
plt.ylim(0,100)
plt.xlabel("x")
plt.ylabel("y=x*x")
plt.title("Plot y=x*x")
plt.plot(x,y)
plt.show()