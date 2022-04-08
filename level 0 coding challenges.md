# Task 0.1
 x = 0
 y = 1

 print(x)
 print(y)

 x = x + 3
 y = y + x

print(x)
print(y)

#Task 0.2
x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + ( 1 * 2 )
a = 1 + 1 * 2 / 2
b = (1 + 1 * 2 ) /  2

print(x)
print(y)
print(z)
print(a)
print(b)

#Task 0.3

def hello(name):
print("hello"+name)

#Task 0.4

def even_or_odd(int x):

print(x + 1)

#Task 0.5

def triangle_area(x,y,z):

s = 0.5 *(x+y+z)

area = sqrt(s*(s-x)*(s-y)*(s-z))
return(area)

#Task 0.6

def maximum(a,b,c):

if a>b:
  if a>c:
   print(a)

   else:

   print(c)

else:

 if b>c:
  print(b)
  else:
  print(c)


#Task 0.7

def celsius_to_fahrenheit(num):
fahrenheit = num*(9/5) + 32
 print(fahrenheit)

#Task 0.8

def hours_and_minutes: 
hours = num%60
minutes = num//60

#Task 0.9

def Vowels(string)
for i in range(len(string)):
 if string[i] in "aeou":
  pirnt(string[1])


Task 0.10

def common_characters(letter1,letter2) :

for i in range(len(letter1)):
 if letter1[1] in letter2:
   print(letter1[1])