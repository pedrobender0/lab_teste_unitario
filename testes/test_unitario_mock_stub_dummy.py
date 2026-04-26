import unittest
from unittest.mock import Mock

from dominio.entidades.conta import Conta
from dominio.servicos.transferencia_service import ServicoTransferencia


class TestServicoTransferencia(unittest.TestCase):

    def test_transferencia_valida_com_notificacao(self):
        # Dummy
        cliente_dummy = Mock()

        # Stub
        stub_validador = Mock()
        stub_validador.is_seguro.return_value = True

        # Mock
        mock_notificador = Mock()

        # Arrange
        conta_origem = Conta(numero=1, cliente=cliente_dummy, saldo_inicial=100.0)
        conta_destino = Conta(numero=2, cliente=cliente_dummy, saldo_inicial=0.0)

        servico = ServicoTransferencia(validador_fraude=stub_validador, notificador=mock_notificador)

        # Act
        resultado = servico.transferir(conta_origem, conta_destino, 50.0)

        # Assert
        self.assertTrue(resultado)
        self.assertEqual(conta_origem.saldo, 50.0)
        self.assertEqual(conta_destino.saldo, 50.0)

        mock_notificador.enviar_email.assert_called_once_with(
            cliente_dummy,
            "Transferência realizada com sucesso"
        )


if __name__ == '__main__':
    unittest.main()
