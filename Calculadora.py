
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
        
    def multiplicar(self):
        print('\n------------ MULTIPLICACIÓN ------------')
        first_number = float(input('Ingresa el primer número : '))
        second_number = float(input('Ingresa el segundo número : '))
        multiplicacion = first_number * second_number
        print('La MULTIPLICACIÓN es: '+ str(multiplicacion))
        print('---------------------------------------- \n')

    def dividir(self):
        print('\n------------ DIVISIÓN ------------')
        first_number = float(input('Ingresa el primer número : '))
        second_number = float(input('Ingresa el segundo número : '))
        division = first_number / second_number
        print('La DIVISIÓN es: '+ str(division))
        print('---------------------------------------- \n')
    
    def raiz(self):
        print('\n------------ RAIZ n ------------')
        numero = float(input('Ingresa el número a calcular : '))
        grado = float(input('Ingresa el grado de la raíz: '))
        raizn = pow(numero,1/grado)
        print('La RAIZ '+ str(grado) + 'a de ' + str(numero) + ' es : '+ str(raizn))
        print('---------------------------------------- \n')

    def exponente(self):
        print('\n------------ EXPONENTE n ------------')
        numexp = float(input('Ingresa el número a calcular : '))
        potencia = float(input('Ingresa el número de potencia: '))
        #exponente = numexp ** potencia
        exponente = np.power(numexp,potencia)
        print('El EXPONENTE de '+str(numexp)+ ' es : '+ str(exponente))
        print('---------------------------------------- \n')