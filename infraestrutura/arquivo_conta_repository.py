import json
import os
from dominio.repositorios.i_conta_repository import IContaRepository
from dominio.entidades.conta import Conta
from dominio.entidades.cliente import Cliente

class ArquivoContaRepository(IContaRepository):
    def __init__(self):
        self.arquivo = "contas.txt"

    def _ler_dados(self):
        if not os.path.exists(self.arquivo):
            return {}
        with open(self.arquivo, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def salvar(self, conta):
        dados = self._ler_dados()
        
        dados[str(conta.numero)] = {
            "numero": conta.numero,
            "saldo": conta.saldo,
            "cliente": {"nome": conta.cliente.nome, "cpf": conta.cliente.cpf},
            "historico": conta.historico.transacoes
        }
        
        with open(self.arquivo, 'w') as f:
            json.dump(dados, f, indent=4)

    def buscar(self, numero):
        dados = self._ler_dados()
        numero_str = str(numero)
        
        if numero_str not in dados:
            return None
            
        c_dict = dados[numero_str]
        
        cliente = Cliente(c_dict["cliente"]["nome"], c_dict["cliente"]["cpf"])
        conta = Conta(c_dict["numero"], cliente, c_dict["saldo"])
        conta.historico.transacoes = c_dict["historico"]
        
        return conta


