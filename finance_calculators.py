import math

# user instructions
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan. \n")

# user input of either 'investment' or 'bond'
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# bond options
if user_input.lower() == 'bond':
    house_value = int(input("Please enter the present value of the house: ")) #P
    house_interest = int(input("Please enter the interest rate: "))
    house_interest_percentage = (house_interest/100)/12 #1
    monthly_payment_plan = int(input("How many months do you plan to repay the bond? ")) #n
    bond_repayment = (house_interest_percentage*house_value)/(1 - (1 + house_interest_percentage)**(-monthly_payment_plan))
    bond_repayment_rounded2 = round(bond_repayment, 2)
    print("Your monthly bond repayments will be: ", +bond_repayment_rounded2)

# investment options
elif user_input.lower() == 'investment':
    investment = user_input.lower()
    deposit = int(input("How much are you depositing? ")) #P
    interest_rate = int(input("What is the interest rate? "))
    years_invested = int(input("How many years do you wish to invest? ")) #t

    # simple or compound interest options
    interest = input("Please choose your interest options from either 'simple' or 'compound': ")
    interest_percentage = (interest_rate/100) #r
    simple_interest = deposit *(1+interest_percentage*years_invested)
    compound_interest = deposit * math.pow((1+interest_percentage),years_invested)
    
    # simple option
    if interest.lower() == 'simple':
        print("Your total amount with the simple interest will be: ", +simple_interest)

    # compound option
    elif interest.lower() == 'compound':
        print("Your total amount with the compound interest will be: ", +compound_interest)

# error message displays user input and repeats user instructions
else:
   print("You entered '" + user_input + "'. Please enter either 'investment' or 'bond' and check your spelling.")
# error message loops program?
