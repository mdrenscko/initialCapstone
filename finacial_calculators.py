import math
A = 0 #total amount once the interest has been applied
repayment = 0 #The amount that a person will have to be repaid on a home loan each month

selection = input("Select a finacial product: (investment or bond): ")
if selection == "investment":
   P = float(input("deposit: ")) 
   r = float(input("interest rate: "))   
   t = float(input("years of investing: "))
   interest = input("Select interest: (simple or compound): ")
   if interest == "simple":
      A = P*(1+r*t)
      print(A)
   elif interest == "compound":
      A =  P * math.pow((1+r),t)
      print(A)
if selection == "bond":
   P = float(input("present value of the house: "))
   i = float(input("monthly interest rate: "))
   n = float(input("number of months to repay: "))
   repayment = (i * P)/(1 - (1 + i)**(-n))
   print(repayment)

 

