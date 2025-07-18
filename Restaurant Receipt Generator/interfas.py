from tkinter import * # para la interfaz
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''  # almacena los numeros precionados en la calculadora
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


def obtener_total():
    global operador
    resultado = str(eval(operador)) # eval nos devueve un int,por lo que la tenemos que guardar en un str
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    """
    sera llaada cada que un check fue marcado, si es asi, establece el cuadro de cmomida
    :return:
    """
    x = 0 # contador para las listas de verificacion
    for c in cuadros_comida:
        if variables_comida[x].get() == 1: # si esta activado, get obten valor
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END) # se elimina el 0
            cuadros_comida[x].focus() # el punsor se ve titiniansi en el espacio
        else: # desactivaos cuadro
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0') # si se desactiva vuelve el 0
        x += 1

    x = 0  # contador para las listas de verificacion
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:  # si esta activado, get obten valor
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)  # se elimina el 0
            cuadros_bebida[x].focus()  # el punsor se ve titiniansi en el espacio
        else:  # desactivaos cuadro
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')  # si se desactiva vuelve el 0
        x += 1

    x = 0  # contador para las listas de verificacion
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:  # si esta activado, get obten valor
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)  # se elimina el 0
            cuadros_postres[x].focus()  # el punsor se ve titiniansi en el espacio
        else:  # desactivaos cuadro
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')  # si se desactiva vuelve el 0
        x += 1


def total():
    """
    sumara la cantidad de comida, en base al tipo y cantidad, ademas de los impuesto
    :return:
    """
    sub_total_comida = 0
    indice = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get())* precios_comida[indice])
        indice += 1
    print(sub_total_comida)

    sub_total_bebida = 0
    indice = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[indice])
        indice += 1
    print(sub_total_bebida)

    sub_total_postres = 0
    indice = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[indice])
        indice += 1
    print(sub_total_postres)

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'${round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'${round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'${round(sub_total_postres, 2)}')
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_impuesto.set(f'${round(impuestos, 2)}')
    var_total.set(f'${round(total, 2)}')


def recibo():

    # nos aseguramos que el tiquet quede completamente en blanco
    texto_recibo.delete(1.0, END)
    numero_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 57 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 70 + '\n')


    indice = 0

    for comida in texto_comida:
        if comida.get() != '0': #solo revisamos aquellas comidas que fueron seleccionadas
            texto_recibo.insert(END, f'{lista_comidas[indice]}\t\t{comida.get()}\t'
                                           f'${int(comida.get()) * precios_comida[indice]}\n')
        indice += 1

    indice = 0

    for bebida in texto_bebida:
        if bebida.get() != '0':  # solo revisamos aquellas comidas que fueron seleccionadas
            texto_recibo.insert(END, f'{lista_bebidas[indice]}\t\t{bebida.get()}\t'
                                     f'${int(bebida.get()) * precios_bebida[indice]}\n')
        indice += 1

    indice = 0

    for postre in texto_postres:
        if postre.get() != '0':  # solo revisamos aquellas comidas que fueron seleccionadas
            texto_recibo.insert(END, f'{lista_postres[indice]}\t\t{postre.get()}\t'
                                     f'${int(postre.get()) * precios_postres[indice]}\n')
        indice += 1

    texto_recibo.insert(END, f'-' * 70 + '\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 70 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 57 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')


