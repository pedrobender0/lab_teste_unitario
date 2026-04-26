import unittest
from dominio.entidades.conta import Conta
from dominio.entidades.cliente import Cliente

def test_saque_com_saldo_suficiente():
    cliente = Cliente(nome="João", cpf="12345678900")
    conta = Conta(numero=123, cliente=cliente, saldo_inicial=500.0)
    
    resultado = conta.sacar(200.0)
    
    assert resultado == True
    assert conta.saldo == 300.0

def test_saque_com_saldo_insuficiente():
    cliente = Cliente(nome="João", cpf="12345678900")
    conta = Conta(numero=123, cliente=cliente, saldo_inicial=100.0)
    
    resultado = conta.sacar(200.0)
    
    assert resultado == False
    assert conta.saldo == 100.0

def test_investimento_poupanca_com_sucesso():
    
    cliente = Cliente(nome="Pedro", cpf="11122233344")
    conta = Conta(numero=124, cliente=cliente, saldo_inicial=500.0)
    
    resultado = conta.investir_poupanca(200.0)
    
    assert resultado == True
    assert conta.saldo == 300.0          
    assert conta.saldo_poupanca == 200.0

if __name__ == '__main__':
    unittest.main()