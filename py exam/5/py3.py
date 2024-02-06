from turtle import color
import numpy as np
from pylab import*
x=np.linspace(-np.pi,np.pi,100)
cos=np.cos(x)
xticks(np.linspace(-np.pi,np.pi,5))
plot(x,cos,color='red',linewidth=2.0,linestyle='-')
show()