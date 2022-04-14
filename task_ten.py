#Task 0.10

def common_characters(letter1,letter2):
 for i in range(len(letter1)):
  if letter1[i] in letter2:
   print(letter1[i])
