def hours_and_minutes(num): 
 minutes = num%60
 hours = num//60
 if minutes ==1:
  if hours == 1:
   print(str(hours)+"hour and "+ str(minutes)+"minute")
  else:
   print(str(hours)+"hours and "+ str(minutes)+"minute")
 else:
  if  hours == 1:
   print(str(hours)+"hour and "+ str(minutes)+"minutes")
  else:
   print(str(hours)+"hours and "+ str(minutes)+"minutes") 
