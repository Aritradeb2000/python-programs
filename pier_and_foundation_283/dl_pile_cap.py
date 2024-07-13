import matplotlib.pyplot as plt
import numpy as np

def plot_pile_cap_diagram(len_pile_cap_long, len_pile_cap_trans, near_stn_left, near_stn_right):
    xpoints = np.array([2, len_pile_cap_long + 2, len_pile_cap_long + 2, 2, 2])
    ypoints = np.array([2, 2, len_pile_cap_trans + 2, len_pile_cap_trans + 2, 2])

    # Create the plot
    fig, ax = plt.subplots()

    # Set limits dynamically
    ax.set_xlim(-2, len_pile_cap_long + 4)
    ax.set_ylim(-2, len_pile_cap_trans + 4)
    ax.set_aspect('equal', adjustable='box')

    # Hide the axis
    plt.axis('off')

    # Plot the rectangle
    plt.plot(xpoints, ypoints)

    mid_x = (2 + len_pile_cap_long + 2) / 2
    mid_y = (2 + len_pile_cap_trans + 2) / 2

    # Arrow along x-axis with added spacing
    plt.annotate('', xy=(2, 0.8), xytext=(len_pile_cap_long + 2, 0.8),
                 arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=2))

    # Arrow along y-axis with added spacing
    plt.annotate('', xy=(0.8, 2), xytext=(0.8, len_pile_cap_trans + 2),
                 arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=2))

    # Arrow for showing traffic direction
    plt.annotate('', xy=(2, 0.5+len_pile_cap_trans + 2), xytext=(len_pile_cap_long + 2, 0.5 + len_pile_cap_trans + 2),
                 arrowprops=dict(arrowstyle='<|-|>', color='black', linewidth=5))
    
    plt.annotate('', xy=(0.6, mid_y + 1), xytext=(-2, mid_y + 1), arrowprops=dict(arrowstyle='<-', color='black', linewidth=2))
    plt.annotate('', xy=(len_pile_cap_long + 2.4, mid_y + 1), xytext=(len_pile_cap_long + 5, mid_y + 1), arrowprops=dict(arrowstyle='<-', color='black', linewidth=2))

    # Texts
    plt.text(mid_x, 1.5, f"{len_pile_cap_long} m", ha='center', va='center')
    plt.text(1.5, mid_y, f"{len_pile_cap_trans} m", ha='center', va='center', rotation='vertical')
    plt.text(mid_x, 1 + len_pile_cap_trans + 2, "TRAFFIC DIRECTION", ha='center')
    plt.text(-1.8, mid_y + 2, f'{near_stn_left}', ha="center")
    plt.text(len_pile_cap_long + 5.2, mid_y + 2, f'{near_stn_right}', ha="center")

    # Show plot
    plt.show()

# Example usage
len_pile_cap_long = 7.500
len_pile_cap_trans = 10.500
near_stn_left = "BOKAJAN STATION"
near_stn_right = "CHONGJAN STATION"

plot_pile_cap_diagram(len_pile_cap_long, len_pile_cap_trans, near_stn_left, near_stn_right)
