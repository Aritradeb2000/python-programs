import DocxHelper
import abut_foundation as af
import input_sheet as isp
import math

#C5
dl = 1
#C6
sidl = 1.2
#C7
ll = 0.5
#c8
water_curr = 1
#C9
earth_pres = 1
#D13
vert_load = 1469.42
#D14
long_moment = -585.79
#D15
trans_moment = 18.4318
#D16
hl = 202.223
#D17
ht = 0.00
#D18
P_min = 110.42
#D19
hor_load_pile = 13.4815
#B21
m = 47.05
#B22
p = 110.42
#B23
m1 = 8.00
#B24
d = 120
#D26
main_bar_dia = 32
#D27
dist_bar_dia = 12
#D28
clea_cover = 75
#D29
sp_bar = 32
#E31
fck = 35
#E32
sigma_co = 10.5
#E33
flex_comp_stress = 17.5
#E34
mod_elas_conc = 29580
#E35
tens_Flex_comb_bend = 240
#E36
tens_shear = 200
#E37
sigma_sc = 205
#C39
deff = 93
#C40
perimeter = math.pi*deff
#B41
Provide = 32
#D41
D41 = 190
#B42
no = 16
#D42
layers = 2
#B43
ast = 257.2288
#D43
D43 = 2.28
#D44
D44 = 65.2389
#B45
x_divided_d = 0.5437
#B46
a = 0.38
#B47
b = 0.43
#B48
c = 0.15
#G49
dist_CG_centre_circle = 22.5806
#G50
eff_area_seg = 6244.67
#G51
eff_momt_iner = 1934821
#G52
trans_area_steel = 1800.6
#G53
eff_tot_area = 8045.27
#B55
e_prime = 17.52683
#B56
e_minus_e_prime = 25.08344
#B57
i_effe = 4594112
#D58
dist_NA_geff = 22.765
#E59
comp_to = 22.7657
#D61
comp_str_conc_1 = 13.7249
#F61
comp_str_conc_2 = 25.6065
#B62
B62 = comp_str_conc_1 + comp_str_conc_2
#D62
D62=B62/10
#E62
E62 = 17.5
#D63
D63 = 110.745
#F63
F63 = D63/10
#F64
F64 = 375











