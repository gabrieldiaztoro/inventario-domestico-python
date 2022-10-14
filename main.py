from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk

# importando cores
cor0 = "#2e2d2b"   # Preto
cor01 = "#feffff"  # Branco
cor02 = "#4fa882"  # verde
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

#frame parte de cima
frameCima = Frame(janela, width=1043, height=50, bg=cor01, relief=FLAT)
frameCima.grid(row=0, column=0)

#frame parte do meio
frameMeio = Frame(janela, width=1043, height=303, pady=20, bg=cor01, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#frame parte de baixo
frameBaixo = Frame(janela, width=1043, height=300, pady=20, bg=cor01, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=1, padx=1, sticky=NSEW)

#Carregando Imagem


janela.mainloop()
