from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=800, height=500)
#window.geometry("800x500")
window.geometry("400x200")
#window.config(background="Cyan")
window.config(padx=100, pady=50)

entry = Entry()
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Segoe UI", 10))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=("Segoe UI", 10))
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text="0", font=("Segoe UI", 10))
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Segoe UI", 10))
km_label.grid(column=2, row=1)


def button_clicked():
    miles = entry.get()
    conversion_factor = 0.62137119
    kilometers = float(miles) / conversion_factor
    rounded_km = round(kilometers, 2)
    result_label.config(text=f"{rounded_km}")


calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
