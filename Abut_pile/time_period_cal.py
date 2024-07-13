import input_sheet as isp

import DocxHelper


def word_print(document,output_path):
   
    DocxHelper.add_main_heading(document, "Time period calculation")
    
    DocxHelper.add_sub_heading(document,"A. Input Data:")
    DocxHelper.add_minor_heading(document,"levels:")
    p = document.add_paragraph()
    p.add_run(f"Top of Bearing Level\t\t\t\t\t= {isp.bot_girder:.3f}  m\n")
    p.add_run(f"Top of Cap Level\t\t\t\t\t= {isp.top_cap_lev:.3f}  m\n")
    p.add_run(f"Bottom of Cap Level\t\t\t\t\t= {isp.top_abut_lev:.3f}  m\n")
    p.add_run(f"Top of Foundation Level\t\t\t\t= {isp.top_pile_cap:.3f}  m\n")
    p.add_run(f"Bottom of Foundation Level\t\t\t\t= {isp.bot_pile_cap_lev:.3f}  m")


    DocxHelper.add_minor_heading(document,"Geometric Details:")
    p = document.add_paragraph()
    p.add_run(f"H1\t\t\t\t\t\t\t\t= {isp.h1:.3f}  m\n")
    p.add_run(f"H2\t\t\t\t\t\t\t\t= {isp.h2:.3f}  m\n")
    p.add_run(f"H3\t\t\t\t\t\t\t\t= {isp.h3:.3f}  m\n")
    p.add_run(f"L\t\t\t\t\t\t\t\t= {isp.L:.3f}  m\n")
    p.add_run(f"Length of Abutment Cap\t\t\t\t\t= {isp.len_bb_abut_cap:.3f}  m\n")
    p.add_run(f"Width of Abutment Cap\t\t\t\t\t= {isp.wid_bb_abut_cap:.3f}  m\n")
    p.add_run(f"Depth of Abutment Cap at Tip\t\t\t\t\t= {isp.dep_bb_abut_cap:.3f}  m\n")
    p.add_run(f"Depth of Abutment Cap at Support\t\t\t\t= {isp.dep_bb_abut_cap:.3f}  m\n")
    p.add_run(f"Shape of Abutment (Rectangular/Circular)\t\t\t= {isp.shape_abut}\n")
    p.add_run(f"Length of Abutment\t\t\t\t\t\t= {isp.len_bb_abut_cap:.3f}  m\n")
    p.add_run(f"Thickness of Abutment\t\t\t\t\t= {isp.width_abutment_shaft:.3f}  m\n")
    p.add_run(f"Dia of Abutment\t\t\t\t\t\t= {isp.dia_abutment:.3f}  m\n")
    p.add_run(f"No of Piles\t\t\t\t\t\t\t= {round(isp.no_piles)}  \n")
    p.add_run(f"Dia of Pile\t\t\t\t\t\t\t= {isp.dia_pile:.3f}  m\n")
    p.add_run(f"Length of Pile Cap\t\t\t\t\t\t= {isp.len_pile_cap_trans:.3f}  m\n")
    p.add_run(f"Width of Abutment Cap\t\t\t\t\t= {isp.len_pile_cap_long:.3f}  m\n")
    p.add_run(f"Depth of Pile Cap\t\t\t\t\t\t= {isp.h3:.3f}  m\n")
    p.add_run(f"Allowable deflection\t\t\t\t\t\t= {isp.allowlable_deflection:.3f}  m\n")
    p.add_run(f"Lateral Pile Capacity\t\t\t\t\t\t= {isp.pile_capacity:.3f}  T")


    DocxHelper.add_minor_heading(document,"Bearing Details:")
    p = document.add_paragraph()
    p.add_run(f"No of Bearing on Abutment cap\t\t\t\t= {round(isp.no_bearing_abut_cap)}\n")
    p.add_run(f"Length of Bearing\t\t\t\t\t\t= {isp.len_bearing}  m\n")
    p.add_run(f"Width of Bearing\t\t\t\t\t\t= {isp.width_bearing}  m\n")
    p.add_run(f"Area of Bearing\t\t\t\t\t\t= {isp.area_bearing:.3f}  m^2\n")
    p.add_run(f"Thickness of bearing\t\t\t\t\t\t= {isp.thk_bearing}  m\n")
    p.add_run(f"No of Elastomer\t\t\t\t\t\t= {round(isp.no_elastomer)}\n")
    p.add_run(f"Thickness of Elastomer\t\t\t\t\t= {isp.thk_elastomer}  m\n")
    p.add_run(f"Total Thickness of Elastomer\t\t\t\t\t= {isp.tot_thk_elastomer:.3f}  m")
    
    DocxHelper.add_minor_heading(document,"Material Properties:")
    p = document.add_paragraph()
    p.add_run(f"Unit Weight of Concrete\t\t\t\t\t= {isp.unit_weight_concrete}  kN/cum\n")
    p.add_run(f"Concrete Grade\t\t\t\t\t\t= M{round(isp.fck)}\n")
    p.add_run(f"E=Modulus of Elasticity\t\t\t\t\t= {isp.Elasticity}  Mpa\n")
    p.add_run(f"G=Shear modulus of Elastomer\t\t\t\t= {isp.shear_modulus_elastomer}  Mpa")
    
    DocxHelper.add_sub_heading(document,"B. Diagram:")
    p = document.add_paragraph()
    #picture


    DocxHelper.add_sub_heading(document,"C. Calculation of Stiffness:")
    
    stiff_index = ["Bearing Stiffness","Pier Stiffness(Kx)","Pier Stiffness(Ky)","Pile Foundation Stiffness"] 
    stiff = [
             
            [isp.kxx[0]],
            [isp.kxx[1]],
            [isp.kxx[2]],
            [isp.kxx[3]]
    ]
    area_index = ["Bearing Area","Area of Abutment","Area of Pile"]
    area = [
             
            [isp.area[0]],
            [isp.area[1]],
            [isp.area[2]]
    ]


    DocxHelper.add_table_to_doc(document,stiff, headers=None, index= stiff_index)
    p = document.add_paragraph()
    DocxHelper.add_table_to_doc(document,area, headers=None, index= area_index)


    p = document.add_paragraph()
    p = document.add_paragraph()
    p.add_run(f"Equivalent longitudinal Stiffnes of the system (Kx)\t\t= {isp.kx_92:.3f}  kN/m\n")
    p.add_run(f"Equivalent Stiffnes of the system (Ky)\t\t\t\t= {isp.kx_95:.3f}  kN/m")

    DocxHelper.add_sub_heading(document,"D. Calculation of Mass:")
    p = document.add_paragraph()
    p.add_run(f"Load of Superstructure\t\t\t\t\t= {isp.load_sup:.3f}  T\n")
    p.add_run(f"Load  of SIDL\t\t\t\t\t\t\t= {isp.load_sidl:.3f}  T\n")
    p.add_run(f"Load of Live Load \t\t\t\t\t\t= {isp.load_live_load:.3f}  T\n")
    p.add_run(f"Load of Abutment Cap\t\t\t\t\t\t= {isp.load_abut_cap:.3f}  T\n")
    p.add_run(f"Load of Abutment\t\t\t\t\t\t= {isp.load_abut:.3f}  T\n")
    p.add_run(f"Lumped Mass along Longitudinal Diretion, ML\t\t= {isp.lumped_mass_long_dir_Ml:.3f}  kN\n")
    p.add_run(f"Lumped Mass along Longitudinal Diretion, MT\t\t= {isp.lumped_mass_long_dir_MT:.3f}  kN")


   
    DocxHelper.add_sub_heading(document,"E. Calculation of Natural time Period:")
    p = document.add_paragraph()
    run=p.add_run("T= 2*π*√(δ/g)")
    run.bold = True
    p.add_run(f"\n\nLongitudinal Deflection(ML.G/Kx) ,δL\t\t\t\t= {isp.delta_l:.3f}  m\n")
    p.add_run(f"Transverse Deflection(MT.G/Ky) ,δT\t\t\t\t= {isp.delta_T:.3f}  m\n")
    p.add_run(f"Natural Time period  along longitudinal direction ,Tx\t\t= {isp.T_x:.3f}  sec\n")
    p.add_run(f"Natural Time period  along transverse direction ,Ty\t\t= {isp.T_y:.3f}  sec")




    document.add_page_break()
    document.save(output_path)

    print("\n\n\t\t*********Time Period Sheet End**********\n\n")