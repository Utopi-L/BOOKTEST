import numpy as np
from pylab import*
x=np.linspace(-np.pi,np.pi,100)
sin,cos=np.sin(x),np.cos(x)
plot(x,sin,color='blue',linewidth=2.0,linestyle='-',label='sin')
plot(x,cos,color='red',linewidth=2.0,linestyle='-',label='cos')
legend(loc='upper left')
show()