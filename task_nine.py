def vowels(string):
 string = string.lower()
 string2 =[]
 vowels = []
 for i in range(len(string)-1):
  if string[i] not in string[i+1:]:
   string2.append(string[i])
 string2.append(string[len(string)-1]) 
 
 for i in range(len(string2)):
  if string2[i] in "aeiou":
   vowels.append(string2[i])

 print("Vowels: ", end="")
 for j in range(len(vowels)-1):
   print(vowels[j],end =",")
 if len(vowels)>1:
   print(vowels[len(vowels)-1])
  
