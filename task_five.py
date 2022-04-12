#Task 0.5

def triangle_area(x,y,z):

s = 0.5 *(x+y+z)

area = sqrt(s*(s-x)*(s-y)*(s-z))
return(area)