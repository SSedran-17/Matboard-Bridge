#DIMENSIONS AS GLOBAL VARIABLES - Y MEASURED FROM THE BOTTOM
ine = 0
t = 1.27 #thickness
h = t+75
b_brid = 80
b_glue = t*2
length = 1260 #length of bridge
diaphragm_w = 30 # width of diaprham
num_rectangles = 6

r1 = 100 #length of rectangle 1 (width is thickness)
y1 = 75.64 #distance from centroid of rectangle to bottom
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

    print("Y-bar:", y_bar)

# SECOND MOMENT OF AREA
def create_i_m_o_a():
    global y_bar
    global t
    global dimensions
    global ine

    #i_o_m_a = 0
    #y = 41.4
    for i in range(0, num_rectangles):
        if dimensions[i][2] == "h":
            ine += (1/12)*(dimensions[i][0])*(t**3) + (dimensions[i][0])*t*((dimensions[i][1]-y_bar)**2)
        else:
            ine += (1/12)*t*(dimensions[i][0])**3 + (dimensions[i][0])*t*((dimensions[i][1]-y_bar)**2)
        print(ine)
    print("Second Moment of Area", ine)

if __name__ == "__main__":
    create_y_bar()
    create_i_m_o_a()
    