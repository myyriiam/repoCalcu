
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
        exponente = np.power(numexp,potencia)
        print('El EXPONENTE de '+str(numexp)+ ' es : '+ str(exponente))
        print('---------------------------------------- \n')
    
    def seno(self):
        print('\n------------ SENO ------------')
        numseno = float(input('Ingresa el angulo en grados : '))
        radianes = (numseno * math.pi) / 180
        seno = math.sin(radianes)
        print('El SENO de '+str(numseno)+ ' es : '+ str(seno))
        print('---------------------------------------- \n')
    
    def coseno(self):
        print('\n------------ COSENO ------------')
        numcos = float(input('Ingresa el angulo en grados : '))
        rad = (numcos * math.pi) / 180
        coseno = math.cos(rad)
        print('El COSENO de '+str(numcos)+ ' es : '+ str(coseno))
        print('---------------------------------------- \n')
    
    
class Calculadora:
    def __init__(self):
        self.cerrarCalcu = False
    def menuInicio(self):
        while True:
            print('\n ********* CALCULADORA *********')
            print('\n Menú de Operaciones: ' 
                    + '\n 1. Sumar'
                    + '\n 2. Restar'
                    + '\n 3. Multiplicar'
                    + '\n 4. Dividir'
                    + '\n 5. Raiz n'
                    + '\n 6. Exponente n'
                    + '\n 7. Seno'
                    + '\n 8. Coseno'
                    + '\n 9. Salir'
                    + '\n\n *****************************')

            opcion = int(input('\n Selecciona una operación: '))
            #print('La opción seleccionada es: ' + str(opcion))
             
            if opcion == 1:
                    operaciones = Operaciones()
                    operaciones.suma()
            elif opcion == 2:
                    operaciones = Operaciones()
                    operaciones.resta()
            elif opcion == 3:
                    operaciones = Operaciones()
                    operaciones.multiplicar()
            elif opcion == 4:
                    operaciones = Operaciones()
                    operaciones.dividir()
            elif opcion == 5:
                    operaciones = Operaciones()
                    operaciones.raiz()
            elif opcion == 6:
                    operaciones = Operaciones()
                    operaciones.exponente()
            elif opcion == 7:
                    operaciones = Operaciones()
                    operaciones.seno()
            elif opcion == 8:
                    operaciones = Operaciones()
                    operaciones.coseno()
            elif opcion == 9:
                    print("Cerrando calculadora, adios!")
                    break
            else:
                    print("Opción incorrecta")

calculadora = Calculadora()
calculadora.menuInicio()

operaciones = Operaciones()


