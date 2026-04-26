import pytest
import os
import tkinter as tk
from unittest.mock import patch

from infraestrutura.arquivo_conta_repository import ArquivoContaRepository
from aplicacao.realizar_saque_use_case import RealizarSaqueUseCase
from apresentacao.tela_principal import TelaPrincipal
from dominio.entidades.cliente import Cliente
from dominio.entidades.conta import Conta

def test_fluxo_funcional_saque_via_interface():
    # 1. ARRANGE (Preparação do ambiente)
    repositorio = ArquivoContaRepository()
    repositorio.arquivo = "banco_funcional.txt"
    if os.path.exists(repositorio.arquivo):
        os.remove(repositorio.arquivo)

    conta_teste = Conta(numero=777, cliente=Cliente(nome="Pedro", cpf="111"), saldo_inicial=500.0)
    repositorio.salvar(conta_teste)

    casos_de_uso = {
        "sacar": RealizarSaqueUseCase(repositorio)
    }

    root = tk.Tk()
    tela = TelaPrincipal(root, casos_de_uso)

    # Simular o usuário digitando nos campos de texto da aba de operações
    tela.entry_num_conta_op.insert(0, "777")
    tela.entry_valor_op.insert(0, "150.0")

    # 2. ACT (Ação)
    # 'patch' para "sequestrar" a caixa de mensagem, assim ela não aparece
    with patch('apresentacao.tela_principal.messagebox.showinfo') as mock_info:
        tela.sacar() 

    # 3. ASSERT (Verificação)
    # Garantir que a caixa de mensagem de sucesso foi chamada exatamente 1 vez
    mock_info.assert_called_once()
    
    argumentos_chamada, _ = mock_info.call_args
    titulo_janela = argumentos_chamada[0]
    texto_mensagem = argumentos_chamada[1]
    
    # Verificar se o usuário viu o que deveria ver
    assert titulo_janela == "Sucesso"
    assert "Saque efetuado!" in texto_mensagem
    assert "Novo saldo: R$ 350.00" in texto_mensagem

    # Verificar se o campo de valor foi limpo após o saque
    assert tela.entry_valor_op.get() == ""

    # Limpeza
    root.destroy()
    if os.path.exists(repositorio.arquivo):
        os.remove(repositorio.arquivo)