import math
import pandas as pd
import DocxHelper
import time
import os
import stiffness_subroutine as ss

def fix_type(value):
    try:
        res = float(value)
        return res
    except ValueError: 
        return value.strip()

# f_name = input("\n\nData File Name-->")  
print("Please review all inputs in the Excel file. After making any necessary changes, please save the Excel file and close it.\n\n")
time.sleep(5)
f_name = "input_abut" + ".xlsx"
# f_name = DocxHelper.resource_path(f_name)
file_path =rf"{f_name}"



command = f'start excel "{f_name}"'
os.system(command)
input("Press enter to continue: ")

name = {}
value_dict = {}  #

dd = {}
ud = {}

df = pd.read_excel(file_path, header=None)

# Loop through rows from 4 to 126
for index in range(3, 71):  # Subtract 1 because Python is 0-indexed
    # Extract data from each row
    
    desc = df.iloc[index, 0]
    val = df.iloc[index, 1]
    unit = df.iloc[index, 2]
    v1 = df.iloc[index, 3]
    
    # Handling NaN values
    if pd.isna(v1) or pd.isna(desc) or pd.isna(val):
        continue

    # Convert val to appropriate type using fix_type function
    val = fix_type(val)

    # Store the values in dictionaries
    name[v1] = f"{v1}"
    dd[v1] = f"{desc}"
    value_dict[v1] = val
    ud[v1] = f"{unit}" if pd.notna(unit) else ""

for key, val in value_dict.items():
    print(f"{key}: {val}")

# try:
Near_stn_left = value_dict['Near_stn_left']
Near_stn_right = value_dict['Near_stn_right']
bridge_no = value_dict['bridge_no']
abut_no = value_dict['abut_no']
span_numb = value_dict['span_numb']
exp_jt = value_dict['exp_jt']
span_len = value_dict['span_len']
eff_span_cc_bearing = value_dict['eff_span_cc_bearing']
overall_girder_length = value_dict['overall_girder_length']
prop_rail_form_level = value_dict['prop_rail_form_level']
struc_depth_girder = value_dict['struc_depth_girder']
gl_abut = value_dict['gl_abut']
top_pile_cap = value_dict['top_pile_cap']
HFL = value_dict['HFL']
discharge = value_dict['discharge']
velocity = value_dict['velocity']
max_scour_non_seismic = value_dict['max_scour_non_seismic']
max_scour_seismic = value_dict['max_scour_seismic']
load_standard = value_dict['load_standard']
typr_sstr = value_dict['typr_sstr']
dl_sstr = value_dict['dl_sstr']
edge_to_edge_sstr = value_dict['edge_to_edge_sstr']
eudl = value_dict['eudl']
no_track = value_dict['no_track']
cc_track_dis = value_dict['cc_track_dis']
tr_force = value_dict['tr_force']
br_force = value_dict['br_force']
type_bearing = value_dict['type_bearing']
fric_coeff_exp_bg = value_dict['fric_coeff_exp_bg']
seis_zone = value_dict['seis_zone']
Z_factor_sstr = value_dict['Z_factor_sstr']
I_factor_sstr = value_dict['I_factor_sstr']
reduction_factor_sup = value_dict['reduction_factor_sup']
reduction_factor_sub = value_dict['reduction_factor_sub']
reduction_factor_fou = value_dict['reduction_factor_fou']
gumma_water = value_dict['gumma_water']
dep_bb_abut_cap = value_dict['dep_bb_abut_cap']
len_bb_abut_cap = value_dict['len_bb_abut_cap']
wid_bb_abut_cap = value_dict['wid_bb_abut_cap']
thick_dirt_wall = value_dict['thick_dirt_wall']
length_pedestral = value_dict['length_pedestral']
width_pedestral = value_dict['width_pedestral']
height_pedestral = value_dict['height_pedestral']
no_pedestral = value_dict['no_pedestral']
depth_bearing = value_dict['depth_bearing']
width_abutment_shaft = value_dict['width_abutment_shaft']
wid_sqr_return_at_junction = value_dict['wid_sqr_return_at_junction']
avg_sqr_return_at_e_edge = value_dict['avg_sqr_return_at_e_edge']
lengt_fly_wing = value_dict['lengt_fly_wing']
dep_fly_end = value_dict['dep_fly_end']
thick_fly_wing = value_dict['thick_fly_wing']
width_the_platform = value_dict['width_the_platform']
no_pile_long_direction = value_dict['no_pile_long_direction']
no_pile_tran_direction = value_dict['no_pile_tran_direction']
dia_pile = value_dict['dia_pile']
c_c_dis_pile_longituidinal = value_dict['c_c_dis_pile_longituidinal']
c_c_dis_pile_transverse = value_dict['c_c_dis_pile_transverse']
phi_soil = value_dict['phi_soil']
i_soil = value_dict['i_soil']
sigma_soil = value_dict['sigma_soil']
alpha_soil = value_dict['alpha_soil']
gumma_soil = value_dict['gumma_soil']
dl_surcharge = value_dict['dl_surcharge']
ll_surchage = value_dict['ll_surchage']
srug_width_form_level = value_dict['srug_width_form_level']
heigh_spilling_earth = value_dict['heigh_spilling_earth']
fck = value_dict['fck']
fyk = value_dict['fyk']
  

