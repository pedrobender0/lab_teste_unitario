from dominio.entidades.cliente import Cliente
from dominio.entidades.conta import Conta
from dominio.entidades.transacao import Deposito

class CriarContaUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.proximo_numero = 1001

    def executar(self, nome, cpf, saldo_inicial):
        if not nome or not cpf: raise ValueError("Nome e CPF obrigatórios!")
        if saldo_inicial < 0: raise ValueError("Saldo inicial não pode ser negativo.")

        cliente = Cliente(nome, cpf)
        conta = Conta(self.proximo_numero, cliente, 0.0)
        self.proximo_numero += 1

        if saldo_inicial > 0:
            deposito = Deposito(saldo_inicial)
            deposito.registrar(conta)

        self.repositorio.salvar(conta)
        return conta

class RealizarDepositoUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def executar(self, numero_conta, valor):
        if valor <= 0: raise ValueError("Valor deve ser maior que zero.")
        conta = self.repositorio.buscar(numero_conta)
        if not conta: raise ValueError("Conta não encontrada.")

        deposito = Deposito(valor)
        deposito.registrar(conta)
        self.repositorio.salvar(conta)
        return conta

class ObterHistoricoUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def executar(self, numero_conta):
        conta = self.repositorio.buscar(numero_conta)
        if not conta: raise ValueError("Conta não encontrada.")
        return conta, conta.historico.transacoes