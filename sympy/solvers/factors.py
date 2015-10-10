def print_factors(x):
   

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)


num = int(raw_input("Enter a number: "))

print_factors(num)

#Notes:this code works to find out factors of a number and then print it
