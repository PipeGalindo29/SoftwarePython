from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import re
import ast


# Creacion de mi ventana -------------------------------------------------------------------------------
MiVentana = Tk()
MiVentana.geometry('800x500') # Ancho y largo a la ventana principal
MiVentana.resizable(False, False) # Con esto hacemos que la ventana principal no se pueda ampliar o disminuir con el mouse
MiVentana.config(background="CadetBlue") # Damos color a la ventana principal
MiVentana.title("Cliente")

# Creacion de archivo .txt -----------------------------------------------------------------------------
archivo1 = open("Nombre.txt")
archivo2 = open("Contraseña.txt")



nombre_text = archivo1.read(11) # Leemos lo que esta en el archivo Nombre.txt
archivo1.close() # Cerramos archivo

contrasena_text = archivo2.read(3) # Leemos lo que esta en el archivo Contraseña.txt
archivo2.close() # Cerramos archivo


# Variables Globales -----------------------------------------------------------------------------------

cont = 0

# Primera Fase -----------------------------------------------------------------------------------------

Titulo1 = Label(MiVentana, text="-----------------------------------  Iniciar Sesión  -------------------------------------", font=("New York",20))
Titulo1.place(x=0, y=50, width=800, height=40) # Creamos un titulo para la ventana principal, dandole medidas y color

Fondo = Label(MiVentana, text="   ", font=("New York",20))
Fondo.place(x=0, y=460, width=800, height=40)

# Creamos nombres y cajas para la ventana principal, dandole medidas y color

Nombre1 = Label(MiVentana, text="Nombre: ", font=("Arial Bold",10),background="CadetBlue")
Nombre1.place(x=345, y=150, width=80, height=20)

Contrasena1 = Label(MiVentana, text="Contraseña: ", font=("Arial Bold",10),background="CadetBlue")
Contrasena1.place(x=325, y=170, width=80, height=20)

cajaNombre1 = Entry(MiVentana,background="CadetBlue")
cajaNombre1.place(x=400, y=150, width=100, height=20)

cajaContrasena1 = Entry(MiVentana,background="CadetBlue")
cajaContrasena1.place(x=400, y=170, width=100, height=20)

respuestaProgram = Label(MiVentana,background="CadetBlue")
respuestaProgram.place(x=300, y=190, width=300, height=20)


# Funciones ------------------------------------------------------------------------------------------

