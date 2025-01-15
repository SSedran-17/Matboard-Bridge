# Imports
import math
import numpy as np
import matplotlib.pyplot as plt

# Defining variables
#DIMENSIONS OF CROSS SECTION - Y MEASURED FROM THE BOTTOM
t = 0 #thickness
ine = 0
cross = "hi"
h = 0
b_brid = 0
b_glue = 0
length = 0 #length of bridge
diaphragm_w = 0 # width of diaprham
num_rectangles = 0
E = 4000
m = 0.2

r1 = 0 #length of rectangle 1 (width is thickness)
y1 = 0 #distance from centroid of rectangle to bottom
h_v1 = "h" # rectangle is vertical or horizontal

r2 = 0
y2 = 0
h_v2 = "v"

r3 = 0
y3 = 0
h_v3 = "h"

r4 = 0
y4 = 0
h_v4 = "h"

r5 = 0
y5 = 0
h_v5 = "v"

r6 = 0
y6 = 0
h_v6 = "v"

r7 = 0
y7 = 0
h_v7 = "v"

r8 = 0
y8 = 0
h_v8 = "v"

dimensions = []

#FLEXURAL STRESSES IN BRIDGE
moment = 0 #moment from BMD  ----CHANGE

#calculated stresses from our cross section
stress_tens = 0 
stress_comp = 0

max_stress_tens = 30 #Max tensile stress of matboard
max_stress_comp = 6 #Max compression stress of matboard

fos_tens = 0 #FOS for tension
fos_comp = 0 #FOS for compression

# SHEAR DATA
Q_brid = 0
Q_glue_top = 0
Q_glue_bottom = 0
Q_glue_hor = 0

shear_bridge = 0 #shear stress on bridge
shear_glue_top = 0 #shear stress on glue joints 
shear_glue_bottom = 0 #shear stress on glue joints 

force_bridge = 0 #shear force on bridge
force_glue = 0 #shear force on glue joints

max_shear = 4 #max shear stress of matboard

shear_glue_strength = 2 # material properties, strength of matboard

#CASES OF SHEAR STRESS
t_cr_case1 = 0
t_cr_case2 = 0
t_cr_case3 = 0
t_cr_case4 = 0

# Length of bridge
L = 1200
last_wheel = L + 176 + 164 + 176 + 164 + 176 + 52

# Load conditions
# Load 1 -> Locomotive at right hand side
# Load 2 -> Locomotive at left hand side
# Udl -> self weight
load0 = [400/6, 400/6, 400/6, 400/6, 400/6, 400/6]
load1 = [66.666666, 66.666666, 66.666666, 66.666666, 90, 90]
load2 = [90, 90, 66.666666, 66.666666, 66.666666, 66.666666]
load3 = [153.33333333/2, 153.33333333/2, 153.33333333/2, 153.33333333/2, 207/2, 207/2]
double = [x*2 for x in load0]
UDL = (0.75*9.8)/L
UDL = 0

# Where are the reaction forces?
Ly_pos = 0
Ry_pos = L

# Coordinates across the bridge
x = np.linspace(0, (L+1), 1200)

# Initial train positions
init = [-176-164-176-164-176, -176-164-176-164, -176-164-176, -176-164, -176, 0]

def init_design_0():
    global t
    global h
    global b_brid
    global b_glue
    global length
    global diaphragm_w
    global num_rectangles

    global r1
    global r2
    global r3
    global r4
    global r5
    global r6

    global y1
    global y2
    global y3
    global y4
    global y5
    global y6

    global dimensions

    
    #DIMENSIONS OF CROSS SECTION - Y MEASURED FROM THE BOTTOM
    t = 1.27 #thickness
    h = t+75
    b_brid = t*2
    b_glue = 11.27
    length = 1260 #length of bridge
    diaphragm_w = 30 # width of diaprham
    num_rectangles = 6

    r1 = 100 #length of rectangle 1 (width is thickness)
    y1 = 75.635 #distance from centroid of rectangle to bottom
    h_v1 = "h" # rectangle is vertical or horizontal

    r2 = 75-1.27
    y2 = (75-1.27)/2 + 1.27
    h_v2 = "v"

    r3 = 5
    y3 = 75-1.27 + 1.27/2
    h_v3 = "h"

    r4 = 5
    y4 = 75-1.27 + 1.27/2
    h_v4 = "h"

    r5 = 75-1.27
    y5 = (75-1.27)/2 + 1.27
    h_v5 = "v"

    r6 = 80
    y6 = 1.27/2
    h_v6 = "h"

    dimensions = [[r1, y1, h_v1], [r2, y2, h_v2], [r3, y3, h_v3], [r4, y4, h_v4], [r5, y5, h_v5], [r6, y6, h_v6]]

