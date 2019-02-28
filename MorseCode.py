#Still working on this as of 9 February, 2019
def main():

    sampleText = str(input("Please enter some text: "))

    finalText = sampleText.upper()

    index = 0

    morse = []
   
    for n in finalText:
          if finalText[index] == " ":
             morse[index] == " "
             index += 1
                  if finalText[index] == ",":
                     morse[index] == "--..--"
                     index += 1
                      if finalText[index] == ".":
                     morse[index] == ".-.-.-"
                     index += 1
                      if finalText[index] == "?":
                         morse[index] == "..--.."
                         index += 1
                          if finalText[index] == "0":
                             morse[index] == "-----"
                             index += 1
                              if finalText[index] == "1":
                                 morse[index] == ".----"
                                 index += 1
                                  if finalText[index] == "2":
                                     morse[index] == "..---"
                                     index += 1
                                      if finalText[index] == "3":
                                         morse[index] == "...--"
                                         index += 1
                                          if finalText[index] == "4":
                                             morse[index] == "....-"
                                             index += 1
                                              if finalText[index] == "5":
                                                 morse[index] == "....."
                                                 index += 1
                                                  if finalText[index] == "6":
                                                     morse[index] == "-...."
                                                     index += 1
                                                      if finalText[index] == "7":
                                                         morse[index] == "--..."
                                                         index += 1
                                                          if finalText[index] == "8":
                                                             morse[index] == "---.."
                                                             index += 1
                                                              if finalText[index] == "9":
                                                                 morse[index] == "----."
                                                                 index += 1
                                                                  if finalText[index] == "A":
                                                                     morse[index] == ".-"
                                                                     index += 1
                                                                      if finalText[index] == "B":
                                                                         morse[index] == "-..."
                                                                         index += 1
                                                                          if finalText[index] == "C":
                                                                             morse[index] == "-.-."
                                                                             index += 1
                                                                              if finalText[index] == "D":
                                                                                 morse[index] == "-.."
                                                                                 index += 1
                                                                                  if finalText[index] == "E":
                                                                                     morse[index] == "."
                                                                                     index += 1
                                                                                      if finalText[index] == "F":
                                                                                         morse[index] == "..-."
                                                                                         index += 1
                                                                                          if finalText[index] == "G":
                                                                                             morse[index] == "--."
                                                                                             index += 1
                                                                                              if finalText[index] == "H":
                                                                                                 morse[index] == "...."
                                                                                                 index += 1
                                                                                                  if finalText[index] == "I":
                                                                                                     morse[index] == ".."
                                                                                                     index += 1
                                                                                                      if finalText[index] == "J":
                                                                                                         morse[index] == ".---"
                                                                                                         index += 1
                                                                                                          if finalText[index] == "K":
                                                                                                             morse[index] == "-.-"
                                                                                                             index += 1
                                                                                                              if finalText[index] == "L":
                                                                                                                 morse[index] == ".-.."
                                                                                                                 index += 1
                                                                                                                  if finalText[index] == "M":
                                                                                                                     morse[index] == "--"
                                                                                                                     index += 1
                                                                                                                      if finalText[index] == "N":
                                                                                                                         morse[index] == "-."
                                                                                                                         index += 1
                                                                                                                          if finalText[index] == "O":
                                                                                                                             morse[index] == "---"
                                                                                                                             index += 1
                                                                                                                              if finalText[index] == "P":
                                                                                                                                 morse[index] == ".--."
                                                                                                                                 index += 1
                                                                                                                                  if finalText[index] == "Q":
                                                                                                                                     morse[index] == "--.-"
                                                                                                                                     index += 1
                                                                                                                                      if finalText[index] == "R":
                                                                                                                                         morse[index] == ".-."
                                                                                                                                         index += 1
                                                                                                                                          if finalText[index] == "S":
                                                                                                                                             morse[index] == "..."
                                                                                                                                             index += 1
                                                                                                                                              if finalText[index] == "T":
                                                                                                                                                 morse[index] == "-"
                                                                                                                                                 index += 1
                                                                                                                                                  if finalText[index] == "U":
                                                                                                                                                     morse[index] == "..-"
                                                                                                                                                     index += 1
                                                                                                                                                      if finalText[index] == "V":
                                                                                                                                                         morse[index] == "...-"
                                                                                                                                                         index += 1
                                                                                                                                                          if finalText[index] == "W":
                                                                                                                                                             morse[index] == ".--"
                                                                                                                                                             index += 1
                                                                                                                                                              if finalText[index] == "X":
                                                                                                                                                                 morse[index] == "-..-"
                                                                                                                                                                 index += 1
                                                                                                                                                                  if finalText[index] == "Y":
                                                                                                                                                                     morse[index] == "-.-"
                                                                                                                                                                     index += 1
                                                                                                                                                                      if finalText[index] == "Z":
                                                                                                                                                                         morse[index] == "--.."
                                                                                                                                                                         index += 1
                                                                                                                                                                      else:
                                                                                                                                                                          index += 1
        
    print("Your sample text is translated into Morse Code below.")      
    print(morse)

main()

    
