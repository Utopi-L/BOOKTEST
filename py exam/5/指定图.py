import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5,10)
y=x**2
fig, axes=plt.subplots(figsize=(8,6),dpi=100)
axes.plot(x,y,'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
plt.show()