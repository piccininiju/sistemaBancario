class user:
    def __init__(self, name, address):
        self.name = name  # Define o nome do usuário
        self.address = address  # Define o endereço do usuário
        self.user_accounts = []  # Lista que armazena as contas associadas ao usuário

    def change_address(self, new_address):
        self.address = new_address  # Atualiza o endereço do usuário

    def add_account(self, new_account):
        self.user_accounts.append(new_account)  # Adiciona a nova conta à lista de contas do usuário