def init_double_webbed():
    global t
    global h
    global b_brid
    global b_glue
    global length
    global diaphragm_w
    global num_rectangles
    global cross

    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global r7

    global y1
    global y2
    global y3
    global y4
    global y5
    global y6
    global y7

    global dimensions

    
    #DIMENSIONS OF CROSS SECTION - Y MEASURED FROM THE BOTTOM
    t = 1.27 #thickness
    h = 100
    b_brid = t*2
    b_glue = 10
    length = 1260 #length of bridge
    diaphragm_w = 30 # width of diaprham
    num_rectangles = 7
    cross = "Web"

    r1 = 100 #length of rectangle 1 (width is thickness)
    y1 = r1-t/2 #distance from centroid of rectangle to bottom
    h_v1 = "h" # rectangle is vertical or horizontal

    r2 = 100 #length of rectangle 1 (width is thickness)
    y2 = r2-t-t/2 #distance from centroid of rectangle to bottom
    h_v2 = "h" # rectangle is vertical or horizontal

    r3 = 96.19
    y3 = t+r3/2
    h_v3 = "v"

    r4 = 77.46
    y4 = r3+t-20-t/2
    h_v4 = "h"

    r5 = 96.19
    y5 = t+r5/2
    h_v5 = "v"

    r6 = 77.46
    y6 = t+20+t/2
    h_v6 = "h"

    r7 = 90
    y7 = t/2
    h_v7 = "v"


    dimensions = [[r1, y1, h_v1], [r2, y2, h_v2], [r3, y3, h_v3], [r4, y4, h_v4], [r5, y5, h_v5], [r6, y6, h_v6], [r7, y7, h_v7]]

def init_double_web_wo_bot():
    global t
    global h
    global b_brid
    global b_glue
    global length
    global diaphragm_w
    global num_rectangles
    global cross

    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global r7

    global y1
    global y2
    global y3
    global y4
    global y5
    global y6
    global y7

    global dimensions

    
    #DIMENSIONS OF CROSS SECTION - Y MEASURED FROM THE BOTTOM
    t = 1.27 #thickness
    h = 100 # Total height
    b_brid = t*2
    b_glue = 10
    length = 1260 #length of bridge
    diaphragm_w = 30 # width of diaprham
    num_rectangles = 7
    cross = "Webb Without Bottom"

    r1 = 100 #length of rectangle 1 (width is thickness)
    y1 = r1-t/2 #distance from centroid of rectangle to bottom
    h_v1 = "h" # rectangle is vertical or horizontal

    r2 = 100 #length of rectangle 1 (width is thickness)
    y2 = r2-t-t/2 #distance from centroid of rectangle to bottom
    h_v2 = "h" # rectangle is vertical or horizontal

    r3 = 96.19
    y3 = t+r3/2
    h_v3 = "v"

    r4 = 77.46
    y4 = r3+t-20-t/2
    h_v4 = "h"

    r5 = 96.19
    y5 = t+r5/2
    h_v5 = "v"

    r6 = 77.46
    y6 = t+20+t/2
    h_v6 = "h"


    dimensions = [[r1, y1, h_v1], [r2, y2, h_v2], [r3, y3, h_v3], [r4, y4, h_v4], [r5, y5, h_v5], [r6, y6, h_v6]]

