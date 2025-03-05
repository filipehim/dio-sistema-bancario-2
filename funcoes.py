def menu():
    return input('''
    ========= MENU =========
        DEPOSITAR       [0]
        SACAR           [1]
        EXTRATO         [2]
        NOVA CONTA      [3]
        LISTAR CONTAS   [4]
        NOVO USUARIO    [5]
        FILTRAR USUARIO [6]
        SAIR            [7]
    =========================
    Escolha uma opção: ''')

def depositar(saldo, extrato, extrato_num):
    from datetime import datetime
    from time import sleep
    print('-='*8)
    print(f'Seu saldo atual é de R$ {saldo}.')
    deposito = int(input('Quanto você quer Depositar? :'))
    sleep(2)
    if deposito > 0: # VALOR POSITIVO
        saldo += deposito
        print('Deposito realizado com Sucesso!')

        # CRIAÇÃO DO EXTRATO
        extrato_num += 1
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato.append(f'''
    -=-=-=-=-=-=-=-=
    TIPO: DEPÓSITO
    VALOR: {deposito}
    DATA: {agora}
    N° EXTRATO: #{extrato_num} 
    -=-=-=-=-=-=-=-=''')
        
    else: # VALOR NEGATIVO
        print('Impossível depositar um valor negativo!')
    
    return saldo, extrato, extrato_num

def sacar(saldo, extrato, extrato_num, limite):
    from datetime import datetime
    from time import sleep
    if limite > 0:
        print('-='*8)
        print(f'Seu saldo atual é de R$ {saldo}.')   
        print(f'Você tem {limite} {'saque disponivel.' if limite == 1 else 'saques disponíveis.'}')  
        saque = int(input('Quanto você quer sacar? :'))
        sleep(2)
        if saque > 0: # VALOR POSITIVO
            sleep(2)
            if saque <= 500:
                if saldo >= saque:
                    limite -= 1
                    saldo -= saque
                    print('Saque realizado com Sucesso!')

                    # CRIAÇÃO DO EXTRATO
                    extrato_num += 1
                    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    extrato.append(f'''
    -=-=-=-=-=-=-=-=
    TIPO: SAQUE
    VALOR: {saque}
    DATA: {agora}
    N° EXTRATO: #{extrato_num} 
    -=-=-=-=-=-=-=-=''')      
                else:
                    print('Saldo Indisponivel!')           
            else:
                print('Não é possível sacar mais que R$ 500,00')

        else: # VALOR NEGATIVO
            print('Impossível sacar um valor negativo!')
    
    else: # LIMITE DE SAQUE
        print('Você já atingiu o seu limite de transações diárias.')
    
    return saldo, extrato, extrato_num, limite

def extrato_(extrato):
    print('Histórico:')
    for e in range(len(extrato), 0, -1):
        print(extrato[e-1])

def criar_usuario():
    while True:
        nome = input('Digite seu nome: ')
        if nome.isalpha() == False:
            print('Nome inválido!')
        else:
            break
    while True:
        cpf = input('Digite seu CPF: ')
        if len(cpf) != 11:
            print('CPF inválido!')
        else:
            break
    while True:
        email = input('Digite seu email: ')
        if '@' not in email:
            print('Email inválido!')
        else:
            break
    senha = input('Digite sua senha: ')
    print('Usuário criado com sucesso!')
    return {
        'nome': nome,
        'cpf': cpf,
        'email': email,
        'senha': senha
    }


def criar_conta(usuarios,contas):
    while True:
        cpf_user = input('Digite seu CPF: ')
        if len(cpf_user) != 11 or cpf_user.isnumeric() == False:
            print('CPF inválido!')
        else:
            for u in usuarios:
                if u['cpf'] == cpf_user:
                    print('Conta criada com sucesso!')
                    return f'''
        Agência:  0001
        C/C:      {len(contas)+1}
        Ttular:   {u['nome']}'''
                else:
                    print('Usuário não encontrado!')
                    break
        
def listar_contas(contas):
    for c in contas:
        print(c)

def filtrar_usuario(cpf, usuarios):
    filtro = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return filtro[0] if filtro else None 