import math
import input_sheet as isp
import DocxHelper
#I37
z_2r = isp.Z_factor_sstr/(2*isp.reduction_factor_sub)
#E81(change)
E81 =0
#F65
F65 =(isp.len_pile_cap_long-isp.width_abutment_shaft)/2+E81
#H83
H83 =(isp.wid_sqr_return_at_junction+isp.avg_sqr_return_at_e_edge)/2
#K115
rec_abut = isp.dl_sstr/2
#K116(change)
long_eccen_K116 =0
#K117
long_eccen_K117 =long_eccen_K116+E81

#K119
long_moment_K119 =rec_abut*long_eccen_K116
#K120
long_moment_K120 =rec_abut*long_eccen_K116
#K123(change)
Transverse_Eccentricity_Reaction  =0
#K124
Transverse_Eccentricity_moment  =Transverse_Eccentricity_Reaction*rec_abut
#K131
tot_sidl = isp.overall_len_deck*6.5
#K132
sidl_rec = round(tot_sidl/2,3)

#K136
long_moment_sidl_K136 =long_eccen_K116*sidl_rec
#K137
long_moment_sidl_K137 =long_eccen_K117*sidl_rec
#K140(change)
Transverse_Eccentricity_K140 =0
#K141
trans_moment_sidl_K141 =Transverse_Eccentricity_K140*sidl_rec
#J143
J143 = isp.thick_dirt_wall+0.3375
#K160
dl_dirt_wall =round(isp.ht_dirt_wall*isp.thick_dirt_wall*isp.len_bb_abut_cap*2.5,3)
#K161
eccen_abut_cg_dirt_wall =-((isp.width_abutment_shaft-isp.thick_dirt_wall)/2-(J143-isp.thick_dirt_wall))
#K162
eccen_pile_cg_dirt_wall =(J143-isp.thick_dirt_wall)+isp.thick_dirt_wall/2+(E81-isp.width_abutment_shaft/2)

#K165
dl_abut_cap =round(isp.wid_bb_abut_cap*isp.dep_bb_abut_cap*isp.len_bb_abut_cap*2.5,3)
#K166
eccen_abut_cg_abut_cap = round((isp.wid_bb_abut_cap/2-isp.width_abutment_shaft/2),2)
#K167
eccen_pile_cg_abut_cap =E81+eccen_abut_cg_abut_cap

#K174
self_weight_pedestal =round(isp.length_pedestral*isp.width_pedestral*isp.height_pedestral*isp.no_pedestral*2.5,3)


#K183(chnage)
self_weight_OHE_Mast =1
#K184
eccen_abut_cg_inspec_plat =0
#K185
eccen_pile_cg_inspec_plat =eccen_abut_cg_inspec_plat+E81

#K188(change)_K190
dl_trans_seismic_restrainer_block =6.598
#K192(change)
dl_long_seismic_restrainer_block =13.708
#K193(change)
eccen_abut_cg =-1.013
#K194(change)
eccen_pile_cg =-1.013

#K197
tot_dead_load_from_abut_cap =dl_dirt_wall+dl_abut_cap+self_weight_pedestal+0+0+self_weight_OHE_Mast+dl_trans_seismic_restrainer_block+dl_long_seismic_restrainer_block
#K199
tot_moment_cl_abut = round(dl_dirt_wall*eccen_abut_cg_dirt_wall+dl_abut_cap*eccen_abut_cg_abut_cap+self_weight_pedestal*long_eccen_K116+self_weight_OHE_Mast*eccen_pile_cg_inspec_plat+0*0+dl_long_seismic_restrainer_block*eccen_abut_cg,2)
#K201
tot_moment_cl_pile = round((dl_dirt_wall*eccen_pile_cg_dirt_wall+dl_abut_cap*eccen_pile_cg_abut_cap+self_weight_pedestal*long_eccen_K117+self_weight_OHE_Mast*eccen_pile_cg_inspec_plat+0*0+dl_long_seismic_restrainer_block*eccen_pile_cg),2)


#K212
tot_height_abut = round(isp.top_abut_lev-isp.top_pile_cap,3)
#K213
sec_area_abut_shaft = isp.len_bb_abut_cap*isp.width_abutment_shaft
#K214
vol_abut_shaft = tot_height_abut*sec_area_abut_shaft
#K215
dead_load_abut_shaft = round(vol_abut_shaft*2.5,3)
#K216
long_eccen_wrt_CL_pileCap =E81
#K217
long_moment_wrt_CL_pileCap =round(dead_load_abut_shaft*long_eccen_wrt_CL_pileCap,3)
#K222
height_square_return =round(isp.prop_rail_form_level-isp.top_pile_cap,3)
#k223
weight_of_two_square_return = round(2*F65*H83*height_square_return*2.5,3)
#K225
long_eccen_wrt_CL_abut_due_to_DL_square_return = -(F65/2-F65+isp.len_pile_cap_long/2)
#K226
long_eccen_wrt_CL_well_due_to_DL_square_return = round(weight_of_two_square_return*long_eccen_wrt_CL_abut_due_to_DL_square_return,2)
#k277
weight_of_pile_cap = round(isp.len_pile_cap_trans*isp.len_pile_cap_long*isp.dep_pile_cap*2.5,3)
#K285
tot_eudl_load = isp.eudl*isp.no_track
#K304
trans_eccen_cl_abut_304=  (isp.cc_track_dis-(isp.cc_track_dis/2))+0.1
#K314_K337
cda = round((0.15+(8/(6+isp.overall_len_deck))),3)
#K317
tot_live_load_shear =round((isp.eudl*(1+cda)),3)
#K318
live_load_reac_abut_318 =tot_live_load_shear/2
#k319
long_moment_ll_abut_ML=live_load_reac_abut_318*long_eccen_K116
#K320               
trans_moment_ll_abut_MT = live_load_reac_abut_318*trans_eccen_cl_abut_304

#K340
tot_live_load =round((isp.eudl*(1+cda)),3)
#K341
live_load_reac_abut_341 =tot_live_load/2
#k342
long_moment_ll_pile_ML=live_load_reac_abut_341*long_eccen_K117
#K343          
trans_moment_ll_pile_MT = live_load_reac_abut_341*trans_eccen_cl_abut_304
#K363
govering_long_force =max(isp.tr_force,isp.br_force)
#K364(change)
dispersion_long_force =0
#K366
net_long_force =govering_long_force*(1-dispersion_long_force/100)
#K368(change)
percent_force_transfer_abut =50
#K370
net_long_force_transfer_abut =round(net_long_force*percent_force_transfer_abut/100,3)
#K371
tractive_force_ll_typeA =net_long_force_transfer_abut*1
#K374
lever_arm_base_abut =round(isp.top_bed_block+isp.depth_bearing+isp.height_pedestral-isp.top_pile_cap,3)
#K375
lever_arm_base_pile_cap =round(isp.top_bed_block+isp.height_pedestral+isp.depth_bearing-isp.bot_pile_cap_lev,3)
#K379
moment_base_abut =net_long_force_transfer_abut*lever_arm_base_abut
#K380
moment_base_pile_cap =round(net_long_force_transfer_abut*lever_arm_base_pile_cap,3)

#K393_K394
tot_friction_force =isp.fric_coeff_exp_bg*(rec_abut+sidl_rec+live_load_reac_abut_341)
#K396
moment_base_abut_K396 =round(max(tot_friction_force, tractive_force_ll_typeA)*lever_arm_base_abut,2)
#K397
moment_base_pile_cap_K397 =(tot_friction_force)*lever_arm_base_pile_cap

#Earth Pressure
#active earth pressure due to backfill
#D415
phi_soil = math.radians(isp.phi_soil)
#D416
i_soil = math.radians(isp.i_soil)
#D417
delta_soil = math.radians(isp.sigma_soil)
#D418
alpha_soil = math.radians(isp.alpha_soil)
#D419
gumma_soil_rad = math.radians(isp.gumma_soil)
#D419
gumma_soil_deg = isp.gumma_soil
#Coefficient of active earth pressure
#D423
ka =  "cos²(φ-α)/[cos2αcos(α+δ)[1+√((sin(φ+δ)sin(φ-i))/(cos(α+δ)cos(α-i)))]²]xcosδ"
#D424
ka_calculated = round((math.cos(phi_soil - alpha_soil)**2) / (math.cos(alpha_soil)**2 * math.cos(alpha_soil + delta_soil) * 
      (1 + math.sqrt((math.sin(phi_soil + delta_soil) * math.sin(phi_soil - i_soil)) / 
      (math.cos(alpha_soil + delta_soil) * math.cos(alpha_soil - i_soil))))**2) * math.cos(delta_soil), 3)
E427 = isp.prop_rail_form_level
E435 = isp.top_pile_cap

D431 = round(E427 - E435, 3)
E437 = isp.bot_pile_cap_lev
C437 = round(E435 - E437, 3)
C432 = D431 + C437
#K448
earth_pressure_base_pile_cap = round(ka_calculated*isp.gumma_soil*C432, 3)




