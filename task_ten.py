def common_characters(letter1,letter2):
 letter1 = letter1.lower()
 letter2 = letter2.lower()
 common_letters = []
 common_letters2 = []
 
 for i in range(len(letter1)-1):
  if letter1[i] in letter2:
   common_letters.append(letter1[i])
  
 for i in range(len(common_letters)-1):
   if common_letters[i] not in common_letters[i+1:]:
    common_letters2.append(common_letters[i])
 common_letters2.append(common_letters[len(common_letters)-1]) 
   
 print("Common letters: ", end="")
 for j in range(len(common_letters2)-1):
   print(common_letters2[j],end =",")
   print(common_letters2[len(common_letters2)-1])
