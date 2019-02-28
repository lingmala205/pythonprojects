#Return initials of a full name.
def main():

    #Prompt the user for input.
    fullName = str(input("Enter your full name: "))

    #Split the string into a list.
    #Then, find the first letter in each index.
    #Join them together.
    initials = '.'.join([letter[0] for letter in fullName.split() ])

    #Print the initials.
    print(initials) 

#Call the main method.
main()
