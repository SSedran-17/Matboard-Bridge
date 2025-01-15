import math

#TO DO
'''
- FUNCTION TO CALCULATE AMOUNT MATBOARD USED
- CHECK UNITS
- CHECK CODE
'''

#EXCEPT FOR THINGS I HAVE EXPLICITILY LABELED WITH " ----CHANGE" THE CODE WILL CHANGE THE VARIABLES WHOSE VALUES ARE EQUAL TO ZERO

#DIMENSIONS AS GLOBAL VARIABLES - Y MEASURED FROM THE BOTTOM
y_bar = 0 # y-bar
i_m_o_a = 0 # I - second moment of area
t = 1.27 #thickness
h = 1.27+80+1.27*2 #total height
length = 1260 #length of bridge
diaphragm_w = 30 # width of diaprham
E = 4000
m = 0.2

r1 = 100 #length of rectangle 1 (width is thickness)
y1 = 1.27+80+1.27+1.27/2 #distance from centroid of rectangle to bottom
h_v = "h" # rectangle is vertical or horizontal

r2 = 100
y2 = 1.27+80+1.27/2
h_v = "h"

r3 = 10
y3 = 1.27+80-1.27/2
h_v = "h"

r4 = 10
y4 = 1.27+80-1.27/2
h_v = "h"

r5 = 78.73
y5 = 1.27+78.73/2
h_v = "v"

r6 = 80
y6 = 1.27+80/2
h_v = "v"

r7 = 78.73
y7 = 1.27+78.73/2
h_v = "v"

r8 = 90
y8 = 1.27/2
h_v = "h"

Q_shear = (y_bar-(r5/2 + t))*2*(r5/2)*t + (y_bar-t/2)*t*r8 + (y_bar-(r6/2 + t))*(r6/2)*t
Q_glue = r1*t*2*(t+r6+2*t-y_bar-t)

dimensions = [[r1, y1, h_v], [r2, y2, h_v], [r3, y3, h_v], [r4, y4, h_v], [r5, y5, h_v], [r6, y6, h_v], [r7, y7, h_v], [r8, y8, h_v]]

moment = 20 #moment from BMD  ----CHANGE

#calculated stresses from our cross section
stress_tens = 0 
stress_comp = 0

max_stress_tens = 30 #Max tensile stress of matboard
max_stress_comp = 6 #Max compression stress of matboard

fos_tens = 0 #FOS for tension
fos_comp = 0 #FOS for compression

shear_bridge = 0 #shear stress on bridge
shear_glue = 0 #shear stress on glue joints 

force_bridge = 20 #shear force on bridge ----CHANGE
force_glue = 10 #shear force on glue joints ----CHANGE

max_shear = 4 #max shear stress of matboard

fos_shear = 0

#shear stress for cases
t_cr_case1 = 0
t_cr_case2 = 0
t_cr_case3 = 0
t_cr_case4 = 0



#Y-BAR, SECOND MOMENT OF AREA, FLEXURAL STRESSES
def create_y_bar():
    global y_bar
    global t
    global dimensions

    y_bar_numerator = 0
    y_bar_denominator = 0

    for i in range(0, len(dimensions)):
        y_bar_numerator += dimensions[i][0]*dimensions[i][1]*t
        y_bar_denominator += dimensions[i][0]*t
    y_bar = y_bar_numerator/y_bar_denominator

def create_i_m_o_a():
    global y_bar
    global t
    global dimensions
    global i_m_o_a

    for i in range(0, len(dimensions)):
        if dimensions[i][2] == "h":
            i_m_o_a += (1/12)*(dimensions[i][0])*(t**3) + (dimensions[i][0])*t*((dimensions[i][1]-y_bar)**2)
        else:
            i_m_o_a += (1/12)*t*(dimensions[i][0])**3 + (dimensions[i][0])*t*((dimensions[i][1]-y_bar)**2)


def stress_tension():
    global stress_tens
    global moment
    global h
    global y_bar
    global i_m_o_a

    stress_tens = (moment*y_bar)/i_m_o_a

def stress_compression():
    global stress_comp
    global moment
    global h
    global y_bar
    global i_m_o_a

    stress_comp = (moment*(h-y_bar))/i_m_o_a


#FACTOR OF SAFETY
def fos_tension():
    global stress_tens
    global fos_tens
    global max_stress_tens

    fos_tens = max_stress_tens/stress_tens

def fos_compression():
    global stress_comp
    global fos_comp
    global max_stress_comp

    fos_comp = max_stress_comp/stress_comp


# SHEAR CALCULATONS
def shear_bridge_calc():
    global t
    global y_bar
    global i_m_o_a
    global shear_bridge
    global force_bridge
    global Q_shear
    b = 90 #width?
    V = force_bridge

    shear_bridge = (Q_shear*V)/(i_m_o_a*b)

def shear_fos_bridge():
    global fos_shear
    global max_shear
    global shear_bridge

    fos_shear = max_shear/shear_bridge

def shear_glue_joints():
    global t
    global y_bar
    global i_m_o_a
    global shear_glue
    global force_glue
    global Q_glue
    b = 10 # width?
    V = force_glue

    shear_bridge = (Q_glue*V)/(i_m_o_a*b)



# BUCKLING OF THIN PLATES
'''
def case_1():
    global E
    global m
    global t
    global t_cr_case1
    k = 4
    b = 80

    t_cr_case1 = (k*math.pi**2*E)/(12(1-m**2))*(t*2/b)**2

def case_2():
    global E
    global m
    global t
    global t_cr_case2
    k = 0.425
    b = 10

    t_cr_case2 = (k*math.pi**2*E)/(12(1-m**2))*(t/b)**2

def case_3(): #not complete no clue what to do
    global E
    global m
    global t
    global t_cr_case3
    k = 0.425
    b = 10

    t_cr_case3 = (k*math.pi**2*E)/(12(1-m**2))*(t/b)**2

def case_4():
    global E
    global m
    global t
    global t_cr_case4
    k = 5
    b = 10
    a = 210 #6 diaphragms

    t_cr_case4 = (k*math.pi**2*E)/(12(1-m**2))*((t/b)**2 + (t/a)**2)
'''

# CALCULATES THE AMOUNT OF MATBOARD USED
def matboard_used():
    global dimensions

    matboard_used = 0

    for i in range(0, len(dimensions)):
        matboard_used += dimensions[i][0]*dimensions[i][1]
    
    matboard_used += 6*77.46*80

    print("Amount of matboard used:", matboard_used)


if __name__ == "__main__":
    print("helllo")
    matboard_used()
    create_y_bar()
    create_i_m_o_a()
    stress_tension()
    stress_compression()
    fos_tension()
    fos_compression()
    shear_bridge_calc()
    shear_fos_bridge()
    shear_glue_joints()
    #case_1()
    #case_2()
    #case_3()
    #case_4()

    print("Calculated tensile stress from our cross section: ", stress_tens)
    print("Calculated compressive stress from our cross section: ", stress_comp)
    print("FOS Tension: ", fos_tens)
    print("FOS Compression: ", fos_comp)
    print("Shear Stress on bridge", shear_bridge)
    print("Shear Stress on glue", shear_glue)
    print("FOS Shear", fos_shear)
    print("Shear stress for Case 1", t_cr_case1)
    print("Shear stress for Case 2", t_cr_case2)
    print("Shear stress for Case 3", t_cr_case3)
    print("Shear stress for Case 4", t_cr_case4)
    

