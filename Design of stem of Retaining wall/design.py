#Design the stem of a retaining wall
import math

ht_wall = float(input("height of the wall: "))
stem_len = float(input("stem length: "))
angle_repose = int(input("angle of repose: "))
den_ret_earth = float(input("Density of Reatined Earth: "))
meter = float(input("Enter the meter value: "))
z=float(input("z: "))
b=float(input("b: "))
phi_bars_1 = float(input("phi bars: "))
cover = float(input("covers: "))
thickness_top = float(input("Enter the thickness at top: "))
sigma_st = float(input("σst: "))
phi_bars_2 = float(input("Phi bars: "))
distribution_steel = float(input("Distribution steel percentage: "))
d_2 = float(input("value of d: "))
pt=float(input("pt: "))
Tc=float(input("Tc: "))
T_bd = float(input("Tbd: "))
thickness_base = float(input("Thickness of base: "))
unit_weight_concrete=float(input("Unit weight of concrete: "))
mu = float(input("μ: "))


base = 0.4*ht_wall
toe = (1/4)*base
val=math.sin(math.radians(angle_repose))
var = (1-math.sin(math.radians(angle_repose)))/(1+math.sin(math.radians(angle_repose)))
pres_horizon = den_ret_earth * ht_wall **2 * var/2
bending_moment_base = pres_horizon * ht_wall/3
bending_moment_top = den_ret_earth * meter**2/2 * var * meter/3
Mr=z*b
M=pres_horizon*2*10**6
d=math.sqrt(M/Mr)
D=d+phi_bars_1/2+cover
thickness_stem_3m = thickness_top+((D-thickness_top)*meter/ht_wall)
d_required_thickness = math.sqrt((pres_horizon/4 * 10**6)/Mr)
D_required_thickness = d_required_thickness + phi_bars_1/2 + cover
A_st_1 = (pres_horizon*2*10**6)/(sigma_st*z*d)
bar_area_1 = 314
spacing_1 = bar_area_1*b/A_st_1
d_3m_below_top = thickness_stem_3m-phi_bars_1/2-cover
A_st_2=(pres_horizon/4*10**6)/(sigma_st*z*d_3m_below_top)
bar_area_2 = 78.54
spacing_2 = bar_area_2*b/A_st_2
D_2 = (D+thickness_top)/2
A_st_3 = (distribution_steel/100)*b*D_2
spacing_3 = (bar_area_2*b)/A_st_3
Tv = (pres_horizon*10**3)/(b*d_2)
Ld1 = (phi_bars_1 * sigma_st)/(4*T_bd)
Ld2 = (phi_bars_2*sigma_st)/(4*T_bd)
wt_wall_1 = (1/2)*0.285*ht_wall*unit_weight_concrete
wt_wall_2 = 0.2*ht_wall*unit_weight_concrete
wt_base = thickness_base*2.4*unit_weight_concrete
wt_soil = 1.315*ht_wall*den_ret_earth
wt_total = wt_wall_1+wt_wall_2+wt_base+wt_soil
moment_total = wt_wall_1*(toe+(2/3)*0.285)+wt_wall_2*(T_bd+0.285+0.2/2)+wt_base*(base/2)+wt_soil*(base-(1.315/2))
distance = moment_total/wt_total
overturn = (wt_total*distance)/(pres_horizon*ht_wall/3) 
sliding = mu*wt_total/pres_horizon


