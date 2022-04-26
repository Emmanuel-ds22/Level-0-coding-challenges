def triangle_area(side_x,side_y,side_z):
 semiperimeter = (side_x+side_y+side_z)/2
 area_squared = semiperimeter*(semiperimeter-side_x)*(semiperimeter-side_y)*(semiperimeter-side_z)
 area = area_squared**0.5
 return area
