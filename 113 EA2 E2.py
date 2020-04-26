from tkinter import *
#1941416hv1941416vhvheduardoeduardo cadena valida
#1941416hvhvhv1941416vhvhvhvhvhvhveduardoeduardo cadena invalida

class Validacion:
    w = "hv"
    i = "1941416"
    j = "eduardo"
    alfabeto = "1946eduarohv"
    def validarAlfabeto (cadena):
        caracteresInvalidos = "0"
        for char in cadena:
            if char not in Validacion.alfabeto:
                if caracteresInvalidos == '0':
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
     #   print (a)

        if a == "0": # Validacion nnumero 4, Valida la subcadena w de la izquierda
            subCadenasW = subCadenaMedio.split(Validacion.i)
        #    print (subCadenasW)
            n = 0
            for i in range(len(subCadenasW[0])):
                if subCadenasW[0][i] == Validacion.w[i%2]:
                    n += 1
                else:
             #       print (i)
                    a = "4"
                    break
            if (n%2 == 1):
                a = "4"
            n = n/2
         #   print (n)
        if a == "0": #Validacion numero 5, valida w de la derecha
            counter = 0
            for i in range(len(subCadenasW[1])):
                if subCadenasW[1][i] == Validacion.w[(i+1)%2]:
                    counter +=1
                else:
                    a = "5"
                    break
            counter = counter / 2
            if counter != 2*n:
                a = "5"
        return a
        
Validacion.validarCadena = staticmethod(Validacion.validarCadena)

def funcion_cadena(lacadena):
    num=Validacion.validarCadena(lacadena)
    if num=="0":
         impresion_tk["text"]="La cadena es valida"
    
    else:
        impresion_tk["text"]="La cadena no es valida"



ventana=Tk()
ventana.geometry("1000x500")

main_title=Label(text="Evidencia de Aprendizaje 2", font=("Arial", 20,"normal"), justify="center")
main_title.pack(padx=10,pady=10)
main_title=Label(text="Este programa analizará una cadena e indicará si es válida o no con base a la siguiente gramática:", font=("Arial", 12,"normal"), justify="center")
main_title.pack(padx=10,pady=10)
main_title=Label(text="L = { i (w)n i (wI)2n j2 | w = hv, i = 1941416, w(inversa) = vh, j = alan, n≥ 1 }",font=("Arial", 10,"normal"))
main_title.pack(padx=10,pady=10)
main_title=Label(text="Solo usar letras minúsculas y sin acentos", font=("Arial", 12,"normal"), justify="center")
main_title.pack(padx=10,pady=10)
main_title=Label(text="Ingrese una cadena", font=("Arial", 12,"normal","bold"), justify="center")
main_title.pack(padx=10,pady=10)

enter=Entry(ventana, font=("Calibri",40,"normal"), justify="center")
enter.pack(padx=10,pady=10)

obtain_data=Button(ventana,text="Enter",font=("Arial", 15,"normal"), justify="center",command=lambda:funcion_cadena(enter.get()))
obtain_data.pack()

impresion_tk=Label(ventana,fg="black", font=("Calibri",25,"normal"),justify="center")
impresion_tk.pack(padx=10,pady=10)


ventana.mainloop()