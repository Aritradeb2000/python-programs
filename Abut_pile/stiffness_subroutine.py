
import math as m 
pi = 3.141592653

def pier_rect_stiffness(E,lx, ly, h) :
    #E = elasticity
    #lx = thickness of abutment 
    #ly = length of abutment
    #h = height abutment(I11)
    area = lx*ly
    E = E*1000
    
    Ixx = (lx**3*ly)/12
    Iyy = (ly**3*lx)/12
    
    cr_Ixx = Ixx*0.75
    cr_Iyy = Iyy*0.75
   
    
    k_xx = 3*E*cr_Ixx/h**3
    k_yy = 3*E*cr_Iyy/h**3
    
    
    #weight = area*h*gama
    
    return k_xx, k_yy, area
    
def pier_circular_stiffness(E,d, h) :
    #E = elasticity
    #d=dia of abutment
    #h = height abutment(I11)
    area = (m.pi*d**2)/4 
    E = E*1000
    
    Ixx = m.pi*d**4/64
    Iyy = Ixx
    
    cr_Ixx = Ixx*0.75
    cr_Iyy = Iyy*0.75
          
    
    
    k_xx = 3*E*cr_Ixx/h**3
    k_yy = 3*E*cr_Iyy/h**3
    
    #weight = area*h*gama
    
    return k_xx, k_yy, area


def bearing_stiffness(n,a,SE,tot_thik):
    #SE =Shear modulus of Elastomer 
    # n = no of bearing
    # a = area of bearing
    # tot_thik = total thickness of elastomer
    
    K_xx = n*a*10**6*SE/(tot_thik*1000)
    area = a

    return K_xx,area

def found_stiffness(n,deflection,pile_capacity,d,l,depth) :
    # n = number of piles
    # deflection = allowable deflection
    # pile_capacity = Capacity of pile
    #d = dia of pile
    #num_pile = no of piles
    #l = length of pile cap
    #depth = depth of pile cap
  
    k_xx = n*pile_capacity*10/deflection
    pile_area = n * ((m.pi*d**2)/4 )
    pile_cap_area = l*depth
    area_foundation = pile_area + pile_cap_area
    return k_xx, area_foundation






# def well_stiffness(E, gama, D, thk, heff ) :
#     Ixx = (pi*D**4/64) - (pi*(D-2*thk)**4/64)
#     Ixx = .75*Ixx 
    
#     k_xx = 3*E*Ixx/heff**3
#     k_yy = k_xx
#     A = pi*D**2/4
#     W = A*gama*.75
#     return k_xx, k_yy, A, W

# def bearing_head(E, gama,numb, lx, ly, ht):
#     Ixx = lx*ly**3
#     Iyy = ly*lx**3
#     Ixx = Ixx* numb 
#     Iyy = Iyy * numb 
#     k_xx = 3*E*Ixx/ht**3
#     k_yy = 3*E*Iyy/ht**3
#     A = lx * ly * numb 
#     W = A * ht * gama
    
#     return k_xx, k_yy, A, W
    
    
def sa_by_g_calculator(T, soil_value):
    
    if(soil_value == 1):
        if(T<.1): return 1 + 15*T
        elif(T>.1 and T<0.4): return 2.5
        elif(T>.4 and T < 4): return 1/T
        elif(T>4): return 0.25

    elif(soil_value == 2):
        if(T<.1): return 1 + 15*T
        elif(T>.1 and T<0.55): return 2.5
        elif(T>.55 and T < 4): return 1.36/T
        elif(T>4): return 0.34
        
    elif(soil_value == 3):
        if(T<.1): return 1 + 15*T
        elif(T>.1 and T<0.67): return 2.5
        elif(T>.67 and T < 4): return 1.67/T
        elif(T>4): return 0.42
    
    else:
        print("Invalid Soil_value Provided. Please provide 1-Rocky, 2-Stiff, 3-soft")
        return None

# sa_g = sa_by_g_calculator(0.3019, 'rocky'),
# print(f"\n\t Sa/g = {sa_g}")
def seismic_factors() :
    zone_no = int(input("Seismic Zone--2/3/4/5--->"))
    imp_factor = float(input("Importance Factor--->"))
    R = float(input("Response Reduction Factor--->"))
    
    # Calculation of Zone factor
    if zone_no == 5 :
        Z = 0.36
        
    elif(zone_no== 4) :
        Z = 0.24
    
    elif(zone_no == 3) :
        Z = 0.16
    
    elif(zone_no == 4) :
        Z = 0.10
    
    return Z, imp_factor, R

def calculate_resultant_stiffness(stiffness_list):
    if not stiffness_list:
        return 0
    inv_sum = sum(1/k for k in stiffness_list)
    return 1 / inv_sum if inv_sum else 0


    
               
               