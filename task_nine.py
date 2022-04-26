def vowels(string):
 srting = string.lower()
 string2 =[]
 for i in range(len(string)-1):
  if string[i] not in string[i+1:]:
   string2.append(string[i])
 string2.append(string[len(string)-1]) 
 
 for j in range(len(string2)-1):
  if string2[j] in "aeiou":
   print(string2[j],end =",")
   
 if string2[len(string2)-1] in "aeiou":
  print(string2[len(string2)-1])
