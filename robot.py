class Robot:

    #Constructor: Se ejecuta al crear una instacia y permite inicializar los atributos
    #self = this (Se refieren a la instancia especifica)
    def __init__(self, nombre, tipo):
        #Atributos
        self.nombre = nombre
        self.tipo = tipo

    #Metodos
    #Es necesario pasar el self como argumento
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre} y soy un robot en una muestra de Robots.")

#Instancia
robotin = Robot("Robotín", "Humanoide")

print(robotin.nombre)
print(robotin.tipo)