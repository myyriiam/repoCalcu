
class Operaciones:
    def __init__(self):
        self.salir = False

    def suma(self):
        print('\n-------------- SUMA --------------')
        first_number = float(input('Ingresa el primer número : '))
        second_number = float(input('Ingresa el segundo número : '))
        suma = first_number + second_number
        print('La SUMA es: '+ str(suma))
        print('---------------------------------- \n')

    def resta(self):
        print('\n-------------- RESTA --------------')
        first_number = float(input('Ingresa el primer número : '))
        second_number = float(input('Ingresa el segundo número : '))
        resta = first_number - second_number
        print('La RESTA es: '+ str(resta))