#H14
span_between_cc_exp_joint = round(overall_girder_length+exp_jt/1000+0.0625*2,3)
#H13
overall_len_deck = round(span_between_cc_exp_joint-exp_jt/1000,3)

#H15
tot_len_bridge = round(span_between_cc_exp_joint*span_numb+exp_jt/1000,3)
#H17
prop_rail_lev = round(prop_rail_form_level+0.738,3)

#H20
bot_girder = round(prop_rail_form_level-struc_depth_girder,3)
#H21
top_bed_block = round(prop_rail_form_level-struc_depth_girder-height_pedestral-depth_bearing,3)
#H22
top_abut_lev = round(top_bed_block-dep_bb_abut_cap,3)
#H24
ht_abut = round(top_abut_lev-top_pile_cap,3)
#H26
bot_pile_cap_lev = round(top_pile_cap-1.8,3)

#H32
eff_lw = round(span_len*span_numb*0+11.775,3)
#H37
loading_standard = "25t Loading-2008"
#H41
sidl = round(overall_len_deck*6.5,3)

#H72
Z_2r = round(Z_factor_sstr/(2*reduction_factor_sup),3)

##########################################Time period Calculation#########################
#I5
top_cap_lev = round(bot_girder -0.461,3)
#I10
h1 = round(bot_girder-top_cap_lev,3)
#I11
h2 = round(top_cap_lev - top_pile_cap,3)
#I12_I26
h3 = round(top_pile_cap-bot_pile_cap_lev,3)
#I13
L = round(h1+h2+h3,3)
#I18
shape_abut = df.iloc[73, 1]
#I21(change)
dia_abutment = 0
#I22
no_piles = round(no_pile_long_direction*no_pile_tran_direction)
#I27
allowlable_deflection = dia_pile/100
#I28
pile_capacity = float(df.iloc[74, 1])
#I30
no_bearing_abut_cap = float(df.iloc[75, 1])
#I31
len_bearing = float(df.iloc[76, 1])
#I32
width_bearing = float(df.iloc[77, 1])
#I33
area_bearing = len_bearing*width_bearing
#I34
thk_bearing = float(df.iloc[78, 1])
#I35
no_elastomer = float(df.iloc[79, 1])
#I36
thk_elastomer = float(df.iloc[80, 1])
#I37
tot_thk_elastomer = no_elastomer*thk_elastomer
#I39
unit_weight_concrete =float(df.iloc[81, 1])
#I41
Elasticity =float(df.iloc[82, 1])
#I42
shear_modulus_elastomer =float(df.iloc[83, 1])

################################################################################################


#H153
len_pile_cap_long = round((no_pile_long_direction-1)*c_c_dis_pile_longituidinal+dia_pile+0.15*2,3)
#H120
ht_dirt_wall = round(prop_rail_form_level-top_bed_block,3)
#H135
len_suare_return_wall = round((len_pile_cap_long-width_abutment_shaft)/2,3)
#H142
Depth_fly_wing_at_junc =round(lengt_fly_wing+dep_fly_end/1.5,3)