def init_double_webbed_without_horizontal():
    global t
    global h
    global b_brid
    global b_glue
    global length
    global diaphragm_w
    global num_rectangles
    global cross

    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global r7

    global y1
    global y2
    global y3
    global y4
    global y5
    global y6
    global y7

    global dimensions

    
    #DIMENSIONS OF CROSS SECTION - Y MEASURED FROM THE BOTTOM
    t = 1.27 #thickness
    h = 120
    b_brid = t*2
    b_glue = 5
    length = 1260 #length of bridge
    diaphragm_w = 30 # width of diaprham
    num_rectangles = 9
    cross = "Webb Without Horizontal"

    r1 = 105 #length of rectangle 1 (width is thickness)
    y1 = h-(t/2) #distance from centroid of rectangle to bottom
    h_v1 = "h" # rectangle is vertical or horizontal

    r2 = 105 #length of rectangle 1 (width is thickness)
    y2 = h-t-(t/2) #distance from centroid of rectangle to bottom
    h_v2 = "h" # rectangle is vertical or horizontal

    r3 = 120-(t*3)
    y3 = h - (t*2) - (r3/2)
    y3 = t+r3/2
    h_v3 = "v"

    r4 = 120-(t*3)
    y4 = h - (t*2) - (r4/2)
    h_v4 = "v"

    r5 = 80
    y5 = t/2
    h_v5 = "h"

    r6 = 5
    y6 = h - t*2 - t/2
    h_v6 = "h"

    r7 = 5
    y7 = h - t*2 - t/2
    h_v7 = "h"

    r8 = 5
    y8 = t + t/2
    h_v8 = "h"

    r9 = 5
    y9 = t + t/2
    h_v9 = "h"

    dimensions = [[r1, y1, h_v1], [r2, y2, h_v2], [r3, y3, h_v3], [r4, y4, h_v4], [r5, y5, h_v5], [r6, y6, h_v6], [r7, y7, h_v7], [r8, y8, h_v8], [r9, y9, h_v9]]

def init_double_webbed_wohor_without_bottom():
    global t
    global h
    global b_brid
    global b_glue
    global length
    global diaphragm_w
    global num_rectangles
    global cross

    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global r7

    global y1
    global y2
    global y3
    global y4
    global y5
    global y6
    global y7

    global dimensions

    
    #DIMENSIONS OF CROSS SECTION - Y MEASURED FROM THE BOTTOM
    t = 1.27 #thickness
    h = 100 
    b_brid = t*2
    b_glue = 10
    length = 1260 #length of bridge
    diaphragm_w = 62.46 # width of diaprham
    num_rectangles = 6
    cross = "Webb Without Horizontal Without Bottom"

    r1 = 100 #length of rectangle 1 (width is thickness)
    y1 = h-t/2 #distance from centroid of rectangle to bottom
    h_v1 = "h" # rectangle is vertical or horizontal

    r2 = 100 #length of rectangle 1 (width is thickness)
    y2 = h-t-t/2 #distance from centroid of rectangle to bottom
    h_v2 = "h" # rectangle is vertical or horizontal

    r3 = 100 - t*2
    y3 = h - t*2 - r3/2
    h_v3 = "v"

    r4 = 100 - t*2
    y4 = h - t*2 - r3/2
    h_v4 = "v"

    r5 = 5
    y5 = h - 2*t - t/2
    h_v5 = "h"

    r6 = 5
    y6 = h - 2*t - t/2
    h_v6 = "h"


    dimensions = [[r1, y1, h_v1], [r2, y2, h_v2], [r3, y3, h_v3], [r4, y4, h_v4], [r5, y5, h_v5], [r6, y6, h_v6]]

# Y-BAR
def create_y_bar():
    global y_bar
    global t
    global dimensions

    y_bar_numerator = 0
    y_bar_denominator = 0

    for i in range(0, num_rectangles):
        y_bar_numerator += dimensions[i][0]*dimensions[i][1]*t
        #print(y_bar_numerator)
        y_bar_denominator += dimensions[i][0]*t
        #print(y_bar_denominator)
    y_bar = y_bar_numerator/y_bar_denominator

    print("Y-bar: ", y_bar)

