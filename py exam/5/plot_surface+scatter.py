import numpy as np
import matplotlib.pyplot as plt
from random import seed,random
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_surf=np.arange(0.1,0.01)
y_surf=np.arange(0.1,0.01)
x_surf,y_surf=np.meshgrid(x_surf,y_surf)
z_surf=np.sqrt(x_surf+y_surf)
ax.plot_surface(x_surf,y_surf,z_surf);
n=100;seed(0)
x=[random()for i in range(n)]
y=[random()for i in range(n)]
z=[random()for i in range(n)]
ax.scatter(x,y,z);
ax.set_xlabel('x label');ax.set_ylabel('y label');
ax.set_zlabel('z label')
plt.show()