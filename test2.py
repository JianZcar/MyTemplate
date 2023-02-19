import tkinter as tk
import random

window = tk.Tk()
window.title(" Magical Name Generator ")

window.geometry("400x400")


# Functions.
def name_gen():
    """
    This function randomly concatenates items from
    two lists and combines them in one name.
    """
    first = ("ara", "isil", "ar", "beo", "boro", "dene", "bele", "eo",
             "teo", "ea", "el", "ele", "ele", "fara", "fea", "dea",
             "bere", "feo", "fan", "tau")
    second = ("gorn", "dur", "wen", "orn", "mir", "thor", "den", "dred",
              "ndil", "dil", "wing", "rond", "mer", "wyn", "nor", "gal",
              "zar", "nar", "mar", "dorn", "ron")
    first_part = random.choice(first)
    second_part = random.choice(second)
    name = (first_part + second_part)
    print(name.title())
    return name.title()


def name_plot():
    temp_lst = []
    for _ in range(10):
        temp_lst.append(name_gen())
    return '\n'.join(temp_lst)


def display_name():
    show_up = name_plot()
    text = tk.Text(master=window, height=10, width=30)
    text.grid(column=0, row=5)
    text.insert(tk.END, show_up)


# Labels
label_head = tk.Label(text=" Hello, Wanderer! \n Choose your name wisely. ", font=("The New Roman", 25))
label_head.grid()

label_enter = tk.Label(text=" Pick the one that suits you best. ")
label_enter.grid(column=0, row=1)

label_output = tk.Label(text='display_name')
label_output.grid()

# Button
button_submit = tk.Button(text="Generate", bg="green", command=display_name)
button_submit.grid(column=0, row=11)

window.mainloop()
