#Task 0.5

def triangle_area(x,y,z):
	x = int(x)
	y = int(y)
	z = int(z)
	
s = (x+y+z)/2

area = sqrt(s*(s-x)*(s-y)*(s-z))
return(area)
