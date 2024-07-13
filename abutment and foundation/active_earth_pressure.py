import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def earth_pressure(earth_pres_abut_bot, earth_pres_msl, foundation_level, bot_abut_level, max_scour_level):
 fig, ax = plt.subplots()

 # Draw the quadrilateral
 quadrilateral_vertices = [
    (0, 0), 
    (earth_pres_msl, 0), 
    (earth_pres_msl, bot_abut_level - max_scour_level), 
    (earth_pres_msl - earth_pres_abut_bot, bot_abut_level - max_scour_level)
]

 quadrilateral = patches.Polygon(quadrilateral_vertices, closed=True, edgecolor='blue', facecolor='none')
 ax.add_patch(quadrilateral)

 # Extend the line
 plt.plot([earth_pres_msl, earth_pres_msl + 0.5], [0, 0], color='black')

 # Draw the triangle
 triangle_vertices = [
    (earth_pres_msl, bot_abut_level - max_scour_level), 
    (earth_pres_msl - earth_pres_abut_bot, bot_abut_level - max_scour_level),
    (earth_pres_msl, foundation_level - bot_abut_level)
 ]

 triangle = patches.Polygon(triangle_vertices, closed=True, edgecolor='blue', facecolor='none')
 ax.add_patch(triangle)

 # Extend the line, base of triangle
 plt.plot([earth_pres_msl, earth_pres_msl + 0.5], [bot_abut_level - max_scour_level, bot_abut_level - max_scour_level], color='black')

 # Extend the top point of triangle
 plt.plot([earth_pres_msl, earth_pres_msl + 0.5], [foundation_level - bot_abut_level, foundation_level - bot_abut_level], color='black')

 ax.set_xlim(-1, earth_pres_msl + 6)
 ax.set_ylim(-1, foundation_level - max_scour_level + 7)
 ax.set_aspect('equal', adjustable='box')

 ax.annotate('', xy=(earth_pres_msl + 0.3, 0), xytext=(earth_pres_msl + 0.3, bot_abut_level - max_scour_level), arrowprops=dict(arrowstyle='<->', color='black'))
 ax.annotate('', xy=(earth_pres_msl + 0.3, bot_abut_level - max_scour_level), xytext=(earth_pres_msl + 0.3, foundation_level - bot_abut_level), arrowprops=dict(arrowstyle='<->', color='black'))
 ax.annotate('', xy=(earth_pres_msl + 6, 0), xytext=(earth_pres_msl + 6, foundation_level - bot_abut_level), arrowprops=dict(arrowstyle='<->', color='black'))

 ax.text(earth_pres_msl + 0.6, 0, f'{max_scour_level}m\nMaximum Scour Level', ha='left', fontsize=7)
 ax.text(earth_pres_msl + 0.6, bot_abut_level - max_scour_level, f'{bot_abut_level}m\nBottom of Abutment Level', ha='left', fontsize=6)
 ax.text(earth_pres_msl + 0.6, foundation_level - bot_abut_level, f'{foundation_level}m\nFoundation Level', ha='left', fontsize=6)
 ax.text(earth_pres_msl + 6.5, (foundation_level - bot_abut_level) / 2, f'{(foundation_level - max_scour_level):.3f}m', ha='left', fontsize=6)
 ax.text(earth_pres_msl/2, 0.5, f'{earth_pres_msl}', va='center', fontsize=8, fontweight='bold')
 ax.text(earth_pres_msl/2, bot_abut_level-max_scour_level+0.5, f'{earth_pres_abut_bot}', va='center', fontsize=8, fontweight='bold')


 ax.set_title("Active Earth Pressure due to Backfill", fontsize=12, fontweight='bold')
 plt.axis('off')
 plt.show()

#Example Usage
earth_pressure(2.630, 3.855, 64.047, 54.421, 51.8)
