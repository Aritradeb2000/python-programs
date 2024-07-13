import matplotlib.pyplot as plt
import numpy as np
def draw_fig_1(base, toe, ht_wall, thickness, thickness_top, width):
 
 xpoints=np.array([0, 0, toe, toe+thickness-thickness_top, toe+thickness, toe+thickness, base, base, 0])
 ypoints=np.array([0, width, width, width+ht_wall, width+ht_wall,width, width, 0, 0])

 xpoints_1=np.array([(toe+thickness)*1.02, base])
 ypoints_1=np.array([width+ht_wall, width+ht_wall])

 plt.xlim(-500, base*1.5)
 plt.ylim(-1000, ht_wall*1.5)

 plt.annotate('', xy=(0, -500), xytext=(base, -500), arrowprops = dict(arrowstyle='<->', color='black'))
 plt.text(base/2, -800, f'{base/1000}m', fontsize=8)

 plt.annotate('',xy=(0, width*1.5), xytext=(toe, width*1.5), arrowprops=dict(arrowstyle='<->', color='black') )
 plt.text(toe/2, width*1.7, f'{toe/1000}m', fontsize=8)

 plt.annotate('', xy=(toe, width*1.5), xytext=(toe+thickness, width*1.5), arrowprops=dict(arrowstyle='<->', color='black') )
 plt.text((toe+(toe+thickness))/2, width*1.7, f'{thickness}', fontsize = 8)

 plt.annotate('', xy=(toe+thickness-thickness_top, width+ht_wall+width*0.7), xytext=(toe+thickness, width+ht_wall+width*0.7), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text(((toe+thickness-thickness_top)+(toe+thickness))/2, width+ht_wall+width,f'{thickness_top}',  ha='center', fontsize=8)

 plt.annotate('', xy=((toe+thickness)*1.5, width+ht_wall), xytext=((toe+thickness)*1.5, width), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text((toe+thickness)*1.55, width+ht_wall/2, f'{ht_wall/1000}m', fontsize = 8)

 plt.annotate('', xy=((toe+thickness)*1.05, width+ht_wall), xytext=((toe+thickness)*1.05, width+ht_wall/2), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text((toe+thickness)*1.1, width+ht_wall*3/4, f'{ht_wall/(2*1000)}m', fontsize =8)

 plt.annotate('', xy=(toe+thickness, width+ht_wall/2), xytext=(toe+thickness-(thickness+thickness_top)/2, width+ht_wall/2), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text((toe+(toe+thickness))/2, width+ht_wall/1.9, f'{(thickness+thickness_top)/2}', fontsize = 8)

 plt.plot(xpoints, ypoints, color='black')
 plt.plot(xpoints_1, ypoints_1, color='black')

 plt.axis(False)

 plt.show()

draw_fig_1(2400, 600, 6000, 485, 200, 450)