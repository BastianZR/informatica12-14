class Paciente(): 
    def __init__(self):  
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def verServicio(self):
        return self.__servicio 

    def asignarNombre(self,n):
        self.__nombre = n
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarGenero(self,g):
        self.__genero = g
    def asignarServicio(self,s):
        self.__servicio = s 

class Sistema():
    def __init__(self):
        # self.__lista_pacientes = {} #Manejar los pacientes en lista, objeto tipo diccionario
        self.__lista_pacientes = [] #Manejar los pacientes en lista, objeto tipo lista.
        #La siguiente variable siempre dependera del tamaño de la lista, por lo cual no se podra modificar
        # con un método de asignar
        

    def ingresarPaciente(self,p):
        #Solicitar datos
        #Guardar paciente en la lista
        # self.__lista_pacientes[p.verCedula()]= p
        self.__lista_pacientes.append(p)
     
    def verNumeroPacientes(self,c):
        print("En el sistema hay: " + str(len(self.__lista_pacientes))+ "pacientes")
       
    def verDatosPacientes(self,c):
        for p in self.__lista_pacientes:
            if c==p.verCedula():
                return p
def main():
    sis=Sistema()
    while True:
        opcion = int(input("ingrese 0 para salir, 1 para ingresar nuevo paciente, 2 ver paciente: "))
        if opcion == 1:
            print("A continuación se solicitan los datos ")
            nombre = input("Ingrese el Nombre: ")
            cedula =int(input("Ingrese la Cédula: "))
            genero =input("Ingrese el Género: ")
            servicio = input("Ingrese el Servicio: ")

            #Crear objeto Paciente y le asigno los datos
            p = Paciente()
            p.asignarNombre(nombre)
            p.asignarCedula(cedula)
            p.asignarGenero(genero)
            p.asignarServicio(servicio)
            sis.ingresarPaciente(p)
        elif opcion == 2:
            c=int(input("Ingrese la cédula a buscar: "))
            p=sis.verDatosPacientes(c)
            print("Nombre: " + p.verNombre())
            print("Cédula: " + star(p.verCedula()))
            print("Género: " + p.verGenero())
            print("Servicio: " + p.verServicio())
        elif opcion !=0:
            continue
        else:
            break


if __name__=="__main__":
    main()
