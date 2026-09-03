def convertIt(stdtime):
   ampm=(stdtime[-2:])
   hrs=int(stdtime[:2])
   
   print(stdtime)
   print(ampm)
   if ampm == "PM":
     print(12+hrs)
  
   
convertIt("04:00 PM")


