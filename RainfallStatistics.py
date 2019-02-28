def main():

    print("Please enter the total rainfall per month in inches.")
    print("Try to ensure your numbers are different from each other.")
    print()
    jan = int(input("Jan Rainfall? "))
    feb = int(input("Feb Rainfall? "))
    mar = int(input("Mar Rainfall? "))
    apr = int(input("Apr Rainfall? "))
    may = int(input("May Rainfall? "))
    jun = int(input("Jun Rainfall? "))
    jul = int(input("Jul Rainfall? "))
    aug = int(input("Aug Rainfall? "))
    sep = int(input("Sep Rainfall? "))
    oct = int(input("Oct Rainfall? "))
    nov = int(input("Nov Rainfall? "))
    dec = int(input("Dec Rainfall? "))


    
    rainfall = [jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec]

    total = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec

    print("The total inches of rainfall for the year is: ",total," inches.")

    average = total/12

    print("The average monthly rainfall is: ",average," inches.")

    monthHI = rainfall.index(max(rainfall))

    if monthHI == 0:
        print("January has the most rainfall.")
    elif monthHI == 1:
        print("February has the most rainfall.")
    elif monthHI == 2:
        print("March has the most rainfall.")
    elif monthHI == 3:
        print("April has the most rainfall.")
    elif monthHI == 4:
        print("May has the most rainfall.")
    elif monthHI == 5:
        print("June has the most rainfall.")
    elif monthHI == 6:
        print("July has the most rainfall.")
    elif monthHI == 7:
        print("August has the most rainfall.")
    elif monthHI == 8:
        print("September has the most rainfall.")
    elif monthHI == 9:
        print("October has the most rainfall.")
    elif monthHI == 10:
        print("November has the most rainfall.")
    elif monthHI == 11:
        print("December has the most rainfall.")
        
    

    
    monthLO = rainfall.index(min(rainfall))

    if monthLO == 0:
        print("January has the least rainfall.")
    elif monthLO == 1:
        print("February has the least rainfall.")
    elif monthLO == 2:
        print("March has the least rainfall.")
    elif monthLO == 3:
        print("April has the least rainfall.")
    elif monthLO == 4:
        print("May has the least rainfall.")
    elif monthLO == 5:
        print("June has the least rainfall.")
    elif monthLO == 6:
        print("July has the least rainfall.")
    elif monthLO == 7:
        print("August has the least rainfall.")
    elif monthLO == 8:
        print("September has the least rainfall.")
    elif monthLO == 9:
        print("October has the least rainfall.")
    elif monthLO == 10:
        print("November has the least rainfall.")
    elif monthLO == 11:
        print("December has the least rainfall.")

main()
    
    
    
