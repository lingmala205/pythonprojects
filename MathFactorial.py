import math

def main():

  while True:
   try:   
    number = int(input('Please enter a nonnegative integer: '))
    print(number,'! = ', math.factorial(number))

   except ValueError:
       print('Please enter an integer (0 or higher.)')


main()
        
