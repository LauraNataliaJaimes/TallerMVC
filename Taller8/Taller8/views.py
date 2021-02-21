#Todo en este proyecto sera la VISTA

from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object): #Clase persona

    def __init__ (self, nombre, apellido): #Constructor: self
        self.nombre = nombre
        self.apellido = apellido

def Vista1(request): #Nombre de la Vista(Request como parametro)
    return HttpResponse("<html><body><h1>Si sirveeee</h1></body></html>")

def Vista2(request): #Llamo al HTML que esta en otra carpeta - Forma larga
    html = open("D:/Documents/UIS/Programación en la Web/Django/Taller8/Taller8/Plantillas/prueba.html")
    plt=Template(html.read())

    html.close()

    p1 = Persona ("Natalia", "Jaimes")#Instancia de la clase Dentro de la Vista
    Ahora = datetime.datetime.now()
    
    ctx= Context({"Actual":Ahora, "Nombre":p1.nombre, "Apellido":p1.apellido}) #Diccionario - Invocar objetos

    documento = plt.render(ctx)

    return HttpResponse(documento)