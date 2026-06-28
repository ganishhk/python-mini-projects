# Salary Tax Estimator (Basic Version)

def tax_estimater(salary):
   if salary<=250000: # no tax for lower salary 
       return "no tax"
   elif salary>250000 and salary<=500000:
       tax=(salary*5)/100
       return f"5% :your tax amount is ={tax:.2f}"
   elif salary>500000 and salary<=1000000:
       tax=(salary*20)/100
       return f"20% :your tax amount is ={tax:.2f}"
   else:
       tax=(salary*30)/100
       return f"30% :your tax amount is ={tax:.2f}"
   
salary=float(input("enter your yearly salary amount :"))
print(tax_estimater(salary))