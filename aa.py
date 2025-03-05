from funcoes import *

saldo = 0
extrato = []
extrato_num = 0
limite = 3
usuarios = []
contas = []

while True:
    opt = menu()
    if opt == '0': # DEPOSITAR
        saldo, extrato, extrato_num = depositar(saldo, extrato, extrato_num)
    elif opt == '1': # SACAR
        saldo, extrato, extrato_num, limite = sacar(saldo, extrato, extrato_num, limite)
    elif opt == '2': # EXTRATO
        extrato_(extrato)
    elif opt == '3': # NOVA CONTA
        contas.append(criar_conta(usuarios,contas))
    elif opt == '4': # LISTAS CONTAS
        listar_contas(contas)
    elif opt == '5': # NOVO USUARIO
        usuarios.append(criar_usuario())
    elif opt == '6': # FILTRAR USUARIO
        cpf = input('Digite o CPF do usuário: ')
        print(filtrar_usuario(cpf, usuarios))
    elif opt == 7: # SAIR
        break
    else:
        print('Opção inválida!')