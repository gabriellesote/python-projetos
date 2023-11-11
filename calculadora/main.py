from tkinter import *
from tkinter import ttk


# cores

cor1 = "#474646"    #cinza
cor2 = "#f5f3f2"    #branco
cor3 = "#fa52ec"    #rosa
cor4 = "#121112"    #preto
cor5 = "#1f092b"    #roxo

# criação da janela
janela =  Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor4)


# criação de frames
frame_tela = Frame(janela, width=235, height=50, bg=cor5)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor2)
frame_corpo.grid(row=1, column=0)

#criando botões

b_1 = Button(frame_corpo, text="C", width=11, height=2)
b_1.place(x=0, y=0)


# loop que faz a janela rodar
janela.mainloop()
