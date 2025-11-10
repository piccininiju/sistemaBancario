from operation import operation  # Importa a classe operation para registrar operações na conta

class account:
    def __init__(self, agency, acc_number, acc_type, acc_holder, overdraft, balance = 0):
        # Inicializa os atributos da conta bancária
        self.agency = agency  # Número da agência
        self.acc_number = acc_number  # Número da conta
        self.acc_type = acc_type  # Tipo de conta ('cc' para conta corrente, 'cp' para poupança)
        self.acc_holder = acc_holder  # Titular da conta (objeto da classe user)
        self.balance = balance  # Saldo inicial da conta (padrão é 0)
        self.overdraft = overdraft  # Limite do cheque especial (aplicável para conta corrente)
        self.history = []  # Histórico de operações

    def deposit(self, amount):
        # Método para realizar um depósito na conta
        self.balance += amount  # Adiciona o valor ao saldo
        op = operation('Depósito', amount)  # Cria um registro de operação de depósito
        self.history.append(op)  # Adiciona a operação ao histórico da conta

    def withdrawal(self, amount):
        # Método para realizar um saque da conta
        available = self.balance + self.overdraft  # Define o valor disponível para saque (saldo + cheque especial, se aplicável)
        if self.balance >= amount:
            # Se há saldo suficiente, realiza o saque normalmente
            self.balance -= amount
            op = operation('Saque', amount)  # Registra a operação de saque
            self.history.append(op)  # Adiciona a operação ao histórico
            return True
        elif self.acc_type == 'cc':
            # Se for conta corrente, permite o uso do cheque especial
            if available >= amount:
                self.balance -= amount
                op = operation('Saque', amount)  # Registra a operação de saque
                self.history.append(op)
                return True
            else:
                return False  # Retorna falso se não houver fundos suficientes, mesmo com o cheque especial
        else:
            return False  # Retorna falso se não houver saldo suficiente (para contas que não sejam 'cc')

    def bank_statement(self, _from, _to):
        extrato = 'Extrato:\n'
        for op in self.history:
            if _from <= op.date <= _to:
                data_str = op.date.strftime('%d/%m/%Y %H:%M')
                if op.op_type == 'Transferência Enviada':
                    extrato += (f'\n{data_str} - {op.op_type} - '
                                f'R${op.value:.2f} - Para: {op.destiny.acc_holder.name} '
                                f'- Conta: {op.destiny.acc_type}')
                else:
                    extrato += f'\n{data_str} - {op.op_type} - R${op.value:.2f}'
        return extrato if extrato != 'Extrato:\n' else 'Nenhuma movimentação no período.'

