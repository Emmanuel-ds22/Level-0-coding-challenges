def hours_and_minutes(num): 
 minutes = num%60
 hours = num//60
 if minutes ==1:
  if hours == 1:
   print(f"{hours} hour and {minutes}minute")
  else:
   print(f"{hours} hours and {minutes}minute")
 else:
  if  hours == 1:
   print(f"{hours} hour and {minutes}minutes")
  else:
   print(f"{hours} hours and {minutes}minutes") 
