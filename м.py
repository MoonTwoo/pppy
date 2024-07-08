import tkinter as tk
from tkinter import ttk

def salary():
    hour = radio_work_hours_var.get()
    day_int = int(day_entry.get())
    pay = rate * day_int * hour
    result_label.config(text=f"Зарплата: {pay}")

def hours():
    label_hours.config(text="Сколько часов в день работаете?")
    salary()
    radio_8_hours.pack()
    radio_4_hours.pack()

# Создание главного окна
window = tk.Tk()
window.title("Расчёт заработной платы")
# --!!!

# Переменные для хранения данных
radio_work_hours_var = tk.IntVar(value=8)
rate = 1000  # Ставка за час
# --!!!

# !!!-- Виджеты интерфейса
day_label = ttk.Label(window, text="Введите количество рабочих дней:")
day_label.pack()

day_entry = ttk.Entry(window)
day_entry.pack()

label_hours = ttk.Label(window, text="")
label_hours.pack()

radio_8_hours = ttk.Radiobutton(window, text="8 часов", variable=radio_work_hours_var, value=8, command=salary)
radio_4_hours = ttk.Radiobutton(window, text="4 часа", variable=radio_work_hours_var, value=4, command=salary)

calculate_button = ttk.Button(window, text="Рассчитать", command=hours)
calculate_button.pack()

result_label = ttk.Label(window, text="")
result_label.pack()
# Виджеты интерфейса --!!!

window.mainloop()