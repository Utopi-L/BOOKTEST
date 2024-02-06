import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [0, 1, 2, 1.5]
Y = [0, 4, 4, 1]
Z = [0, 2, 0, 0]

ax.plot_trisurf(X, Y, Z)
plt.show()
