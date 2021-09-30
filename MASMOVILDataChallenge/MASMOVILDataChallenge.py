
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")
 
class Trabajador(Persona):
    """Clase que representa a un Trabajador"""

    def __init__(self, nombre, edad, departamento, puesto):
        """Constructor de clase Trabajador"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, nombre, edad)

        # Nuevos atributos
        self.departamento = departamento
        self.puesto = puesto
    
    def presentation(self):
        super().presentation()
        print(f"Mi departamento es {self.departamento} y mi puesto es {self.puesto}")

		
nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()

nombre2='Fernando'
trabajador_1 = Trabajador(nombre2,35,'BigData','DataAnalyst')
trabajador_1.presentation()