def word_print(document, output_path):
     DocxHelper.add_main_heading(document, "Serviceabilty Check of Pile for A1")
     p=document.add_paragraph()
     DocxHelper.add_main_heading(document, "Case - II Normal Load Case, Live Load Type - A with Water Current and Buoyancy")
     p=document.add_paragraph()
     DocxHelper.add_minor_heading(document, "nonseismic Case")
     p=document.add_paragraph()
     p.add_run("Load Case \t\t\t\tLoad Factor\n")
     p.add_run(f"Dead Load\t\t\t\t={dl}\n")
     p.add_run(f"SIDL\t\t\t\t\t={sidl}\n")
     p.add_run(f"Live Load\t\t\t\t={ll}\n")
     p.add_run(f"Water Current\t\t\t\t={water_curr}\n")
     p.add_run(f"Earthpressure\t\t\t\t={earth_pres}\n")
     

     p=document.add_paragraph()
     p.add_run(f"Vertical Load\t\t\t\t={vert_load}T\n")
     p.add_run(f"Longitudinal Moment (ML)\t\t={long_moment}T-m\n")
     p.add_run(f"Transverse Moment (MT\t\t{trans_moment}T-m\n")
     p.add_run(f"Horizontal Load (HL)\t\t\t={hl}T\n")
     p.add_run(f"Horizontal Load (HT)\t\t\t={ht}T\n")
     run=p.add_run(f"PMIN = P/n - ML/ZL- MT/ZT")
     run.bold=True
     p.add_run(f"\t\t\t\t{P_min}T\n")
     p.add_run(f"Horizontal Load per Pile \t\t={hor_load_pile}T\n")
     
     p=document.add_paragraph()
     p.add_run(f"M  {m}Ton-m  Grade of Concrete   M35\n")
     p.add_run(f"P{p}TonGrade of steelFe500D\n")
     p.add_run(f"m  {m1}\n")
     p.add_run(f"D  {d}cm\n")
     p.add_run("case: seismic\n")
     p.add_run(f"Main bar dia\t\t\t\t={main_bar_dia}mm\n")
     p.add_run(f"Distributor bar dia\t\t\t={dist_bar_dia}mm\n")
     p.add_run(f"Clea Cover\t\t\t\t={clea_cover}mm\n")
     p.add_run(f"Spacer bar\t\t\t\t={sp_bar}mm\n")

     p=document.add_paragraph()
     DocxHelper.add_minor_heading(document, "Allowable Stresses:")
     p=document.add_paragraph()
     p.add_run(f"Charecteristic Compressive strength,fck\t={fck}MPa\n")
     p.add_run(f"Direct Compressive Stress ,σco\t\t={sigma_co}Mpa\n")
     p.add_run(f"Flexural compressive Stress\t\t\t={flex_comp_stress}Mpa\n")
     p.add_run(f"Modulus of Elasticity of concrete,e\t\t={mod_elas_conc}Mpa\n")
     p.add_run(f"Tension in flexure & Combined Bending ,σst\t={tens_Flex_comb_bend}Mpa\n")
     p.add_run(f"Tension in Shear\t\t\t\t={tens_shear}Mpa\n")
     p.add_run(f"Direct Compression ,σsc\t\t\t={sigma_sc}Mpa\n")

     p=document.add_paragraph()
     p.add_run(f"Deff\t\t\t\t\t\t={deff}cm\n")
     p.add_run(f"Perimeter\t\t\t\t\t={perimeter:.3f}cm\n")
     p.add_run(f"Provide\t{Provide}mm@\t\t\t{D41}mm/cc\n")
     p.add_run(f"No.\t\t{no} in\t\t\t{layers} layers\n")
     p.add_run(f"Ast=\t\t{ast}sq.cm\t\t{D43}%\t\tOK\n")
     p.add_run(f"Assume NA at a depth of     {D44}cm from extreme compression fibre.\n")
     p.add_run(f"x/D\t\t\t\t\t\t={x_divided_d}\n")
     p.add_run(f"A\t\t\t\t\t\t={a}\n")
     p.add_run(f"B\t\t\t\t\t\t={b}\n")
     p.add_run(f"C\t\t\t\t\t\t={c}\n")
     p.add_run(f"Distance of CG of effective segment from the centre of circle\t\t={dist_CG_centre_circle}cm\n")
     p.add_run(f"Effective area of segment\t\t\t\t\t\t={eff_area_seg}sq.cm\n")
     p.add_run(f"Effective moment of inertia of segment about its own centroid\t={eff_momt_iner}cm⁴\n")
     p.add_run(f"Transfomed are due to area of steel\t\t\t\t\t={trans_area_steel}sq.cm\n")
     p.add_run(f"Effective total  area\t\t\t\t\t\t\t={eff_tot_area}sq.cm\n")
     p.add_run(f"Distance of CGeff of effective segment from the physical centroid of whole section is=\n")
     p.add_run(f"e'\t\t\t\t\t\t={e_prime}cm\n")
     p.add_run(f"e-e'\t\t\t\t\t\t={e_minus_e_prime}cm\n")
     p.add_run(f"Ieff\t\t\t\t\t\t={i_effe}cm⁴\n")
     p.add_run(f"Distance of NA below CGeff\t\t\t={dist_NA_geff}cm\n")
     p.add_run(f"Compared to\t\t{comp_to}cm \t\tHence OK\n")
     run=p.add_run(f"Compressive stress in concrete={comp_str_conc_1}+{comp_str_conc_2}={B62:.3f}Kg/sqcm\t{D62:.3f}Mpa<{E62} \t\t\t\t\t\t\tHence OK\n")
     run.bold=True
     run=p.add_run(f"Tensile stress in steel={D63}Kg/sqcm \t{F63}Mpa<{F64} \t\tHence OK")
     run.bold=True



     document.add_page_break()
     document.save(output_path)