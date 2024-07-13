#BR 172 PIER WELL ELEVATION
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
def draw_elevation(well_cap_dia,well_cap_ht, wdth_shaft_bt, pier_ht,pier_cap_ht,pier_cap_wdth,bearing_ht, bearing_wdth, depth_cross_girder, well_dia, type_sstr, rail_from_lvl, pier_cap_wdth_varing, noofpiles_transv,pile_dia,spacing_y  ):

    coordinates_1 = [(0,0), (well_cap_dia/2,0), (well_cap_dia/2, well_cap_ht), (wdth_shaft_bt/2, well_cap_ht), (wdth_shaft_bt/2, well_cap_ht+pier_ht), (-wdth_shaft_bt/2,well_cap_ht+pier_ht ), (-wdth_shaft_bt/2,well_cap_ht), (-well_cap_dia/2, well_cap_ht), (-well_cap_dia/2,0), (0,0)]
    # Extract x and y coordinates separately
    x_coords_1 = [coord[0] for coord in coordinates_1]
    y_coords_1 = [coord[1] for coord in coordinates_1]

    # Plotting
    plt.plot(x_coords_1,y_coords_1, 'k')

    def draw_brng(center_x,center_y,brng_wdth,brng_ht):
        plt.plot([center_x,center_x+brng_wdth/2,center_x+brng_wdth/2, center_x-brng_wdth/2, center_x-brng_wdth/2, center_x],[center_y, center_y, center_y+brng_ht, center_y+brng_ht, center_y, center_y], 'k')

    temp_y1 = well_cap_ht + pier_ht

    coordinates_2 = [(wdth_shaft_bt/2,temp_y1), (pier_cap_wdth/2+pier_cap_wdth_varing, temp_y1+pier_cap_wdth_varing), (pier_cap_wdth/2+pier_cap_wdth_varing, temp_y1+pier_cap_wdth_varing+pier_cap_ht ), (-pier_cap_wdth/2-pier_cap_wdth_varing, temp_y1+pier_cap_wdth_varing+pier_cap_ht ), (-pier_cap_wdth/2-pier_cap_wdth_varing, temp_y1+pier_cap_wdth_varing), (-wdth_shaft_bt/2,temp_y1)]
    # Extract x and y coordinates separately
    x_coords_2 = [coord[0] for coord in coordinates_2]
    y_coords_2 = [coord[1] for coord in coordinates_2]

    # Plotting
    plt.plot(x_coords_2,y_coords_2, 'k')
    draw_brng(pier_cap_wdth/4,temp_y1+pier_cap_ht+pier_cap_wdth_varing,bearing_wdth,bearing_ht)
    draw_brng(-pier_cap_wdth/4,temp_y1+pier_cap_ht+pier_cap_wdth_varing,bearing_wdth,bearing_ht)

    #girder drawing
    temp_y1 = well_cap_ht + pier_ht + pier_cap_wdth_varing
    temp_y2 = temp_y1 + bearing_ht+pier_cap_ht
    coordinates_3 = [(.05,temp_y2), (well_cap_dia/2*1.3, temp_y2), (well_cap_dia/2*1.3,depth_cross_girder+temp_y2), (well_cap_dia/2*1.3, temp_y2+depth_cross_girder), (.05,temp_y2+depth_cross_girder ), (.05,temp_y2)]
    # Extract x and y coordinates separately
    x_coords_3 = [coord[0] for coord in coordinates_3]
    y_coords_3 = [coord[1] for coord in coordinates_3]
    plt.plot(x_coords_3,y_coords_3, 'k')

    coordinates_4 = [(-.05,temp_y2), (-well_cap_dia/2*1.3, temp_y2), (-well_cap_dia/2*1.3,depth_cross_girder+temp_y2), (-well_cap_dia/2*1.3, temp_y2+depth_cross_girder), (-.05,temp_y2+depth_cross_girder ), (-.05,temp_y2)]
    # Extract x and y coordinates separately
    x_coords_4 = [coord[0] for coord in coordinates_4]
    y_coords_4 = [coord[1] for coord in coordinates_4]
    plt.plot(x_coords_4,y_coords_4, 'k')




    #Drawing Well

    coordinates_5 = [(0,0), (well_dia/2,0), (well_dia/2,-2), (well_dia/2,0), (0,0),(-well_dia/2,0), (-well_dia/2,-2), (-well_dia/2+well_dia*(4/10),-2), (-well_dia/2+well_dia*(5/10),-1.5),(-well_dia/2+well_dia*(5/10),-2.5), (-well_dia/2+well_dia*(6/10),-2), (well_dia/2,-2) ]
    # Extract x and y coordinates separately
    x_coords_5 = [coord[0] for coord in coordinates_5]
    y_coords_5 = [coord[1] for coord in coordinates_5]
    # plt.plot(x_coords_5,y_coords_5)