def DatosC():

    ventana_secundaria = Toplevel()
    ventana_secundaria.geometry('800x500')
    ventana_secundaria.title("Cliente")
    ventana_secundaria.config(background="CadetBlue")

    # Nombres ---------------------------------------------------------------------------

    Titulo1 = Label(ventana_secundaria,
                    text="-----------------------------------  Informacion  -------------------------------------",
                    font=("New York", 20))
    Titulo1.place(x=0, y=30, width=800, height=40)

    Fondo = Label(ventana_secundaria, text="   ", font=("New York", 20))
    Fondo.place(x=0, y=460, width=800, height=40)

    Nombre2 = Label(ventana_secundaria, text="Nombre: ", font=("Arial Bold", 10),background="CadetBlue")
    Nombre2.place(x=345, y=112, width=100, height=20)

    Apellido = Label(ventana_secundaria, text="Apellido: ", font=("Arial Bold", 10),background="CadetBlue")
    Apellido.place(x=345, y=134, width=100, height=20)

    Edad = Label(ventana_secundaria, text="Edad: ", font=("Arial Bold", 10),background="CadetBlue")
    Edad.place(x=360, y=156, width=100, height=20)

    Genero = Label(ventana_secundaria, text="Genero: ", font=("Arial Bold", 10),background="CadetBlue")
    Genero.place(x=350, y=178, width=100, height=20)

    Cedula = Label(ventana_secundaria, text="Cedula: ", font=("Arial Bold", 10),background="CadetBlue")
    Cedula.place(x=350, y=200, width=100, height=20)

    Ciudad = Label(ventana_secundaria, text="Ciudad: ", font=("Arial Bold", 10),background="CadetBlue")
    Ciudad.place(x=350, y=222, width=100, height=20)

    Direccion = Label(ventana_secundaria, text="Direccion: ", font=("Arial Bold", 10),background="CadetBlue")
    Direccion.place(x=335, y=244, width=100, height=20)

    Correo = Label(ventana_secundaria, text="Correo: ", font=("Arial Bold", 10),background="CadetBlue")
    Correo.place(x=350, y=266, width=100, height=20)

    respuestaEdad = Label(ventana_secundaria,background="CadetBlue")
    respuestaEdad.place(x=330, y=286, width=300, height=20)

    respuestaCedula = Label(ventana_secundaria,background="CadetBlue")
    respuestaCedula.place(x=330, y=286, width=300, height=20)

    respuestaGuardado = Label(ventana_secundaria, font=("Arial Bold", 20),background="CadetBlue")
    respuestaGuardado.place(x=150, y=386, width=750, height=50)
    # Cajas ------------------------------------------------------------------------------

    cajaNombre2 = Entry(ventana_secundaria,background="CadetBlue")
    cajaNombre2.place(x=400, y=112, width=100, height=20)

    cajaApellido = Entry(ventana_secundaria,background="CadetBlue")
    cajaApellido.place(x=400, y=134, width=100, height=20)

    cajaEdad = Entry(ventana_secundaria,background="CadetBlue")
    cajaEdad.place(x=400, y=156, width=100, height=20)

    cajaGenero = Entry(ventana_secundaria,background="CadetBlue")
    cajaGenero.place(x=400, y=178, width=100, height=20)

    cajaCedula = Entry(ventana_secundaria,background="CadetBlue")
    cajaCedula.place(x=400, y=200, width=100, height=20)

    cajaCiudad = Entry(ventana_secundaria,background="CadetBlue")
    cajaCiudad.place(x=400, y=222, width=100, height=20)

    cajaDireccion = Entry(ventana_secundaria,background="CadetBlue")
    cajaDireccion.place(x=400, y=244, width=100, height=20)

    cajaCorreo = Entry(ventana_secundaria,background="CadetBlue")
    cajaCorreo.place(x=400, y=266, width=100, height=20)


    def soluciones():
        edad = int(cajaEdad.get())
        cedula = cajaCedula.get()
        edad1 = cajaEdad.get()
        nombre = cajaNombre2.get()
        apellido = cajaApellido.get()
        genero = cajaGenero.get()
        ciudad = cajaCiudad.get()
        direccion = cajaDireccion.get()
        correo = cajaCorreo.get()

        if(len(cedula) < 8):
            respuestaCedula["text"] = "Error, la cedula tiene menos de 8 digitos"
            print("Error, la cedula tiene menos de 8 digitos")
        else:
            respuestaCedula.destroy()
            if (edad < 30):
                respuestaEdad["text"] = "la persona tiene menos de 30 años"
                print("La persona tiene menos de 30 años")
                respuestaGuardado["text"] = "Los datos se han guardado correctamente"

                # Creacion del archivo final
                archivo_final = open("archivo_final.txt", "w")
                archivo_final.write("Nombre: ")
                archivo_final.write(nombre)
                archivo_final.write("\n")
                archivo_final.write("Apellido: ")
                archivo_final.write(apellido)
                archivo_final.write("\n")
                archivo_final.write("Edad: ")
                archivo_final.write(edad1)
                archivo_final.write("\n")
                archivo_final.write("Genero: ")
                archivo_final.write(genero)
                archivo_final.write("\n")
                archivo_final.write("Cedula: ")
                archivo_final.write(cedula)
                archivo_final.write("\n")
                archivo_final.write("Ciudad: ")
                archivo_final.write(ciudad)
                archivo_final.write("\n")
                archivo_final.write("Direccion: ")
                archivo_final.write(direccion)
                archivo_final.write("\n")
                archivo_final.write("Correo: ")
                archivo_final.write(correo)
                archivo_final.write("\n")
                archivo_final.close()
            elif (edad > 60):
                respuestaEdad["text"] = "la persona tiene mas de 60 años"
                print("La persona tiene mas de 60 años")
                respuestaGuardado["text"] = "Los datos se han guardado correctamente"

                #Creacion del archivo final
                archivo_final = open("archivo_final.txt","w")
                archivo_final.write("Nombre: ")
                archivo_final.write(nombre)
                archivo_final.write("\n")
                archivo_final.write("Apellido: ")
                archivo_final.write(apellido)
                archivo_final.write("\n")
                archivo_final.write("Edad: ")
                archivo_final.write(edad1)
                archivo_final.write("\n")
                archivo_final.write("Genero: ")
                archivo_final.write(genero)
                archivo_final.write("\n")
                archivo_final.write("Cedula: ")
                archivo_final.write(cedula)
                archivo_final.write("\n")
                archivo_final.write("Ciudad: ")
                archivo_final.write(ciudad)
                archivo_final.write("\n")
                archivo_final.write("Direccion: ")
                archivo_final.write(direccion)
                archivo_final.write("\n")
                archivo_final.write("Correo: ")
                archivo_final.write(correo)
                archivo_final.write("\n")
                archivo_final.close()

    def borrar_sec():
        # Delete odo ------------------------------------------------------------------------
        Nombre2.destroy()
        Apellido.destroy()
        Edad.destroy()
        Genero.destroy()
        Cedula.destroy()
        Direccion.destroy()
        Correo.destroy()
        respuestaEdad.destroy()
        respuestaCedula.destroy()
        boton1.destroy()

        # Nombres ---------------------------------------------------------------------------

        Nombre3 = Label(ventana_secundaria, text="Nombre: ", font=("Arial Bold", 10),background="CadetBlue")
        Nombre3.place(x=345, y=112, width=100, height=20)

        Apellido1 = Label(ventana_secundaria, text="Apellido: ", font=("Arial Bold", 10),background="CadetBlue")
        Apellido1.place(x=345, y=134, width=100, height=20)

        Edad1 = Label(ventana_secundaria, text="Edad: ", font=("Arial Bold", 10),background="CadetBlue")
        Edad1.place(x=360, y=156, width=100, height=20)

        Genero1 = Label(ventana_secundaria, text="Genero: ", font=("Arial Bold", 10),background="CadetBlue")
        Genero1.place(x=350, y=178, width=100, height=20)

        Cedula1 = Label(ventana_secundaria, text="Cedula: ", font=("Arial Bold", 10),background="CadetBlue")
        Cedula1.place(x=350, y=200, width=100, height=20)

        Ciudad1 = Label(ventana_secundaria, text="Ciudad: ", font=("Arial Bold", 10),background="CadetBlue")
        Ciudad1.place(x=350, y=222, width=100, height=20)

        Direccion1 = Label(ventana_secundaria, text="Direccion: ", font=("Arial Bold", 10),background="CadetBlue")
        Direccion1.place(x=335, y=244, width=100, height=20)

        Correo1 = Label(ventana_secundaria, text="Correo: ", font=("Arial Bold", 10),background="CadetBlue")
        Correo1.place(x=350, y=266, width=100, height=20)

        respuestaEdad1 = Label(ventana_secundaria,background="CadetBlue")
        respuestaEdad1.place(x=330, y=286, width=300, height=20)

        respuestaCedula1 = Label(ventana_secundaria,background="CadetBlue")
        respuestaCedula1.place(x=330, y=286, width=300, height=20)

        respuestaGuardado1 = Label(ventana_secundaria, font=("Arial Bold", 20),background="CadetBlue")
        respuestaGuardado1.place(x=150, y=386, width=750, height=50)
        # Cajas ------------------------------------------------------------------------------

        cajaNombre3 = Entry(ventana_secundaria,background="CadetBlue")
        cajaNombre3.place(x=400, y=112, width=100, height=20)

        cajaApellido1 = Entry(ventana_secundaria,background="CadetBlue")
        cajaApellido1.place(x=400, y=134, width=100, height=20)

        cajaEdad1 = Entry(ventana_secundaria,background="CadetBlue")
        cajaEdad1.place(x=400, y=156, width=100, height=20)

        cajaGenero1 = Entry(ventana_secundaria,background="CadetBlue")
        cajaGenero1.place(x=400, y=178, width=100, height=20)

        cajaCedula1 = Entry(ventana_secundaria,background="CadetBlue")
        cajaCedula1.place(x=400, y=200, width=100, height=20)

        cajaCiudad1 = Entry(ventana_secundaria,background="CadetBlue")
        cajaCiudad1.place(x=400, y=222, width=100, height=20)

        cajaDireccion1 = Entry(ventana_secundaria,background="CadetBlue")
        cajaDireccion1.place(x=400, y=244, width=100, height=20)

        cajaCorreo1 = Entry(ventana_secundaria,background="CadetBlue")
        cajaCorreo1.place(x=400, y=266, width=100, height=20)

        def soluciones1():
            edad2 = int(cajaEdad1.get())
            cedula1 = cajaCedula1.get()
            edad1 = cajaEdad.get()
            nombre = cajaNombre2.get()
            apellido = cajaApellido.get()
            genero = cajaGenero.get()
            ciudad = cajaCiudad.get()
            direccion = cajaDireccion.get()
            correo = cajaCorreo.get()

            if (len(cedula1) < 8):
                respuestaCedula1["text"] = "Error, la cedula tiene menos de 8 digitos"
                print("Error, la cedula tiene menos de 8 digitos")
            else:
                respuestaCedula1.destroy()
                if (edad2 < 30):
                    respuestaEdad1["text"] = "la persona tiene menos de 30 años"
                    print("La persona tiene menos de 30 años")
                    respuestaGuardado1["text"] = "Los datos se han guardado correctamente"

                    # Creacion del archivo final
                    archivo_final = open("archivo_final.txt", "w")
                    archivo_final.write("Nombre: ")
                    archivo_final.write(nombre)
                    archivo_final.write("\n")
                    archivo_final.write("Apellido: ")
                    archivo_final.write(apellido)
                    archivo_final.write("\n")
                    archivo_final.write("Edad: ")
                    archivo_final.write(edad1)
                    archivo_final.write("\n")
                    archivo_final.write("Genero: ")
                    archivo_final.write(genero)
                    archivo_final.write("\n")
                    archivo_final.write("Cedula: ")
                    archivo_final.write(cedula1)
                    archivo_final.write("\n")
                    archivo_final.write("Ciudad: ")
                    archivo_final.write(ciudad)
                    archivo_final.write("\n")
                    archivo_final.write("Direccion: ")
                    archivo_final.write(direccion)
                    archivo_final.write("\n")
                    archivo_final.write("Correo: ")
                    archivo_final.write(correo)
                    archivo_final.write("\n")
                    archivo_final.close()
                elif (edad1 > 60):
                    respuestaEdad1["text"] = "la persona tiene mas de 60 años"
                    print("La persona tiene mas de 60 años")
                    respuestaGuardado1["text"] = "Los datos se han guardado correctamente"

                    # Creacion del archivo final
                    archivo_final = open("archivo_final.txt", "w")
                    archivo_final.write("Nombre: ")
                    archivo_final.write(nombre)
                    archivo_final.write("\n")
                    archivo_final.write("Apellido: ")
                    archivo_final.write(apellido)
                    archivo_final.write("\n")
                    archivo_final.write("Edad: ")
                    archivo_final.write(edad1)
                    archivo_final.write("\n")
                    archivo_final.write("Genero: ")
                    archivo_final.write(genero)
                    archivo_final.write("\n")
                    archivo_final.write("Cedula: ")
                    archivo_final.write(cedula1)
                    archivo_final.write("\n")
                    archivo_final.write("Ciudad: ")
                    archivo_final.write(ciudad)
                    archivo_final.write("\n")
                    archivo_final.write("Direccion: ")
                    archivo_final.write(direccion)
                    archivo_final.write("\n")
                    archivo_final.write("Correo: ")
                    archivo_final.write(correo)
                    archivo_final.write("\n")
                    archivo_final.close()

        boton3 = Button(ventana_secundaria, text="Guardar", command=soluciones1)
        boton3.place(x=375, y=306, width=80, height=20)



    boton1 = Button(ventana_secundaria, text="Guardar", command=soluciones)
    boton1.place(x=375, y=306, width=80, height=20)

    boton2 = Button(ventana_secundaria, text="Borrar", command=borrar_sec)
    boton2.place(x=375, y=326, width=80, height=20)

    ventana_secundaria.focus()
    ventana_secundaria.grab_set()




