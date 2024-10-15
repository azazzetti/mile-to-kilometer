from tkinter import *

window = Tk()
window.title("Mile to KM")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# -------------------- MILES TO KM FUNCTION -------------------- #
def miles_to_km():
    miles = miles_input.get()
    result = float(miles) * float(1.60934)
    result_label.config(text=f"{result}")


# -------------------- MILES ENTRY -------------------- #
miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)

# -------------------- MILES LABEL -------------------- #

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# -------------------- IS EQUAL TO -------------------- #

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# -------------------- MILES IN KM -------------------- #

result_label = Label(text="0")
result_label.grid(column=1,row=1)

# --------------------      KM     -------------------- #

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

# -------------------- CALCULATE BUTTON -------------------- #

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row= 2)

window.mainloop()