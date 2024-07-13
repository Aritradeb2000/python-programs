import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
xpoints=np.array([0, 0, 2.800, 2.800, 2.800-(3-1.9)/2, 2.800-(3-1.9)/2, 2.800+3.000-(3-1.9)/2, 2.800+3.000-(3-1.9)/2, 2.800+3.000-2*(3-1.9)/2, 2.800+3.000-2*(3-1.9)/2, 7.500,7.500, 0])
ypoints=np.array([0, 1.800, 1.800, 1.800*4, 1.800*4+0.300, 1.800*4+0.300+1.200, 1.800*4+0.300+1.200, 1.800*4+0.300, 1.800*4, 1.800, 1.8, 0, 0])

plt.xlim(-3, 7.500*1.5)
plt.ylim(-3, 1.800*8)

plt.axis('off')

# Plot the rectangle
plt.plot(xpoints, ypoints)

xpoints_parallel=np.array([2.800-(3-1.9)/2, 2.800+3.000-(3-1.9)/2])
ypoints_parallel=np.array([1.800*4+(0.300+1.200)*1.3, 1.800*4+(0.300+1.200)*1.3])

ax.add_patch(patches.Rectangle((2.800, 1.800*4+(0.300+1.200)*1.3), 2.800*0.15, 1.800*0.3, edgecolor='blue', facecolor='none'))
ax.add_patch(patches.Rectangle((7.500/1.78, 1.800*4+(0.300+1.200)*1.3), 2.800*0.15, 1.800*0.3, edgecolor='blue', facecolor='none'))



plt.plot(xpoints_parallel, ypoints_parallel)

plt.show()

