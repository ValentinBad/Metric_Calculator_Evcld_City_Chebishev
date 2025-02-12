import tkinter as tk  # Імпорт бібліотеки Tkinter для створення GUI
from tkinter import messagebox  # Імпорт messagebox для виводу повідомлень про помилки
import math  # Імпорт модуля math для математичних обчислень

# Функція для обчислення відстаней між двома точками у 3D-просторі
def calculate_distance():
    try:
        # Отримуємо введені координати точок
        x1, x2, x3 = float(entry_x1.get()), float(entry_x2.get()), float(entry_x3.get())
        y1, y2, y3 = float(entry_y1.get()), float(entry_y2.get()), float(entry_y3.get())
        
        # Обчислення Евклідової відстані
        evklid = math.sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2 + (x3 - y3) ** 2)
        
        # Обчислення Манхеттенської відстані
        city = abs(x1 - y1) + abs(x2 - y2) + abs(x3 - y3)
        
        # Обчислення Чебишовської відстані
        cheb = max(abs(x1 - y1), abs(x2 - y2), abs(x3 - y3))
        
        # Вивід результатів на екран
        label_evklid.config(text=f"Evklid: {evklid:.2f}")
        label_city.config(text=f"City: {city:.2f}")
        label_cheb.config(text=f"Cheb: {cheb:.2f}")
    except ValueError:
        # Вивід повідомлення про помилку у разі некоректного вводу
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення")

# Функція для очищення всіх полів вводу та результатів

def clear_fields():
    entry_x1.delete(0, tk.END)
    entry_x2.delete(0, tk.END)
    entry_x3.delete(0, tk.END)
    entry_y1.delete(0, tk.END)
    entry_y2.delete(0, tk.END)
    entry_y3.delete(0, tk.END)
    label_evklid.config(text="Evklid:")
    label_city.config(text="City:")
    label_cheb.config(text="Cheb:")

# Створення головного вікна Tkinter
root = tk.Tk()
root.title("Калькулятор метрик")  # Назва вікна

# Виведення заголовка
tk.Label(root, text="Калькулятор метрик розробив Бадай Валентин").grid(row=0, column=0, columnspan=4)

# Створення міток для полів вводу координат
tk.Label(root, text="V1").grid(row=1, column=0)
tk.Label(root, text="V2").grid(row=2, column=0)

# Поля вводу для координат точки V1
entry_x1 = tk.Entry(root)
entry_x2 = tk.Entry(root)
entry_x3 = tk.Entry(root)

# Поля вводу для координат точки V2
entry_y1 = tk.Entry(root)
entry_y2 = tk.Entry(root)
entry_y3 = tk.Entry(root)

# Розміщення полів вводу на формі
entry_x1.grid(row=1, column=1)
entry_x2.grid(row=1, column=2)
entry_x3.grid(row=1, column=3)
entry_y1.grid(row=2, column=1)
entry_y2.grid(row=2, column=2)
entry_y3.grid(row=2, column=3)

# Мітки для відображення результатів
label_evklid = tk.Label(root, text="Evklid:")
label_city = tk.Label(root, text="City:")
label_cheb = tk.Label(root, text="Cheb:")

# Розміщення міток для відстаней
label_evklid.grid(row=3, column=0, columnspan=1)
label_city.grid(row=4, column=0, columnspan=1)
label_cheb.grid(row=5, column=0, columnspan=1)

# Кнопка для обчислення відстаней
button_calculate = tk.Button(root, text="Обрахувати", command=calculate_distance, width=15)
button_calculate.grid(row=4, column=4)

# Кнопка для очищення полів вводу
button_clear = tk.Button(root, text="Очистити", command=clear_fields, width=15)
button_clear.grid(row=5, column=4)

# Запуск головного циклу Tkinter для роботи GUI
root.mainloop()
