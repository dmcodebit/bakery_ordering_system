import tkinter as tk
from tkinter import ttk, messagebox

def submit_order():
    order_summary = (
        f"Order Summary:\n"
        f"Dessert: {dessert.get().strip()}\n"
        f"Drink: {drink.get().strip()}\n"
        f"Bread: {bread.get().strip()}"
        f"Order Type: {order.get().strip()}"
        f"\n\nThank you for your order!"
    )
    messagebox.showinfo("Order Confirmation", order_summary)

window = tk.Tk()
window.title('Dessert Order')
window.geometry('500x300')

ttk.Label(window, text="Online Dessert Shop", background='green', foreground="white",
          font=("Times New Roman", 15)).grid(row=0, column=1, pady=10)

def create_combobox(label_text, values, row):
    ttk.Label(window, text=label_text, font=("Times New Roman", 10)).grid(column=0, row=row, padx=10, pady=10)
    var = tk.StringVar()
    combobox = ttk.Combobox(window, width=27, textvariable=var, values=values)
    combobox.grid(column=1, row=row)
    combobox.current(0)
    return combobox

dessert = create_combobox("Select Base dessert:", ['Muffin', 'Cake', 'Ice Cream'], 1)
drink = create_combobox("Select Add-On drink:", ['Coffee', 'Tea', 'Juice', 'None'], 2)
bread = create_combobox("Select Add-On bread:", ['Baguette', 'Croissant', 'Sourdough', 'None'], 3)
order = create_combobox("Select Order Type:", ['Pickup', 'Delivery', 'Hire - In Area Assistance'], 4)


ttk.Button(window, text="Submit Order", command=submit_order).grid(column=1, row=5, pady=20)

window.mainloop()
