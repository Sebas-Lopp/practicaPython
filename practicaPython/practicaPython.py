import tkinter as tk
from tkinter import messagebox

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbedad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar_campos():
    limpiar_campos()

def guardar_datos():
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbedad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    datos = "Nombres: " + nombres + "\n" + "Edad: " + edad + " a�os\n" + "Estatura: " + estatura + "\n" + "Tel�fonos: " + telefono + "\n" + "G�nero: " + genero + "\n"

    with open("datos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")

    messagebox.showinfo("Informaci�n", "Datos guardados con �xito:\n\n" + datos)
    limpiar_campos()

ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")
var_genero = tk.IntVar()

lbNombre = tk.Label(ventana, text="Nombres:")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Tel�fono:")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbedad = tk.Entry(ventana)
tbedad.pack()

lbEstatura = tk.Label(ventana, text="Estatura:")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="G�nero:")
lbGenero.pack()
rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_campos)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
btnGuardar.pack()

ventana.mainloop()


