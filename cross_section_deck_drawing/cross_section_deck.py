import matplotlib.pyplot as plt
import numpy as np
def draw_structure(polygon_distance, polygon_length, polygon_height, girder_height, num_polygons, shift_distance, side_polygon_length):
 # Function to plot a polygon with given x and y points
 def plot_polygon(ax, xpoints, ypoints, shift_x=0, shift_y=0):
     ax.plot(xpoints + shift_x, ypoints + shift_y, color="black")


 xpoints = np.array([0, 0, polygon_distance, polygon_distance, polygon_height, polygon_height, polygon_distance, polygon_distance+polygon_length, polygon_distance+polygon_length+girder_height/3, polygon_distance+polygon_length+girder_height/3, polygon_distance+polygon_length, polygon_distance])
 ypoints = np.array([girder_height, 0, 0, girder_height, polygon_height, polygon_height*2, girder_height*3, girder_height*3,polygon_height*2, polygon_height, girder_height, girder_height])

 # Create figure and axis
 fig, ax = plt.subplots()

 # Calculate plot limits based on the number of polygons and spacing
 x_min = shift_distance * (num_polygons) - 2
 x_max = -shift_distance*(num_polygons+1)
 y_min = -1
 y_max = max(ypoints)*2

 plt.xlim(x_min, x_max)
 plt.ylim(y_min, y_max)

 # Plot the main polygon and additional polygons
 for i in range(num_polygons):
     plot_polygon(ax, xpoints, ypoints, shift_x=shift_distance * i)


 xpoints_parallel = np.array([polygon_distance+polygon_length, polygon_distance+polygon_length, polygon_distance+side_polygon_length*2, polygon_distance+side_polygon_length*2, polygon_distance+side_polygon_length*2-girder_height/3, polygon_distance+side_polygon_length*2-girder_height/3, polygon_distance+side_polygon_length*2, -shift_distance*2-girder_height/3, -shift_distance*2-girder_height/3, polygon_distance+side_polygon_length*2])
 ypoints_parallel = np.array([girder_height, 0, 0, girder_height, polygon_height, polygon_height*2, girder_height*3, girder_height*3, girder_height, girder_height])

 xpoints_parallel_1 = np.array([shift_distance*2, shift_distance*2+girder_height/3, shift_distance*2+girder_height/3, shift_distance*2, -(polygon_length+polygon_distance)*(num_polygons-1)-side_polygon_length, -(polygon_length+polygon_distance)*(num_polygons-1)-side_polygon_length, shift_distance*2])
 ypoints_parallel_1 = np.array([girder_height, 2, polygon_height*2, girder_height*3, girder_height*3, girder_height,girder_height])

 x_line = np.array([-(polygon_length+polygon_distance)*(num_polygons-1)-side_polygon_length, -(polygon_length+polygon_distance)*(num_polygons-1)-side_polygon_length, -(polygon_length+polygon_distance)*(num_polygons-1)-side_polygon_length+girder_height/3, -(polygon_length+polygon_distance)*(num_polygons-1)-side_polygon_length+girder_height/3, -(polygon_length*2+polygon_distance+polygon_distance/2) ])
 y_line = np.array([girder_height*3, polygon_distance+polygon_length+girder_height/3, polygon_distance+polygon_length+girder_height/3, polygon_distance+side_polygon_length, polygon_distance+side_polygon_length])

 x_line_dashed = np.array([-(polygon_length*2+polygon_distance+polygon_distance/2), -(polygon_length*2+polygon_distance+polygon_distance/2)])
 y_line_dashed = np.array([polygon_distance+polygon_length+girder_height/3, -girder_height/3])

 x_line_parallel = np.array([-shift_distance*2-girder_height/3, -shift_distance*2-girder_height/3, polygon_distance*2+polygon_length+side_polygon_length-girder_height/3, polygon_distance*2+polygon_length+side_polygon_length-girder_height/3, (6+polygon_distance+side_polygon_length*2)/2 ])
 y_line_parallel = np.array([girder_height*3, polygon_distance+polygon_length+girder_height/3, polygon_distance+polygon_length+girder_height/3, polygon_distance+side_polygon_length, polygon_distance+side_polygon_length ])

 x_line_dashed_1 = np.array([(-shift_distance+polygon_distance+side_polygon_length*2)/2, (6+polygon_distance+side_polygon_length*2)/2])
 y_line_dashed_1 = y_line_dashed

 x_line_dashed_2 = np.array([(-(polygon_distance+polygon_length)-polygon_length)/2, (-(polygon_distance+polygon_length)-polygon_length)/2])
 y_line_dashed_2 = y_line_dashed

 x_line_dashed_3 = np.array([(0+polygon_distance)/2, (0+polygon_distance/2)])
 y_line_dashed_3 = y_line_dashed

 x_line_over = np.array([-(polygon_length*2+polygon_distance+polygon_distance/2), (6+polygon_distance+side_polygon_length*2)/2])
 y_line_over = np.array([((girder_height*3)+polygon_distance+side_polygon_length)/2, ((girder_height*3)+polygon_distance+side_polygon_length)/2])


 #add arrows
 ax.annotate('', xy=(-14.5, 6), xytext=(-10.75, 6), arrowprops=dict(arrowstyle='<->'))
 ax.text((-14.5-10.75)/2.3, 6*1.05, f'{1500}', ha='right', fontsize = 8)

 ax.annotate('', xy=(-10.75, 6), xytext=(-4.75, 6), arrowprops=dict(arrowstyle='<->'))
 ax.text((-10.75-4.75)/2.3, 6*1.05, f'{2500}', ha='right', fontsize = 8)

 ax.annotate('', xy=(-4.75, 6), xytext=(1.25, 6), arrowprops=dict(arrowstyle='<->'))
 ax.text((-4.75+1.25)/2, 6*1.05, f'{2500}', ha='center', fontsize = 8)

 ax.annotate('', xy=(1.25, 6), xytext=(7.25, 6), arrowprops=dict(arrowstyle='<->'))
 ax.text((1.25+7.25)/2, 6*1.05, f'{2500}', ha='center', fontsize = 8)

 ax.annotate('', xy=(7.25, 6), xytext=(11, 6), arrowprops=dict(arrowstyle='<->'))
 ax.text((7.25+11)/2, 6*1.05, f'{1500}', ha='center', fontsize = 8)

 ax.annotate('', xy=(-10.75, 5.5), xytext=(-10.75, 5), arrowprops=dict(arrowstyle='<->'))
 ax.text(-10, 5.25, '300', ha='center', fontsize = 8)

 ax.annotate('', xy=(-6, -0.5), xytext=(-3.5, -0.5), arrowprops=dict(arrowstyle='<->'))
 ax.text((-6-3.5)/2, -0.75, f'{500}', ha='center', fontsize=8)

 #ax.annotate('', xy=(-1.5,(4.5+1.5)/2), xytext=(-1, (4.5+1.5)/2), arrowprops=dict(arrowstyle='<-'))
 ax.text((-3.5-0)/2, (4.5+1.5)/2, '200x200\n fillets', ha='center', va = 'center', fontsize = 8)





 plt.plot(xpoints_parallel, ypoints_parallel, color='black')
 plt.plot(xpoints_parallel_1, ypoints_parallel_1, color='black')
 plt.plot(x_line, y_line, color='black')
 plt.plot(x_line_dashed, y_line_dashed, linestyle='dashed', color='black')
 plt.plot(x_line_parallel, y_line_parallel, color='black')
 plt.plot(x_line_dashed_1, y_line_dashed_1, linestyle='dashed', color='black')
 plt.plot(x_line_dashed_2, y_line_dashed_2, linestyle='dashed', color='black')
 plt.plot(x_line_dashed_3, y_line_dashed_3, linestyle='dashed', color='black')
 plt.plot(x_line_over, y_line_over, color='black')

 # Remove the axis
 plt.axis(False)

 # Display the plot
 plt.show()


draw_structure(2.5, 3.5, 2, 1.5, 3, -6, 3)