#Drawing Pile
    isOdd = False
    centeres = []
    if(int(noofpiles_transv) % 2 == 1): isOdd= True
    if isOdd: centeres.append(0)
    for i in range(1,int(noofpiles_transv/2)+1):
        if(isOdd):
            centeres.append(i*spacing_y)
        else:
            if(i == 1): centeres.append(spacing_y/2)
            else:
                centeres.append(centeres[-1] + spacing_y)

    print(centeres)

    

    def draw_pile_helper(pile_dia,center):
        coord_x = [-pile_dia/2 + center, -pile_dia/2 + center,pile_dia/2+ center, pile_dia/2+ center, pile_dia/2+ center - pile_dia/4,pile_dia/2+ center - pile_dia/2,pile_dia/2+ center - pile_dia/2, (pile_dia/2+ center - pile_dia/2)- pile_dia/4, -pile_dia/2 + center]
        coord_y = [-2, 0, 0,-2, -2, -2.2, -1.8, -2, -2  ]
        plt.plot(coord_x,coord_y, 'k')
    
    for ele in centeres:
        draw_pile_helper(pile_dia,ele)
    for ele in centeres:
        draw_pile_helper(pile_dia,-ele)


    
    #vertical Line
    plt.plot([0,0],[-2.6,depth_cross_girder+temp_y2+.3],'--', linewidth = 1)

    #Adding Texts
    plt.text((0-well_cap_dia/2*1.3)/2,(temp_y2+temp_y2+depth_cross_girder)/2,f'{type_sstr}',ha = 'center', fontsize=8)
    plt.text((well_cap_dia/2*1.3)/2,(temp_y2+temp_y2+depth_cross_girder)/2,f'{type_sstr}',ha = 'center', fontsize=8)
    plt.text((well_cap_dia/2*1.3)/2,temp_y2+depth_cross_girder+.1,f'Rail Formation Level\n{rail_from_lvl} m',ha = 'center', fontsize=8)
    arrow1 = FancyArrowPatch((-well_cap_dia/2, well_cap_ht/2), (well_cap_dia/2, well_cap_ht/2),
                        arrowstyle='<->', color='black', mutation_scale=10)
    plt.text(0,well_cap_ht/2-.5,f'{well_cap_dia}',ha = 'center')
    # plt.text()
    plt.gca().add_patch(arrow1)
    arrow2 = FancyArrowPatch((-wdth_shaft_bt/2, well_cap_ht + pier_ht/2), (wdth_shaft_bt/2, well_cap_ht + pier_ht/2),
                    arrowstyle='<->', color='black', mutation_scale=10)
    plt.gca().add_patch(arrow2)
    plt.text(0,well_cap_ht + pier_ht/2+.5,f'{wdth_shaft_bt} m',ha = 'center')

    arrow3 = FancyArrowPatch((-pier_cap_wdth/2-pier_cap_wdth_varing, temp_y1+ pier_cap_wdth_varing), (pier_cap_wdth/2+pier_cap_wdth_varing, temp_y1+pier_cap_wdth_varing),
                arrowstyle='<->', color='black', mutation_scale=10)
    plt.gca().add_patch(arrow3)
    plt.text(0,temp_y1+ pier_cap_wdth_varing+0.2,f'{pier_cap_wdth} m',ha = 'center')

    

    plt.title('ELEVATION')
    # Set aspect ratio and limits
    # plt.gca().set_aspect('equal')
    # plt.xlim(-circle_radius - 1, circle_radius + 1)
    # plt.ylim(-circle_radius - 1, circle_radius + 1)

    # Hide axes
    plt.axis(False)
    # plt.grid(True)
    # Show the plot
    plt.tight_layout()
    plt.savefig("abcd.png")
    plt.show()
    

draw_elevation(7.5,1.8,1.9,10.5,1.2,3,0.435,0.450,.9,7, f"45.7m Open Web Girder", 56.005, 0.3, 3, 1.2, 3)

