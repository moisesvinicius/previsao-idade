from datetime import datetime
import tkinter as tk
import tkinter.messagebox as mb

def calcular_idade_futura():
    try:
        # Obter os valores inseridos
        nome = entry_nome.get()
        data_nascimento_str = entry_data_nascimento.get()
        anos_futuro = int(entry_anos_futuro.get())

        # Converter a data de nascimento para um objeto datetime
        data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')

        # Calcular a idade no futuro
        hoje = datetime.now()
        ano_futuro = hoje.year + anos_futuro
        idade_futura = ano_futuro - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

        # Mostrar o resultado
        mensagem = f"{nome}, daqui a {anos_futuro} anos você terá {idade_futura} anos."
        mb.showinfo("Resultado", mensagem)
    
    except ValueError as e:
        mb.showerror("Erro", f"Entrada inválida: {e}")
    
    # Limpar os campos de entrada após o cálculo
    entry_nome.delete(0, tk.END)
    entry_data_nascimento.delete(0, tk.END)
    entry_anos_futuro.delete(0, tk.END)

# Criação da janela principal
janela = tk.Tk()
janela.title('Previsão de Idade')
janela.config(bg='#000000')
janela.geometry('450x500')

# Texto principal
texto_principal = tk.Label(text='PREVISÃO DE IDADE', bg='#000000', fg='#D3D3D3', font=('Arial', 20))
texto_principal.place(x=80, y=20)

# Nome
nome_label = tk.Label(text='Nome: ', bg='#000000', fg='#D3D3D3', font=('Arial', 14))
nome_label.place(x=20, y=80)
entry_nome = tk.Entry(janela, font=('Arial', 14))
entry_nome.place(x=100, y=80, width=300)

# Data de Nascimento
data_nascimento_label = tk.Label(text='Data de Nascimento (dd/mm/aaaa): ', bg='#000000', fg='#D3D3D3', font=('Arial', 14))
data_nascimento_label.place(x=20, y=120)
entry_data_nascimento = tk.Entry(janela, font=('Arial', 14))
entry_data_nascimento.place(x=20, y=150, width=300)

# Anos no Futuro
anos_futuro_label = tk.Label(text='Quantos anos no futuro: ', bg='#000000', fg='#D3D3D3', font=('Arial', 14))
anos_futuro_label.place(x=20, y=190)
entry_anos_futuro = tk.Entry(janela, font=('Arial', 14))
entry_anos_futuro.place(x=20, y=220, width=100)

# Botão para calcular
btn_calcular = tk.Button(janela, text='Calcular', font=('Arial', 14), command=calcular_idade_futura)
btn_calcular.place(x=20, y=260, width=100)

# Início do loop principal da interface gráfica
janela.mainloop()
