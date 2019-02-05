import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def update_plot(i, data, scat):
    scat = plt.scatter(x[i], y[i], c=c[i], s=10)
    return scat


numframes = 1000
numpoints = 1
x = np.random.random((numframes, numpoints))
y = np.random.random((numframes, numpoints))
c = np.random.random((numframes, numpoints))

fig = plt.figure()
scat = plt.scatter(x[0], y[0], c=c[0], s=10)

ani = animation.FuncAnimation(fig,
                              update_plot,
                              interval=1,
                              frames=range(numframes),
                              fargs=(c, scat))
plt.show()
