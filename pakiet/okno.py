from tkinter import Tk, Label, Button


def click(button):
    button.config(text=f"Działa!")

# def create_command(func,*args,**kwargs):
#     def command():
#         return func(*args,**kwargs)
#     return command


#################
root = Tk()

root.title('moja aplikacja v0.1')
root.geometry("500x500")

button = Button(root, text="kliknij", width=10)
button.pack()

label = Label(root, text="kite.com/python/docs/tkinter", font=135, fg="blue")
label.pack()

button.config(command=lambda: click(button))

root.mainloop()
