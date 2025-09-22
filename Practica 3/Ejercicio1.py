import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        self.numeroDeVidas = 3
    def actualizaRecord(self):
        self.record += 1
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivine un número entre el 0 y el 10")
        while self.numeroDeVidas > 0:
            print("Te quedan", self.numeroDeVidas, "vidas.")
            entrada = input("Ingresa tu número: ")
            numero = int(entrada)
            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if numero < self.numeroAAdivinar:
                    print("El número secreto es mayor.")
                else:
                    print("El número secreto es menor.")
                if self.quitaVida():
                    print("Intenta nuevamente...")
                else:
                    print("¡Te quedaste sin vidas!")
                    print("El número correcto era:", self.numeroAAdivinar)
class Aplicacion:
    def main(self):
        juego = JuegoAdivinaNumero(3)
        juego.juega()
app = Aplicacion()
app.main()