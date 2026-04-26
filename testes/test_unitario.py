import unittest
from dominio.entidades.conta import Conta

class TestUnitario(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()