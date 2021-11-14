from random import choice
from tkinter import Tk, Label, Button

available_choices = ["paper", "rock", "scissors"]


def play(player, cpu):
    win_with = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False

def play_cmd(player):
    global text_label
    cpu = choice(available_choices)
    is_user_winner = play(player,cpu)
    if is_user_winner is None:
        text_label.config(text="Remis!Spróbuj ponownie",fg="blue")
    elif is_user_winner:
        text_label.config(text="Wygrałeś człowieku!Daj mi się odegrać!",fg="green")
    else:
        text_label.config(text="Wygrałem! Jestem od Ciebie lepszy człowieku!!",fg="red")

"""
Poniżej kod odpowiedzialny za wygląd okna
"""

root = Tk()
root.title("Moja pierwsza gierka")
root.geometry("300x150")

text_label = Label(root, font=40, text="Zagrajmy w grę!")
text_label.pack()

Button(root, text="📝 papier", font=40, width=10).pack()
Button(root, text="🛑 kamień", font=40, width=10).pack()
Button(root, text="✂️ nożyce", font=40, width=10).pack()

root.mainloop()