G438 = earth_pressure_base_pile_cap
#at base of abutment wall
#K441(change)
earth_pressure_abutment_base = "KaγH"
#K442
earth_pressure_abutment_base_calculated = round(ka_calculated * gumma_soil_deg * D431 , 3)
#K443
total_force_abutment_base = round(0.5 * earth_pressure_abutment_base_calculated * D431 * isp.len_bb_abut_cap, 3)
#K444
lever_arm_abutment_base = round(D431/3, 3)
#K445
moment_base_abutment_wall = round(total_force_abutment_base*lever_arm_abutment_base, 3)

#at base of pile cap

#K449
force_pile_cap_only = round(0.5*(earth_pressure_abutment_base_calculated+earth_pressure_base_pile_cap)*C437*isp.len_pile_cap_trans, 3)
#K451
lever_arm_pile_cap_base = round((C437/3)*((2*earth_pressure_abutment_base_calculated)+earth_pressure_base_pile_cap)/(earth_pressure_abutment_base_calculated+earth_pressure_base_pile_cap), 3)
#K452
total_force_bottom_pile_cap = total_force_abutment_base+force_pile_cap_only
#K454
total_moment_bottom_pile_cap = round((total_force_abutment_base*(lever_arm_abutment_base+C437)+force_pile_cap_only*lever_arm_pile_cap_base),3)

#Active earth pressure due to surcharge effect
#K464
abutment_height = D431
#K465
thickness_pile_cap = C437
#K466
total_height_with_pile_cap = abutment_height+thickness_pile_cap
#G468
L_minus_B = isp.len_bb_abut_cap - isp.srug_width_form_level

#B471
case1 = "Case-1"
#B509
case2 = "Case-2"
#D470
if total_height_with_pile_cap < L_minus_B:
    D470 = case1
else:
    D470 = case2
D477 = abutment_height + thickness_pile_cap
#K487
pressure_top_case1 = round((isp.dl_surcharge+isp.ll_surchage)/isp.srug_width_form_level*ka_calculated, 3)
#K489
pressure_bottom_case1 = round((isp.dl_surcharge+isp.ll_surchage)/(isp.srug_width_form_level+total_height_with_pile_cap)*ka_calculated, 3)
#K490
surcharge_pressure_bottom_abutment_case1 = round((isp.dl_surcharge+isp.ll_surchage)/(isp.srug_width_form_level+D431)*ka_calculated, 3)
#K492
p1_case1_case1 = round(pressure_bottom_case1*D477, 3)
#K493
acting_at_p1_case1_case1 = total_height_with_pile_cap/2
#K494
p2_case1_case1 = round(pressure_bottom_case1*D477**2*ka_calculated/(2*isp.srug_width_form_level), 3)
#K495
acting_at_p2_case1_case1 = round(2* total_height_with_pile_cap/3, 3)
#K497
p1_case2_case1 = round(surcharge_pressure_bottom_abutment_case1*abutment_height, 3)
#K498
acting_at_p1_case2_case1 = abutment_height/2
#K499
p2_case2_case1 = round(surcharge_pressure_bottom_abutment_case1*abutment_height**2*ka_calculated/(2*isp.srug_width_form_level), 3)
#K500
acting_at_p2_case2_case1 = round(2*abutment_height/3, 3)

#K502
horizontal_force_base_abutment_wall_case1 = round((p1_case2_case1+p2_case2_case1)*isp.len_bb_abut_cap, 3)
#K503
moment_base_abutment_wall_case1 = round((p1_case2_case1*acting_at_p1_case2_case1+p2_case2_case1*acting_at_p2_case2_case1)*isp.len_bb_abut_cap, 3)

#K506
horizontal_force_pile_cap_case1 = (p1_case1_case1+p2_case1_case1)*isp.len_bb_abut_cap
#K507
total_moment_base_pile_cap_case1 = round((p1_case1_case1*acting_at_p1_case1_case1+p2_case1_case1*acting_at_p2_case1_case1)*isp.len_bb_abut_cap, 3)




#K526
pressure_top_case2 = round(((isp.ll_surchage+isp.dl_surcharge)/isp.srug_width_form_level)*ka_calculated, 3)
#K528
pressure_bottom_case2 = round(((isp.ll_surchage+isp.dl_surcharge)/isp.len_bb_abut_cap)*ka_calculated, 3)
#K529
surcharge_pressure_bottom_abutment_case2 = pressure_bottom_case2

C513 = isp.len_bb_abut_cap - isp.srug_width_form_level
E510 = pressure_top_case2
D522 = pressure_bottom_case2
B515 = total_height_with_pile_cap
D522 = pressure_bottom_case2
D515 = pressure_bottom_case2
G513 = abutment_height
C516 = round(G513-C513, 3)
C519 = B515-C516-C513
if G513 < C513:
    D516 = round(D515 + ((E510 - D515) / C513) * (C513 - G513), 3)
else:
    D516 = D515
#K531
p1_case1_case2 = round(C513*(E510+D522)/2, 3)
D515 = pressure_bottom_case2
#K532
acting_at_p1_case1_case2 = round(B515-((C513/3)*(2*D515+E510)/(D515+E510)), 3)
#K533
p2_case1_case2 = round(D522*(C516+C519), 3)
#K534
acting_at_p2_case1_case2 = round(C519/2, 3)
#K536
if C513 < G513:
    p1_case2_case2 = round((C513 * (E510 + D515)) / 2, 3)
else:
    p1_case2_case2 = round((G513 * (E510 + D516)) / 2, 3)

#K537
if C513 < G513:
    acting_at_p1_case2_case2 = round(G513 - (((C513 - C516) / 3) * (2 * D515 + E510) / (D515 + E510)), 3)
else:
    acting_at_p1_case2_case2 = round(G513 - ((G513 / 3) * (2 * D516 + E510) / (D516 + E510)), 3)

#K538
if G513 < C513:
    p2_case2_case2 = 0
else:
    p2_case2_case2 = round(D515 * C516, 3)

#K539
if G513 < C513:
    acting_at_p2_case2_case2 = 0
else:
    acting_at_p2_case2_case2 = C516 / 2

#K542
horizontal_force_base_abutment_wall_case2 = round((p1_case2_case2+p2_case2_case2)*isp.len_bb_abut_cap, 3)
#K543
moment_base_abutment_wall_case2 = round((p1_case2_case2*acting_at_p1_case2_case2 + p2_case2_case2*acting_at_p2_case2_case2)*isp.len_bb_abut_cap, 3)

#K546
horizontal_force_pile_cap= round((p1_case1_case2+p2_case1_case2)*isp.len_pile_cap_trans, 3)
#K547
total_moment_base_pile_cap = round((p1_case1_case2*acting_at_p1_case1_case2 + p2_case1_case2*acting_at_p2_case1_case2)*isp.len_pile_cap_trans, 3)

#K552
if D470 == case1:
    p1_final = p1_case1_case1
else:
    p1_final = p1_case1_case2

#K553
if D470 == case1:
    acting_at_p1_final = acting_at_p1_case1_case1
else:
    acting_at_p1_final = acting_at_p1_case1_case2

#K554
if D470 == case1:
    p2_final = p2_case1_case1
else:
    p2_final = p2_case1_case2

#K555
if D470 == case1:
    acting_at_p2_final = acting_at_p2_case1_case1
else:
    acting_at_p2_final = acting_at_p2_case1_case2


#K558
if D470 == case1:
    total_horizontal_force_final = horizontal_force_base_abutment_wall_case1
else:
    total_horizontal_force_final = horizontal_force_base_abutment_wall_case2

#K559
if D470 == case1:
    moment_base_abutment_wall_final = moment_base_abutment_wall_case1
else:
    moment_base_abutment_wall_final = moment_base_abutment_wall_case2

#K562
if D470 == case1:
    horizontal_force_pile_cap_final = horizontal_force_pile_cap
else:
    horizontal_force_pile_cap_final = horizontal_force_pile_cap

#K563
if D470 == case1:
    total_moment_base_pile_cap_final = total_moment_base_pile_cap
else:
    total_moment_base_pile_cap_final = total_moment_base_pile_cap

#K577
height_backfill_abut_wall = round(abutment_height, 3)
#K578
avg_height_backfill_return_wall_trans = height_backfill_abut_wall
#K579
eff_width_outer_cantilever = round((isp.len_pile_cap_trans - isp.len_bb_abut_cap)/2, 3)

#K580
W = round((2*eff_width_outer_cantilever+isp.len_bb_abut_cap-2*H83)*F65*D431*gumma_soil_deg, 3)
#K581
eccen_CG_pile = long_eccen_wrt_CL_abut_due_to_DL_square_return
#K582
longitudinal_moment_CG_pile_1 = round(W * eccen_CG_pile, 3)

#K591
spelling_length_front_abut = round(isp.len_pile_cap_long - F65 - isp.width_abutment_shaft, 3)
#K592
height_spiling_earth = round((isp.ht_abut + isp.dep_bb_abut_cap)/2, 3)
#K593
vertical_load_front_earthfill = round(spelling_length_front_abut*isp.len_pile_cap_trans*height_spiling_earth* gumma_soil_deg, 3)
#K594
eccen_CG_pile_e2 = round(spelling_length_front_abut/2 + E81 + isp.width_abutment_shaft/2, 3)
#K595
longitudinal_moment_CG_pile_2 = round(vertical_load_front_earthfill*eccen_CG_pile_e2, 3)

if total_height_with_pile_cap < L_minus_B:
        var1 = "Therefore, H<L-B Case 1 is applicable"
