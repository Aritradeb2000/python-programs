import matplotlib.pyplot as plt
import input_sheet as isp
import numpy as np

def plot_abutment_diagram(len_bb_abut_cap, wid_abut_shaft):
    # Define the points for the rectangle
    xpoints = np.array([1, len_bb_abut_cap, len_bb_abut_cap, 1, 1])
    ypoints = np.array([1, 1, wid_abut_shaft, wid_abut_shaft, 1])

    # Define midpoint for annotation
    mid_x = (1 + len_bb_abut_cap) / 2
    mid_y = (1 + wid_abut_shaft) / 2

    # Arrow along x-axis with added spacing
    plt.annotate('', xy=(len_bb_abut_cap, 0.5), xytext=(1, 0.5),
                 arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=2))

    # Double-headed thick hollow arrow along y-axis outside the rectangle on the left side and bigger
    plt.annotate('', xy=(0.5, wid_abut_shaft + 1), xytext=(0.5, 0),
                 arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=4, fill=False))

    # Arrow along y-axis inside the rectangle and centered
    plt.annotate('', xy=(mid_x, wid_abut_shaft), xytext=(mid_x, 1),
                 arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=2))

    # Text annotation for dimensions with added spacing
    plt.text(mid_x, 0.25, f"{len_bb_abut_cap} m", ha='center', va='center')
    plt.text(mid_x + 0.5, mid_y, f"{wid_abut_shaft} m", ha='center', va='center', rotation='vertical')

    # Annotation for "TRAFFIC DIRECTION" with some spacing
    plt.text(0.3, mid_y, "TRAFFIC DIRECTION", ha='right', va='center', fontsize=8)

    # Hide axis
    plt.axis('off')

    # Plot the rectangle
    plt.plot(xpoints, ypoints)

    # Set plot limits for better visualization
    plt.xlim(-2, len_bb_abut_cap + 2)
    plt.ylim(-2, wid_abut_shaft + 3)

    # Show plot
    plt.show()

# Example usage
len_bb_abut_cap = isp.len_bb_abut_cap
wid_abut_shaft = isp.width_abutment_shaft

plot_abutment_diagram(len_bb_abut_cap, wid_abut_shaft)





