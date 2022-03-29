
import math

def cal():
    print(" Press 1 for Investments or 2 for Bonds")
    print("[1] Investment")
    print("[2] Bond")
cal()
option = int(input("Please select:  "))
while option != 0:
    if option == 1:
        print("Calculate Investment")
        principal = float(input('Principal amount: '))
        rate = float(input('Rate of interest: '))
        time = float(input('Time in number of years: '))
        Simple_interest = (principal*rate*time)/100
        Compound_interest = principal * ((1+rate/100)**time - 1)
        print("Simple interest is:", Simple_interest)
        print("Compound interest is:", Compound_interest)
        print("\n")
        cal()
        option = int(input("Please select: "))
    elif option == 2:
        print("Calculate Bond")
        pp = float(input("Number of payments per period"))
        wait = float(input("Number of years to maturity: "))
        interest = float(input ("input interest: "))
        fv = float(input("input house amount: "))
        c = fv * ((1+interest/100)**pp - 1)
        bondPrice = ((fv*c/pp*(1-(1+interest/pp)**(-pp*wait)))/(interest/pp)) + fv*(1+(interest/pp))**(-pp*wait)
        print(bondPrice)
        print(" ")
        cal()
        option = int(input("Please select: "))

