import random
from tkinter import messagebox


def main():

    # 1 = rock
    # 2 = paper
    # 3 = scissors 
    computer = random.randint(1,3)

    user = str(input("Please enter 'rock', 'paper', or 'scissors': "))
    print()
    print("The computer has chosen: ")
    if (computer == 1):
        print("rock")
    elif (computer == 2):
        print("paper")
    elif (computer == 3):
        print("scissors")
        

    if (computer == 1 and user == 'rock'):
        messagebox.showinfo("Rock, Paper, Scissors", "It's a tie. Please play again.")

    elif(computer == 1 and user == 'paper'):
        messagebox.showinfo("Rock, Paper, Scissors", "You win!")
        
    elif(computer == 1 and user == 'scissors'):
        messagebox.showinfo("Rock, Paper, Scissors", "The computer wins. Better luck next time!")

    elif(computer == 2 and user == 'rock'):
        messagebox.showinfo("Rock, Paper, Scissors", "The computer wins. Better luck next time!")

    elif(computer == 2 and user == 'paper'):
        messagebox.showinfo("Rock, Paper, Scissors", "It's a tie. Please play again.")

    elif(computer == 2 and user == 'scissors'):
        messagebox.showinfo("Rock, Paper, Scissors", "You win!")

    elif(computer == 3 and user == 'rock'):
        messagebox.showinfo("Rock, Paper, Scissors", "You win!")

    elif(computer == 3 and user == 'paper'):
        messagebox.showinfo("Rock, Paper, Scissors", "The computer wins. Better luck next time!")

    elif(computer == 3 and user == 'scissors'):
        messagebox.showinfo("Rock, Paper, Scissors", "It's a tie. Please play again.")

    else:
        messagebox.showinfo("Rock, Paper, Scissors", "Today is a great day!")

main()
        




        
