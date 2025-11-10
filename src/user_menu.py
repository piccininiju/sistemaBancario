from tkinter import *
from datetime import datetime, timedelta

def user_menu(janela, clear, exit, bank, ind):
    def back_menu():
        clear()
        user_menu(janela, clear, exit, bank, ind)

    def destroy_widgets(widgets):
        for widget in widgets:
            widget.destroy()

    def show_message(message, color='black'):
        Label(text=message, font='Lato 16', fg=color).pack(pady=10, padx=10)

    def deposit():
        clear()
        msg = Label(text='\nQual o valor do depósito?', font='Lato 16')
        msg.pack(pady=10)
        val = Entry(font='Lato 16')
        val.pack(padx=20, pady=20)

        btns = Frame()
        btns.pack(padx=20, pady=20)
        enter = Button(btns, text='Confirma', font='Lato 16', command=lambda: confirm_deposit([msg, val, btns]))
        enter.pack(side='left', padx=10)
        back = Button(btns, text='Voltar', font='Lato 16', command=back_menu)
        back.pack(side='left')

        def confirm_deposit(widgets):
            retorno = bank.deposit(ind, val.get())
            destroy_widgets(widgets)
            show_message(retorno, color='green')
            Button(text='Voltar', font='Lato 16', command=back_menu).pack(padx=20, pady=20)

    def balance():
        clear()
        show_message(f'\nSeu saldo é: R${bank.get_balance(ind): .2f}')
        Button(text='Voltar', font='Lato 16', command=back_menu).pack(padx=20, pady=20)

    def withdrawal():
        clear()
        msg = Label(text='\nQual o valor do saque?', font='Lato 16')
        msg.pack(padx=20, pady=20)
        val = Entry(font='Lato 16')
        val.pack(padx=20, pady=20)

        btns = Frame()
        btns.pack(pady=10)
        enter = Button(btns, text='Confirma', font='Lato 16', command=lambda: confirm_withdrawal([msg, val, btns]))
        enter.pack(side='left', padx=10)
        back = Button(btns, text='Voltar', font='Lato 16', command=back_menu)
        back.pack(side='left')

        def confirm_withdrawal(widgets):
            retorno = bank.withdrawal(ind, val.get())
            destroy_widgets(widgets)
            show_message(retorno)
            Button(text='Voltar', font='Lato 16', command=back_menu).pack(padx=20, pady=20)

    def overdraft():
        clear()
        show_message(bank.get_overdraft(ind))
        Button(text='Voltar', font='Lato 16', command=back_menu).pack(padx=20, pady=20)

    def adress():
        clear()
        msg = Label(text='\nQual seu novo endereço?', font='Lato 16')
        msg.pack(padx=20, pady=20)
        val = Entry(font='Lato 16')
        val.pack(padx=20, pady=20)

        btns = Frame()
        btns.pack(pady=10)
        enter = Button(btns, text='Confirma', font='Lato 16', command=lambda: confirm_address([msg, val, btns]))
        enter.pack(side='left', padx=10)
        back = Button(btns, text='Voltar', font='Lato 16', command=back_menu)
        back.pack(side='left')

        def confirm_address(widgets):
            retorno = bank.address(ind, val.get())
            destroy_widgets(widgets)
            show_message(retorno)
            Button(text='Voltar', font='Lato 16', command=back_menu).pack(padx=20, pady=20)

    def delete():
        clear()
        ok, retorno = bank.close_request(ind)

        def confirm():
            clear()
            show_message(retorno)
            Button(text='Voltar', font='Lato 16', command=back_menu).pack(padx=20, pady=20)

        if ok:
            show_message('\nQuer solicitar a exclusão da conta?')
            btns = Frame()
            btns.pack(pady=10)
            Button(btns, text='Sim', font='Lato 16', command=confirm).pack(side='left', padx=10)
            Button(btns, text='Não', font='Lato 16', command=back_menu).pack(side='left')
        else:
            confirm()

    def transfer():
        clear()
        msgAG = Label(text='\nQual a agência de destino?', font='Lato 16')
        msgAG.pack(padx=20, pady=20)
        valAG = Entry(font='Lato 16')
        valAG.pack(padx=20, pady=20)
        msgCC = Label(text='\nQual a conta de destino?', font='Lato 16')
        msgCC.pack(padx=20, pady=20)
        valCC = Entry(font='Lato 16')
        valCC.pack(padx=20, pady=20)

        btns = Frame()
        btns.pack(pady=10)
        enter = Button(btns, text='Confirma', font='Lato 16',
                       command=lambda: confirm_account([msgAG, valAG, msgCC, valCC, btns]))
        enter.pack(side='left', padx=10)
        back = Button(btns, text='Voltar', font='Lato 16', command=back_menu)
        back.pack(side='left')

        def confirm_account(widgets):
            ok_to, ind_to = bank.check_account(valAG.get(), valCC.get())
            destroy_widgets(widgets)
            if ok_to:
                val = Label(text='\nQual o valor da transferência?', font='Lato 16')
                val.pack()
                inp = Entry(font='Lato 16')
                inp.pack(padx=20, pady=20)

                btns2 = Frame()
                btns2.pack(pady=10)
                go = Button(btns2, text='Confirma', font='Lato 16',
                            command=lambda: confirm_transfer([val, inp, btns2], ind_to, inp))
                go.pack(side='left', padx=10)
                Button(btns2, text='Voltar', font='Lato 16', command=back_menu).pack(side='left')
            else:
                show_message('\nConta ou agência de destino não encontrada', 'red')
                Button(text='Voltar', font='Lato 16', command=back_menu).pack()

        def confirm_transfer(widgets, ind_to, inp):
            retorno = bank.transfer(ind, ind_to, inp.get())
            destroy_widgets(widgets)
            show_message(retorno)
            Button(text='Voltar', font='Lato 16', command=back_menu).pack(padx=20, pady=20)

    def statement():
        clear()
        msgInit = Label(text="Data de INÍCIO (dd/mm/aaaa)", font='Lato 16')
        msgInit.pack(padx=20, pady=20)
        data_inicio_entry = Entry(font='Lato 16')
        data_inicio_entry.pack(padx=20, pady=20)
        msgEnd = Label(text="Data de FIM (dd/mm/aaaa)", font='Lato 16')
        msgEnd.pack(padx=20, pady=20)
        data_fim_entry = Entry(font='Lato 16')
        data_fim_entry.pack(padx=20, pady=20)

        btns = Frame()
        btns.pack(pady=10)
        bnt = Button(btns, text="Ver Extrato", font='Lato 16',
                     command=lambda: confirmar([msgInit, data_inicio_entry, msgEnd, data_fim_entry, btns]))
        bnt.pack(side='left', padx=10)
        Button(btns, text='Voltar', font='Lato 16', command=back_menu).pack(side='left')

        def confirmar(widgets):
            try:
                _from = datetime.strptime(data_inicio_entry.get(), "%d/%m/%Y")
                _to = datetime.strptime(data_fim_entry.get(), "%d/%m/%Y") + timedelta(hours=23, minutes=59, seconds=59)
                destroy_widgets(widgets)
                resultado = bank.statement(ind, _from, _to)
                show_message("Extrato gerado com sucesso!", color='green')
                Label(text=resultado, font='Lato 14').pack(pady=10, padx=10)
            except ValueError:
                show_message("Formato de data inválido. Use dd/mm/aaaa", color='red')
            Button(text='Voltar', font='Lato 16', command=back_menu).pack(padx=20, pady=20)

    # Menu principal do usuário
    options = [
        ("Deposito", deposit),
        ("Saldo", balance),
        ("Saque", withdrawal),
        ("Transferência", transfer),
        ("Extrato", statement),
        ("Troca de endereço", adress),
        ("Solicitar exclusão da conta", delete),
        ("Limite do cheque especial", overdraft),
        ("Sair", exit),
    ]

    for btn_text, func in options:
        Button(text=btn_text, font='Lato 16', command=func).pack(pady=3, padx=10)
