from tkinter import *
from tkinter import Tk, StringVar, ttk

# importando cores
cor01 = "#2e2d2b"  # Preto
cor02 = "#feffff"  # Branco
cor03 = "#38576b"  # Verde
cor04 = "#403d3d"
cor05 = "#e06636"  # Profit
cor06 = "#038cfc"  # Azul
cor07 = "#3fbfb9"  # Verde
cor08 = "#263238"  # +Verde
cor09 = "#e9edf5"  # +verde

# Criando Frontend JANELA

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=cor09)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


janela.mainloop()
