import math

#DIMENSIONS OF CROSS SECTION - Y MEASURED FROM THE BOTTOM
t = 0 #thickness
ine = 0
h = 0
b_brid = 0
b_glue = 0
length = 0 #length of bridge
diaphragm_w = 0 # width of diaprham
num_rectangles = 0
E = 4000
m = 0.2
cross = "hi"

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
moment = 76300 #moment from BMD  ----CHANGE

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

force_bridge = 257 #shear force on bridge ----CHANGE - check is these right
force_glue = 257 #shear force on glue joints ----CHANGE

max_shear = 4 #max shear stress of matboard


#CASES OF SHEAR STRESS
t_cr_case1 = 0
t_cr_case2 = 0
t_cr_case3 = 0
t_cr_case4 = 0

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
    b_brid = 2.54
    b_glue = 10
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
    h = t+75
    b_brid = t*2
    b_glue = t*2
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
    h = t+75
    b_brid = t*2
    b_glue = t*2
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
    h = t+75
    b_brid = t*2
    b_glue = 10
    length = 1260 #length of bridge
    diaphragm_w = 30 # width of diaprham
    num_rectangles = 5
    cross = "Webb Without Horizontal"

    r1 = 100 #length of rectangle 1 (width is thickness)
    y1 = r1-t/2 #distance from centroid of rectangle to bottom
    h_v1 = "h" # rectangle is vertical or horizontal

    r2 = 100 #length of rectangle 1 (width is thickness)
    y2 = r2-t-t/2 #distance from centroid of rectangle to bottom
    h_v2 = "h" # rectangle is vertical or horizontal

    r3 = 96.19
    y3 = t+r3/2
    h_v3 = "v"

    r4 = 96.19
    y4 = t+r5/2
    h_v4 = "v"

    r5 = 90
    y5 = t/2
    h_v5 = "h"

    r6 = 10
    y6 = t + r3 - t + t/2
    h_v6 = "h"

    r7 = 10
    y7 = t + r3 - t + t/2
    h_v7 = "h"


    dimensions = [[r1, y1, h_v1], [r2, y2, h_v2], [r3, y3, h_v3], [r4, y4, h_v4], [r5, y5, h_v5], [r6, y6, h_v6], [r7, y7, h_v7]]


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
    h = t+75
    b_brid = t*2
    b_glue = 10
    length = 1260 #length of bridge
    diaphragm_w = 30 # width of diaprham
    num_rectangles = 4
    cross = "Webb Without Horizontal Without Bottom"

    r1 = 100 #length of rectangle 1 (width is thickness)
    y1 = r1-t/2 #distance from centroid of rectangle to bottom
    h_v1 = "h" # rectangle is vertical or horizontal

    r2 = 100 #length of rectangle 1 (width is thickness)
    y2 = r2-t-t/2 #distance from centroid of rectangle to bottom
    h_v2 = "h" # rectangle is vertical or horizontal

    r3 = 96.19
    y3 = t+r3/2
    h_v3 = "v"

    r4 = 96.19
    y4 = t+r4/2
    h_v4 = "v"

    r5 = 10
    y5 = t + r3 - t + t/2
    h_v5 = "h"

    r6 = 10
    y6 = t + r3 - t + t/2
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
            ine += (1/12)*t*(dimensions[i][0])**3 + (dimensions[i][0])*t*((dimensions[i][1]-y_bar)**2)
        #print(ine)
    print("Second Moment of Area: ", ine)


# FLEXURAL STRESSES
def stress_tension():
    global stress_tens
    global moment
    global y_bar
    global ine

    stress_tens = (moment*y_bar)/ine
    print("Bridge Flexural Tensile Stress: ", stress_tens)

def stress_compression():
    global stress_comp
    global moment
    global h
    global y_bar
    global ine

    stress_comp = (moment*(h-y_bar))/ine
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
    global r3
    global r7
    global r1

    Q_brid = 2*(y_bar-t)*t*((y_bar-t)/2)+r5*t*(y_bar-t/2)

    Q_glue_top = (r1*t)*(y_bar-t-t)

    Q_glue_bottom = (r5*t)*(y_bar-t)
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

    Q_brid = y_bar*t*y_bar/2*2

    Q_glue_top = (r1*t)*(y_bar-t-t)

    print("Q: ", Q_brid)
    print("Q Glue Top: ", Q_glue_top)



