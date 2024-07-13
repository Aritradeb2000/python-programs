import matplotlib.pyplot as plt
import numpy as np

def draw_case_diagram(tot_height, eff_len_abut, height_upto_bot_abut, sur_wid_form_level, pressure_form_level, pressure_L_minus_B):
 C514=eff_len_abut-sur_wid_form_level 
 C518=height_upto_bot_abut-C514
 C520= tot_height-C518-C514
 E518 = tot_height - C514


 xpoints = np.array([0, pressure_L_minus_B, pressure_L_minus_B, pressure_L_minus_B, pressure_form_level, 0, 0, 0, 0])
 ypoints = np.array([0, 0, C520, C520+C518, tot_height, tot_height, C520+C518, C520, 0])

 plt.plot(xpoints, ypoints)

 plt.plot([0,pressure_L_minus_B+0.5],[0, 0], color='black')
 plt.plot([-0.3, pressure_L_minus_B+1], [C520, C520], color='black')
 plt.plot([-0.3, pressure_L_minus_B+1], [C520+C518, C520+C518], color='black')
 plt.plot([pressure_L_minus_B, pressure_L_minus_B], [C520+C518, tot_height], color='black', linestyle='dashed')

 plt.annotate('', xy=(-0.1, 0), xytext=(-0.1, C520), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text(-0.5, C520/2, f'{C520:.3f}m', ha='left', fontsize = 8)

 plt.annotate('', xy=(-0.1, C520), xytext=(-0.1, C520+C518), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text(-0.5, C520+C518/2, f'{C518:.3f}m', ha='left', fontsize=8)

 plt.annotate('', xy=(-1, 0), xytext=(-1, tot_height), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text(-1, tot_height+0.5, f'formation level', ha='left', fontsize=8)
 plt.text(-1.4, (tot_height)/2, f'{tot_height}m', ha='left', fontsize=8)
 plt.text((pressure_form_level-pressure_L_minus_B)/2, C520+C518+C514+0.5, f'{pressure_form_level}T/m²', ha='left', fontsize=8)

 plt.annotate('', xy=(pressure_L_minus_B+0.1, 0), xytext=(pressure_L_minus_B+0.1, C520+C518), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text(pressure_L_minus_B+0.2, C520+C518/2, f'{E518}m Bottom of Abutment', ha='left', fontsize=8)

 plt.annotate('', xy=(pressure_form_level+0.7, C520), xytext=(pressure_form_level+0.7, tot_height), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text(pressure_form_level+0.8, (tot_height)/2, f'5.626m', ha='left', fontsize='8')
 plt.annotate('', xy=(-0.1, C520+C518), xytext=(-0.1, tot_height), arrowprops=dict(arrowstyle='<->', color='black'))
 plt.text(-0.5, (tot_height+height_upto_bot_abut)/2, f'{C514:.3f}m', ha='left', fontsize = 8)

 plt.text(pressure_L_minus_B/2, -0.3, f'{pressure_L_minus_B}T/m²', ha='left',  fontsize=6)
 plt.text(pressure_L_minus_B/2, C520+C518/2, f'{pressure_L_minus_B}T/m²',  ha='left',  fontsize=6)
 plt.text(pressure_L_minus_B+0.5, 0.2, f'MSL', ha='left', fontsize=8)



 plt.xlim(-2, pressure_form_level+3)
 plt.ylim(-2, tot_height+3)

 plt.axis('off')
 plt.show()

#example usage
# eff_len_abut = 6.85
# sur_wid_form_level = 3
# tot_height=8.247
# pressure_L_minus_B = 0.725
# pressure_form_level = 1.656
# height_upto_bot_abut = 5.626

draw_case_diagram(8.247, 6.85, 5.626, 7, 1.656, 0.725)