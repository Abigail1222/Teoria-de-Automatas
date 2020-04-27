from tkinter import *
#1941416hv1941416vhvheduardoeduardo cadena valida
#1941416hvhvhv1941416vhvhvhvhvhvhveduardoeduardo cadena invalida

class Validacion:
    w = "hv"
    i = "1941416"
    j = "eduardo"
    alfabeto = "1946eduarohv"
    def validarAlfabeto (cadena):
        caracteresInvalidos = "\0"
        for char in cadena:
            if char not in Validacion.alfabeto:
                if caracteresInvalidos == "\0":
                    caracteresInvalidos = ""
                caracteresInvalidos += char
        return caracteresInvalidos
    def validarCadena (cadena):
        a = "0"
        n = 0 #Numero de repeticiones
        subCadenaMedio = ""
        subCadenasW = ""
        if a == "0": # Validación numero 1, ver si la matricula esta al principio
            mat = cadena[:len(Validacion.i)]
            if mat != Validacion.i:
                a = "1"
    
        if a == "0": # Valdación numero 2, ver si al final de la cadena está j2
            nombre = cadena[len(cadena)-(len(Validacion.j) * 2):]
            j2 = Validacion.j + Validacion.j
            if nombre != j2:
                a = "2"
        
        if a == "0": # Validación numero 3, ver si en la cadena de en medio esta la matricula
            subCadenaMedio = cadena[:len(cadena)-(len(Validacion.j) * 2)]
            subCadenaMedio = subCadenaMedio[len(Validacion.i):]
            if Validacion.i not in subCadenaMedio:
                a = "3"

        if a == "0": # Validacion nnumero 4, Valida la subcadena w de la izquierda
            if subCadenaMedio[:len(Validacion.i)] == Validacion.i:
                a = "42"
            else:
                subCadenasW = subCadenaMedio.split(Validacion.i)
                n = 0
                for i in range(len(subCadenasW[0])):
                    if subCadenasW[0][i] == Validacion.w[i%2]:
                        n += 1
                    else:
                        a = "4"
                        break
                if (n%2 == 1 and a == "0"):
                    a = "41" # No esta completo w (hvhvh)
                n = n/2

        if a == "0": #Validacion numero 5, valida w de la derecha
            counter = 0
            if subCadenasW[1] == "":
                a = "53"
            else:
                for i in range(len(subCadenasW[1])):
                    if subCadenasW[1][i] == Validacion.w[(i+1)%2]:
                        counter +=1
                    else:
                        a = "5"
                        break
                if (counter % 2 == 1 and a == "0"):
                    a = "51"
                counter = counter / 2
                if (counter != 2*n and a == "0"):
                    a = "52" # No esta completo wi vhvhv
        return a
Validacion.validarCadena = staticmethod(Validacion.validarCadena)

def funcion_cadena():
    cadena=enter.get("1.0","end-1c")
    respuesta = Validacion.validarAlfabeto(cadena)
    if (respuesta != "\0"):
        impresion_tk["text"]="La cadena es invalida \n Se encontraron los siguientes caracteres que no estan en el alfabeto: " + str(respuesta)
    else:
        respuesta = Validacion.validarCadena(cadena)
        if respuesta != "0":
            impresion_tk["text"]="La cadena es invalida"
        if respuesta == "0":
            impresion_tk["text"]="La cadena es valida"
        elif respuesta == "1":
            impresion_tk["text"]="i (matricula) no encontrada al principio de la cadena"
        elif respuesta == "2":
            impresion_tk["text"]="j al cuadrado no encontrado al final de la cadena"
        elif respuesta == "3":
             impresion_tk["text"]="i (matricula) no encontrada en medio de la cadena"
        elif respuesta == "4":
            impresion_tk["text"]="Error en wn despues de la i (matricula) al principio, posibles errores:\nCaracteres de w en desorden\nSe encontraron caracteres no pertenecientes a w"     
        elif respuesta == "41":
            impresion_tk["text"]="Cadenas de w incompletas"
        elif respuesta == "42":
            impresion_tk["text"]="No se encontro w entre la primera y segunda i (matricula)"
        elif respuesta == "5":
            impresion_tk["text"]="Error en (wI)2n despues de la i (matricula) de en medio, posibles errores:\nCaracteres de (wI) en desorden\nSe encontraron caracteres no pertenecientes a (wI)"
        elif respuesta == "51":
            impresion_tk["text"]="Cadenas de (wI) incompletas"
            
        elif respuesta == "52":
            impresion_tk["text"]="(wI) no se repite el doble de veces que las veces que se repitio w"
            
        elif respuesta == "53":
            impresion_tk["text"]="No se encontro (wI)"
            



ventana=Tk()
ventana.geometry("1000x700")

main_title=Label(text="Evidencia de Aprendizaje 2", font=("Arial", 20,"normal"), justify="center")
main_title.pack(padx=10,pady=10)
main_title=Label(text="Este programa analizará una cadena e indicará si es válida o no con base a la siguiente gramática:", font=("Arial", 12,"normal"), justify="center")
main_title.pack(padx=10,pady=10)
main_title=Label(text="L = { i (w)n i (wI)2n j2 | w = hv, i = 1941416, w(inversa) = vh, j = eduardo, n≥ 1 }",font=("Arial", 10,"normal"))
main_title.pack(padx=10,pady=10)
main_title=Label(text="Solo usar letras minúsculas y sin acentos", font=("Arial", 12,"normal"), justify="center")
main_title.pack(padx=10,pady=10)
main_title=Label(text="Ingrese una cadena", font=("Arial", 12,"normal","bold"), justify="center")
main_title.pack(padx=10,pady=10)

enter=Text(ventana, font=("Calibri",15,"normal"),height=1, width=110)
enter.pack(padx=10,pady=10)

obtain_data=Button(ventana,text="Enter",font=("Arial", 15,"normal"), justify="center",command=lambda: funcion_cadena())#command=lambda:funcion_cadena(enter.get()))
obtain_data.place(x=5, y=5) 
obtain_data.pack(padx=54,pady=5)
btn = Button(ventana, text='Limpiar espacio', font=("Arial",15,"normal"), command=lambda: enter.delete(1.0,END))
btn.pack()

impresion_tk=Label(ventana,fg="black", font=("Calibri",12,"normal"),justify="center")
impresion_tk.pack(padx=10,pady=10)


ventana.mainloop()