'''def Q_bridge():
    global y_bar
    global t
    global Q_brid
    global dimensions

    for i in range(0, num_rectangles): #[lenght, height of centroid above bottom, horixontal or verical]
        if dimensions[i][1] <= y_bar:
            if dimensions[i][2] == "v":
                Q_brid += (y_bar-dimensions[i][1])*(y_bar-(dimensions[i][1]-dimensions[i][0]/2))*t
                #y_bar-(y-r/2)
            else:
                Q_brid += (y_bar-dimensions[i][1])*(dimensions[i][0])*t

    print("Q For Bridge: ", Q_brid)

def Q_glue_joints():
    global y_bar
    global t
    global Q_glue_top
    global Q_glue_bottom

    
    for i in range (0, num_rectangles):
        if dimensions[i][1] > y_bar:
            Q_glue_top += (dimensions[i][0])*t*(dimensions[i][1]-y_bar)
    print("Q Glue Joints on Top: ", Q_glue_top)

    for i in range (0, num_rectangles):
        if dimensions[i][2] == "h" and dimensions[i][1] == t/2:
            Q_glue_bottom += (dimensions[i][0])*t*(y_bar-t/2)
    print("Q Glue Joints on Bottom: ", Q_glue_bottom)'''

    

def shear_bridge_calc():
    global t
    global y_bar
    global ine
    global shear_bridge
    global force_bridge
    global b_brid
    global Q_brid

    shear_bridge = (Q_brid*force_bridge)/(ine*b_brid)
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
    Q_glue_top = 4350

    shear_glue_top = (Q_glue_top*force_glue)/(ine*b_glue)
    print("Shear Force on Top Glue Joints: ", shear_glue_top)

    shear_glue_bottom = (Q_glue_bottom*force_glue)/(ine*b_glue)
    print("Shear Force on Top Glue Joints: ", shear_glue_bottom)

# BUCKLING OF THIN PLATES
def case_1():
    global E
    global m
    global t
    global t_cr_case1
    k = 4
    b = 80

    t_cr_case1 = (k*math.pi**2*E)/(12*(1-m**2))*(t/b)**2
    print("Shear stress for Case 1: ", t_cr_case1)
    

def case_2():
    global E
    global m
    global t
    global t_cr_case2
    k = 0.425
    b = 10

    t_cr_case2 = (k*math.pi**2*E)/(12*(1-m**2))*(t/b)**2
    print("Shear stress for Case 2: ", t_cr_case2)

def case_3(): #not complete no clue what to do
    global E
    global m
    global t
    global t_cr_case3
    k = 5
    b = 10

    t_cr_case3 = (k*math.pi**2*E)/(12*(1-m**2))*(t/b)**2
    
    print("Shear stress for Case 3: ", t_cr_case3)
    

def case_4():
    global E
    global m
    global t
    global t_cr_case4
    k = 5
    b = 10
    a = 210 #6 diaphragms

    t_cr_case4 = (k*math.pi**2*E)/(12*(1-m**2))*((t/b)**2 + (t/a)**2)
    print("Shear stress for Case 4: ", t_cr_case4)


# CALCULATES THE AMOUNT OF MATBOARD USED
def matboard_used():
    global dimensions

    matboard_used = 0

    for i in range(0, num_rectangles):
        matboard_used += dimensions[i][0]*length
    
    matboard_used += 6*77.46*80

    print("Amount of matboard used:", matboard_used)




if __name__ == "__main__":
    init_double_webbed_without_horizontal()
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
    print("FOS For Flexural Stresses")
    fos_tension()
    fos_compression()
    print("\n")


    print("Shear Forces:")
    if cross == "Web":
        Q_double_webbed()
    elif cross == "Webb Without Bottom":
        Q_double_webbed_wo_bot()
    elif cross == "Webb Without Horizontal":
        Q_double_webbed_wohor()
    elif cross == "Webb Without Horizontal Without Bottom":
        Q_double_webbed_wohor_wobot()
    shear_bridge_calc()
    shear_glue_calc()
    print("\n")
    '''
    print("Thin-Plate Buckling: ")
    case_1()
    case_2()
    case_3()
    case_4()
    print("\n")'''




    