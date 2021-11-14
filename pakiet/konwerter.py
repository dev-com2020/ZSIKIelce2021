import tkinter as tk


def far_to_cel():
    far = ent_temp.get()
    cel = (5 / 9) * (float(far) - 32)
    lbl_result["text"] = f"{round(cel, 2)} \N{DEGREE CELSIUS}"


root = tk.Tk()
root.title("Konwerter temperatury")
root.resizable(width=False, height=False)

frm_entry = tk.Frame(master=root)
ent_temp = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE CELSIUS}")

ent_temp.grid(row=0, column=0, sticky='e')
lbl_temp.grid(row=0, column=1, sticky='w')

btn_convert = tk.Button(master=root, text="\N{DEGREE CELSIUS}",command=far_to_cel)

lbl_result = tk.Label(master=root, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, padx=10)
lbl_result.grid(row=0, column=2, padx=10)

root.mainloop()
