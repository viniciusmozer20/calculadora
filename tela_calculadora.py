import tkinter as tk
import math

# --- Janela principal ---
janela = tk.Tk()
janela.title("Calculadora")
janela.configure(bg="black")  # fundo preto
janela.resizable(False, False)

# --- Variáveis globais ---
resultado = 0
operacao = ""
novo_numero = False  # indica se deve limpar o visor ao digitar número

# --- Funções da calculadora ---

# Atualiza o visor e o histórico
def atualizar_historico(texto):
    historico.config(text=texto)

def clicar_numero(num):
    global novo_numero
    if novo_numero:
        visor.delete(0, tk.END)
        novo_numero = False
    visor.insert(tk.END, str(num))

def clicar_operacao(op):
    global resultado, operacao, novo_numero
    try:
        valor_atual = float(visor.get())
    except ValueError:
        valor_atual = 0

    if operacao == "":
        resultado = valor_atual
    else:
        calcular_resultado(valor_atual)

    operacao = op
    atualizar_historico(f"{resultado} {operacao}")
    novo_numero = True

def calcular_resultado(valor_atual):
    global resultado, operacao
    if operacao == "+":
        resultado += valor_atual
    elif operacao == "-":
        resultado -= valor_atual
    elif operacao == "*":
        resultado *= valor_atual
    elif operacao == "/":
        if valor_atual != 0:
            resultado /= valor_atual
        else:
            visor.delete(0, tk.END)
            visor.insert(0, "Erro: Divisão por 0")
            atualizar_historico("")
            return
    visor.delete(0, tk.END)
    visor.insert(0, str(resultado))

def clicar_igual():
    global resultado, operacao
    try:
        valor_atual = float(visor.get())
    except ValueError:
        valor_atual = 0
    calcular_resultado(valor_atual)
    atualizar_historico("")
    operacao = ""

def clicar_raiz():
    global resultado
    try:
        valor_atual = float(visor.get())
    except ValueError:
        valor_atual = 0

    if valor_atual >= 0:
        resultado = math.sqrt(valor_atual)
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
        atualizar_historico(f"√({valor_atual})")
    else:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro: Raiz neg.")
        atualizar_historico("")

def limpar():
    global resultado, operacao
    visor.delete(0, tk.END)
    resultado = 0
    operacao = ""
    atualizar_historico("")

# --- Histórico ---
historico = tk.Label(janela, text="", anchor="e", bg="black", fg="gray", font=("Arial", 12))
historico.grid(row=0, column=0, columnspan=4, sticky="we", padx=5, pady=5)

# --- Visor ---
visor = tk.Entry(janela, width=20, font=("Arial", 24), bg="black", fg="white", justify="right", bd=0, insertbackground="white")
visor.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

# --- Botões ---
botoes = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
    ("C", 6, 0), ("√", 6, 1)
]

for texto, linha, coluna in botoes:
    if texto.isdigit() or texto == ".":
        tk.Button(janela, text=texto, width=5, height=2, bg="#333333", fg="white", font=("Arial", 18),
                  bd=0, highlightthickness=0, command=lambda t=texto: clicar_numero(t)).grid(row=linha, column=coluna, padx=2, pady=2)
    elif texto in "+-*/":
        tk.Button(janela, text=texto, width=5, height=2, bg="#555555", fg="white", font=("Arial", 18),
                  bd=0, highlightthickness=0, command=lambda t=texto: clicar_operacao(t)).grid(row=linha, column=coluna, padx=2, pady=2)
    elif texto == "=":
        tk.Button(janela, text=texto, width=5, height=2, bg="#777777", fg="white", font=("Arial", 18),
                  bd=0, highlightthickness=0, command=clicar_igual).grid(row=linha, column=coluna, padx=2, pady=2)
    elif texto == "C":
        tk.Button(janela, text=texto, width=5, height=2, bg="#aa3333", fg="white", font=("Arial", 18),
                  bd=0, highlightthickness=0, command=limpar).grid(row=linha, column=coluna, padx=2, pady=2)
    elif texto == "√":
        tk.Button(janela, text=texto, width=5, height=2, bg="#5555aa", fg="white", font=("Arial", 18),
                  bd=0, highlightthickness=0, command=clicar_raiz).grid(row=linha, column=coluna, padx=2, pady=2)

# --- Rodar ---
janela.mainloop()
