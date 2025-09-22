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
        self.numeroAAdivinar = random.randint(0, 10)
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    def juega(self):
        self.reiniciaPartida()
        print("Adivine un número entre el 0 y el 10")
        while self.numeroDeVidas > 0:
            print("Te quedan", self.numeroDeVidas, "vidas.")
            entrada = input("Ingresa un número: ")
            numero = int(entrada)
            if not self.validaNumero(numero):
                print("Error")
                continue
            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if numero < self.numeroAAdivinar:
                    print("El número secreto es mayor.")
                else:
                    print("El número secreto es menor.")
                if not self.quitaVida():
                    print("¡Te quedaste sin vidas!")
                    print("El número correcto era:", self.numeroAAdivinar)
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        pares = []
        for n in range(0, 11):
            if n % 2 == 0:
                pares.append(n)
        self.numeroAAdivinar = random.choice(pares)
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            if numero % 2 == 0:
                return True
            else:
                print("Solo se permiten números pares.")
                return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        impares = []
        for n in range(0, 11):
            if n % 2 != 0:
                impares.append(n)
        self.numeroAAdivinar = random.choice(impares)
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            if numero % 2 != 0:
                return True
            else:
                print("Solo se permiten números impares.")
                return False
class Aplicacion:
    def main(self):
        juego_normal = JuegoAdivinaNumero(3)
        juego_par = JuegoAdivinaPar(3)
        juego_impar = JuegoAdivinaImpar(3)
        print("=== Juego Normal ===")
        juego_normal.juega()
        print("=== Juego Pares ===")
        juego_par.juega()
        print("=== Juego Impares ===")
        juego_impar.juega()
app = Aplicacion()
app.main()