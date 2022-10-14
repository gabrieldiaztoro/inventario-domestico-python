from importlib.metadata import entry_points
from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date


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

# frame parte de cima
frameCima = Frame(janela, width=1043, height=50, bg=cor01, relief=FLAT)
frameCima.grid(row=0, column=0)

# frame parte do meio
frameMeio = Frame(janela, width=1043, height=303,
                  pady=20, bg=cor01, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# frame parte de baixo
frameBaixo = Frame(janela, width=1043, height=300,
                   pady=20, bg=cor01, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=1, padx=1, sticky=NSEW)

# Carregando Imagem
app_img = Image.open('imagem_cadastro.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frameCima, image=app_img, text=' Inventário doméstico', width=900,
                 compound=LEFT, relief=RAISED, anchor=NW, font=("Verdana 20 bold"), bg=cor01, fg=cor04)
app_logo.place(x=0, y=0)


# editando frame cima
# editando frame meio
# criando entradas
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief='solid')
e_nome.place(x=130, y=11)


l_local = Label(frameMeio, text='Sala/Área', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief='solid')
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief='solid')
e_descricao.place(x=130, y=71)

l_model = Label(frameMeio, text='Marca/Modelo', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_model.place(x=10, y=100)
e_model = Entry(frameMeio, width=30, justify='left', relief='solid')
e_model.place(x=130, y=101)



# editando frame baixo

janela.mainloop()
