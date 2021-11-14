from tkinter import Tk, Label, Button

clicks = 0

def click(button):
    global clicks
    clicks += 1
    button.config(text=f"Działa! {clicks}")

# def create_command(func,*args,**kwargs):
#     def command():
#         return func(*args,**kwargs)
#     return command


#################
root = Tk()

root.title('moja aplikacja v0.1')
root.geometry("500x500")

button = Button(root, text="kliknij", width=10)


label = Label(root, text="kite.com/python/docs/tkinter", font=135, fg="blue")


button.config(command=lambda: click(button))


button.pack()
label.pack()
root.mainloop()
