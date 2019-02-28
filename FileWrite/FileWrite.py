#I am going to write to a notepad .txt file.

def main():

    #Open the file to write in
    outfile = open('FileWrite.txt', 'w')

    #Write in the file
    outfile.write('Testing testing this page\n')
    outfile.write('Python is cool and gets better always\n')
    outfile.write('I like food, period.\n')
    outfile.write('Logic offers serenity few can truly enjoy.\n')

    #Close the file
    #outfile.close()

#Call the main function
main()
