def fizz_buzz (x):
 
   
     for n in range(1,x+1):
         if (n % 3 ==0) and (n % 5 ==0):
             print('FizzBuz')
         else:
            if (n % 3 ==0):
               print('fizz')
            if (n % 5 ==0):
               print('buzz')
            else:
                 print(n)
        


        
fizz_buzz(15)
