import math
def triangle_area(side_x,side_y,side_z):
 semiperimeter = (side_x+side_y+side_z)/2
 area = math.sqrt(semiperimeter*(semiperimeter-side_x)*(semiperimeter-side_y)*(semiperimeter-side_z))
 return area
