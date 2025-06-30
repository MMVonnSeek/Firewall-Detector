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


def executar_teste(resultado_text):
    resultado_text.delete(1.0, tk.END)
    resultados = simular_conexoes(conexoes)
    for ip, porta, status in resultados:
        resultado_text.insert(tk.END, f"{ip}:{porta} - {status}\n")


def mostrar_regras():
    regras = obter_regras_firewall()
    janela_regras = tk.Toplevel()
    janela_regras.title("Regras do Firewall")
    txt = tk.Text(janela_regras, height=30, width=80)
    txt.pack()
    for linha in regras:
        txt.insert(tk.END, linha + "\n")


def iniciar_interface():
    janela = tk.Tk()
    janela.title("Firewall Detector")

    tk.Label(janela, text="IP:").grid(row=0, column=0)
    ip_entry = tk.Entry(janela)
    ip_entry.grid(row=0, column=1)

    tk.Label(janela, text="Porta:").grid(row=0, column=2)
    porta_entry = tk.Entry(janela)
    porta_entry.grid(row=0, column=3)

    lista_text = tk.Text(janela, height=5, width=50)
    lista_text.grid(row=1, column=0, columnspan=4)

    resultado_text = tk.Text(janela, height=10, width=50)
    resultado_text.grid(row=3, column=0, columnspan=4)

    tk.Button(janela, text="Adicionar", command=lambda: adicionar_entrada(ip_entry, porta_entry, lista_text)).grid(row=0, column=4)
    tk.Button(janela, text="Testar Conexões", command=lambda: executar_teste(resultado_text)).grid(row=2, column=0, columnspan=2)
    tk.Button(janela, text="Ver Regras do Firewall", command=mostrar_regras).grid(row=2, column=2, columnspan=2)

    janela.mainloop()