else:
        var1 = "Therefore, H>L-B Case 2 is applicable"
print(acting_at_p2_case1_case2)




def word_print(document, output_path):
    DocxHelper.add_main_heading(document, "DESIGN OF ABUTMENT AND FOUNDATION")
    p=document.add_paragraph()
    run=p.add_run(f"Bridge No.\t\t\t\t\t\t{int(isp.bridge_no)}\n")
    run.bold = True
    run=p.add_run(f"ABUTMENT NO.\t\t\t\t\t{isp.abut_no}\n")
    run.bold = True
    run=p.add_run(f"SPAN ARRANGEMENT:-\t\t\t\t{isp.span_numb}x{isp.span_len}m\n")
    run.bold = True

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "1.0 INTRODUCTION")
    p=document.add_paragraph()
    p.add_run("The system consists of a solid rectangular abutment with monolithic dirt wall, square return wall and solid abutment cap. The top dimensions of the abutment cap are fixed so as to fit in the details of superstucture.\n")
    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "2.0 REFERENCE")
    p=document.add_paragraph()
    p.add_run("For the design of the abutment and its different components generally the provisions of IRS(Indian Railway Standards) Codes have been followed.  Followings are the main references.\n")
    p.add_run("i. IRS Bridge Rules\n")
    p.add_run("ii. IRS Concrete Bridge Codes-1997\n")
    p.add_run("iii. IRS Substructure codes.\n")
    p.add_run("iv. IRS Seismic code for earthquake resistance design-2020\n")
    p.add_run("v. IS:2911(Part1/Sec2)-2010\n")
    p.add_run("vi. IS:14593-1998\n")
    p.add_run("vii. IRC:78\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "3.0 DESIGN PARAMETERS")
    p=document.add_paragraph()
    p.add_run(f"Proposed Rail Level\t\t\t\tRL\t\t\t{isp.prop_rail_lev}m\n")
    p.add_run(f"Proposed Rail Formation Level\t\tRL\t\t\t{isp.prop_rail_form_level}m\n")
    p.add_run(f"Structural Depth of Composite Girder at center\t\t\t{isp.struc_depth_girder}m\n")
    p.add_run(f"Bottom of Girder Level\t\t\t\tRL\t\t\t{isp.bot_girder}m\n")
    p.add_run(f"Top of Bed Block Level\t\t\t\tRL\t\t\t{isp.top_bed_block}m\n")
    p.add_run(f"Top of Abutment Level\t\t\t\tRL\t\t\t{isp.top_abut_lev}m\n")
    p.add_run(f"Ground Level\t\t\t\t\tRL\t\t\t{isp.gl_abut}m\n")
    p.add_run(f"Top of Pile Cap Level\t\t\t\tRL\t\t\t{isp.top_pile_cap}m\n")
    p.add_run(f"Bottom of Pile Cap Level\t\t\tRL\t\t\t{isp.bot_pile_cap_lev}m\n")
    p.add_run(f"High Flood Level (HFL)\t\t\tRL\t\t\t{isp.HFL}m\n")
    p.add_run(f"Design Discharge\t\t\t\t\t\t\t{isp.discharge}cumec\n")
    p.add_run(f"Max Velocity of Flood (m/sec)\t\t\t\t\t\t{isp.velocity}m/sec\n")
    p.add_run(f"Scour LVL at Abutment\t\t\tRL\t\t\t{isp.max_scour_non_seismic}m\n")

    p=document.add_paragraph()
    p.add_run(f"Seismic Zone\t\t\t\t\t\t=\t\t{isp.seis_zone}\n")
    p.add_run(f"z\t\t\t\t\t={isp.Z_factor_sstr}Z/2R\t={isp.Z_2r}\t\t{z_2r}\n")
    p.add_run(f"Importance Factor (I)\t\t\t={isp.reduction_factor_sup}\t\t\t\t{isp.reduction_factor_sub}\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "4.0 SPAN DETAILS")
    p=document.add_paragraph()
    p.add_run("The Abutment is supporting  Composite Girder of Effective Span  18.3  m. The Details of  Span is gives as under\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document,"4.1 Span 1")
    p=document.add_paragraph()
    p.add_run(f"Effective span between c/c of bearing\t\t\t\t\t={isp.eff_span_cc_bearing}m\n")
    p.add_run(f"Overall span\t\t\t\t\t\t\t\t{isp.overall_girder_length}m\n")
    p.add_run(f"Span between c/c of Expansion Joints\t\t\t\t\t{isp.span_between_cc_exp_joint}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "6.0 DEAD LOAD CALCULATION")
    p=document.add_paragraph()
    p.add_run("Anticlockwise Moments are taken as positive\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "6.1 Dead Load from Superstructure")
    p=document.add_paragraph()
    p.add_run(f"Load for DL\t\t\t\t\t\t\t\t\t={isp.dl_sstr}T\n")
    p.add_run(f"Weight of superstructure (Span)\t\t\t\t\t\t={isp.dl_sstr}T\n")
    p.add_run(f"Reaction on Abutment\t\t\t\t\t\t\t\t={rec_abut}T\n")
    p.add_run(f"Longitudinal Eccentricity of Reaction w.r.t. C/L of Abutment, eL₁\t\t={long_eccen_K116}m\n")
    p.add_run(f"Longitudinal Eccentricity of Reaction w.r.t. Pile Cap CG, eL₂\t\t\t={long_eccen_K117}m\n\n")
 
    p.add_run(f"Longitudinal Moment due to DL about C/L of Abutment={rec_abut}x{long_eccen_K116}\t\t={long_moment_K119}T-m\n")
    p.add_run(f"Longitudinal Moment due to DL about Pile Cap CG={rec_abut}x{long_eccen_K117}\t\t\t={long_moment_K120}T-m\n\n")
    p.add_run("The Superstructure is symmetric about Centre Line of Soffit; therefore there is no Transverse Eccentricty\n")
    p.add_run(f"Transverse Eccentricity of Reaction, eT\t\t\t\t\t={Transverse_Eccentricity_Reaction}\n")
    p.add_run(f"Transverse Moment  due to DL\t\t\t{rec_abut}x{Transverse_Eccentricity_Reaction}\t\t={Transverse_Eccentricity_moment}\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "6.2 Super Imposed Dead Load (SIDL) from Superstructure")
    p=document.add_paragraph()
    p.add_run("Caluculation of SIDL:\n")
    p.add_run(f"Total  Load for SIDL\t\t\t\t\t\t\t\t={tot_sidl}T\n")
    p.add_run(f"SIDL Reaction\t\t\t\t\t\t\t\t\t={sidl_rec}T\n")
    p.add_run(f"Longitudinal Eccentricity of Reaction w.r.t. C/L of Abutment, eL1\t\t={long_eccen_K116}m\n")
    p.add_run(f"Longitudinal Eccentricity of Reaction w.r.t. Pile Cap CG, eL2\t\t\t={long_eccen_K117}m\n\n")
    p.add_run(f"Longitudinal Moment due to SIDL about C/L of Abutment={sidl_rec}x{long_eccen_K116}\t={long_moment_sidl_K136}T-m\n")
    p.add_run(f"Longitudinal Moment due to SIDL about Pile Cap CG = {sidl_rec}x{long_eccen_K117}\t\t={long_moment_sidl_K137}T-m\n\n")
    p.add_run("The Superstructure is symmetric about Centre Line of Soffit; therefore there is no Transverse Eccentricty\n")
    p.add_run(f"Transverse Eccentricity of Reaction, eT\t\t\t\t\t={Transverse_Eccentricity_K140}m\n")
    p.add_run(f"Transverse Moment  due to SIDL={sidl_rec}x{Transverse_Eccentricity_K140}\t\t\t\t\t={trans_moment_sidl_K141}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "6.3 Dead Load from Abutment Cap")
    p=document.add_paragraph()
    p.add_run(f"Length of bed block\t\t\t\t\t\t\t\t={isp.len_bb_abut_cap}m\n")
    p.add_run(f"Width of bed block\t\t\t\t\t\t\t\t={isp.wid_bb_abut_cap}m\n")
    p.add_run(f"Depth of Bed block\t\t\t\t\t\t\t\t={isp.dep_bb_abut_cap}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "[a] Dead Load of Dirt Wall")
    p=document.add_paragraph()

    p.add_run(f"Dead Load\t\t\t={isp.ht_dirt_wall}x{isp.thick_dirt_wall}x{isp.len_bb_abut_cap}x2.5\t\t\t\t={dl_dirt_wall}T\n")
    p.add_run(f"Eccentricity w.r.t. Abutment CG=-[({isp.width_abutment_shaft}-{isp.thick_dirt_wall}/2-({J143}-{isp.thick_dirt_wall}))]\t\t\t={eccen_abut_cg_dirt_wall}m\n")
    p.add_run(f"Eccentricity w.r.t. Pile Cap CG\t\t\t\t\t\t\t={eccen_pile_cg_dirt_wall:.3f}m\n")
    
    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "[b] Dead Load of Abutment Cap")
    p=document.add_paragraph()
    p.add_run(f"Dead Load\t\t\t={isp.wid_bb_abut_cap}x{isp.dep_bb_abut_cap}x{isp.len_bb_abut_cap}x2.5\t\t\t\t={dl_abut_cap}T\n")
    p.add_run(f"Eccentricity w.r.t. Abutment CG\t\t\t\t\t\t={eccen_abut_cg_abut_cap}m\n")
    p.add_run(f"Eccentricity w.r.t. Pile Cap CG\t\t\t\t\t\t\t={eccen_pile_cg_abut_cap}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "[c] Dead Load of pedestals on Abutment Cap")
    p=document.add_paragraph()
    p.add_run(f"Size of pedestals\t\t\tLongitudinal direction\t\t\t={isp.length_pedestral}m\n")
    p.add_run(f"Transverse direction\t\t\t\t\t\t\t\t={isp.width_pedestral}m\n")
    p.add_run(f"Height\t\t\t\t\t\t\t\t\t\t={isp.height_pedestral}m\n")
    p.add_run(f"Total number of pedestrals\t\t\t\t\t\t\t={isp.no_pedestral}nos.\n")
    p.add_run(f"Self weight of Pedestals\t\t={isp.no_pedestral}x{isp.length_pedestral}x{isp.width_pedestral}x{isp.height_pedestral}x2.5\t\t={self_weight_pedestal}T\n")
    p.add_run(f"Eccentricity w.r.t. Abutment CG\t\t\t\t\t\t={long_eccen_K116}m\n")
    p.add_run(f"Eccentricity w.r.t. Pile Cap CG\t\t\t\t\t\t\t={long_eccen_K117}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "[d] Dead Load of OHE Mast")
    p=document.add_paragraph()
    p.add_run(f"Self weight of OHE Mast\t\t\t\t\t\t\t={self_weight_OHE_Mast}T\n")
    p.add_run(f"Ecentricity Inspection Platform W.r.t Abutment CG\t\t\t\t={eccen_abut_cg_inspec_plat}m\n")
    p.add_run(f"Eccentricity w.r.t. Pile Cap CG\t\t\t\t\t\t\t={eccen_pile_cg_inspec_plat}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "[e] Dead Load of Raised Portion of Transverse Seismic Restrainer Block")
    p=document.add_paragraph()
    p.add_run(f"s/w of seismic restrainer block \t=2 x 0.725 x 1.300 x 1.400 x 2.5 \t={dl_trans_seismic_restrainer_block}T\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "[f] Dead Load of Raised Portion of Longitudinal Seismic Restrainer Block")
    p=document.add_paragraph()
    p.add_run(f"s/w of seismic restrainer block \t\t\t\t\t\t={dl_long_seismic_restrainer_block}T\n")
    p.add_run(f"Ecentricity W.r.t Abutment CG\t\t\t\t\t\t\t={eccen_abut_cg}m\n")
    p.add_run(f"Ecentricity W.r.t Pile cap CG\t\t\t\t\t\t\t={eccen_pile_cg}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "Total Dead Load from Abutment Cap including Bearings, Pedestals")
    p=document.add_paragraph()
    p.add_run(f"={dl_dirt_wall:.3f}+{dl_abut_cap:.3f}+{self_weight_pedestal:.3f}+0+0+{self_weight_OHE_Mast:.3f}+{dl_trans_seismic_restrainer_block:.3f}+{dl_long_seismic_restrainer_block:.3f}={tot_dead_load_from_abut_cap:.3f}T\n")
    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "Total Longitudinal Moment about CL of Abutment due to above Dead Load")
    p=document.add_paragraph()
    p.add_run(f"={dl_dirt_wall:.3f}x{eccen_abut_cg_dirt_wall:.3f}+{dl_abut_cap:.3f}x{eccen_abut_cg_abut_cap:.3f}+{self_weight_pedestal:.3f}x{long_eccen_K116:.3f}+{self_weight_OHE_Mast:.3f}x{eccen_pile_cg_inspec_plat:.3f}+0x0+{dl_long_seismic_restrainer_block:.3f}x{eccen_abut_cg:.3f}={tot_moment_cl_abut:.3f}T-m\n")
    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "Total Longitudinal Moment about CL of Pile Cap due to above Dead Load")
    p=document.add_paragraph()
    p.add_run(f"={dl_dirt_wall:.3f}x{eccen_pile_cg_dirt_wall:.3f}+{dl_abut_cap:.3f}x{eccen_pile_cg_abut_cap:.3f}+{self_weight_pedestal:.3f}x{long_eccen_K117:.3f}+{self_weight_OHE_Mast:.3f}x{eccen_pile_cg_inspec_plat:.3f}+0x0+{dl_long_seismic_restrainer_block:.3f}x{eccen_pile_cg:.3f}={tot_moment_cl_pile:.3f}T-m\n")
    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "6.4 Dead Load of Abutment Shaft")
    p=document.add_paragraph()
    p.add_run("The Abutment has Rectangular Section.")
    p=document.add_paragraph()
    p.add_run(f"Total height of abutment=\t\t{isp.top_abut_lev}-{isp.top_pile_cap}\t\t\t={tot_height_abut}m\n")
    p.add_run(f"Sectional area of Abutment Shaft\t={isp.len_bb_abut_cap}x{isp.width_abutment_shaft}\t\t\t\t={sec_area_abut_shaft:.3f}m²\n")
    p.add_run(f"Volume of Abutment Shaft\t\t={tot_height_abut}x{sec_area_abut_shaft:.3f}\t\t\t\t={vol_abut_shaft}m³\n")
    p.add_run(f"Dead Load of Abutment Shaft\t\t={vol_abut_shaft}x2.5\t\t\t\t={dead_load_abut_shaft:.3f}T\n")
    p.add_run(f"Longitudinal Eccentricity w.r.t. Pile Cap CG, eL\t\t\t\t\t={E81}m\n")
    p.add_run(f"Longitudinal Moment about Pile Cap CG={dead_load_abut_shaft}x{E81}\t\t\t\t={long_moment_wrt_CL_pileCap:.3f}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "6.5 Dead Load of Square Return")
    p=document.add_paragraph()
    p.add_run(f"Length of Square Return=\t\t\t\t\t\t\t{F65}m\n")
    p.add_run(f"Average width of Square Return\t\t\t\t\t\t={H83}m\n")
    p.add_run(f"Height of Square Return\t\t={isp.prop_rail_form_level}-{isp.top_pile_cap}\t\t\t={height_square_return}m\n")
    p.add_run(f"Weight of Two Square Returns\t\t=2x{F65}x{H83}x{height_square_return}x2.5\t\t\t={weight_of_two_square_return}T\n")
    p.add_run(f"Longitudinal Eccentricity w.r.t. Pile Cap CG=[({F65}/2-{F65}+{isp.len_pile_cap_long})]/2\t\t={long_eccen_wrt_CL_abut_due_to_DL_square_return}m\n")
    p.add_run(f"Longitudinal Moment about Pile Cap CG={weight_of_two_square_return}x{long_eccen_wrt_CL_abut_due_to_DL_square_return}\t\t\t\t={long_eccen_wrt_CL_well_due_to_DL_square_return}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "6.7 Dead Load of Pile Cap")
    p=document.add_paragraph()
    p.add_run(f"Length of Pile Cap (perpendicular to track)\t\t\t\t\t={isp.len_pile_cap_trans}m\n")
    p.add_run(f"Width of Pile Cap (parallel to track)\t\t\t\t\t\t={isp.len_pile_cap_long}m\n")
    p.add_run(f"Depth of Pile Cap\t\t\t\t\t\t\t\t={isp.dep_pile_cap}m\n")
    p.add_run(f"Weight of Pile Cap\t\t\t={isp.len_pile_cap_trans}x{isp.len_pile_cap_long}x{isp.dep_pile_cap}x2.5\t\t\t={weight_of_pile_cap:.3f}T\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "7.0 VERTICAL LIVE LOAD CALCULATION")
    p=document.add_paragraph()
    p.add_run(f"Standard of Loading\t\t\t{isp.load_standard}\n")
    p.add_run("(Note : Please Refer Appendix XXIII of IRS:Bridge Rules)\n")
    p.add_run(f"Loaded Length (Edge to Edge of Superstructure)\t\t\t\t={isp.overall_len_deck}m\n")
    p.add_run(f"Total EUDL Load  (Shear) for {isp.overall_len_deck} m span ( for single track loaded)\t={isp.eudl}T\n")
    p.add_run(f"Here Total {isp.no_track} Nos. tracks are placed on single sub-structure\n")
    p.add_run(f"Total EUDL Load  (Shear) for {isp.overall_len_deck} m span (when 1 track loaded, concentrically)={tot_eudl_load}\n")
    p.add_run(f"Longitudinal Eccentricity w.r.t C/L of Abutment, eL1\t\t\t\t={long_eccen_K116}m\n")
    p.add_run(f"Longitudinal Eccentricity of Reaction w.r.t. Pile Cap CG, eL2\t\t\t={long_eccen_K117}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "Calculation of transverse eccentricity")
    p=document.add_paragraph()
    p.add_run("[a] When single track at edge loaded\n")
    p.add_run(f"Transverse Eccentricity w.r.t. C/L of Abutment, eT\t\t\t\t={trans_eccen_cl_abut_304}m\n")
    p.add_run("(Note : Please Refer Cl: 2.5.1 of IRS:Bridge Rule for Transverse Eccentricity )\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "Computation of Moment Due to LL")
    p=document.add_paragraph()
    p.add_run("(Note : Please refer clause 2.4.1.1 (a) of IRS:Bridge Rule)\n")
    p.add_run(f"CDA \t\t= 0.15 + [ 8 / (6 + L)] \t\t\t\tSubject to Maximum of 1.0\n")
    p.add_run(f"Therefore, CDA=0.15 + [ 8 / ( 6 + {isp.overall_len_deck} ) ]\t\t\t\t\t={cda:.3f}\n")
    p.add_run("Augmented load calculation\n")
    p.add_run("[a] When single track at edge loaded\n")
    p.add_run(f"Total Live Load (Shear)={isp.eudl}x(1+{cda})\t\t\t\t\t={tot_live_load_shear:.3f}T\n")
    p.add_run(f"Live Load Reaction on Abutment\t\t={tot_live_load_shear:.3f}/2.0\t\t\t={live_load_reac_abut_318:.3f}T\n")
    p.add_run(f"Longitudinal Moment due to LL on Abutment, ML={live_load_reac_abut_318:.3f}x{long_eccen_K116}\t\t\t={long_moment_ll_abut_ML:.3f}T-m\n")
    p.add_run(f"Transverse Moment due to LL on Abutment, MT={live_load_reac_abut_318:.3f}x{trans_eccen_cl_abut_304}\t\t={trans_moment_ll_abut_MT:.3f}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "For Design of Deep Foundation (Pile Foundation)")
    p=document.add_paragraph()
    p.add_run("(Note : CDA is not considered for design of Deep Foundations as per Cl:6.9.3 of IRS:Code of Practice for the Design of Sub- Structures and Foundation of Bridges.)\n")
    p.add_run(f"Therefore, CDA for Foundation\t\t\t\t\t\t={cda:.3f}\n")
    p.add_run("Augmented load calculation\n")
    p.add_run("[a] When single track at edge loaded\n")
    p.add_run(f"Total Live Load (Shear) excluding CDA\t={isp.eudl}x(1+{cda})\t\t={tot_live_load:.3f}T\n")
    p.add_run(f"Live Load Reaction on Abutment\t\t={tot_live_load:.3f}/2.0\t\t\t={live_load_reac_abut_341}T\n")
    p.add_run(f"Longitudinal Moment due to LL on Pile Cap, ML={live_load_reac_abut_341:.3f}x{long_eccen_K117}\t\t\t={long_moment_ll_pile_ML}T-m\n")
    p.add_run(f"Transverse Moment due to LL on Pile Cap, MT  ={live_load_reac_abut_341:.3f}x{trans_eccen_cl_abut_304}\t\t\t={trans_moment_ll_pile_MT:.3f}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "8.0 HORIZONTAL LOAD CALCULATION")
    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "8.1 TRACTIVE EFFORT / BRAKING FORCE")
    p=document.add_paragraph()
    p.add_run("(Please Refer Appendix XXIV of IRS Bridge Rules )\n")
    p.add_run(f"Loaded Length (Edge to Edge of Superstructure)\t\t\t\t={isp.overall_len_deck}m\n")
    p.add_run(f"Tractive Force for {isp.overall_len_deck} m Loaded Span=\t\t\t\t\t{isp.tr_force}T\n")
    p.add_run(f"Braking Force for {isp.overall_len_deck} m Loaded Span\t\t\t\t\t={isp.br_force}T\n")
    p.add_run(f"Governing Longitudinal Force\t\t\t=max({isp.tr_force},{isp.br_force})\t\t={govering_long_force}T\n")
    p.add_run(f"Dispersion of Longitudinal Force\t\t\t\t\t\t={dispersion_long_force}%\n")
    p.add_run("(Note : Refer Clause 2.8.3.4, IRS : Bridge Rules)\n")
    p.add_run(f"Net Longitudinal Force\t\t\t\t={govering_long_force}x(1-{dispersion_long_force}/100)\t\t={net_long_force}T\n")
    p.add_run(f"Type of bearing\t\t\t={isp.type_bearing}\n")
    p.add_run(f"Percent Force Transferred to Abutment\t\t\t\t\t={percent_force_transfer_abut}%\n\n")
    p.add_run(f"Therefore, Net Longitudinal Force Transferred to Abutment\t\t\t={net_long_force_transfer_abut:.3f}T\n")
    p.add_run(f"Tractive force for Type A Live Load\t\t={net_long_force_transfer_abut:.3f}x1\t\t\t={tractive_force_ll_typeA}T\n")
    p.add_run(f"Lever Arm w.r.t. Base of Abutment\t\t={isp.top_bed_block}+{isp.depth_bearing}+{isp.height_pedestral}-{isp.top_pile_cap}  ={lever_arm_base_abut:.3f}m\n")
    p.add_run(f"Lever Arm w.r.t. Base of Pile Cap\t\t={isp.top_bed_block}+{isp.height_pedestral}+{isp.depth_bearing}-{isp.bot_pile_cap_lev}  ={lever_arm_base_pile_cap}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "Moment Calculation")
    p=document.add_paragraph()
    p.add_run("[a] When single track at edge loaded (Type A)\n")
    p.add_run(f"Moment about Base of Abutment\t\t={net_long_force_transfer_abut}x{lever_arm_base_abut:.3f}\t\t\t={moment_base_abut:.3f}T-m\n")
    p.add_run(f"Moment about Bottom of Pile Cap\t\t={net_long_force_transfer_abut}x{lever_arm_base_pile_cap}\t\t\t={moment_base_pile_cap}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "8.2 FRICTIONAL RESISTANCE DUE TO BEARING")
    p=document.add_paragraph()
    p.add_run("(Please Refer Cl:5.6.2 of IRS:Bridge & Substructure Code & Cl:2.7 of IRS:Bridge Rule)\n")
    p.add_run(f"Co-efficient of Friction\t\t\t\t\t\t\t\t={isp.fric_coeff_exp_bg}\n")
    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "For Type A loading")
    p=document.add_paragraph()
    p.add_run(f"Total Frictional Force\t\t={isp.fric_coeff_exp_bg}x({rec_abut}+{sidl_rec}+{live_load_reac_abut_341:.3f})\t\t={tot_friction_force:.3f}T\n")
    p.add_run(f"Frictional Force\t\t\t\t\t\t\t\t={tot_friction_force}T\n\n")
    p.add_run(f"Moment about Base of Abutment= max({tot_friction_force:.3f},{tractive_force_ll_typeA})x{lever_arm_base_abut}\t\t={moment_base_abut_K396:.2f}T-m\n")
    p.add_run(f"Moment about Bottom of Pile Cap= max({tot_friction_force},{tractive_force_ll_typeA})x{moment_base_pile_cap_K397:.3f}\t\t=T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "8.3 EARTH PRESSURE")
    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "8.3.1 ACTIVE EARTH PRTESSURE DUE TO BACKFILL")
    p=document.add_paragraph()
    p.add_run(f"φ\t\t={isp.phi_soil}\n")
    p.add_run(f"i\t\t={isp.i_soil}\n")
    p.add_run(f"δ\t\t={isp.sigma_soil}\n")
    p.add_run(f"α\t\t={isp.alpha_soil}\n")
    p.add_run(f"γ\t\t={isp.gumma_soil}T/cum\n\n")

    p.add_run("Co-efficient of active earth pressure\n\n")
    p.add_run(f"Ka= {ka}\n")
    p.add_run(f"Ka= {ka_calculated}\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "At base of Abutment Wall")
    p=document.add_paragraph()
    p.add_run(f"Earth Pressure at Abutment Base\t\t\t\t\t\t={earth_pressure_abutment_base}\n")
    p.add_run(f"={ka_calculated}x{gumma_soil_rad:.3f}x{D431}=\t\t\t\t\t\t\t\t{earth_pressure_abutment_base_calculated:.3f}T/m²\n")
    p.add_run(f"Total Force at Abutment Base\t\t=0.5x{earth_pressure_abutment_base_calculated}x{D431}x{isp.len_bb_abut_cap}\t\t={total_force_abutment_base:.3f}T\n")
    p.add_run(f"Lever Arm w.r.t. Abutment Base\t={D431}/3.0\t\t\t\t={lever_arm_abutment_base}m\n")
    p.add_run(f"Moment about Base of Abutment Wall={total_force_abutment_base:.3f}x{lever_arm_abutment_base}\t\t\t\t={moment_base_abutment_wall:.3f}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "At base of Pile Cap")
    p=document.add_paragraph()
    p.add_run(f"Earth Pressure at base of Pile Cap\t={ka_calculated}x{isp.gumma_soil}x{C432}\t\t\t={earth_pressure_base_pile_cap:.3f}T/m²\n")
    p.add_run(f"Force on Pile Cap only\t\t\t=0.5x({earth_pressure_abutment_base_calculated}+{earth_pressure_base_pile_cap})x{C437}x{isp.len_bb_abut_cap}\t\t={force_pile_cap_only:.3f}T\n")
    p.add_run(f"Lever Arm w.r.t. Pile Cap Base=({C437}/3)x((2x{earth_pressure_abutment_base_calculated})+{earth_pressure_base_pile_cap})/({earth_pressure_abutment_base_calculated}+{earth_pressure_base_pile_cap})\t={lever_arm_pile_cap_base:.3f}m\n")
    p.add_run(f"Total Moment at bottom of Pile Cap\t=({total_force_abutment_base}x({lever_arm_abutment_base+C437})+{force_pile_cap_only}x{lever_arm_pile_cap_base})\t={total_moment_bottom_pile_cap}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "8.3.2 ACTIVE EARTH PRESSURE DUE TO SURCHARGE EFFECT")
    p=document.add_paragraph()
    p.add_run("(Note : Please Refer CL. 5.8.2 Of IRS : Substructure & Foundation Code.)\n\n")
    p.add_run(f"Dead Load Surcharge\t\t\t=V\t\t\t\t\t={isp.dl_surcharge}T/m\n")
    p.add_run(f"Live Load Surchage\t\t\t=L\t\t\t\t\t={isp.ll_surchage}T/m\n")
    p.add_run(f"Surcharge Width at Formation Level\t=B\t\t\t\t\t={isp.srug_width_form_level}m\n")
    p.add_run(f"Length of Abutment\t\t\t=L\t\t\t\t\t={isp.len_bb_abut_cap}m\n")
    p.add_run(f"Height of Abutment\t\t\t=h\t\t\t\t\t={abutment_height}m\n")
    p.add_run(f"Thickness of Pile Cap\t\t\t=D\t\t\t\t\t={C437}m\n")
    p.add_run(f"Total height with Pile Cap\t\t=Lp\t\t\t\t\t={isp.len_pile_cap_trans}m\n")
    p.add_run(f"L-B\t\t\t\t\t={isp.len_bb_abut_cap}-{isp.srug_width_form_level}\t\t\t\t={L_minus_B}m\n")

    

    p=document.add_paragraph()
    p.add_run(f"{var1}\n")
    run.bold = True
    p.add_run(f"calculation required for {D470}\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "Case-1")
    p=document.add_paragraph()
    p.add_run(f"Pressure at Top\t=[ (S + V ) / B ] Ka\t=({isp.dl_surcharge}+{isp.ll_surchage})/{isp.srug_width_form_level}x{ka_calculated}\t\t={pressure_top_case1:.3f}T/m²\n")
    p.add_run(f"Pressure at Bottom=[ (S + V ) / (B + H ) ] Ka\t=({isp.dl_surcharge}+{isp.ll_surchage})/({isp.srug_width_form_level}+{total_height_with_pile_cap})x{ka_calculated}={pressure_bottom_case1}T/m²\n")
    p.add_run(f"Surcharge Pressure at Bottom of Abutment\t\t\t\t\t={surcharge_pressure_bottom_abutment_case1}T/m²\n")
    p.add_run("Calculation for Bottom of Pile Cap :\n")
    p.add_run(f"P1\t\t\t={pressure_bottom_case1}x{D477}\t\t\t\t\t\t={p1_case1_case1}T/m\n")
    p.add_run(f"acting at\t\t={total_height_with_pile_cap}/2\t\t\t\t\t\t={acting_at_p1_case1_case1}m\n")
    p.add_run(f"P2\t\t\t={pressure_bottom_case1}x{D477}²x{ka_calculated}/(2x{isp.srug_width_form_level})\t\t\t\t={p2_case1_case1}T/m\n")
    p.add_run(f"acting at\t\t=2x{total_height_with_pile_cap}/3\t\t\t\t\t\t={acting_at_p2_case1_case1}m\n")
    p.add_run("Calculation for bottom of Abutment :\n")
    p.add_run(f"P1\t\t\t={surcharge_pressure_bottom_abutment_case1}x{abutment_height}\t\t\t\t\t\t={p1_case2_case1}T/m\n")
    p.add_run(f"acting at\t\t={abutment_height}/2\t\t\t\t\t\t={acting_at_p1_case2_case1}m\n")
    p.add_run(f"P2\t\t\t={surcharge_pressure_bottom_abutment_case1}x{abutment_height}²x{ka_calculated}/(2x{isp.srug_width_form_level})\t\t\t\t={p2_case2_case1}T/m\n")
    p.add_run(f"acting at\t\t=2x{abutment_height}/3\t\t\t\t\t\t={acting_at_p2_case2_case1}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "At Base of Abutment Wall")
    p=document.add_paragraph()
    p.add_run(f"Horizontal Force at Base of Abutment Wall =({p1_case2_case1}+{p2_case2_case1})x{isp.len_bb_abut_cap}\t\t={horizontal_force_base_abutment_wall_case1}T\n")
    p.add_run(f"Moment about Base of Abutment Wall =({p1_case2_case1}x{acting_at_p1_case2_case1}+{p2_case2_case1}x{acting_at_p2_case2_case1})x{isp.len_bb_abut_cap}\t={moment_base_abutment_wall_case1}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "At Base of Pile Cap")
    p=document.add_paragraph()
    p.add_run(f"Horizontal force on Pile Cap \t\t=({p1_case1_case1}+{p2_case1_case1})x{isp.len_bb_abut_cap}\t\t\t={horizontal_force_pile_cap_case1}T\n")
    p.add_run(f"Total Moment about Base of Pile Cap\t=({p1_case1_case1}x{acting_at_p1_case1_case1}+{p2_case1_case1}x{acting_at_p2_case1_case1})x{isp.len_bb_abut_cap}\t={total_moment_base_pile_cap_case1}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "Case-2")
    p=document.add_paragraph()
    p.add_run(f"Pressure at Top\t\t=[ (S + V ) / B ] Ka=({isp.dl_surcharge}+{isp.ll_surchage})/{isp.srug_width_form_level}x{ka_calculated}\t={pressure_top_case1:.3f}T/m²\n")
    p.add_run(f"Pressure at Bottom\t=[ (S + V ) / (B + H ) ] Ka=(({isp.ll_surchage}+{isp.dl_surcharge})/{isp.len_bb_abut_cap})x{ka_calculated}\t={pressure_bottom_case2}T/m²\n")
    p.add_run(f"Surcharge Pressure at Bottom of Abutment\t\t\t\t\t={surcharge_pressure_bottom_abutment_case2}T/m²\n")
    p.add_run("Calculation for Bottom of Pile Cap :\n")
    p.add_run(f"P1\t\t\t={C513}x({E510}+{D522})/2\t\t\t\t={p1_case1_case2}T/m\n")
    p.add_run(f"acting at\t\t={B515}-(({C513}/3)x(2x{D515}+{E510})/({D515}+{E510})\t={acting_at_p1_case1_case2}m\n")
    p.add_run(f"P2\t\t\t={D522}x({C516}+{C519:.3f})\t\t\t\t\t={p2_case1_case2}T/m\n")
    p.add_run(f"acting at\t\t={C519:.3f}/2\t\t\t\t\t={acting_at_p2_case1_case2}m\n")
    p.add_run("Calculation for bottom of Abutment :\n")
    p.add_run(f"P1\t\t\t={surcharge_pressure_bottom_abutment_case1}x{abutment_height}\t\t\t\t\t\t={p1_case2_case2}T/m\n")
    p.add_run(f"acting at\t\t={abutment_height}/2\t\t\t\t\t\t={acting_at_p1_case2_case2}m\n")
    p.add_run(f"P2\t\t\t={surcharge_pressure_bottom_abutment_case1}x{abutment_height}²x{ka_calculated}/(2x{isp.srug_width_form_level})\t\t\t\t={p2_case2_case2}T/m\n")
    p.add_run(f"acting at\t\t=2x{abutment_height}/3\t\t\t\t\t\t={acting_at_p2_case2_case2}m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "At Base of Abutment Wall")
    p=document.add_paragraph()
    p.add_run(f"Horizontal Force at Base of Abutment Wall =(({p1_case2_case2}+{p2_case2_case2})x{isp.len_bb_abut_cap}\t\t\t={horizontal_force_base_abutment_wall_case2}T\n")
    p.add_run(f"Moment about Base of Abutment Wall\t =({p1_case2_case2}x{acting_at_p1_case2_case2}+{p2_case2_case2}x{acting_at_p2_case2_case2})x{isp.len_bb_abut_cap}\t\t={moment_base_abutment_wall_case2}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "At Base of Pile Cap")
    p=document.add_paragraph()
    p.add_run(f"Horizontal force on Pile Cap \t\t\t=({p1_case1_case2}+{p2_case1_case2})x{isp.len_bb_abut_cap}\t\t={horizontal_force_pile_cap}T\n")
    p.add_run(f"Total Moment about Base of Pile Cap\t=({p1_case1_case2}x{acting_at_p1_case1_case2}+{p2_case1_case2}x{acting_at_p2_case1_case2:.3f})x{isp.len_bb_abut_cap}\t={total_moment_base_pile_cap}T-m\n")


    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "Final Result:")
    p=document.add_paragraph()
    p.add_run("At pile cap\n")
    p.add_run(f"P1\t\t\t\t\t\t\t\t\t\t={p1_final}\n")
    p.add_run(f"acting at\t\t\t\t\t\t\t\t\t={acting_at_p1_final}\n")
    p.add_run(f"P2\t\t\t\t\t\t\t\t\t\t={p2_final}\n")
    p.add_run(f"acting at: \t\t\t\t\t\t\t\t\t={acting_at_p2_final:.3f}\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "At Base of Abutment Wall")
    p=document.add_paragraph()
    p.add_run(f"Total Horizontal Force at Base of Abutment Wall=\t\t\t\t{total_horizontal_force_final}T\n")
    p.add_run(f"Moment about Base of Abutment Wall\t\t\t\t\t\t={moment_base_abutment_wall_final}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "At Base of Pile Cap")
    p=document.add_paragraph()
    p.add_run(f"Horizontal force on Pile Cap only\t\t\t\t\t\t={horizontal_force_pile_cap_final}T\n")
    p.add_run(f"Total Moment about Base of Pile Cap\t\t\t\t\t\t={total_moment_base_pile_cap_final}T-m\n")


    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "9.0 VERTICAL LOAD DUE TO EARTH")
    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "9.1 VERTICAL LOAD DUE TO BACKFILL ON PILE CAP")
    p=document.add_paragraph()
    p.add_run(f"Height of back fill behind abutment wall\t\t\t\t\t={height_backfill_abut_wall}m\n")
    p.add_run(f"Avg. height of back fill beyond Return Wall in Trans. Direction\t\t={height_backfill_abut_wall}m\n")
    p.add_run(f"Eff. width of outer cantilever Pile Cap loaded with Earthfill\t\t\t={eff_width_outer_cantilever}m\n")
    p.add_run(f"W\t\t=(2x{eff_width_outer_cantilever}+{isp.len_bb_abut_cap}-2x{H83})x{F65}x{D431}x{gumma_soil_deg}\t\t\t\t={W}T\n")
    p.add_run(f"Eccentricity w.r.t. CG of Pile Group\t\t\t\t\t\t={eccen_CG_pile}m\n")
    p.add_run(f"Longitudinal Moment about CG of Pile Group={W} x {eccen_CG_pile}\t={longitudinal_moment_CG_pile_1}T-m\n")

    p=document.add_paragraph()
    DocxHelper.add_minor_heading(document, "9.2 VERTICAL LOAD DUE TO FRONT EARTHFILL")
    p=document.add_paragraph()
    p.add_run(f"Spilling Length in front of Abutment\t\t\t\t\t\t={spelling_length_front_abut}m\n")
    p.add_run(f"Height of Spilling Earth\t\t\t=({isp.ht_abut} + {isp.dep_bb_abut_cap})/2\t\t\t={height_spiling_earth}m\n")
    p.add_run(f"Vertical Load Due to Front Earthfill\t\t={spelling_length_front_abut}x{isp.len_pile_cap_trans}x{height_spiling_earth}x{gumma_soil_deg}\t\t={vertical_load_front_earthfill}T\n")
    p.add_run(f"Eccentricity w.r.t. CG of Pile Group e2\t\t\t\t\t\t={eccen_CG_pile_e2}m\n")
    p.add_run(f"Longitudinal Moment about CG of Pile Group\t={vertical_load_front_earthfill}x{eccen_CG_pile_e2}\t\t\t={longitudinal_moment_CG_pile_2}T-m\n")


    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.0 SEISMIC FORCE")
    # p=document.add_paragraph()
    # p.add_run("(Note : Please refer Seismic code for earthquake resistant design of railway bridge)\n")
    # p.add_run(f"Design Horizontal Seismic Coefficient αh for long. direction ={isp.I_factor_sstr}x{isp.Sa_g_90}x{isp.Z_2r}={}\n")
    # p.add_run(f"Design Horizontal Seismic Coefficient αh for trans. direction ={isp.Z_2r}x{isp.Sa_g_107}x{isp.I_factor_sstr}={}\n")
    # p.add_run(f"Design Vertical Seismic Coefficient αv=(2/3)x{}={}\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.1 ON SUPER STRUCTURE DEAD LOAD")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Longitudinal direction")
    # p=document.add_paragraph()
    # p.add_run("(Note : Seismic Force will act at Top of Bearings)\n")
    # p.add_run(f"Horizontal Seismic Force for {isp.span_between_cc_exp_joint} (c/c Bearing)  Span ={}x{rec_abut}ELx={}T\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment{isp.top_bed_block}+{isp.height_pedestral}+{isp.depth_bearing}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap{isp.top_bed_block}+{isp.height_pedestral}+{isp.depth_bearing}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Base of Abutment{}x{}MLx={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap{}x{}MLy={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Transverse direction")
    # p=document.add_paragraph()
    # p.add_run("(Note : Seismic Force will act at CG of Superstructure)\n")
    # p.add_run(f"Horizontal Seismic Force for {isp.span_between_cc_exp_joint} (c/c Bearing)  Span ={}x{rec_abut}ELy={}T\n")
    # p.add_run(f"For {isp.span_between_cc_exp_joint} m (c/c Bearing) Superstructure span CG Level ={isp.top_bed_block}+{isp.depth_bearing}+{isp.height_pedestral}+{isp.struc_depth_girder}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}MLy={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLy={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.2 ON SUPER IMPOSED DEAD LOAD (SIDL)")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Longitudinal direction")
    # p=document.add_paragraph()
    # p.add_run("(Note : Seismic Force will act at Top of Bearings)")
    # p.add_run(f"Horizontal Seismic Force for {isp.span_between_cc_exp_joint} (c/c Bearing)  Span ={}x{sidl_rec}ELx={}T\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={isp.top_bed_block}+{isp.height_pedestral}+{isp.depth_bearing}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={isp.top_bed_block}+{isp.height_pedestral}+{isp.depth_bearing}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}MLx={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLx={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Transverse direction")
    # p=document.add_paragraph()
    # p.add_run("(Note : Seismic Force will act at Rail level)")
    # p.add_run(f"Horizontal Seismic Force for  (c/c Bearing)  Span ={}x{sidl_rec}ELy={}T\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={isp.prop_rail_lev}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={isp.prop_rail_lev}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}MLy={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLy={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.3 ON ABUTMENT CAP")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "[a] Dirt Wall")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Longitudinal direction")
    # p=document.ad_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{dl_dirt_wall}ELx={}T\n")
    # p.add_run(f"Distance of C.G. of Dirt Wall From B/O of Dirt Wall={isp.ht_dirt_wall}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={isp.top_bed_block}+{}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={isp.top_bed_block}+{}-{isp.bot_pile_cap_lev}={}m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Transverse direction")
    # p=document.ad_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{dl_dirt_wall}ELy={}T\n")
    # p.add_run(f"Distance of C.G. of Dirt Wall From B/O of Dirt Wall={isp.ht_dirt_wall}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={isp.top_bed_block}+{}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={isp.top_bed_block}+{}-{isp.bot_pile_cap_lev}={}m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "[b] Abutment cap")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Longitudinal direction")
    # p=document.ad_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{dl_abut_cap}ELx={}T\n")
    # p.add_run(f"Distance of C.G. of Abutment cap From B/O of Abutment cap={isp.ht_abut}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={isp.top_abut_lev}+{}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={isp.top_abut_lev}+{}-{isp.bot_pile_cap_lev}={}m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Transverse direction")
    # p=document.ad_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{dl_abut_cap}ELy={}T\n")
    # p.add_run(f"Distance of C.G. of Abutment cap From B/O of Abutment cap={isp.ht_abut}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={isp.top_abut_lev}+{}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={isp.top_abut_lev}+{}-{isp.bot_pile_cap_lev}={}m\n")


    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "[c] Pedestals")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Longitudinal direction")
    # p=document.ad_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{self_weight_pedestal}ELx={}T\n")
    # p.add_run(f"Distance of C.G. From top of Abutment cap={isp.height_pedestral}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={isp.top_bed_block}+{}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={isp.top_bed_block}+{}-{isp.bot_pile_cap_lev}={}m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Transverse direction")
    # p=document.ad_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{self_weight_pedestal}ELy={}T\n")
    # p.add_run(f"Distance of C.G. From top of Abutment cap={isp.height_pedestral}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={isp.top_bed_block}+{}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={isp.top_bed_block}+{}-{isp.bot_pile_cap_lev}={}m\n")

    # p=document.add_paragraph()
    # p.add_run(f"Total Horizontal Load Due to Abutment Cap Components in long. direction{}+{}+{}ELx={}T\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}+{}x{}+{}x{}MLx={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}+{}x{}+{}x{}MLx={}T-m\n")
    # p.add_run(f"Total Horizontal Load Due to Abutment Cap Components in trans. direction={}+{}+{}ELy={}T\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}+{}x{}+{}x{}MLy={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}+{}x{}+{}x{}MLy={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.4 ON ABUTMENT WALL")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Longitudinal Direction")
    # p=document.add_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{dead_load_abut_shaft}ELx={}T\n")
    # p.add_run(f"Level of C. G. of Abutment (RL)={isp.top_abut_lev}+{isp.top_pile_cap}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t.  Abutment Base={}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t to Bottom of Pile Cap={}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}MLx={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLx={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Transverse Direction")
    # p=document.add_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{dead_load_abut_shaft}ELy={}T\n")
    # p.add_run(f"Level of C. G. of Abutment (RL)={isp.top_abut_lev}+{isp.top_pile_cap}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t.  Abutment Base={}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t to Bottom of Pile Cap={}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}MLy={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLy={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.5 ON SQUARE RETURN")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Longitudinal Direction")
    # p=document.add_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{weight_of_two_square_return}ELx={}T\n")
    # p.add_run(f"Level of C. G. of Square return (RL)={isp.prop_rail_form_level}+{isp.top_pile_cap}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t.  Abutment Base={}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t to Bottom of Pile Cap={}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}MLx={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLx={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Transverse Direction")
    # p=document.add_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{dead_load_abut_shaft}ELy={}T\n")
    # p.add_run(f"Level of C. G. of Square return (RL)={isp.top_abut_lev}+{isp.top_pile_cap}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t.  Abutment Base={}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t to Bottom of Pile Cap={}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}MLy={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLy={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.7 ON PILE CAP")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Longitudinal Direction")
    # p=document.add_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{weight_of_pile_cap}ELx={}T\n")
    # p.add_run(f"Level of C. G. of Pile Cap (RL)={isp.bot_pile_cap_lev}+{isp.top_pile_cap}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t to Bottom of Pile Cap={}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLx={}T-m\n")`

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "Transverse Direction")
    # p=document.add_paragraph()
    # p.add_run(f"Horizontal Seismic Force={}x{weight_of_pile_cap}ELy={}T\n")
    # p.add_run(f"Level of C. G. of Pile Cap (RL)={isp.bot_pile_cap_lev}+{isp.top_pile_cap}/2={}m\n")
    # p.add_run(f"Lever Arm w.r.t to Bottom of Pile Cap={}-{isp.bot_pile_cap_lev}={}m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLy={}T-m\n")`

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.8 SUMMARY OF SEISMIC FORCES DUE TO DEAD LOADS")
    # p=document.add_paragraph()
    # p.add_run(f"Total Longitudinal Seismic Force on Abutment due to Dead Loads\t\tELx = {}+{}+{}+{}={}T\n")
    # p.add_run(f"Total Longitudinal Seismic Force on Pile Cap due to Dead Loads\t\tELx = {}+{}+{}+{}={}T\n")
    # p.add_run(f"Total Longitudinal Moment about Base of Abutment due to Dead Loads\t\tMLx = {}+{}+{}+{}={}T-m\n")
    # p.add_run(f"Total Longitudinal Moment about Bottom of Pile Cap due to Dead Loads\t\tMLx = {}+{}+{}+{}+{}+{}+{}={}T-m\n")
    # p.add_run(f"Total Transverse Seismic Force on Abutment due to Dead Loads\t\tELy = {}+{}+{}+{}={}T\n")
    # p.add_run(f"Total Transverse Seismic Force on Pile Cap due to Dead Loads\t\tELy = {}+{}+{}+{}={}T\n")
    # p.add_run(f"Total Transverse Moment about Base of Abutment due to Dead Loads\t\tMLy = {}+{}+{}+{}={}T-m\n")
    # p.add_run(f"Total Transverse Moment about Bottom of Pile Cap due to Dead Loads\t\tMLy = {}+{}+{}+{}+{}+{}+{}={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.9 ON 50% LIVE LOAD IN TRANSVERSE DIRECTION")
    # p=document.add_paragraph()
    # p.add_run("(Note : Refer clause 2.12.6, IRS:Bridge Rules)\n")
    # p.add_run(f"Point of application of the force={isp.prop_rail_lev}={isp.prop_rail_lev}m\n")
    # p.add_run(f"Lever Arm w.r.t. Base of Abutment={}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Lever Arm w.r.t. Bottom of Pile Cap={}-{isp.bot_pile_cap_lev}m\n")
    # p.add_run("[a] When single track at edge loaded (Type A)\n")
    # p.add_run(f"Horizontal Seismic Force=[{live_load_reac_abut_318}x(1+{cda})]x0.50x{}\t\tELy={}T\n")
    # p.add_run(f"Moment about Base of Abutment={}x{}\t\tMLy={}T-m\n")
    # p.add_run(f"Moment about Bottom of Pile Cap={}x{}MLy={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.10 SEISMIC FORCES IN VERTICAL DIRECTION DUE TO DEAD LOADS")
    # p=document.add_paragraph()
    # p.add_run(f"Seismic Force on Abutment due to Dead Loads in Vertical Direction\t\tELz={}x{}/{}={}T\n")
    # p.add_run(f"Seismic Force on Pile Cap due to Dead Loads in Vertical Direction\t\tELz={}x{}/{}={}T\n")
    # p.add_run(f"Longitudinal Eccentricity of Reaction w.r.t. C/L of Abutment, eL1={long_eccen_K116}m\n")
    # p.add_run(f"Longitudinal Eccentricity of Reaction w.r.t. Pile Cap CG, eL2={long_eccen_K117}m\n")
    # p.add_run(f"Longitudinal Moment due to DL about C/L of Abutment={}x{}={}T-m\n")
    # p.add_run(f"Longitudinal Moment due to DL about Pile Cap CG={}x{}={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "10.11 SEISMIC FORCES IN VERTICAL DIRECTION DUE TO LIVE LOADS")
    # p=document.add_paragraph()
    # p.add_run("[a] When single track at edge loaded (Type A)\n")
    # p.add_run(f"Seismic Force due to Live Load  in Vertical Direction\t\tELz={}x{}/{}={}T\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "11.0 DYNAMIC INCREMENT OF EARTH PRESSURE")
    # p=document.add_paragraph()
    # p.add_run("(Note : Please Refer Cl. 5.12.6 Of IRS:Substructure & Foundation Code )")
    # p.add_run(f"αh={isp.Z_factor_sstr}/2/({isp.reduction_factor_fou}x{isp.I_factor_sstr}x{isp.Sa_g_90})={}\n")
    # p.add_run(f"αv={}x2/3\n")
    # p.add_run(f"φ={isp.phi_soil}\n")
    # p.add_run(f"β={isp.alpha_soil}\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "For + ve αv")
    # p=document.add_paragraph()
    # p.add_run(f"λ=tan-1[αh / (1 + αv)]=ATAN({}/(1+{}) radians={})\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "For - ve αv")
    # p=document.add_paragraph()
    # p.add_run(f"λ=tan-1[αh / (1 - αv)]=ATAN({}/(1-{}) radians={})\n")
    # p.add_run("Active Earth Pressure Coefficient\n")
    # p.add_run(f"Ca = (((1 + αv) x cos2(φ-α-λ))/(cosλ x cos2α x cos(δ + α + λ))) x [1 / (1 + √((sin(φ + δ) x sin(φ - i - λ)) / (cos(δ + α + λ) x cos(α - i))]2\n")
    # p.add_run("Co-efficient of dynamic increment\n")
    # p.add_run(f"Ca=max({}, {})={}\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "11.1 DYNAMIC INCREMENT DUE TO ACTIVE EARTH PRESSURE OF BACKFILL")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "At Base of Abutment Wall")
    # p=document.add_paragraph()
    # p.add_run(f"Increment in Force=[({}-{ka_calculated})/{ka_calculated}]x{total_force_abutment_base}={}T\n")
    # p.add_run(f"Lever Arm w.r.t. Abutment Base={D431}/2.0={}m\n")
    # p.add_run(f"Increment in Moment about Abutment Base={}x{}={}T-m\n")


    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "At Base of Pile Cap")
    # p=document.add_paragraph()
    # p.add_run(f"Increment in Force=[({}-{ka_calculated})/{ka_calculated}]x{total_force_bottom_pile_cap}\tELx={}T\n")
    # p.add_run(f"Lever Arm w.r.t. Pile Cap Bottom={C432}/2.0={}m\n")
    # p.add_run(f"Increment in Moment about Pile Cap Bottom=\tMLx={total_moment_bottom_pile_cap}x{}/{total_force_bottom_pile_cap}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "11.w DYNAMIC INCREMENT DUE TO ACTIVE EARTH PRESSURE OF SURCHARGE")
    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "At Abutment Base")
    # p=document.add_paragraph()
    # p.add_run(f"Increment in Force=[({}-{ka_calculated})/{ka_calculated}]x{total_horizontal_force_final}={}T\n")
    # p.add_run(f"Lever Arm w.r.t. Abutment Base= 0.66x{D431}={}m\n")
    # p.add_run(f"Increment in Moment about Abutment Base= {}x{}={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "At Base of Pile Cap")
    # p=document.add_paragraph()
    # p.add_run(f"Increment in Force=[({}-{ka_calculated})/{ka_calculated}]x{horizontal_force_pile_cap_final}\tELx={}T\n")
    # p.add_run(f"Lever Arm w.r.t. Pile Cap Bottom=0.66x{C432}={}m\n")
    # p.add_run(f"Increment in Moment about Pile Cap Bottom={}x{}\tMLx={}T-m\n")

    # p=document.add_paragraph()
    # DocxHelper.add_minor_heading(document, "11.3 Buoyancy Effect (B)")
    # p=document.add_paragraph()
    # p.add_run(f"Abutment shaft under water in HFL condition ={isp.HFL}-{isp.top_pile_cap}={}m\n")
    # p.add_run(f"Pile cap under water in HFL condition = {}m\n")
    # p.add_run(f"Uplift due to Pile Cap . = -{isp.len_pile_cap_trans}x{isp.len_pile_cap_long}x{}x{isp.gumma_water}={}T\n")
    # p.add_run(f"Uplift due to Abutment Shaft ={}x-{sec_area_abut_shaft}x{isp.gumma_water}={}T\n")












    document.add_page_break()
    document.save(output_path)

    print("\n\n\t\t*********Abutment and Foundation End**********\n\n")