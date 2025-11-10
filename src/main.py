from tkinter import *
from user_menu import user_menu
from adm_menu import adm_menu
from bank import Bank

# Instância principal do banco
bank = Bank()

# Criação da janela principal
janela = Tk()
janela.geometry("900x800")

# Topo com o título
top = Frame(janela)
top.pack(side=TOP, fill=X)
rotulo = Label(top, text="CATBANK", foreground="purple")
rotulo.pack()
rotulo.configure(relief="ridge", font="Lato 24 bold", background="pink")

# === Funções auxiliares ===

def clear():
    """Remove todos os widgets da janela, exceto o topo."""
    for widget in janela.winfo_children():
        if widget != top :
            widget.destroy()

def destroy_widgets(widgets):
    """Destrói os widgets informados (atalho para evitar repetição)."""
    for widget in widgets:
        widget.destroy()

def close():
    """Fecha o aplicativo."""
    janela.destroy()

def exit():
    """Retorna ao menu inicial."""
    clear()
    init()

# === Telas de entrada ===

def userEntry():
    """Tela de login do usuário (cliente)."""
    clear()

    def backEntry():
        """Retorna à tela de login do usuário."""
        clear()
        userEntry()

    def entrar(agencia_txt, conta_txt):
        """Valida a conta e redireciona ao menu do usuário, se válida."""
        destroy_widgets([msgAG, msgCC, ag, cc, go, back])
        try:
            agencia = int(agencia_txt)
            conta = int(conta_txt)
            ok, ind = bank.check_account(agencia, conta)
            if ok:
                user_menu(janela, clear, exit, bank, ind)
            else:
                raise ValueError
        except:
            Label(text='\nErro: Conta ou agência não encontrada', font='Lato 16').pack(pady=10, padx=10)
            Button(text='Voltar', font='Lato 16', command=backEntry).pack(pady=10, padx=10)

    # Campos de entrada do usuário
    msgAG = Label(text='\nDigite o número da sua agência: ', font='Lato 16')
    msgAG.pack(pady=10, padx=10)
    ag = Entry(font='Lato 16')
    ag.pack(pady=10, padx=10)

    msgCC = Label(text='\nDigite o número da sua conta: ', font='Lato 16')
    msgCC.pack(pady=10, padx=10)
    cc = Entry(font='Lato 16')
    cc.pack(pady=10, padx=10)
    buttons = Frame()
    buttons.pack(pady=10)
    go = Button(buttons, text='Entrar', font='Lato 16', command=lambda: entrar(ag.get(), cc.get()))
    go.pack(side='left', pady=20)
    back = Button(buttons, text='Voltar', font='Lato 16', command=init)
    back.pack(side='left', padx=20)

def admEntry():
    """Tela de login do administrador."""
    clear()

    def backEntry():
        """Retorna à tela de login do administrador."""
        clear()
        admEntry()

    def entrar(ident_txt):
        """Valida o administrador e redireciona ao menu administrativo."""
        destroy_widgets([msgID, id, go, back])
        try:
            ok = bank.check_account_adm(ident_txt)
            if ok:
                adm_menu(janela, clear, exit, bank)
            else:
                raise ValueError
        except:
            Label(text='\nErro: Conta ou agência não encontrada', font='Lato 16').pack(pady=10, padx=10)
            Button(text='Voltar', font='Lato 16', command=backEntry).pack(pady=10, padx=10)

    # Campo de entrada de ID do administrador
    msgID = Label(text='\nDigite o número da sua identificação: ', font='Lato 16')
    msgID.pack(pady=10, padx=10)
    id = Entry(font='Lato 16')
    id.pack(pady=10, padx=10)
    buttons = Frame()
    buttons.pack(pady=10)
    go = Button(buttons, text='Entrar', font='Lato 16', command=lambda: entrar(id.get()))
    go.pack(side='left', pady=20)
    back = Button(buttons, text='Voltar', font='Lato 16', command=init)
    back.pack(side='left', padx=20)


# === Menu inicial ===

def init():
    """Tela inicial com opções para usuário, administrador ou sair."""
    clear()
    frame_btn = Frame()
    frame_btn.pack(pady=10)

    # Botões principais do menu
    a = Button(frame_btn, text="Usuário", font='Lato 16', command=userEntry)
    b = Button(frame_btn, text="Administrador", font='Lato 16', command=admEntry)
    c = Button(frame_btn, text="Sair", font='Lato 16', command=close)

    for w in (a, b, c):
        w.pack(side='left', padx=20, pady=20)

# Inicializa o programa
init()
janela.mainloop()
