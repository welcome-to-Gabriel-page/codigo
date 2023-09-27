# Sistema GED do Projeto Integrador 21/09
# AUTOR: Gabriel de Paiva Silva

import mysql.connector

print('Sistema GED do Projeto Integrador')

entrada = 'INATIVO'
perfil = "VAZIO"
status = "VAZIO"

print('Escolha uma opção: ')
print('1. Cadastrar\n2.Logar')
opcao = int(input('Digite uma das opções: '))


if opcao == 1:
    print('Opção escolhida: Cadastrar')
    print('Informe seus dados: ')
    login = input('Login: ')
    senha = input('Senha: ')
    email = input('Email: ')

    meuBanco = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ads2023ged',
    )

    meuCursor = meuBanco.cursor()

    SQL = "insert into usuarios(login, senha, email, tipo, status) values (%s, %s, %s, %s, %s)"
    DADOS = (login, senha, email, 'U', 'A')

    meuCursor.execute(SQL, DADOS)
    meuBanco.commit()
    meuCursor.close()
    meuBanco.close()
    print('Usuário cadastrado com sucesso!\n')

    entrada = "ATIVO"

if opcao == 2:
    print('Opção escolhida: Logar')
    print('Informe seus dados: ')
    login = input('Login: ')
    senha = input('Senha: ')

    meuBanco = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ads2023ged',
    )

    meuCursor = meuBanco.cursor()

    SQL = "select * from usuarios where login = %s and senha = %s"
    DADOS = (login, senha)

    meuCursor.execute(SQL, DADOS)
    consultaBanco = meuCursor.fetchone()
    idusuario = consultaBanco[0]
    perfil = consultaBanco[5]
    status = consultaBanco[4]

    if(consultaBanco):
        entrada = "ATIVO"
    else:
        entrada = "INATIVO"

    meuCursor.close()
    meuBanco.close()


if (entrada == "ATIVO" and perfil == "U" and status == "A"):

    continuar = "S"

    while((continuar == "S" or continuar == "s") and entrada != "INATIVO"):
        print('Usuário autenticado no sistema!')
        print('1. Visualizar Dados\n2. Alterar Senha\n3. Sair')
        opcao = int(input('Digite uma opção: '))

        if(opcao == 1):
            print('Opção selecionada: Visualizar Dados')
            print('Dados cadastrados: ')
            meuBanco = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='ads2023ged',
            )
            meuCursor = meuBanco.cursor()
            SQL = "select * from usuarios where idusuario = %s"
            DADOS = (idusuario, )
            meuCursor.execute(SQL, DADOS)
            consultaBanco = meuCursor.fetchone()
            print('Dados do usuário: ')
            print('idusuario: ', consultaBanco[0])
            print('Login: ', consultaBanco[1])
            print('Senha: ', consultaBanco[2])
            print('Email: ', consultaBanco[3])
            print('Tipo: ', consultaBanco[4])
            print('Status: ', consultaBanco[5])
            meuCursor.close()
            meuBanco.close()

        if(opcao == 2):
            print('Opção selecionada: Atualizar dados')
            print('Informe seus dados:')
            senha = input('Nova Senha: ')
            email = input('Novo Email: ')

            meuBanco = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='ads2023ged',
            )
            meuCursor = meuBanco.cursor()

            SQL = "update usuarios set email = %s, senha = %s where idusuario = %s"
            DADOS = (email, senha, idusuario)
            meuCursor.execute(SQL, DADOS)
            meuBanco.commit()
            print('Dados atualizados!')
            meuCursor.close()
            meuBanco.close()

            print('Deseja continuar no programa?')
            continuar = input('Digite S/N: ')

        if(opcao == 3):
            print('Opção selecionada: Sair')
            entrada = "INATIVO"
            perfil = "VAZIO"
            status = "VAZIO"
            idusuario = -1
                

else:
    print('Usuário não autenticado.')





