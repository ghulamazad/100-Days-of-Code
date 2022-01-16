from tkinter import *


def miles_to_km():
    miles = mile_input.get()
    km = float(miles) * 1.609
    result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=200, height=200)
window.config(padx=26, pady=26)

mile_input = Entry(width=7, text="0")
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

iseqaul_label = Label(text="is equal to")
iseqaul_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
