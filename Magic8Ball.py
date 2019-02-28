import random
import turtle

def main():

    turtle.hideturtle()
    circle(0,0,200,'black')
    circle(0,0,90,'white')
    circle(0,45,45,'black')
    circle(0,-45,45,'black')
    circle(0,45,40,'white')
    circle(0,-45,40,'white')
    


    print("Step right up and have your questions answered!")
    print()
    question()

def question():

     listSentences = ["Yes, of course!","Without a doubt, yes.",
                     "You can count on it.","For sure!","Ask me later.",
                     "I'm not sure.","I can't tell you right now.",
                     "I'll tell you after my nap.","No way!I don't think so.",
                     "Without a doubt, no.","The answer is clearly NO."]

     index = random.randint(0, len(listSentences)-1)

     
     prompt_user = str(input("Ask any question to the Magic 8 Ball: "))
     print()
     print("The Magic 8 Ball says: ",listSentences[index])
     print()
     play_again = str(input("Do you want to play again? 'Yes' or 'No'? "))
     if play_again == 'Yes':
        question()
     elif play_again == 'No':
         print("Thanks for playing!")
     else:
         print("Thanks for playing!")



def circle(x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
main()
