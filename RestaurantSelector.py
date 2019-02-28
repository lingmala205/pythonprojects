def main():

   while True: 
    answer1 = input('Is anyone in your party a vegetarian? ')
    answer2 = input('Is anyone in your party a vegan? ')
    answer3 = input('Is anyone in your party gluten-free? ')
    
    if (answer1=='yes' and answer2=='yes' and answer3=='yes'):
        print('Here are your restaurant choices:')
        print('Corner Cafe')
        print("The Chef's Kitchen")
        break
            
    elif (answer1=='yes' and answer2=='yes' and answer3=='no'):
        print('Here are your restaurant choices:')
        print('Corner Cafe')
        print("The Chef's Kitchen")
        break
            
    elif (answer1=='yes' and answer2=='no' and answer3=='yes'):
        print('Here are your restaurant choices:')
        print('Main Street Pizza Company')
        print('Corner Cafe')
        print("The Chef's Kitchen")
        break


    elif (answer1=='no' and answer2=='yes' and answer3=='yes'):
        print('Here are your restaurant choices:')
        print('Corner Cafe')
        print("The Chef's Kitchen")
        break


    elif (answer1=='no' and answer2=='no' and answer3=='yes'):
        print('Here are your restaurant choices:')
        print('Main Street Pizza Company')
        print('Corner Cafe')        
        print("The Chef's Kitchen")
        break


    
    elif (answer1=='yes' and answer2=='no' and answer3=='no'):
        print('Here are your restaurant choices:')
        print('Main Street Pizza Company')
        print('Corner Cafe')        
        print("Mama's Fine Italian")
        break


    
    elif (answer1=='no' and answer2=='yes' and answer3=='no'):
        print('Here are your restaurant choices:')
        print('Corner Cafe')        
        print("The Chef's Kitchen")
        break


    
    elif (answer1=='no' and answer2=='no' and answer3=='no'):
        print('Here are your restaurant choices:')
        print("Joe's Gourmet Burgers")
        break


    else:
        print("Please enter either 'yes' or 'no' for each question. Thank you.")


main()
