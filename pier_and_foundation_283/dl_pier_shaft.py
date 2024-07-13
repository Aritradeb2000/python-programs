import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_dl_pier_shaft(len_pier_shaft, width_pier_shaft):

    plt.title("Dead Load of Pier shaft")
    rect_length = round(len_pier_shaft - width_pier_shaft, 3)
    radius = width_pier_shaft / 2
    

    # Create figure and axes
    fig, ax = plt.subplots()

    # Add the rectangle
    ax.add_patch(patches.Rectangle((radius, 0), rect_length, width_pier_shaft, edgecolor='blue', facecolor='none'))

    # Add semicircles
    circle_left = patches.Arc((radius, width_pier_shaft / 2), width_pier_shaft, width_pier_shaft, angle=0, theta1=90, theta2=270, edgecolor='blue')
    ax.add_patch(circle_left)

    circle_right = patches.Arc((len_pier_shaft - radius, width_pier_shaft / 2), width_pier_shaft, width_pier_shaft, angle=0, theta1=270, theta2=90, edgecolor='blue')
    ax.add_patch(circle_right)

    # Add annotations for the length of the rectangle
    plt.annotate('', xy=(radius, -0.4), xytext=(len_pier_shaft - radius, -0.4),
                 arrowprops=dict(arrowstyle='<->', color='black'))
    plt.text(len_pier_shaft / 2, -0.7, f'{rect_length} m', ha='center', va='bottom')

    # Add annotations for the overall length
    plt.annotate('', xy=(0, width_pier_shaft + 0.3), xytext=(len_pier_shaft, width_pier_shaft + 0.3),
                 arrowprops=dict(arrowstyle='<->', color='black'))
    plt.text(len_pier_shaft / 2, width_pier_shaft + 0.4, f'{len_pier_shaft} m', ha='center', va='bottom')

    # Add annotations for the width
    plt.annotate('', xy=(len_pier_shaft / 2, 0), xytext=(len_pier_shaft / 2, width_pier_shaft),
                 arrowprops=dict(arrowstyle='<->', color='black'))
    plt.text((len_pier_shaft / 2) + 0.4, width_pier_shaft / 2, f'{width_pier_shaft} m', ha='center', va='bottom')

    # Set limits and aspect ratio
    ax.set_xlim(-1, len_pier_shaft + 1)
    ax.set_ylim(-1, width_pier_shaft + 1)
    ax.set_aspect('equal', adjustable='box')

    plt.axis('off')

    # Show plot
    plt.show()

# Parameters
draw_dl_pier_shaft(9.000, 3.900)