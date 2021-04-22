intrest = float(input("enter the yearly interest rate:"))
amount = int(input("enter the monthly interest rate:"))
no_of_month_paid = int(input("enter a number:"))
print('Month\tCD Value')
count = 0
Month = 1
while count < no_of_month_paid:
    cd_value = amount + amount * (intrest / 1200)
    amount = cd_value
    count += 1
    roundvalue = round(cd_value, 2)
    print(Month, '\t', roundvalue)


# The monthly payment for a given loan pays the principal and the interest. The monthly interest is computed by multiplying the monthly interest rate and the balance(the remaining principal).
# The principal paid for the month is therefore the monthly payment minus the monthly interest. Write a program that lets the user enter the loan amount, number of years, and interest rate and displays the payment schedule for the
# loan.

# I still want to adjust somthing in this code