def guardar():
    informacion_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(informacion_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    # limpiamos el cuadro de texto
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    # variables comida guarda el valor 1 o 0 del check box
    for variables in variables_comida:
        variables.set(0)
    for variables in variables_bebida:
        variables.set(0)
    for variables in variables_postres:
        variables.set(0)

    # reseteamos los paneles de costo
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

# iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# evitar maximizar
# aplicacion.resizable(0, 0)
aplicacion.resizable(False, False)


# -------------------------------------
# Establecer titulo y color pagina
# -------------------------------------


# establecer titulo en la ventana
aplicacion.title('Mi Restaurante - Sistema de facturación')

# color fondo de la ventana
aplicacion.config(bg='burlywood')

# -------------------------------------
# Panel superior
# -------------------------------------


panel_superior = Frame(aplicacion, bd=1,  relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Dosis', 55), bg='burlywood', width=24)
etiqueta_titulo.grid(row=0, column=0)

# -------------------------------------
# Panel menu
# -------------------------------------


panel_izquierdo = Frame(aplicacion, bd=1,  relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1,  relief=FLAT, bg='azure4', padx=90)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)


# -------------------------------------
# Panel derecha
# -------------------------------------


panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()


# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# -------------------------------------
# lista productos
# -------------------------------------


lista_comidas = ['pollo', 'pozole', 'gorditas', 'tacos', 'enchiladas', 'quesadillas', 'mole', 'tamales']
lista_bebidas = ['agua', 'cola cola', 'horchata', 'jamaica', 'tamarindo', 'cerveza', 'tequila', 'cafe']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mouse', 'pastel1', 'pastel2', 'pastel3']


# -------------------------------------
# Generar items comida
# -------------------------------------


variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    # CREAR CHECKNUTTON
    variables_comida.append('')
    variables_comida[contador] = IntVar()  # esta variable contiene el 0 o 1 del check button
    # onvalue -> valor de checkbutton cuando se activa la casilla, off value cuando se desactiva
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)  # sticky es para justificar a la izquierda

    # CREAR LOS CUADROS DE ENTRADA
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,  # solo se activa al seleccionar platillo
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1


# -------------------------------------
# Generar items bebida
# -------------------------------------


variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebidas in lista_bebidas:

    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas,
                          text=bebidas.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_bebida[contador],
                          command=revisar_check)
    bebidas.grid(row=contador,
                 column=0,
                 sticky=W)  # sticky es para justificar a la izquierda
    # CREAR LOS CUADROS DE ENTRADA
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1


# -------------------------------------
# Generar items postres
# -------------------------------------


variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador],
                          command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)  # sticky es para justificar a la izquierda

    # CREAR LOS CUADROS DE ENTRADA
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    contador += 1


# -------------------------------------
# Etiquetas de costos comida
# -------------------------------------

# variables
var_costo_comida = StringVar()

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,  # esta en modo lectura
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)


# -------------------------------------
# Etiquetas de costos bebida
# -------------------------------------


# variables
var_costo_bebida = StringVar()

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,  # esta en modo lectura
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# -------------------------------------
# Etiquetas de costos postre
# -------------------------------------


# variables
var_costo_postre = StringVar()

etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,  # esta en modo lectura
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)


# -------------------------------------
# Etiquetas subtotal
# -------------------------------------


# variables
var_subtotal = StringVar()

etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')

etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,  # esta en modo lectura
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)


# -------------------------------------
# Etiquetas impuestos
# -------------------------------------


# variables
var_impuesto = StringVar()

etiqueta_impuesto = Label(panel_costos,
                          text='Impuesto',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')

etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,  # esta en modo lectura
                       textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)


# -------------------------------------
# Etiquetas Total
# -------------------------------------


# variables
var_total = StringVar()

etiqueta_total = Label(panel_costos,
                       text='total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')

etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,  # esta en modo lectura
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)


# -------------------------------------
# Botones
# -------------------------------------


botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 9, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)

    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)


# -------------------------------------
# Area recibo
# -------------------------------------


texto_recibo = Text(panel_recibo,
                    font=('Dosis', 9, 'bold'),
                    bd=1,
                    width=42,
                    height=16)
texto_recibo.grid(row=0, column=0)


# -------------------------------------
# Area calculadora
# -------------------------------------


visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=23,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'CE', 'R', '0', '/']

botones_guardados = []

fila = 1
columna = 0 # Haremos columnas del 1 a la 3
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                     text=boton.title(),
                     font=('Dosis', 15, 'bold'),
                     fg='white',
                     bg='azure4',
                     bd=1,
                     width=5
                     )
    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1 #agregamos valores a filacada ves que llegue a la tercera columna
    columna += 1
    if columna >= 4:
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
botones_guardados[12].config(command=obtener_total)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# evitar que la aplicacion se cierra
aplicacion.mainloop()