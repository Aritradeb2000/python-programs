import matplotlib.pyplot as plt
import numpy as np
import abut_foundation as af





def plot_case_diagram(pressure_bottom, C519, C516, C513, pressure_top, G513, D516, B515, tot_height, var_dec):

 xpoints = np.array([0, pressure_bottom, pressure_bottom, pressure_bottom, pressure_top, 0, 0])
 ypoints = np.array([0, 0, C519, var_dec, tot_height, tot_height, 0])

 plt.xlim(-1, 5)
 plt.ylim(-1, 8)

 join_x = np.array([0, pressure_top])
 join_y = np.array([C519, C519])
 plt.plot(join_x, join_y)

 join_x_parallel = np.array([0, pressure_bottom])
 join_y_parallel = np.array([var_dec, var_dec])
 plt.plot(join_x_parallel, join_y_parallel, linestyle = 'dotted')

 join_x_perpendicular = np.array([pressure_bottom, pressure_bottom])
 join_y_perpendicular = np.array([var_dec, tot_height])
 plt.plot(join_x_perpendicular, join_y_perpendicular, linestyle = 'dotted')
 plt.axis('off')


 arrow_props = dict(arrowstyle='<->', color='black')
 arrow_props_1= dict(arrowstyle = '<-', color= 'blue', linewidth = 2)
 #arrow_props_2= dict(arrowstyle = '->', color= 'blue', linewidth = 2)
 plt.annotate('', xy=(-0.3, 0), xytext=(-0.3, C519), arrowprops=arrow_props)
 plt.annotate('', xy=(-0.3, C519), xytext=(-0.3, var_dec), arrowprops= arrow_props)
 plt.annotate('', xy=(-0.3, var_dec), xytext=(-0.3, tot_height), arrowprops= arrow_props)
 plt.annotate('', xy=(-0.7, 0), xytext=(-0.7, tot_height), arrowprops= arrow_props)
 plt.annotate('', xy=(0, -0.5), xytext = (pressure_bottom, -0.5), arrowprops= arrow_props)
 plt.annotate('', xy=(pressure_top+0.05, var_dec), xytext = (pressure_top+0.05, tot_height), arrowprops= arrow_props)
 plt.annotate('', xy=(0, tot_height+0.5), xytext = (pressure_top, tot_height+0.5), arrowprops= arrow_props)
 plt.annotate('', xy=(pressure_top-0.4, tot_height*(2/3)), xytext=(pressure_bottom-0.3, tot_height*(2/3)), arrowprops= arrow_props_1)
 plt.annotate('', xy=(pressure_top-0.4, C519/2), xytext= (pressure_bottom/2, C519/2), arrowprops= arrow_props_1)

 plt.text(-0.5, C519/2, f'{C519}m', ha='center', va='bottom', fontsize=8)
 plt.text(-0.5, var_dec-0.08, f'-0.068m', ha='center', va='bottom', fontsize=8)
 plt.text(-0.5, (tot_height+var_dec)/2, f'{C513}m', ha='center', va='bottom', fontsize=8)
 plt.text(-0.9, tot_height/2, f'{B515}m', ha='center', va='bottom', fontsize=8)
 plt.text(pressure_bottom/2, -D516, f'{pressure_bottom}m', ha='center', va='bottom', fontsize=8)
 plt.text(pressure_bottom/2, C519-0.3, f'{D516}', ha='center', va='bottom', fontsize=8)
 plt.text(pressure_bottom/2, C519+0.3, f'{pressure_bottom}', ha='center', va='bottom', fontsize=8)
 plt.text(pressure_top/2, tot_height+0.7, f'{pressure_top}', ha='center', va='bottom', fontsize=8)
 plt.text(pressure_top+0.06, tot_height/2, f'{G513} m Height of abutment', va='bottom', fontsize=8)
 plt.text(pressure_bottom+0.05, C519+0.05, f'Bottom of abutment', va='bottom', fontsize=8)
 plt.text(pressure_top-0.3, tot_height*(2/3), 'P1', va='bottom')
 plt.text(pressure_top-0.3, C519/2, "P2'", va='bottom')


 plt.plot(xpoints, ypoints)

 plt.show()

#Example usage
pressure_bottom = af.pressure_bottom_case2 #0.782
C519 = round(af.C519, 3) #1.8
C516 = af.C516 #0.068
C513 = af.C513 #4.85
pressure_top = af.pressure_top_case2 #2.047
G513 = af.G513 #4.782
D516 = af.D516 #0.800
B515 = af.B515 #6.582
tot_height = C519 + -(C516) + G513 #6.65
var_dec = C519 + -(C516) #1.868

plot_case_diagram(pressure_bottom, C519, C516, C513, pressure_top, G513, D516, B515, tot_height, var_dec)