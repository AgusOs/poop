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

    def hacerTruco(self):
        if self.tipo == "Humanoide":
            print(f"Soy {self.nombre} y estoy haciendo el paso del robot")
        else:
            print(f"Soy {self.tipo} de tipo {self.tipo}")

#Instancia
robotin = Robot("Robotín", "Humanoide")

robotin.hacerTruco()

print(robotin.nombre)
print(robotin.tipo)