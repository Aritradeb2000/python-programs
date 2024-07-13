import matplotlib.pyplot as plt
import input_sheet as isp
import numpy as np

def plot_pile_cap_diagram(len_pile_cap_long, len_pile_cap_trans, near_stn_left, near_stn_right):
    xpoints = np.array([2, len_pile_cap_long, len_pile_cap_long, 2, 2])
    ypoints = np.array([2, 2, len_pile_cap_trans, len_pile_cap_trans, 2])


    plt.xlim = (-2, 16)
    plt.ylim = (-2, 14)    # Hide axis
    plt.axis('off')

    # Plot the rectangle
    plt.plot(xpoints, ypoints)

    mid_x = (2 + len_pile_cap_long) / 2
    mid_y = (2 + len_pile_cap_trans) / 2

    # Arrow along x-axis with added spacing
    plt.annotate('', xy=(2, 1.8), xytext=(len_pile_cap_long, 1.8),
                 arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=2))

    # Arrow along y-axis with added spacing
    plt.annotate('', xy=(1.8, 2), xytext=(1.8, len_pile_cap_trans),
                 arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=2))

    # Arrow for showing traffic direction
    plt.annotate('', xy=(6, 0.2 + len_pile_cap_trans), xytext=(len_pile_cap_long - 4, 0.2 + len_pile_cap_trans),
                 arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=5))
    
    plt.annotate('', xy=(1.6, mid_y+1), xytext=(0, mid_y + 1), arrowprops= dict(arrowstyle='<-', color='black', linewidth = 2))
    plt.annotate('', xy=(len_pile_cap_long+0.4, mid_y+1), xytext=(len_pile_cap_long+2, mid_y + 1), arrowprops= dict(arrowstyle='<-', color='black', linewidth = 2))

    # Texts
    plt.text(mid_x, 1.5, f"{len_pile_cap_long} m", ha='center', va='center')
    plt.text(1.5, mid_y, f"{len_pile_cap_trans} m", ha='center', va='center', rotation='vertical')
    plt.text(mid_x, 0.5 + len_pile_cap_trans, "TRAFFIC DIRECTION", ha='center')
    plt.text(0.8, mid_y+ 0.5, f'{near_stn_left}', ha="center")
    plt.text(len_pile_cap_long+1.2, mid_y+ 0.5, f'{near_stn_right}', ha="center")

    # Show plot
    plt.show()

# Example usage
len_pile_cap_long = isp.len_pile_cap_long
len_pile_cap_trans = isp.len_pile_cap_trans
near_stn_left = isp.Near_stn_left 
near_stn_right = isp.Near_stn_right

plot_pile_cap_diagram(len_pile_cap_long, len_pile_cap_trans, near_stn_left, near_stn_right)
