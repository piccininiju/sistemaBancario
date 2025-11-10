from tkinter import *


def adm_menu(janela, clear, exit, bank):
    """
    Menu do administrador. Permite visualizar solicitações de exclusão,
    buscar contas por agência/conta e retornar ao menu principal.

    Parâmetros:
        - janela: janela principal da aplicação
        - clear: função para limpar a interface
        - exit: função que volta ao menu inicial
        - bank: instância do banco com dados de contas
    """

    # === Funções auxiliares ===

    def back_menu():
        """Limpa a tela e retorna ao menu de administrador."""
        clear()
        adm_menu(janela, clear, exit, bank)

    def destroy_widgets(widgets):
        """Remove da tela todos os widgets fornecidos em uma lista."""
        for w in widgets:
            w.destroy()

    # === Funcionalidades administrativas ===

    def accept(ind):
        """
        Aceita e executa a remoção de uma conta que solicitou exclusão.
        """
        retorno = bank.adm_remove(ind)
        clear()
        Label(text=retorno, font='Lato 14').pack(pady=10, padx=10)
        Button(text='Voltar', font='Lato 16', command=back_menu).pack(pady=10, padx=10)

    def exclude():
        """
        Mostra as solicitações de exclusão de contas. Permite aceitá-las.
        """
        retorno, ind = bank.removeList()
        clear()
        Label(text='Você possui as seguintes solicitações: ', font='Lato 16').pack(pady=10, padx=10)
        Label(text=retorno, font='Lato 14').pack(pady=10, padx=10)

        if len(bank.requests) != 0:
            Button(text='Aceita solicitação', font='Lato 16', command=lambda: accept(ind)).pack(pady=10, padx=10)

        Button(text='Voltar', font='Lato 16', command=back_menu).pack(pady=10, padx=10)

    def search():
        """
        Busca uma conta com base em número da agência e conta. Exibe dados do cliente.
        """
        clear()

        def entrar(a, b):
            """Executa a busca por conta e exibe os dados, se encontrados."""
            destroy_widgets([msgAG, msgCC, ag, cc, go])
            try:
                agencia = int(a)
                conta = int(b)
                ok, ind = bank.check_account(agencia, conta)

                if ok:
                    clear()
                    lista = Frame()
                    lista.pack(pady=10, padx=10)

                    acc = bank.accounts[ind]
                    Label(lista, text='Nome: ' + acc.acc_holder.name, font='Lato, 16').pack(pady=10, padx=10)
                    Label(lista, text='Endereço: ' + str(acc.acc_holder.address), font='Lato, 16').pack(pady=10, padx=10)
                    Label(lista, text='Tipo de conta: ' + str(acc.acc_type), font='Lato, 16').pack(pady=10, padx=10)
                    Label(lista, text=f'Saldo: R${acc.balance: .2f}', font='Lato, 16').pack(pady=10, padx=10)
                    Label(lista, text=f'Limite cheque especial: R${acc.overdraft: .2f}', font='Lato, 16').pack(pady=10, padx=10)
                    Button(text='Voltar', font='Lato 16', command=back_menu).pack(pady=10, padx=10)
                else:
                    raise ValueError
            except:
                Label(text='\nErro: Conta ou agência não encontrada', font='Lato 16').pack(pady=10, padx=10)
                Button(text='Voltar', font='Lato 16', command=back_menu).pack(pady=10, padx=10)

        # Campos para entrada de dados da conta a buscar
        msgAG = Label(text='\nDigite o número da agência: ', font='Lato 16')
        msgAG.pack(pady=10, padx=10)
        ag = Entry(font='Lato 16')
        ag.pack(pady=10, padx=10)

        msgCC = Label(text='\nDigite o número da conta: ', font='Lato 16')
        msgCC.pack(pady=10, padx=10)
        cc = Entry(font='Lato 16')
        cc.pack(pady=10, padx=10)

        go = Button(text='Pesquisar', font='Lato 16', command=lambda: entrar(ag.get(), cc.get()))
        go.pack(pady=10, padx=10)


    # === Menu com botões ===

    # Cada botão chama uma função relacionada à administração
    options = [
        ('Solicitações de exclusão de conta', exclude),
        ('Buscar cliente', search),
        ('Sair', exit)
    ]

    for txt, cmd in options:
        Button(text=txt, font='Lato 16', command=cmd).pack(pady=3, padx=10)
