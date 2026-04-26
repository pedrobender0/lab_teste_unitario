from dominio.entidades.cliente import Cliente
from dominio.entidades.historico import Historico

class Conta:
    def __init__(self, numero: int, cliente: Cliente, saldo_inicial: float = 0.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.saldo_poupanca = 0
        self.historico = Historico()

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False
    
    def investir_poupanca(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.saldo_poupanca += valor
            return True
        return False