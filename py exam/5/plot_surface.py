import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

delta=0.025
x=np.arange(-3.0,3.0,delta)
y=np.arange(-2.0,2.0,delta)
X,Y=np.meshgrid(x,y)
rv1=scipy.stats.multivariate_normal([0.0,0.0],[[1.0,0.0],[0.0,1.0]])
Z1=rv1.pdf(np.dstack((X,Y)))
rv2=scipy.stats.multivariate_normal([1,1],[[1.5,0.0],[0.0,0.5]])
Z2=rv2.pdf(np.dstack((X,Y)))
Z=10.0*(Z2-Z1)
fig =plt.figure()
ax=fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z,cmap=plt.get_cmap('rainbow'),linewidth=0.2)
plt.show()