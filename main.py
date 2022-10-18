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
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW,
               font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief='solid')
e_nome.place(x=130, y=11)


l_local = Label(frameMeio, text='Sala/Área', height=1,
                anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief='solid')
e_local.place(x=130, y=41)


l_descricao = Label(frameMeio, text='Descrição', height=1,
                    anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief='solid')
e_descricao.place(x=130, y=71)


l_model = Label(frameMeio, text='Marca/Modelo', height=1,
                anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_model.place(x=10, y=100)
e_model = Entry(frameMeio, width=30, justify='left', relief='solid')
e_model.place(x=130, y=101)


l_calendario = Label(frameMeio, text='Data da compra', height=1,
                     anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_calendario.place(x=10, y=130)
e_calendario = DateEntry(
    frameMeio, width=12, background='darkblue', borderwidth=2, year=2022)
e_calendario.place(x=130, y=131)


l_valor = Label(frameMeio, text='Valor da compra', height=1,
                anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_valor.place(x=10, y=160)
e_model = Entry(frameMeio, width=30, justify='left', relief='solid')
e_model.place(x=130, y=161)


l_serial = Label(frameMeio, text='Número da série', height=1,
                 anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify='left', relief='solid')
e_serial.place(x=130, y=191)


# Criando botoes

# botao carregar
l_carregar = Label(frameMeio, text='Imagem do item', height=1,
                   anchor=NW, font=('Ivi 10 bold'), bg=cor01, fg=cor04)
l_carregar.place(x=10, y=220)

b_carregar = Button(frameMeio, width=29, text='carregar'.upper(
), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivi 8'), bg=cor01, fg=cor0)
b_carregar.place(x=130, y=221)


# botao inserir
# primeiramente carregando imagem do botao
img_add = Image.open('imagem_inserir.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio, image=img_add, width=95, text='  Adicionar'.upper(
), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=cor01, fg=cor0)
b_inserir.place(x=330, y=10)

# botao atualizar
# primeiramente carregando imagem do botao
img_atualizar = Image.open('imagem_atualizar.png')
img_atualizar = img_atualizar.resize((20, 20))
img_atualizar = ImageTk.PhotoImage(img_atualizar)

b_atualizar = Button(frameMeio, image=img_atualizar, width=95, text='  Atualizar'.upper(
), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=cor01, fg=cor0)
b_atualizar.place(x=330, y=50)


# botao excluir
# primeiramente carregando imagem do botao
img_excluir = Image.open('imagem_excluir.png')
img_excluir = img_excluir.resize((20, 20))
img_excluir = ImageTk.PhotoImage(img_excluir)

b_excluir = Button(frameMeio, image=img_excluir, width=95, text='  Excluir'.upper(
), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=cor01, fg=cor0)
b_excluir.place(x=330, y=90)


# botao visualizar
# primeiramente carregando imagem do botao
img_visualizar = Image.open('imagem_visualizar.png')
img_visualizar = img_visualizar.resize((20, 20))
img_visualizar = ImageTk.PhotoImage(img_visualizar)

b_visualizar = Button(frameMeio, image=img_visualizar, width=95, text='  Visualizar'.upper(
), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=cor01, fg=cor0)
b_visualizar.place(x=330, y=221)

# CRIANDO LABEL DE QUANTIDADE TOTAL
l_total = Label(frameMeio, text='', width=14, height=2,
                anchor=CENTER, font=('Ivi 17 bold'), bg=cor07, fg=cor01)
l_total.place(x=450, y=17)

l_total_ = Label(frameMeio, text='  Valor Total de todos os itens  ', height=1,
                 anchor=NW, font=('Ivi 10 bold'), bg=cor07, fg=cor01)
l_total_.place(x=450, y=12)


# CRIANDO SEGUNDO LABEL
l_qtd = Label(frameMeio, text='', width=14, height=2,
              anchor=CENTER, font=('Ivi 17 bold'), bg=cor07, fg=cor01)
l_qtd.place(x=450, y=90)

l_qtd_ = Label(frameMeio, text='  Quantidade total de itens  ', height=1,
               anchor=NW, font=('Ivi 10 bold'), bg=cor07, fg=cor01)
l_qtd_.place(x=450, y=92)


# editando frame baixo



janela.mainloop()
