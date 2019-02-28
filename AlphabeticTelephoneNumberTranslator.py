def main():

    prompt_user = str(input("Please enter a 10-character telephone number in the format XXX-XXX-XXXX: "))

    received_input = prompt_user.upper()

  

    new_result = ''
    
    count = 0
    
    for value in received_input:
        if value == 'A' or value == 'B' or value == 'C':
           value = '2'
           count += 1

        elif value == 'D' or value == 'E' or value == 'F':
             value = '3'
             count += 1

        elif value == 'G' or value == 'H' or value == 'I':
             value = '4'
             count += 1
           
        elif value == 'J' or value == 'K' or value == 'L':
             value = '5'       
             count += 1
           
        elif value == 'M' or value == 'N' or value == 'O':
             value = '6'
             count += 1

        elif value == 'P' or value == 'Q' or value == 'R' or value == 'S':
             value = '7'
             count += 1

        elif value == 'T' or value == 'U' or value == 'V':
             value = '8'
             count += 1

        elif value == 'W' or value == 'X' or value == 'Y' or value == 'Z':
             value = '9'
             count += 1

        new_result = new_result + value

    print(new_result)
    print(count)

main()
            
