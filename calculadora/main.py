from tkinter import *
from tkinter import ttk


# cores

cor1 = "#474646"    #cinza
cor2 = "#f5f3f2"    #branco
cor3 = "#ffa20d"    #laranja
cor4 = "#121112"    #preto
cor5 = "#253352"    #azul

# criação da janela
janela =  Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor4)





# criação de frames
frame_tela = Frame(janela, width=235, height=50, bg=cor5)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor2)
frame_corpo.grid(row=1, column=0)

# Criando labels
valor_texto = StringVar()

# variavel todos valores
todos_valores = ''

# Criando Função
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    valor_texto.set(todos_valores)

# função para calcular

def calcular():
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor5, fg=cor2)

app_label.place(x=0, y=0)

# Criando botões
# primeira linha

b_clear = Button(frame_corpo, command = limpar_tela, text="C", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)

b_porcentagem = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_porcentagem.place(x=118, y=0)

b_divisao = Button(frame_corpo,command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_divisao.place(x=177, y=0)


# segunda linha

b_n7 = Button(frame_corpo,command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n7.place(x=0, y=52)

b_n8 = Button(frame_corpo,command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n8.place(x=59, y=52)

b_n9 = Button(frame_corpo,command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n9.place(x=118, y=52)

b_multiplicacao = Button(frame_corpo,command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_multiplicacao.place(x=177, y=52)


# terceira linha

b_n4 = Button(frame_corpo,command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n4.place(x=0, y=104)

b_n5 = Button(frame_corpo,command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n5.place(x=59, y=104)

b_n6 = Button(frame_corpo,command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n6.place(x=118, y=104)

b_subtracao = Button(frame_corpo,command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_subtracao.place(x=177, y=104)

# quarta linha

b_n1 = Button(frame_corpo,command = lambda: entrar_valores('1'),text="1", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n1.place(x=0, y=156)

b_n2 = Button(frame_corpo,command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n2.place(x=59, y=156)

b_n3 = Button(frame_corpo,command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n3.place(x=118, y=156)

b_soma = Button(frame_corpo,command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_soma.place(x=177, y=156)

# quinta linha

b_n0 = Button(frame_corpo,command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_n0.place(x=0, y=208)

b_ponto = Button(frame_corpo, command = lambda: entrar_valores('.'),text=".", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_ponto.place(x=118, y=208)

b_igual = Button(frame_corpo,command = calcular, text="=", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=208)



# loop que faz a janela rodar
janela.mainloop()
