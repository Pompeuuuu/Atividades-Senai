import tkinter as tk
from tkinter import messagebox

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.config(bg = "yellow")


# Entrada para exibir os números e o resultado
entry = tk.Entry(janela, width=20, font=('Arial', 20), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(janela, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda key=button: press(key) if key != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botão Clear
tk.Button(janela, text='C', padx=20, pady=20, font=('Arial', 14), command=clear).grid(row=row_val, column=col_val)

# Iniciar a interface gráfica
janela.mainloop()
