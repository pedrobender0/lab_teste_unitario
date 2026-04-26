from dominio.entidades.transacao import Saque
from dominio.repositorios.i_conta_repository import IContaRepository

class RealizarSaqueUseCase:
    def __init__(self, repositorio: IContaRepository):
        self.repositorio = repositorio

    def executar(self, numero_conta, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        
        conta = self.repositorio.buscar(numero_conta)
        if not conta:
            raise ValueError("Conta não encontrada.")
            
        if conta.saldo < valor:
            raise ValueError(f"Saldo insuficiente! Saldo atual: R$ {conta.saldo:.2f}")

        saque = Saque(valor)
        saque.registrar(conta)

        self.repositorio.salvar(conta)
        return conta


