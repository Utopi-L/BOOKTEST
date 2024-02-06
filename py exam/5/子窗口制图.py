import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5,10)
y=x**2
plt.subplot(1,2,1)
plt.plot(x,y,'r--')
plt.subplot(1,2,2)
plt.plot(y,x,'g*-')
plt.show()