print(f"{'The height of the wall is':<40}: {ht_wall}m")
print(f"{'Assume width of the base to be':<40} 0.4H")
print(f"{'Base':<20} = {f'0.4x{ht_wall}':<20} = {base:.3f} m")
print("Assume the base ratio of 1:4")
print(f"Toe={base:.3f}x(1/4) = {toe:.3f} m")
print("3.Bending moment and thickness of stem")
print(f"Consider {stem_len} m length of stem")
print("Horizontal presure of earth on stem")
print("P = (WH²/2)x((1-sin∅)/(1+sin∅))")
print(f"Where (1-sin∅)/(1+sin∅) = (1-sin{angle_repose}⁰)/(1+sin{angle_repose}⁰) = (1-{val:.3f})/(1+{val:.3f})={var:.3f}")
print(f"P=(({den_ret_earth}x{ht_wall}²)/2)x{var:.3f} = {pres_horizon:.3f}kN")
print(f"Bending Moment at the base, i.e., {ht_wall}m below the top,")
print(f"M = PxH/3 = {pres_horizon:.3f}x{ht_wall}/3={bending_moment_base:.3f} kN-m")
print(f"Bending moment at {meter}m below the top.")
print(f"M=({den_ret_earth}x{meter}²/2)x{var:.3f}x({meter}/3)={bending_moment_top:.3f} kN-m")
print("Thickness of stem")
print("At base, equate Mr to M")
print(f"{z}bd² = {pres_horizon*2:.3f}x10⁶")
print(f"{z}x{b}xd² = {pres_horizon*2:.3f}x10⁶")
print(f"d={d:.3f}mm")
print(f"Assuming {phi_bars_1}mm ∅ bars and {cover} mm cover,")
print(f"D={d:.3f}+{phi_bars_1}/2+{cover}={D:.3f} mm")
print(f"Provide {thickness_top}mm thickness at the top. Dimensions of section are shown in fig 12.6.")
print(f"Thickness of stem available at {meter} m below the top,")
print(f"D={thickness_top}+(({D:.3f}-{thickness_top})x{meter})/{ht_wall}={thickness_stem_3m:.3f} mm")
print("Required Thickness")
print(f"{z:.3f}x{b:.3f}xd² = {pres_horizon/4:.3f}x10⁶")
print(f"d={d_required_thickness:.3f} mm")
print(f"D={d_required_thickness:.3f}+{phi_bars_1}/2+{cover}={D_required_thickness:.3f}mm<{thickness_stem_3m:.3f}(provided). O.K.")
print("4. Steel: Main Steel")
print(f"(a) {ht_wall}m below the top")
print(f"Ast = M/σstZ = ({pres_horizon*2:.3f}x10⁶)/({sigma_st:.3f}x{z:.3f}x{d:.3f})={A_st_1:.3f} mm²")
print(f"Providing {phi_bars_1}mm ∅ bars, area of one bar is {bar_area_1} mm.")
print(f"Spacing = {bar_area_1}x{b}/{A_st_1:.3f} = {spacing_1:.3f} mm c/c")
print(f"(b) 3m below the top")
print("Ast = M/σstZ")
print(f"Here d={thickness_stem_3m:.3f}-{phi_bars_1}/2-{cover}={d_3m_below_top:.3f} mm")
print(f"Ast=({pres_horizon/4:.3f}x10⁶)/({sigma_st:.3f}x{z}x{d_3m_below_top:.3f})={A_st_2:.3f} mm²")
print(f"Providing {phi_bars_2}mm ∅ bars, area of one bar is {bar_area_2} mm²")
print(f"Spacing = ({bar_area_2}x{b})/{A_st_2:.3f}={spacing_2:.3f} mm c/c.")
print(f"Distribution steel = {distribution_steel}% of Ag")
print(f"Ast=({distribution_steel}/100)xbD,")
print(f"Where D=({D:.3f}+{thickness_top:.3f})/2 = {D_2:.3f} mm")
print(f"=({distribution_steel:.3f}/100)x{b:.3f}x{D_2:.3f}")
print(f"={A_st_3:.3f}mm²")
print(f"Providing {phi_bars_2} mm ∅ bars, area of one bar is {bar_area_2} mm²")
print(f"Spacing = ({bar_area_2}x{b:.3f})/{A_st_3:.3f}={spacing_3:.3f} mm c/c.")
print("Check for shear")
print(f"V={pres_horizon:.3f}kN")
print(f"Tv = V/bd = ({pres_horizon:.3f}x10³)/({b}x{d_2:.3f}) = {Tv:.3f} N/mm²")
print(f"for concrete M15 and pt= {pt}")
print(f"Tc = {Tc}N/mm²> {Tv:.3f} N/mm²")
print(f"Hence no shear reinforcement is required.")
print("6.Development length")
print(f"(a) At the base of stem for {phi_bars_1} mm ∅ bars")
print("Ld = ∅σs/(4xTbd)")
print(f"Where ∅={phi_bars_1} mm")
print(f"σs = {sigma_st:.3f} N/mm²")
print(f"Tbd = {T_bd:.3f} N/mm²")
print (f"Ld = ({phi_bars_1}x{sigma_st})/(4x{T_bd}) = {Ld1:.3f} mm")
print(f"(b) At 3m below for the top 10mm, ∅ bars,")
print("Ld = ∅σs/(4xTbd)")
print(f"=({phi_bars_2}x{sigma_st})/(4x{T_bd})={Ld2:.3f} mm")
print("The steel with its development length is shown in fig 12.7")
print("Check for stability")
print(f"Assume thickness of the base as {thickness_base} m.")
print("referring to fig 12.8,")
print("Total vertical Loads")
print("weight of wall")
print(f"1: (1/2)x{0.285}x{ht_wall}x{unit_weight_concrete} = {wt_wall_1:.3f} kN")
print(f"2: {0.2}x{ht_wall}x{unit_weight_concrete} = {wt_wall_2:.3f} kN")
print("Weight of Base")
print(f"3: {thickness_base}x2.4x{unit_weight_concrete} = {wt_base:.3f} kN")
print("Weight of soil")
print(f"4: {1.315}x{ht_wall}x{den_ret_earth} = {wt_soil:.3f} kN")
print(f"Total = WT = {wt_total:.3f} kN")
print("Distance of total load WT from toe, T,")
print("Distance = (Σmoment/Σload)")
print(f"Σmoment = {wt_wall_1:.3f}x({toe:.3f}+(2/3)x{0.285})+{wt_wall_2:.3f}x({T_bd:.3f}+{0.285}+{0.2}/2)+{wt_base:.3f}*({base:.3f}/2)+{wt_soil:.3f}*({base:.3f}-({1.315}/2) = {moment_total:.3f} kN-m")
print(f"distance = {moment_total:.3f}/{wt_total:.3f}={distance:.3f}m")
print("factor of safety")
print("(i)for overturning")
if(overturn>distance):
    print(f"(WxX)/(PxH/3) = ({wt_total:.3f}*{distance:.3f})/({pres_horizon:.3f}x{ht_wall:.3f}/3) = {overturn:.3f}>{distance:.3f}. O.K.")
else:
    print(f"(WxX)/(PxH/3) = ({wt_total:.3f}*{distance:.3f})/({pres_horizon:.3f}x{ht_wall:.3f}/3) = {overturn:.3f}<{distance:.3f}.\n Therefore it is not safe against overturning.")


print("(ii)for sliding")
if(sliding>distance):
    print(f"μW/P = ({mu}x{wt_total:.3f}/{pres_horizon:.3f}={sliding:.3f}>{distance:.3f}. O.K.")
else:
    print(f"μW/P = ({mu}x{wt_total:.3f}/{pres_horizon:.3f}={sliding:.3f}<{distance:.3f}\n Therefore, it is not safe against sliding. The following improvements are suggested: (a) increase the base width or (b) provide suitable key.")


