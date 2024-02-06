def aa(X,Y,sigx=1.0,sigy=1.0,mu_x=0.0,mu_y=0.0,sigxy=0.0):
    Xmu=X-mu_x
    Ymu=Y-mu_y
    ro=sigxy/(sigx*sigy)
    z=Xmu**2/sigx**2 + Ymu**2/sigy**2-2*ro*Xmu*Ymu/(sigx*sigy)
    denom=2*np.pi*sigx*sigy*np.sqrt(1-ro**2)
    return np.exp(-z/(2*(1-ro**2)))/denom
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
delta=0.025
x=np.arange(-3.0,3.0,delta)
y=np.arange(-2.0,2.0,delta)
X,Y=np.meshgrid(x,y)
Z1=aa(X,Y,1.0,1.0,0.0,0.0)
Z2=aa(X,Y,1.5,0.5,1,1)
Z=10.0*(Z2-Z1)
plt.figure()
plt.figure()
CS=plt.contour(X,Y,Z,10)
plt.clabel(CS,inline=1,fontsize=10)
plt.title('Simplest default with labels')
plt.show()
