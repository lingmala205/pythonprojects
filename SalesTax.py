def main():

    purchase = float(input('Please enter the amount of purchase: $'))

    stateSalesTax = 0.05 * purchase
    countySalesTax = 0.025 * purchase

    totalSale = purchase + stateSalesTax + countySalesTax
    print('The state sales tax is: $',stateSalesTax)
    print('The county sales tax is: $',countySalesTax)
    print('The total sale is: $',totalSale)

main()