# SECOND MOMENT OF AREA
def create_ine():
    global y_bar
    global t
    global dimensions
    global ine


    for i in range(0, num_rectangles):
        if dimensions[i][2] == "h":
            ine += (1/12)*(dimensions[i][0])*(t**3) + (dimensions[i][0])*t*((dimensions[i][1]-y_bar)**2)

        else:
            ine += (1/12)*t*((dimensions[i][0])**3) + (dimensions[i][0])*t*((dimensions[i][1]-y_bar)**2)
          
        #print(ine)
    print("Second Moment of Area: ", ine)

# FLEXURAL STRESSES
def stress_tension():
    global stress_tens
    global moment
    global y_bar
    global ine

    stress_tens = (abs(moment)*y_bar)/ine
    print("Bridge Flexural Tensile Stress: ", stress_tens)

def stress_compression():
    global stress_comp
    global moment
    global h
    global y_bar
    global ine

    stress_comp = (abs(moment)*(h-y_bar))/ine
    print("Bridge Flexural Compressive Stress: ", stress_comp)

#FACTOR OF SAFETY
def fos_tension():
    global stress_tens
    global fos_tens
    global max_stress_tens

    fos_tens = max_stress_tens/stress_tens
    print("FOS Tension: ", fos_tens)

def fos_compression():
    global stress_comp
    global fos_comp
    global max_stress_comp

    fos_comp = max_stress_comp/stress_comp
    print("FOS Compression: ", fos_comp)

def fos_shear():
    global shear_bridge
    global max_shear

    fos_sh = max_shear/shear_bridge
    print("FOS Shear: ", fos_sh)

def fos_glue():
    global shear_glue_top
    global shear_glue_bottom
    global shear_glue_strength

    fos_g_top = shear_glue_strength/shear_glue_top
    fos_g_bot = shear_glue_strength/shear_glue_bottom
    print("FOS Shear Top Glue: ", fos_g_top)
    print("FOS Shear Bottom Glue: ", fos_g_bot)

def fos_buck_flex():
    global stress_comp
    global t_cr_case1
    global t_cr_case2
    global t_cr_case3

    fos_buck_flex1 = t_cr_case1/stress_comp
    fos_buck_flex2 = t_cr_case2/stress_comp
    fos_buck_flex3 = t_cr_case3/stress_comp
    print("FOS Flexural Buckling, Middle Flange: ", fos_buck_flex1)
    print("FOS Flexural Buckling, Overhangs: ", fos_buck_flex2)
    print("FOS Flexural Buckling, Web: ", fos_buck_flex3)
    
def fos_buck_shear():
    global shear_bridge
    global t_cr_case4

    fos_buck_shear = t_cr_case4/shear_bridge
    print("FOS Shear Buckling: ", fos_buck_shear)

# SHEAR CALCULATONS
def Q_double_webbed():
    global y_bar
    global t
    global Q_brid
    global Q_glue_top
    global Q_glue_bottom
    global Q_glue_hor
    global dimensions
    global r3
    global r6
    global r7
    global r1

    Q_brid = (y_bar-(r3/2+t))*(r3*t)*2+t*r6*(y_bar-(20+t+t/2))+t*r7*(y_bar-t/2)

    Q_glue_top = (r1*t)*(y_bar-t-t)

    Q_glue_bottom = (r7*t)*(y_bar-t)

    Q_glue_hor = (r4*t)*(y_bar-(20+t+t/2))

    print("Q: ", Q_brid)
    print("Q Glue Bottom: ", Q_glue_bottom)
    print("Q Glue Top: ", Q_glue_top)
    print("Q Glue Horizontals: ", Q_glue_hor)

def Q_double_webbed_wo_bot():
    global y_bar
    global t
    global Q_brid
    global Q_glue_top
    global Q_glue_bottom
    global dimensions
    global r3
    global r6
    global r1
    global Q_glue_hor

    Q_brid = (y_bar-(r3/2+t))*(r3*t)*2+t*r6*(y_bar-(20+t+t/2))

    Q_glue_top = (r1*t)*(y_bar-t-t)

    Q_glue_hor = (r4*t)*(y_bar-(20+t+t/2))

    print("Q: ", Q_brid)
    print("Q Glue Bottom: ", Q_glue_bottom)
    print("Q Glue Top: ", Q_glue_top)
    print("Q Glue Horizontals: ", Q_glue_hor)

