#Suppose you have a certain amount of money in a savings
#account that earns compound monthly interest, and you want
#to calculate the amount that you will have after a specific number of
#months. The formula is as follows:
#F = P x (1 + i)^t
#F is the future value of the account after the specified time period.
#P is the present value of the account.
#i is the monthly interest rate.
#t is the number of months.


def main():

    #Enter 'P', the present value
    p = float(input('Please enter the present value of the account: $'))

    #Enter 'i', the monthly interest rate
    i = float(input('Please enter the monthly interest rate(%): '))

    #Enter 't', the number of months that the money will be left in the account
    t = float(input('Please enter the number of months that the money will be left in the account: '))

    print()

    futureValue = p * ((1 + (i/100))**t)

    print('The amount of money you will have after ', t, 'months is: $',futureValue)

main()
  
