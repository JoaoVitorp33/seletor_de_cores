from tkinter import *
import tkinter.messagebox

# Cores

cor0 = "#444466" #black
cor1 = "#feffff" #white
cor2 = "#004338"

# Criando a janela

janela = Tk()
janela.geometry("530x205")
janela.configure(bg=cor1)

# Configurando a janela

tela = Label(janela, bg=cor0, width=40, height=10, bd=1)
tela.grid(row=0, column=0)

frame_direita = Frame(janela, bg=cor1)
frame_direita.grid(row=0, column=1, padx=5)

frame_baixo = Frame(janela, bg=cor1)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)

# Função scale

def escala(valor):
    r=s_red.get()
    g=s_green.get()
    b=s_blue.get()
      
    rgb = f'{r}, {g}, {b}'
    
    hexadecimal = "#%02x%02x%02x" % (r,g,b)
    
    # Alterando a cor do fundo da tela
    
    tela['bg'] = hexadecimal
    
    # Alterando a entry
    
    e_cor.delete(0,END)
    e_cor.insert(0,hexadecimal)
    
# Função clicar

def onClick():
    # Informar
    tkinter.messagebox.showinfo('Cor', "a cor foi copiada")
    
    #Serve para criar o botão copiar
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy()

# Configurando frame direita

l_red = Label(frame_direita, text='Red', bg=cor1, width=7, fg='red', anchor='nw', font=('Time New Roman', 12, "bold"))
l_red.grid(row=0, column=0)
s_red = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='red', orient=HORIZONTAL)
s_red.grid(row=0, column=1)

l_green = Label(frame_direita, text='Green', bg=cor1, width=7, fg='green', anchor='nw', font=('Time New Roman', 12, "bold"))
l_green.grid(row=1, column=0)
s_green = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='green', orient=HORIZONTAL)
s_green.grid(row=1, column=1)

l_blue = Label(frame_direita, text='Blue', bg=cor1, width=7, fg='blue', anchor='nw', font=('Time New Roman', 12, "bold"))
l_blue.grid(row=2, column=0)
s_blue = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='blue', orient=HORIZONTAL)
s_blue.grid(row=2, column=1)

# Configurando frame baixo

l_rgb = Label(frame_baixo, text='CÓDDIGO HEX :', bg=cor1, font=('Ivy', 10, "bold"))
l_rgb.grid(row=0, column=0, padx=5)

#Entry

e_cor = Entry(frame_baixo, width=12, font=('Ivy', 10, "bold"), justify=CENTER)
e_cor.grid(row=0, column=1, padx=5)

#Botão Copiar

b_copiar = Button(frame_baixo, command=onClick, text='Copiar a cor', bg=cor1, font=('Ivy', 8, "bold"), relief=RAISED, overrelief=RIDGE)
b_copiar.grid(row=0, column=2, padx=5)

#App nome

l_app_nome = Label(frame_baixo, text='Seletor de Cores', bg=cor1, font=('Ivy', 15, "bold"))
l_app_nome.grid(row=0, column=3, padx=40)


janela.mainloop()