#H152
len_pile_cap_trans = round((no_pile_tran_direction-1)*c_c_dis_pile_transverse+dia_pile+0.15*2,3)

#H154
dep_pile_cap = round(dia_pile*1.5,3)



################################Time Period###########################################
#Calculate Stiffness
#F78
k_bearing = ss.bearing_stiffness(no_bearing_abut_cap,area_bearing,shear_modulus_elastomer,tot_thk_elastomer)[0]
#F86
kxx_pier = ss.pier_rect_stiffness(Elasticity,width_abutment_shaft,len_bb_abut_cap,h2)[0] if shape_abut.lower() == "rectangular" else ss.pier_circular_stiffness(Elasticity,dia_abutment,h2)[0]
#F87
kyy_pier = ss.pier_rect_stiffness(Elasticity,width_abutment_shaft,len_bb_abut_cap,h2)[1] if shape_abut.lower() == "rectangular" else ss.pier_circular_stiffness(Elasticity,dia_abutment,h2)[1]
#F81
area_pier =ss.pier_rect_stiffness(Elasticity,width_abutment_shaft,len_bb_abut_cap,h2)[2] if shape_abut.lower() == "rectangular" else ss.pier_circular_stiffness(Elasticity,dia_abutment,h2)[2]

#H89
K_found = ss.found_stiffness(no_piles,allowlable_deflection,pile_capacity,dia_pile,len_pile_cap_trans,h3)[0]

k_area = ss.found_stiffness(no_piles,allowlable_deflection,pile_capacity,dia_pile,len_pile_cap_trans,h3)[1]

kxx =[k_bearing,kxx_pier,kyy_pier,K_found]
area = [area_bearing,area_pier,k_area]

stiffness_eq_long =[k_bearing,kxx_pier,K_found]
stiffness_eq_trans =[k_bearing,kyy_pier,K_found]
#H92
kx_92 =ss.calculate_resultant_stiffness(stiffness_eq_long)
#H95
kx_95 =ss.calculate_resultant_stiffness(stiffness_eq_trans)


#calculatiuon masss
#H98
load_sup = dl_sstr/2
#H99
load_sidl =sidl/2
#H100
load_live_load = eudl/2
#H101
load_abut_cap =(dep_bb_abut_cap*wid_bb_abut_cap*len_bb_abut_cap*2.5)
#H102
load_abut =((top_abut_lev-top_pile_cap)*(len_bb_abut_cap*width_abutment_shaft)*2.5)

load = [load_sup,load_sidl,load_live_load,load_abut_cap,load_abut]

H103 =(load_sup+ load_sidl+load_abut_cap/2+load_abut/2)
#H104
lumped_mass_long_dir_Ml =(load_sup+ load_sidl+load_abut_cap/2+load_abut/2)*9.81

#H106
lumped_mass_long_dir_MT =(load_live_load*0.5+H103)*9.81

#Caculation Natural Time period
#H111
delta_l = lumped_mass_long_dir_Ml/kx_92
#H112
delta_T = lumped_mass_long_dir_MT/kx_95
#H113
T_x =2*math.pi*(delta_l/9.807)**0.5
#H114
T_y =2*math.pi*(delta_T/9.807)**0.5


#################################################################################################################





#K88
T_88 = T_x
#K90
Sa_g_90  = round(1 + 15 * T_88 if T_88 < 0.1 else 2.5 if T_88 < 0.55 else 1.36 / T_88 if 0.55 < T_88 < 3 else 0.45, 3)
#K105
T_105 = T_y
#K107
Sa_g_107 = round(1 + 15 * T_105 if T_105 < 0.1 else 2.5 if T_105 < 0.55 else 1.36 / T_105 if 0.55 < T_105 < 3 else 0.45, 3)






def get_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter the correct data type.")



print("\n\n")

