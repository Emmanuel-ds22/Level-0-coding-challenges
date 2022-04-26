def common_characters(letter1,letter2):
 letter1 = letter1.lower()
 letter2 = letter2.lower()
 
 for i in range(len(letter1)-1):
  if letter1[i] in letter2:
   print(letter1[i],end=",")
   
 if letter1[len(letter1)-1] in letter2:  
   print(letter1[len(letter1)-1],end="")
   