def Q_double_webbed_wohor():
    global y_bar
    global t
    global Q_brid
    global Q_glue_top
    global Q_glue_bottom
    global dimensions
    global r5
    global r3
    global r7
    global r1

    Q_brid = 2*(y_bar-t)*t*(y_bar-((y_bar-t)/2))+r5*t*(y_bar-(t/2))

    Q_glue_top = (r1*t)*(h-y_bar-(t/2)) + (r2*t)*(h-y_bar-(t)-(t/2))

    Q_glue_bottom = (r5*t)*(y_bar-(t/2))

    # Q_brid = 14697.186

    # Q_glue_top = 11662.791

    # Q_glue_bottom = 7555.484

    print("Q: ", Q_brid)
    print("Q Glue Bottom: ", Q_glue_bottom)
    print("Q Glue Top: ", Q_glue_top)

def Q_double_webbed_wohor_wobot():
    global y_bar
    global t
    global Q_brid
    global Q_glue_top
    global Q_glue_bottom
    global dimensions
    global r3
    global r1

    Q_brid = y_bar*t*(y_bar/2)*2

    Q_glue_top = (r1*t)*(y_bar-t-t)

    print("Q: ", Q_brid)
    print("Q Glue Top: ", Q_glue_top)

def shear_bridge_calc():
    global t
    global y_bar
    global ine
    global shear_bridge
    global force_bridge
    global b_brid
    global Q_brid

    # Design 0
    #Q_brid = 6186.9

    shear_bridge = (Q_brid*abs(force_bridge))/(ine*b_brid)
    print("Shear Force on Bridge: ", shear_bridge)

def shear_glue_calc():
    global t
    global y_bar
    global ine
    global shear_glue_top
    global shear_glue_bottom
    global force_glue
    global b_glue
    global Q_glue_top
    global Q_glue_bottom

    # Design 0
    #Q_glue_top = 4353
    #Q_glue_bottom = 4353

    shear_glue_top = (Q_glue_top*abs(force_glue))/(ine*b_glue)
    print("Shear Force on Top Glue Joints: ", shear_glue_top)

    #shear_glue_bottom = (Q_glue_bottom*abs(force_glue))/(ine*b_glue)
    #print("Shear Force on Bottom Glue Joints: ", shear_glue_bottom)

# BUCKLING OF THIN PLATES
def case_1():
    global E
    global m
    global t
    global t_cr_case1
    k = 4

    # b for case 1 - how far apart are the webs?
    b = 65
    #b = 80

    t_cr_case1 = (k*math.pi**2*E)/(12*(1-m**2))*(t/b)**2
    print("Shear stress capacity for Case 1: ", t_cr_case1)
    
def case_2():
    global E
    global m
    global t
    global t_cr_case2

    k = 0.425
    b = 21.27
    #b = 10

    # b for case 2 - how long are the overhangs?

    t_cr_case2 = ((k*(math.pi**2)*E)/(12*(1-m**2)))*(t/b)**2
    print("Shear stress capacity for Case 2: ", t_cr_case2)

def case_3():
    global E
    global m
    global t
    global t_cr_case3
    global y_bar
    k = 6

    # b for case 3 - height - ybar
    #b = (120-t*3)/2
    b = 120-y_bar

    t_cr_case3 = (k*(math.pi**2)*E)/(12*(1-m**2))*(t/b)**2
    
    print("Shear stress capacity for Case 3: ", t_cr_case3)

def case_4():
    global E
    global m
    global t
    global t_cr_case4
    global h
    k = 5

    # h for case 4 - total height
    h = 120
    #h = 75+1.27
    a = 240 #6 diaphragms
    #a = 400

    t_cr_case4 = ((k*(math.pi**2)*E)/(12*(1-m**2)))*((t/h)**2 + (t/a)**2)
    print("Shear stress capacity for Case 4: ", t_cr_case4)