def word_print(document,output_path):
   
    DocxHelper.add_main_heading(document, "INPUT DATA")
    
    DocxHelper.add_minor_heading(document,"General Details:-")
    p = document.add_paragraph()
    p.add_run(f"Nearest station in the Left side\t\t\t\t\t= {Near_stn_left}\n")
    p.add_run(f"Nearest station in the Right side\t\t\t\t= {Near_stn_right}\n")
    p.add_run(f"Bridge No.\t\t\t\t\t\t\t= {round(bridge_no)}\n")
    p.add_run(f"Abutment No.\t\t\t\t\t\t\t= {abut_no}\n")
    p.add_run(f"Number of span\t\t\t\t\t\t= {round(span_numb)}\n")
    p.add_run(f"Expansion Joint\t\t\t\t\t\t= {exp_jt}  mm\n")
    p.add_run(f"Span Length\t\t\t\t\t\t\t= {span_len}  m\n")

    p.add_run(f"Effective span between c/c of bearing\t\t\t\t= {eff_span_cc_bearing}  m\n")
    p.add_run(f"Overall Length of Girder\t\t\t\t\t= {overall_girder_length}  m\n")
    p.add_run(f"Overall Length of Deck\t\t\t\t\t\t= {overall_len_deck}  m\n")
    p.add_run(f"Span between c/c of Expansion Joints\t\t\t\t= {span_between_cc_exp_joint}  m\n")
    p.add_run(f"Total length of Bridge\t\t\t\t\t\t= {tot_len_bridge}  m\n")
    
    DocxHelper.add_minor_heading(document,"Level Details:-")
    p = document.add_paragraph()
    p.add_run(f"Proposed Rail Level\t\t\t\t\t\t= {prop_rail_lev} m\n")
    p.add_run(f"Proposed Rail Formation Level\t\t\t\t= {prop_rail_form_level} m\n")
    p.add_run(f"Structural Depth of Girder\t\t\t\t\t= {struc_depth_girder} m\n")
    p.add_run(f"Bottom of girder level/top of bearing level\t\t\t= {bot_girder} m\n")
    p.add_run(f"Top of Bed Block Level\t\t\t\t\t\t= {top_bed_block} m\n")
    p.add_run(f"Top of abutment level\t\t\t\t\t\t= {top_abut_lev} m\n")
    p.add_run(f"Ground Level at abutment Location\t\t\t\t= {gl_abut} m\n")
    p.add_run(f"Height of Abutment \t\t\t\t\t\t= {ht_abut} m\n")
    p.add_run(f"Top of pile cap level\t\t\t\t\t\t= {top_pile_cap} m\n")
    p.add_run(f"Bottom of Pile Cap Level\t\t\t\t\t= {bot_pile_cap_lev} m\n")

    DocxHelper.add_minor_heading(document,"Hydraulics Details:-")
    p = document.add_paragraph()
    p.add_run(f"Highest Flood Level(HFL)\t\t\t\t\t= {HFL} m\n")
    p.add_run(f"Design Discharge \t\t\t\t\t\t= {discharge} cumecs\n")
    p.add_run(f"Max Velocity of Flood (m/sec)\t\t\t\t\t= {velocity} m/s\n")
    p.add_run(f"Effective Linear Waterway (Lw)\t\t\t\t= {eff_lw} m\n")
    p.add_run(f"Maximum scour Level at Pier (non-seismic)\t\t\t= {max_scour_non_seismic} m\n")
    p.add_run(f"Maximum scour Level at Pier (seismic)\t\t\t= {max_scour_seismic} m\n")
    
    

    DocxHelper.add_minor_heading(document,"Superstructure Details:-")
    p = document.add_paragraph()
    p.add_run(f"Loading Standard\t\t\t\t\t\t= {load_standard} \n")
    p.add_run(f"Type of Superstructure\t\t\t\t\t= {typr_sstr}\n")
    p.add_run(f"Dead Load of Superstructure\t\t\t\t\t= {dl_sstr} T\n")
    p.add_run(f"SIDL\t\t\t\t\t\t\t\t= {sidl} T\n")
    run = p.add_run("\n(Note : Please Refer Appendix XXIII of IRS:Bridge Rules)\n")
    run.bold = True
    p.add_run(f"Loaded Length (Edge to Edge of Superstructure)\t\t= {edge_to_edge_sstr} m\n")
    p.add_run(f"EUDL Load\t\t\t\t\t\t\t= {eudl} T")
    p.add_run(f"\nNo of Track\t\t\t\t\t\t\t= {no_track} \n")
    p.add_run(f"C/C Track distance\t\t\t\t\t\t= {cc_track_dis} m\n")
    p.add_run(f"Tractive Force\t\t\t\t\t\t\t= {tr_force} T\n")    
    p.add_run(f"Breaking Force\t\t\t\t\t\t\t= {br_force} T\n") 
    run = p.add_run("\n(Please Refer Appendix XXIV of IRS Bridge Rules )\n")
    run.bold = True
    p.add_run(f"\nType of bearing\t\t\t= {type_bearing} \n")
    p.add_run(f"Co efficient of friction due to Beraing\t= {fric_coeff_exp_bg} \n\n")
    run = p.add_run("(Please Refer Cl. No. 2.7.1. of IRS Bridge Rules)\n")
    run.bold = True
    
    p.add_run(f"Seismic Zone\t\t= {seis_zone}\n")
    p.add_run(f"Z (Zone factor)\t\t= {Z_factor_sstr} (Table 1A, IRS Seismic Code: 2020)")
    p.add_run(f"\nI (Importance factor)\t= {I_factor_sstr} (Table 2, IRS Seismic Code: 2020)")
    p.add_run("\n\n(Table 7 RDSO guidelines on seismic design of railway bridges)")
    p.add_run(f"\n R (for superstructure)\t\t\t={reduction_factor_sup}")
    p.add_run(f"\n R (for substructure)\t\t\t={reduction_factor_sub}")
    p.add_run("\n(Clause 4.2.3, IRS Seismic Code: 2020)")
    p.add_run(f"\n R (for earth pressure calculation)\t={reduction_factor_fou}")
    p.add_run("\n\n(As earth pressure is not passing through elastomeric beariing and dynamic increament of earth pressure is not related to bearing, R is not taken as 1 )")
    
    p.add_run(f"\nZ/2R\t\t\t\t\t= {Z_2r}\t(Cl: 9.4.1, IRS Seismic Code: 2020)")
    
    run = p.add_run("\n\nCalculation of Fundamental Natural Time Period for Longitudinal Direction: For Abutment\n")
    run.bold = True
    run.underline = True
    p.add_run(f"\nSo Fundamental Time Period (T = 2 π√(δ/g)) \t\t={T_88:.3f}  sec")
    p.add_run(f"\nConsider Soil Site as Medium Soil Site (Type II), Sa/g \t={Sa_g_90}")
    
    run = p.add_run("\n\nCalculation of Fundamental Natural Time Period for Transverse Direction: For Abutment\n")
    run.bold = True
    run.underline = True
    p.add_run(f"\nSo Fundamental Time Period (T = 2 π√(δ/g)) \t\t={T_105:.3f}   sec")
    p.add_run(f"\nConsider Soil Site as Medium Soil Site (Type II), Sa/g \t={Sa_g_107}")
    
    p.add_run(f"\n\nγwater  ={gumma_water} T per cum")


    DocxHelper.add_minor_heading(document,"Abutment Details:-")
    p = document.add_paragraph()
    

    p.add_run(f"Depth of Bed Block/ Abutment Cap\t\t\t= {dep_bb_abut_cap} m\n")   
    p.add_run(f"Length of  Bed Block/ Abutment Cap\t\t\t= {len_bb_abut_cap} m\n")   
    p.add_run(f"Width of  Bed Block/ Abutment Cap\t\t\t= {wid_bb_abut_cap} m\n\n")

    p.add_run(f"Height of Dirt Wall\t\t\t\t\t= {ht_dirt_wall} m\n")
    p.add_run(f"Length of Dirt wall\t\t\t\t\t= {len_bb_abut_cap} m\n")
    p.add_run(f"Thickness of Dirt wall\t\t\t\t\t= {thick_dirt_wall} m\n\n")
    
    p.add_run(f"Length of pedestal\t\t\t\t\t= {length_pedestral} m\n")
    p.add_run(f"Width of pedestal\t\t\t\t\t= {width_pedestral} m\n")
    p.add_run(f"Height of pedestal\t\t\t\t\t= {height_pedestral} m\n")
    p.add_run(f"No of pedestal\t\t\t\t\t\t= {no_pedestral} \n")
    p.add_run(f"Depth of Bearing\t\t\t\t\t= {depth_bearing} m\n")
    p.add_run(f"Width of Abutment shaft\t\t\t\t= {width_abutment_shaft} m\n")
    p.add_run(f"Length of Square return\t\t\t\t= {len_suare_return_wall} m\n")
    p.add_run(f"width of Square return at junction\t\t\t= {wid_sqr_return_at_junction} m\n")
    p.add_run(f"Avg. width of Square return at edge\t\t\t= {avg_sqr_return_at_e_edge} m\n\n")
   
    p.add_run(f"Length of Fly wing\t\t\t\t\t= {lengt_fly_wing} m\n")
    p.add_run(f"Depth of Fly wing at end\t\t\t\t= {dep_fly_end} m\n")
    p.add_run(f"Depth of Fly wing at junction\t\t\t\t= {Depth_fly_wing_at_junc} m\n")
    p.add_run(f"Thickness of Fly wing\t\t\t\t\t= {thick_fly_wing} m\n\n")

    p.add_run(f"Width of the Platform\t\t\t\t\t= {width_the_platform} m\n\n")
    
    p.add_run(f"No of Pile in Longitudinal Direction\t\t\t= {no_pile_long_direction} \n")
    p.add_run(f"No of Pile in Transverse Direction\t\t\t= {no_pile_tran_direction} \n")
    

    p.add_run(f"Dia. Of Pile\t\t\t\t\t\t= {dia_pile} m\n")
    p.add_run(f"c/c distance between pile Longituidinal\t\t= {c_c_dis_pile_longituidinal} m\n")
    p.add_run(f"c/c distance between pile Transverse\t\t\t= {c_c_dis_pile_transverse} m\n")
    p.add_run(f"Length Pile cap in Transverse Direction\t\t= {len_pile_cap_trans} m\n")
    p.add_run(f"Length Pile cap in Longitudinal Directionn\t\t= {len_pile_cap_long} m\n")
    p.add_run(f"Depth of Pile Cap\t\t\t\t\t= {dep_pile_cap} m\n")

   
    DocxHelper.add_minor_heading(document, "Soil Details:-")
    p = document.add_paragraph()
    p.add_run(f"φ \t\t={round(phi_soil)} deg\n")
    p.add_run(f"I \t\t={round(i_soil)} deg\n")
    p.add_run(f"δ \t\t={round(sigma_soil)} deg\n")
    p.add_run(f"α \t\t={round(alpha_soil)} deg\n")
    p.add_run(f"γ \t\t={gumma_soil} T/cum\n\n")
    p.add_run(f"Dead Load Surcharge\t\t\t\t= {dl_surcharge} T/m\n")
    p.add_run(f"Live Load Surcharge\t\t\t\t= {ll_surchage} T/m\n")
    p.add_run(f"Surcharge Width at Formation Level\t\t= {srug_width_form_level} m\n")

    run = p.add_run("\n\n(Note : Please Refer CL. 5.8.2 Of IRS : Substructure & Foundation Code.)\n")
    run.bold = True
    p.add_run(f"Height of Spilling Earth \t= {round(heigh_spilling_earth)}  m")
    p.add_run(f"\nCharateristics compressive stress for concrete (fck) \t= {round(fck)}  mpa")
    p.add_run(f"\nCharateristics Tensile stress for concrete (fy) \t\t= {round(fyk)}  mpa")


    document.add_page_break()
    document.save(output_path)

    print("\n\n\t\t*********Input Sheet End**********\n\n")
    
