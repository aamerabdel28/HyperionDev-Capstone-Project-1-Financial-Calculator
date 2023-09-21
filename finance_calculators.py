import math


def user_input(message): #method to be called at each variable of the interest calculations to check if they are numbers. If they are not, print error message
    while True:
        user_input = input(message)
        try:
            user_input = float(user_input)
            return user_input
        except:
            print("Please enter a valid number")

print ("This program allows you to access two financial calculators to help you calculate interest for:\n")
print ("""1) investment - to calculate the amount of interest you'll earn on your investment
2) bond - to calculate the amount you'll have to pay on a home loan\n""")


while True:

    select_calc = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))

    if select_calc.lower() == "investment": #converting input to lowercase and doing a lowercase string comparison to make input case insensitive
        money = user_input("\nPlease enter the amount of money you are depositing in pounds: ")
        inv_rate = user_input("Please enter the interest rate in percentage form: ")
        inv_rate = inv_rate/100 #dividing interest percentage by 100 to represent it in decimal form for future calculation
        time = user_input("Please enter the number of years you will invest for: ")

        while True: #nested while loop to repeat interest type prompt if input is neither 'simple' or 'compound'
            interest = str(input("Please enter the type of interest ('simple' or 'compound'): "))
            if interest.lower() == "simple":
                total_earned = money*(1+(inv_rate)*time) 
                total_earned = '{0:.2f}'.format(total_earned) #formatting total amount earned to 2 decimal places
                print(f"\nIn {time} years you will have earned: £{total_earned}")
                break
            elif interest.lower() == "compound":
                total_earned = money*math.pow((1+(inv_rate)),time)
                total_earned = '{0:.2f}'.format(total_earned)
                print(f"\nIn {time} years you will have earned: £{total_earned}")
                break
            else: 
                print("You have entered an invalid input.")      
        break

    elif select_calc.lower() == "bond":
        present_value = user_input("\nPlease enter the present value of your house: ")
        bond_rate = user_input("Please enter the interest rate in percentage form: ")
        bond_rate = bond_rate/100
        monthly_BR = bond_rate/12 #dividing yearly interest rate by 12 to obtain monthly interest rate
        repay_time = user_input("Please enter the amount of time in months you plan to take to repay the bond: ")
        repayment = (monthly_BR*present_value)/(1-(1+monthly_BR)**(-repay_time))
        repayment = '{0:.2f}'.format(repayment)
        print(f"\nAmount you will have to repay per month: £{repayment}")
        break
    else: 
        print("You have entered an invalid input.")