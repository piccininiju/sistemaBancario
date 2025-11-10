from datetime import datetime  # Importa a classe datetime para registrar a data e hora das operações

class operation:
    def __init__(self, op_type, value, origin=None, destiny=None):
        self.op_type = op_type  # Define o tipo da operação
        self.value = value  # Define o valor movimentado na operação
        self.origin = origin  # Armazena a conta de origem (caso seja uma transferência)
        self.destiny = destiny  # Armazena a conta de destino (caso seja uma transferência)
        self.date = datetime.now()  # Registra a data e hora exata da operação