def IngresaC():
    nombre = cajaNombre1.get()
    contrasena = cajaContrasena1.get()
    global cont, archivo1


    if(cont < 3):
        if ((nombre != nombre_text) | (contrasena != contrasena_text)):
            respuestaProgram["text"] = "El nombre o la contraseña son incorrectos"
            cont = cont+1
            print(cont)
        else:
            respuestaProgram["text"] = "Los datos que ha ingresado son correctos"
            DatosC()
    else:
        messagebox.showinfo(title="Error", message="Ha superado el numero de intentos")


def Borrar():
    cajaNombre1.destroy()
    cajaContrasena1.destroy()
    boton1.destroy()

    Nombre2 = Label(MiVentana, text="Nombre: ", font=("Arial Bold", 10),background="CadetBlue")
    Nombre2.place(x=345, y=150, width=80, height=20)

    Contrasena2 = Label(MiVentana, text="Contraseña: ", font=("Arial Bold", 10),background="CadetBlue")
    Contrasena2.place(x=325, y=170, width=80, height=20)

    cajaNombre2 = Entry(MiVentana,background="CadetBlue")
    cajaNombre2.place(x=400, y=150, width=100, height=20)

    cajaContrasena2 = Entry(MiVentana,background="CadetBlue")
    cajaContrasena2.place(x=400, y=170, width=100, height=20)

    def IngresaC1():
        nombre = cajaNombre2.get()
        contrasena = cajaContrasena2.get()
        global cont

        if (cont < 3):
            if ((nombre != nombre_text) | (contrasena != contrasena_text)):
                respuestaProgram["text"] = "El nombre o la contraseña son incorrectos"
                cont = cont + 1
                print(cont)
            else:
                respuestaProgram["text"] = "Los datos que ha ingresado son correctos"
                DatosC()
        else:
            messagebox.showinfo(title="Error", message="Ha superado el numero de intentos")

    boton3 = Button(MiVentana, text="Ingresar", command=IngresaC1)
    boton3.place(x=375, y=210, width=80, height=20)

# Botones --------------------------------------------------------------------------------------------

boton1 = Button(MiVentana, text="Ingresar", command=IngresaC)
boton1.place(x=375, y=210, width=80, height=20)


boton2 = Button(MiVentana, text="Borrar", command=Borrar)
boton2.place(x=375, y=230, width=80, height=20)




MiVentana.mainloop()