import pytest
import os
from infraestrutura.arquivo_conta_repository import ArquivoContaRepository
from aplicacao.realizar_saque_use_case import RealizarSaqueUseCase
from dominio.entidades.cliente import Cliente
from dominio.entidades.conta import Conta

def test_integracao_saque_e_salvamento_no_arquivo():
    # 1. ARRANGE (Preparação)
    repositorio = ArquivoContaRepository()
    repositorio.arquivo = "banco_de_teste.txt" 
    
    if os.path.exists(repositorio.arquivo):
        os.remove(repositorio.arquivo)
        
    # Cadastra uma conta diretamente no arquivo com R$ 1000,00
    cliente = Cliente(nome="Maria", cpf="09876543211")
    conta_inicial = Conta(numero=999, cliente=cliente, saldo_inicial=1000.0)
    repositorio.salvar(conta_inicial)
    
    # Instancia o Caso de Uso passando o nosso repositório
    use_case = RealizarSaqueUseCase(repositorio)
    
    # 2. ACT (Ação)
    # Executa o saque através do caso de uso (como a tela do sistema faria)
    use_case.executar(numero_conta=999, valor=300.0)
    
    # 3. ASSERT (Verificação)
    conta_atualizada = repositorio.buscar(999)
    
    assert conta_atualizada is not None
    assert conta_atualizada.saldo == 700.0
    
    # Limpeza do arquivo temporário no final do teste
    if os.path.exists(repositorio.arquivo):
        os.remove(repositorio.arquivo)