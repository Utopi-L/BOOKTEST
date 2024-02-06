import numpy as np
import matplotlib.pyplot as plt
data =np.random.randint(1,11,5)
plt.pie(data,explode=[0,0,0.2,0,0])