import tkinter as tk
from tkinter import messagebox

# Função para calcular o fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Função para processar a entrada e exibir o resultado
def calcular_fatorial():
    try:
        numero = int(entry_numero.get())  # Obtém o valor digitado pelo usuário
        if numero < 0:
            messagebox.showerror("Erro", "Por favor, insira um número não negativo.")
        else:
            resultado = fatorial(numero)
            label_resultado.config(text=f"O fatorial de {numero} é {resultado}", fg="green")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Fatorial")
root.geometry("400x300")  # Tamanho da janela
root.config(bg="indigo")  # Cor de fundo escura

# Título
label_titulo = tk.Label(root, text="Calculadora de Fatorial", font=("Arial", 20, "bold"), bg="indigo", fg="lightcyan")
label_titulo.pack(pady=20)

# Caixa de entrada para o número
label_instrucao = tk.Label(root, text="Digite um número:", font=("Arial", 12), bg="indigo", fg="yellow")
label_instrucao.pack()

entry_numero = tk.Entry(root, font=("Arial", 14), width=10)
entry_numero.pack(pady=10)

# Botão para calcular o fatorial
botao_calcular = tk.Button(root, text="Calcular", font=("Arial", 14), bg="lime", fg="midnightblue", command=calcular_fatorial)
botao_calcular.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="", font=("Arial", 14), bg="azure", fg="darkmagenta")
label_resultado.pack(pady=20)

# Iniciar a aplicação
root.mainloop()
