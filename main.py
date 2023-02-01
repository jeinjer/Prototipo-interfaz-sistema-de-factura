from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def total():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)


def final():
    sub_total_comidas = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comidas = round((sub_total_comidas + float(cantidad.get()) * precios_comida[p]), 2)
        p += 1

    sub_total_bebidas = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebidas = round((sub_total_bebidas + float(cantidad.get()) * precios_bebida[p]), 2)
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = round((sub_total_postres + float(cantidad.get()) * precios_postres[p]), 2)
        p += 1

    subtotal = round((sub_total_comidas + sub_total_bebidas + sub_total_postres), 2)
    impuestos = round((subtotal * 0.07), 2)
    total = round((subtotal + impuestos), 2)

    var_costo_comida.set(f'${sub_total_comidas}')
    var_costo_bebida.set(f'${sub_total_bebidas}')
    var_costo_postre.set(f'${sub_total_postres}')
    var_subtotal.set(f'${subtotal}')
    var_impuesto.set(f'${impuestos}')
    var_total.set(f'${total}')


def recibo():
    texto_recibo.delete(1.0, END)
    numero_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Recibo\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, f'Items\t\tCant.\tCosto\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'${round((int(comida.get())*precios_comida[x]), 2)}\n')
            x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'${round((int(bebida.get())*precios_bebida[x]), 2)}\n')
            x += 1

    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                     f'${round((int(postre.get())*precios_postres[x]), 2)}\n')
            x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Costo Comidas: \t\t\t {var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo Bebidas: \t\t\t {var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo Postres: \t\t\t {var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t {var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t {var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Costo Total: \t\t\t {var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto!')


def guardar():
    informacion_recibo = texto_recibo.get(1.0, END)
    archivo_recibo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo_recibo.write(informacion_recibo)
    archivo_recibo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def revisar_check():
    x = 0
    for _ in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for _ in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1

    x = 0
    for _ in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def reset():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)
    for p in variables_comida:
        p.set(0)
    for p in variables_bebidas:
        p.set(0)
    for p in variables_postres:
        p.set(0)
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# iniciar tkinter
app = Tk()

# establecer tamaño de ventana
app.geometry('1220x630+200+220')

# evitar maximizar
app.resizable(0, 0)

# cambiar titulo
app.title('Gestor Restaurante')

# cambiar color de fondo de ventana
app.config(bg='lightblue')

# panel superior
pan_sup = Frame(app, bd=1, relief=FLAT)
pan_sup.pack(side=TOP)

# etiqueta de titulo
et_tit = Label(pan_sup,
               text='Sistema de facturacion',
               fg='azure4',
               font=('Dosis', 58),
               bg='lightblue',
               width=27)

et_tit.grid(row=0, column=0)

# panel izquierdo
pan_izq = Frame(app, bd=1, relief=FLAT)
pan_izq.pack(side=LEFT)

# panel costos
pan_costos = Frame(pan_izq, bd=1, relief=FLAT, bg='azure4', padx=50)
pan_costos.pack(side=BOTTOM)

# panel comidas
pan_comidas = LabelFrame(pan_izq,
                         text='Comida',
                         font=('Dosis', 19, 'bold'),
                         bd=1,
                         relief=FLAT,
                         fg='azure4')

pan_comidas.pack(side=LEFT)

# panel bebidas
pan_bebidas = LabelFrame(pan_izq,
                         text='Bebida',
                         font=('Dosis', 19, 'bold'),
                         bd=1,
                         relief=FLAT,
                         fg='azure4')

pan_bebidas.pack(side=LEFT)

# panel postres
pan_postres = LabelFrame(pan_izq,
                         text='Postre',
                         font=('Dosis', 19, 'bold'),
                         bd=1,
                         relief=FLAT,
                         fg='azure4')

pan_postres.pack(side=LEFT)

# panel derecha
pan_der = Frame(app, bd=1,
                relief=FLAT)
pan_der.pack(side=RIGHT)

# panel calculadora
pan_calc = Frame(pan_der,
                 bd=1,
                 relief=FLAT,
                 bg='lightblue')
pan_calc.pack()

# panel recibo
pan_recibo = Frame(pan_der,
                   bd=1,
                   relief=FLAT,
                   bg='lightblue')
pan_recibo.pack()

# panel botones
pan_botones = Frame(pan_der,
                    bd=1,
                    relief=FLAT,
                    bg='lightblue')
pan_botones.pack()

# lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Salmon', 'Merluza',
                 'Kebab', 'Pizza', 'Asado', 'Empanada']

lista_bebidas = ['Fernet', 'Agua', 'Sprite', 'Soda',
                 'Coca-Cola', 'Fanta', 'Vino tinto', 'Cerveza']

lista_postres = ['Flan', 'Torta', 'Lemon Pie', 'Helado', 'Fruta',
                 'Brownie', 'Mousse', 'Strudel']

# checkbuttons comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(pan_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)

    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(pan_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# checkbuttons bebida
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebida in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(pan_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebidas[contador],
                         command=revisar_check)

    bebida.grid(row=contador,
                column=0,
                sticky=W)
    # crear cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(pan_bebidas,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_bebidas[contador])

    cuadros_bebidas[contador].grid(row=contador,
                                   column=1)
    contador += 1

# checkbuttons postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(pan_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postres[contador],
                         command=revisar_check)

    postre.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(pan_postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])

    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costos de comida y campos de entrada
etiqueta_costo_comida = Label(pan_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0, column=0, padx=41)
texto_costo_comida = Entry(pan_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# etiquetas de costos de bebida y campos de entrada
etiqueta_costo_bebida = Label(pan_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_bebida.grid(row=1, column=0, padx=41)
texto_costo_bebida = Entry(pan_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# etiquetas de costos de postres y campos de entrada
etiqueta_costo_postre = Label(pan_costos,
                              text='Costo Postre',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_postre.grid(row=2, column=0, padx=41)
texto_costo_postre = Entry(pan_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# etiqueta de subtotal
etiqueta_subtotal = Label(pan_costos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')

etiqueta_subtotal.grid(row=0, column=2, padx=41)
texto_subtotal = Entry(pan_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# etiqueta de impuesto
etiqueta_impuesto = Label(pan_costos,
                          text='Impuesto',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')

etiqueta_impuesto.grid(row=1, column=2, padx=41)
texto_impuesto = Entry(pan_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# etiqueta de total
etiqueta_total = Label(pan_costos,
                       text='Total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')

etiqueta_total.grid(row=2, column=2, padx=41)
texto_total = Entry(pan_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ['Total', 'Recibo', 'Guardar', 'Reset']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(pan_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=final)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=reset)

# area de recibo
texto_recibo = Text(pan_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)

# calculadora
visor_calculadora = Entry(pan_calc,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

# botones calculadora
lista_botones = ['7', '8', '9', '+',
                 '4', '5', '6', '-',
                 '1', '2', '3', 'x',
                 '=', 'Borrar', '0', '/']
botones_guardados = []
fila, columna = 1, 0
for boton in lista_botones:
    boton = Button(pan_calc,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)

    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=total)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# mantener pantalla abierta
app.mainloop()
