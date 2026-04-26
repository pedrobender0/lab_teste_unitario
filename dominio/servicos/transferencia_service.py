class ServicoTransferencia:

    def __init__(self, validador_fraude, notificador):
        self.validador_fraude = validador_fraude
        self.notificador = notificador

    def transferir(self, conta_origem, conta_destino, valor):
        if not self.validador_fraude.is_seguro(conta_origem, valor):
            return False

        if conta_origem.sacar(valor):
            conta_destino.depositar(valor)

            self.notificador.enviar_email(conta_origem.cliente, "Transferência realizada com sucesso")
            return True

        return False