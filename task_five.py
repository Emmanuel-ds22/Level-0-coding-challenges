#Task 0.5


import math
def triangle_area(x,y,z):
 s = (x+y+z)/2
 area = math.sqrt(s*(s-x)*(s-y)*(s-z))
 print(area)
