def main():

    #Open a file named FileRead.txt
    infile = open('FileRead.txt', 'r')

    #Read the file's contents
    fileContents = infile.read()

    #Close the file
    infile.close()

    #Print data that was read into memory.
    print(fileContents)

#Call the maiin function
main()
