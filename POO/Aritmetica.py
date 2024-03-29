class Aritmetica:
    """
    Clase Arítmetica para realizar las operaciones de sumar, restar, etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(5, 3)
print(f'La suma es: {aritmetica1.sumar()}')
print(f'La resta es: {aritmetica1.restar()}')
print(f'La multiplicación es: {aritmetica1.multiplicar()}')
print(f'La división es: {aritmetica1.dividir():.2f}')