import matplotlib.pyplot as plt
import input_sheet as isp
import numpy as np

len_pile_cap_long = isp.len_pile_cap_long
len_pile_cap_trans = isp.len_pile_cap_trans

xpoints = np.array([1, len_pile_cap_trans, len_pile_cap_trans, 1, 1])
ypoints = np.array([1, 1, len_pile_cap_long, len_pile_cap_long, 1])

# Define midpoint for annotation
mid_x = (1 + len_pile_cap_trans) / 2
mid_y = len_pile_cap_long / 2

# Arrow along x-axis
plt.annotate('', xy=(len_pile_cap_trans, 0), xytext=(1, 0),
             arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=2), label='Arrow Line X')

# Arrow along y-axis
plt.annotate('', xy=(0, len_pile_cap_long), xytext=(0, 1),
             arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=2), label='Arrow Line Y')

# Text annotation for dimensions
plt.text(-1, len_pile_cap_long / 2, f"{len_pile_cap_long} m", ha='right')
plt.text(mid_x, -0.5, f"{len_pile_cap_trans} m", va='top', ha='center')

plt.axis('off')
plt.plot(xpoints, ypoints)
plt.xlim(-2, len_pile_cap_trans + 1)  # Adjust x-axis limit for better visualization
plt.ylim(-2, len_pile_cap_long + 1)    # Adjust y-axis limit for better visualization
plt.show()

