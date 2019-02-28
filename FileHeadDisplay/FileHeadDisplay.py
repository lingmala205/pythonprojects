#Write a program that asks the user for the name of a file.
#The program should display only the first five lines of
#the file's contents. If the file contains less than five lines,
#it should display the file's entire contents.

def main():

    #Get the name of a file:
    filename = input('Enter a filename: ')

    try:

        #Open the file.
        infile = open(filename, 'r')

        #Read five lines.
        count = 0;
        maximumCount = 5;


        for line in infile: #For every line in the file
            #If there are less than 5 lines,
            #then print out each line's information.
            if count < maximumCount: 
                print(line, end="")
                count += 1    #Count how many lines pass inspection.
            else:
                #Otherwise, end the application
                break

    #Throw an exception if the query is faulty.
    except IOError:
        print('An error occured trying to read the file you requested.')
    
main()