# CALCULATES THE AMOUNT OF MATBOARD USED
def matboard_used():
    global dimensions

    matboard_used = 0

    for i in range(0, num_rectangles):
        matboard_used += dimensions[i][0]*dimensions[i][1]*1.27
    
    matboard_used += 6*(77.46)*80*1.27

    print("Amount of matboard used:", matboard_used)

def sfd_bmd_calc(x1, ly_pos1, ly1, ry_pos1, ry1, distances1, loadd, udl1):
    '''This function calculates the sheer force and bending moment
    across the bridge, given a certain load condition and reaction
    forces.
    distances1 = position of the train's 6 sets of wheels
    loadd = weight of the train's 6 sets of wheels
    udl1 = self weight of the bridge'''

    # Initialize lists to store each SF and M value in
    sflist = []
    mlist = []

    for coord in x1:
        # For every point along the bridge...
        # Reset temporary variables (sf1, m1)
        # Which stores the SF and M for a 
        # specific point (coord) on the bridge

        sf1 = 0
        m1 = 0

        # Each if statement checks if the current
        # coordinate is farther than a given applied
        # force, be it the weight of the train
        # or reaction forces. Taken from LHS

        if coord >= ly_pos1:
            sf1 += ly1
            m1 += ly1*coord

        if coord >= ry_pos1:
            sf1 += ry1
            m1 += ry1*(coord-(ry_pos1-1))

        # Eg. is the current coordinate farther than the first
        # train wheel? If it is, add it to the current SF / M

        if coord >= distances1[0] and distances1[0] >= 0 and distances1[0] <= L:
            sf1 -= loadd[0]
            m1 -= loadd[0]*(coord-distances1[0])

        if coord >= distances1[1] and distances1[1] >= 0 and distances1[1] <= L:
            sf1 -= loadd[1]
            m1 -= loadd[1]*(coord-distances1[1])

        if coord >= distances1[2] and distances1[2] >= 0 and distances1[2] <= L:
            sf1 -= loadd[2]
            m1 -= loadd[2]*(coord-distances1[2])

        if coord >= distances1[3] and distances1[3] >= 0 and distances1[3] <= L:
            sf1 -= loadd[3]
            m1 -= loadd[3]*(coord-distances1[3])
        
        if coord >= distances1[4] and distances1[4] >= 0 and distances1[4] <= L:
            sf1 -= loadd[4]
            m1 -= loadd[4]*(coord-distances1[4])

        if coord >= distances1[5] and distances1[5] >= 0 and distances1[5] <= L:
            sf1 -= loadd[5]
            m1 -= loadd[5]*(coord-distances1[5])

        # Every point on the bridge is affected by the self weight
        # Albeit not by very much, but it is still accounted for

        m1 -= udl1*coord*(coord/2)
        sf1 -= udl1*coord

        # Add the SF / M at this point to the list of SFs / Ms

        sflist.append(sf1)
        mlist.append(m1)

    return sflist, mlist

def sfd_bmd_graph(x1, sf1, m1):

    # Graph the list of SF values or M values
    # Versus x (the current coordinate or position
    # on the bridge)

    plt.plot(x1, sf1)   
    plt.axvline(linewidth=1, color='r') 
    plt.axhline(linewidth=1, color='r')
    plt.title("Shear Force Diagram")
    plt.xlabel("Length (mm)")
    plt.ylabel("Force (N)")
    plt.show()

    plt.plot(x1, m1)
    plt.axvline(linewidth=1, color='r') 
    plt.axhline(linewidth=1, color='r')
    plt.title("Bending Moment Diagram")
    plt.xlabel("Length (mm)")
    plt.ylabel("Force (N*mm)")
    plt.show()

def sfd_bmd_envelope(x1, sf1, m1):
    max_shear = [max(sf1, key=abs), x1[sf1.index(max(sf1, key=abs))]]
    max_moment = [max(m1, key=abs), x1[m1.index(max(m1, key=abs))]]
    return max_shear, max_moment

