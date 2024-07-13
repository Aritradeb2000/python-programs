import matplotlib.pyplot as plt
import matplotlib.patches as patches



def draw_plan_diagram(len_pile_cap_transverse, len_pier_shaft, wid_pier_shaft):

 # Create a new figure and axis
 fig, ax = plt.subplots()

 #draw the rectangle
 rectangle = patches.Rectangle((0,0), wid_pier_shaft*5, len_pile_cap_transverse, edgecolor='blue', facecolor='none')
 ax.add_patch(rectangle)

 # Draw the capsule shape
 capsule = patches.FancyBboxPatch(
     (wid_pier_shaft*2, len_pile_cap_transverse/5), wid_pier_shaft, len_pile_cap_transverse*(3/5), boxstyle="round,pad=0.1,rounding_size=1.2", edgecolor='purple', facecolor='none'
 )
 ax.add_patch(capsule)

 ax.annotate('',xy=(0, len_pile_cap_transverse*1.2), xytext=(wid_pier_shaft*2.4, len_pile_cap_transverse*1.2), arrowprops=dict(arrowstyle='<-', color='black', linewidth=2))
 ax.text(0, len_pile_cap_transverse*1.1, 'C/L of Foundation', fontsize=8, fontweight='bold')

 ax.annotate('', xy=(wid_pier_shaft*5, len_pile_cap_transverse*1.2), xytext=(wid_pier_shaft*2.6, len_pile_cap_transverse*1.2), arrowprops=dict(arrowstyle='<-', color='black', linewidth=2))
 ax.text(wid_pier_shaft*4, len_pile_cap_transverse*1.1, '0.0 C/L of Pier Shaft', ha='right', fontsize=8, fontweight='bold')

 ax.annotate('', xy=(wid_pier_shaft*5.2, 0), xytext=(wid_pier_shaft*5.2, len_pile_cap_transverse), arrowprops=dict(arrowstyle='<->', color='black'))
 ax.text(wid_pier_shaft*5.3, len_pile_cap_transverse/2, f'{len_pile_cap_transverse}m', fontsize=8)
 ax.annotate('', xy=(wid_pier_shaft*1.8, len_pile_cap_transverse/5), xytext=(wid_pier_shaft*1.8, len_pile_cap_transverse*4/5), arrowprops=dict(arrowstyle='<->', color='black'))
 ax.text(wid_pier_shaft*1.5, len_pile_cap_transverse/2, f'{len_pier_shaft}m',  fontsize=8)
 ax.annotate('', xy=(wid_pier_shaft*2, len_pile_cap_transverse/2), xytext=(wid_pier_shaft*3, len_pile_cap_transverse/2), arrowprops=dict(arrowstyle='<->', color='black'))
 ax.text(wid_pier_shaft*2.51, len_pile_cap_transverse/1.9, f'{wid_pier_shaft}m') 
 

 #Draw the dashed vertical line
 plt.plot([wid_pier_shaft*5/2, wid_pier_shaft*5/2], [0, len_pile_cap_transverse*1.2], 'purple', linestyle='--')


 # Set the axis limits
 ax.set_xlim(-1, wid_pier_shaft*7)
 ax.set_ylim(-1, len_pile_cap_transverse+3)

 #Hide the axes
 ax.axis('off')

 # Show the plot
 plt.show()


draw_plan_diagram(10.500, 7.000, 1.900)
