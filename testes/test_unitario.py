import unittest
from unittest.mock import Mock
from dominio.entidades.conta import Conta

class TestUnitario(unittest.TestCase):
#EXERCÍCIO 7.1 - TESTE UNITÁRIO
    def test_investir_poupanca(self):
        # Arrange
        conta = Conta(numero=123, cliente="Pedro", saldo_inicial=100.0)
        valor_investimento = 40.0

        # Act
        resultado = conta.investir_poupanca(valor_investimento)

        # Assert
        self.assertTrue(resultado)
        self.assertEqual(conta.saldo, 60.0)
        self.assertEqual(conta.saldo_poupanca, 40.0)

#EXERCÍCIO 7.5 - TDD

    def test_aplicar_rendimento_poupanca_deve_aumentar_saldo_em_meio_porcento(self):
        # Arrange
        cliente_mock = Mock()
        conta = Conta(numero=123, cliente=cliente_mock)

        conta.saldo_poupanca = 1000.0

        # Act
        # Na hora que chamei, esse método não existe
        conta.aplicar_rendimento_poupanca()

        # Assert
        self.assertEqual(conta.saldo_poupanca, 1005.0)


if __name__ == '__main__':
    unittest.main()