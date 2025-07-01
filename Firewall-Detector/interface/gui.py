import tkinter as tk
from tkinter import messagebox
from detector.regras import obter_regras_firewall
from detector.analise import simular_conexoes
from detector.utils import validar_ip, validar_porta

conexoes = []

def adicionar_entrada(ip_entry, porta_entry, lista_text):
    ip = ip_entry.get()
    porta = porta_entry.get()

    if not validar_ip(ip):
        messagebox.showerror("Erro", "IP inválido.")
        return
    if not validar_porta(porta):
        messagebox.showerror("Erro", "Porta inválida.")
        return

    conexoes.append((ip, int(porta)))
    lista_text.insert(tk.END, f"{ip}:{porta}\n")
    ip_entry.delete(0, tk.END)
    porta_entry.delete(0, tk.END)

def executar_teste(resultado_frame):
    for widget in resultado_frame.winfo_children():
        widget.destroy()
    resultados = simular_conexoes(conexoes)
    for ip, porta, status in resultados:
        cor = 'lime' if status == "Permitido" else 'red'
        label = tk.Label(resultado_frame, text=f"{ip}:{porta} - {status}", fg=cor, bg='#1e1e1e', font=('Courier', 10))
        label.pack(anchor='w')

def mostrar_regras():
    regras = obter_regras_firewall()
    janela_regras = tk.Toplevel()
    janela_regras.title("Regras do Firewall")
    janela_regras.configure(bg='#2e2e2e')
    txt = tk.Text(janela_regras, height=30, width=80, bg='#1e1e1e', fg='lime')
    txt.pack()
    for linha in regras:
        txt.insert(tk.END, linha + "\n")

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Firewall Detector")
    janela.configure(bg='#2e2e2e')

    icone = tk.PhotoImage(file='C:/Users/Max/Documents/GitHub/Firewall-Detector/Firewall-Detector/interface/MM.png')
    janela.iconphoto(False, icone)

    tk.Label(janela, text="IP:", bg='#2e2e2e', fg='white', font=('Courier', 10)).grid(row=0, column=0)
    ip_entry = tk.Entry(janela, bg='black', fg='lime', insertbackground='white', font=('Courier', 10))
    ip_entry.grid(row=0, column=1)

    tk.Label(janela, text="Porta:", bg='#2e2e2e', fg='white', font=('Courier', 10)).grid(row=0, column=2)
    porta_entry = tk.Entry(janela, bg='black', fg='lime', insertbackground='white', font=('Courier', 10))
    porta_entry.grid(row=0, column=3)

    lista_text = tk.Text(janela, height=5, width=50, bg='#1e1e1e', fg='lime', insertbackground='white', font=('Courier', 10))
    lista_text.grid(row=1, column=0, columnspan=4, pady=5)

    resultado_frame = tk.Frame(janela, bg='#1e1e1e', bd=1, relief='sunken')
    resultado_frame.grid(row=3, column=0, columnspan=4, pady=5, sticky='nsew')

    style_btn = {'bg': '#333', 'fg': 'white', 'font': ('Courier', 10), 'activebackground': '#555', 'activeforeground': 'lime'}

    tk.Button(janela, text="Adicionar", command=lambda: adicionar_entrada(ip_entry, porta_entry, lista_text), **style_btn).grid(row=0, column=4, padx=5)
    tk.Button(janela, text="Testar Conexões", command=lambda: executar_teste(resultado_frame), **style_btn).grid(row=2, column=0, columnspan=2, pady=5)
    tk.Button(janela, text="Ver Regras do Firewall", command=mostrar_regras, **style_btn).grid(row=2, column=2, columnspan=2, pady=5)

    janela.mainloop()
