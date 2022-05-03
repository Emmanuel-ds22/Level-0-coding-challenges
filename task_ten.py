def common_characters(letter1,letter2):
 letter1 = letter1.lower()
 letter2 = letter2.lower()
 common_letters = []
 
 for i in range(len(letter1)-1):
  if letter1[i] in letter2:
   common_letters.append(letter1[i])
   
 print("Common letters: ", end="")
 for j in range(len(common_letters)-1):
   print(common_letters[j],end =",")
 if len(common_letters)>0:
   print(common_letters[len(common_letters)-1])
  
