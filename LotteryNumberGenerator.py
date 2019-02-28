#Enable random number generation
import random

def main():

    #Make the random numbers
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)
    e = random.randint(0,9)
    f = random.randint(0,9)
    g = random.randint(0,9)

    #Create a list out of the random numbers.
    lottery = [a,b,c,d,e,f,g]

    #Create a lottery tag line.
    print("Here are the lucky numbers:")
    #Print the numbers out in lottery-style.
    for x in range(7):
        print(lottery[x], end =" ") 

#Call the main method.
main()

    
