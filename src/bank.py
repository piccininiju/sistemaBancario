from operation import operation
from user import user
from account import account
from userADM import userADM

class Bank:
    def __init__(self):
        # Criação de usuários com seus respectivos endereços
        user1 = user('Juvina Piccinini', 'Rua das flores, 02 - Botafogo, RJ')
        user2 = user('Dori Marie Piccinini', 'Rua das bolas de pelo, 05 - Botafogo, RJ')
        
        # Criação de contas associadas aos usuários
        account_user1 = account(1, 1, 'cc', user1, 300, 100)  # Conta corrente com saldo inicial de 300 e cheque especial de 100
        account_user2 = account(2, 1, 'cc', user2, 500, 200)  # Conta corrente com saldo inicial de 500 e cheque especial de 200
        account_user2_cp = account(2, 2, 'cp', user2, 0, 100)  # Conta poupança com saldo inicial de 0 e limite de 100
        adm1 = userADM(23)
        adm2 = userADM(34)

        # Associando contas aos usuários
        user1.user_accounts = [account_user1]
        user2.user_accounts = [account_user2, account_user2_cp]
        
        # Lista de usuários e contas no banco
        self.users = [user1, user2]
        self.accounts = [account_user1, account_user2, account_user2_cp]
        self.requests = []  # Lista de solicitações de exclusão de conta
        self.userADM = [adm1, adm2]

    def check_account_adm(self, id_):
        intId = int(id_)
        for i in range(len(self.userADM)):
            if self.userADM[i].id_adm == intId:
                return True
        return False

    def check_account(self, ag, cc):
        """Verifica se uma conta com a agência e conta informadas existe"""
        intAG = int(ag)
        intCC = int(cc)
        for i in range(len(self.accounts)):
            if self.accounts[i].agency == intAG and self.accounts[i].acc_number == intCC:
                return True, i
        return False, 0

    def deposit(self, ind, val):
        """Realiza um depósito na conta informada"""
        valInt = float(val)
        self.accounts[ind].deposit(valInt)
        return f'\nDepósito de R${valInt: .2f} realizado'

    def get_balance(self, ind):
        """Retorna o saldo da conta informada"""
        return self.accounts[ind].balance

    def withdrawal(self, ind, val):
        """Realiza um saque, se houver saldo suficiente"""
        valInt = float(val)
        if self.accounts[ind].withdrawal(valInt):
            return f'\nSaque de R${valInt: .2f} realizado'
        else:
            return '\nSaldo insuficiente'

    def get_overdraft(self, ind):
        """Informa o limite do cheque especial se a conta for corrente"""
        if self.accounts[ind].acc_type == 'cc':
            return f'\nSeu limite do cheque especial é R${self.accounts[ind].overdraft: .2f}'
        else:
            return '\nConta poupança não tem cheque especial!'

    def transfer(self, ind, ind_to, val):
        intVal = float(val)
        """Realiza uma transferência entre contas se houver saldo suficiente"""
        available = self.accounts[ind].balance + self.accounts[ind].overdraft
        if self.accounts[ind].balance >= intVal:
            self.accounts[ind].balance -= intVal
            self.accounts[ind_to].balance += intVal

            # Registra a operação nos históricos das contas
            op_from = operation('Transferência Enviada', intVal, self.accounts[ind], self.accounts[ind_to])
            self.accounts[ind].history.append(op_from)
            op_to = operation('Transferência Recebida', intVal, self.accounts[ind], self.accounts[ind_to])
            self.accounts[ind_to].history.append(op_to)
            return f'\nTransferência de R${intVal: .2f} para {self.accounts[ind_to].acc_holder.name}'

        elif self.accounts[ind].acc_type == 'cc' and available >= intVal:
            self.accounts[ind].balance -= intVal
            self.accounts[ind_to].balance += intVal

            # Registra a operação nos históricos das contas
            op_from = operation('Transferência Enviada', intVal, self.accounts[ind], self.accounts[ind_to])
            self.accounts[ind].history.append(op_from)
            op_to = operation('Transferência Recebida', intVal, self.accounts[ind], self.accounts[ind_to])
            self.accounts[ind_to].history.append(op_to)
            return f'\nTransferência de R${intVal: .2f} para {self.accounts[ind_to].acc_holder.name}'

        else:
            return '\nSaldo insuficiente, incluindo cheque especial'

    def address(self, ind, new_add):
        """Atualiza o endereço do usuário vinculado à conta informada"""
        for i in range(len(self.users)):
            if self.users[i] == self.accounts[ind].acc_holder:
                self.users[i].address = new_add
                return f'\nSeu novo endereço é {self.users[i].address}'
                break
    
    def close_request(self, ind):
        """Adiciona solicitação de exclusão de conta à lista de pedidos"""
        for i in range (len(self.requests)):
            if self.requests[i] == ind:
                return False, 'Solicitação de exclusão da conta já enviada. Aguarde a confirmação do administrador.'
        self.requests.append(ind)
        return True, 'Solicitação enviada! Aguarde a confirmação do administrador.'

    def removeList(self):
        """Função para administração do banco, processa pedidos de exclusão de conta"""
        if self.requests:
            aux = sorted(self.requests, reverse = True) # Remover do maior indice para o menor
            for ind in aux:
                return f'\nO usuário {self.accounts[ind].acc_holder.name} deseja excluir sua conta do tipo {self.accounts[ind].acc_type}.\n', ind
        else:
            return '\nNenhuma solicitação pendente', 0

    def adm_remove(self, ind):
        self.accounts[ind].acc_holder.user_accounts.remove(self.accounts[ind])
        self.accounts.remove(self.accounts[ind])
        self.requests.remove(ind)
        return '\nConta removida'



    def statement(self, ind, _from, _to):
        """Gera um extrato bancário dentro do período especificado"""
        return self.accounts[ind].bank_statement(_from, _to)