def reaction_forces(distances1, udl1, loadd):
    shear = 0
    moment = 0

    for j in range(len(distances1)):
        if distances1[j] >= 0 and distances1[j] <= L:
            # Which of the train's wheels are on the bridge?
            moment += distances1[j]*loadd[j]
            shear += loadd[j]

    Ry1 = (1/L)*(udl1*L*(L/2) + moment)
    Ly1 = shear + udl1*L - Ry1

    return Ly1, Ry1

def iterate_positions(x1, ly_pos1, ry_pos1, init_distances, loadd, udl1, last_wheel1):
    front_of_train = []
    max_shear_positions = []
    max_shear_values = []
    max_moment_positions = []
    max_moment_values = []
    results = []

    for i in range(0, last_wheel1, 1):

        distances1 = [d + i for d in init_distances]

        # Reaction forces
        Ly1, Ry1 = reaction_forces(distances1, udl1, loadd)

        sfd1, bmd1 = sfd_bmd_calc(x1, ly_pos1, Ly1, ry_pos1, Ry1, distances1, loadd, udl1)

        # Envelope - where on the bridge do we find the max shear/moment?
        max_s, max_m = sfd_bmd_envelope(x1, sfd1, bmd1)

        # sfd_bmd_graph(x1, sfd1, bmd1)

        front_of_train.append(str(distances1[5]))
        max_shear_positions.append(max_s[1])
        max_shear_values.append(max_s[0])
        max_moment_positions.append(max_m[1])
        max_moment_values.append(max_m[0])

    shear_key = max_shear_values.index(max(max_shear_values, key=abs))
    moment_key = max_moment_values.index(max(max_moment_values, key=abs))

    max_max_shear = [front_of_train[shear_key], max_shear_positions[shear_key], 
                     max_shear_values[shear_key]]
    max_max_moment = [front_of_train[moment_key], max_moment_positions[moment_key], 
                      max_moment_values[moment_key]]

    results = [front_of_train, max_shear_positions, max_shear_values,
               max_moment_positions, max_moment_values, max_max_shear, max_max_moment]

    return results

def envelope_graph(x1, sheer_env, moment_env):
    plt.plot(x1, sheer_env)    
    plt.title("Shear Envelope")
    plt.xlabel("Distance along bridge (mm)")
    plt.ylabel("Max Force (N)")
    plt.axes()
    plt.show()

    plt.plot(x1, moment_env)
    plt.title("Moment Envelope")
    plt.xlabel("Distance Along Bridge (mm)")
    plt.ylabel("Max Force (N*mm)")
    plt.axes()
    plt.show()

if __name__ == "__main__":

    # Calculate shear and moment forces
    results = iterate_positions(x, Ly_pos, Ry_pos, init, load0, UDL, last_wheel)

    # MAX SHEAR VALUE
    force_bridge = results[5][2]
    force_glue = results[5][2]
    shear = results[5][2]
    moment = results[4][1028]

    #init_design_0()
    #init_double_webbed_without_horizontal()
    init_double_webbed_wohor_without_bottom()
    print("\n")
    print("General Material Properties: ")
    create_y_bar()
    create_ine()
    matboard_used()
    print("\n")

    print("Flexural Stress Data:")
    stress_tension()
    stress_compression()
    print("\n")

    # --------------------
    print("Shear Forces:")
    if cross == "Web":
        Q_double_webbed()
    elif cross == "Webb Without Bottom":
        Q_double_webbed_wo_bot()
    elif cross == "Webb Without Horizontal":
        Q_double_webbed_wohor()
    elif cross == "Webb Without Horizontal Without Bottom":
        Q_double_webbed_wohor()
    shear_bridge_calc()
    shear_glue_calc()
    print("\n")

    print("Thin-Plate Buckling: ")
    case_1()
    case_2()
    case_3()
    case_4()
    print("\n")

    print("FOS for Shear Stresses")
    fos_shear()
    fos_glue()
    print("\n")
    print("FOS For Flexural Stresses")
    fos_tension()
    fos_compression()
    print("\n")
    print("FOS for Thin-Plate Buckling")
    # Case 2
    fos_buck_flex()
    # Case 4
    fos_buck_shear()

