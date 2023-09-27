import mysql.connector

minhaconexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='evapolyane1408',
    database='ads2023ged'
)

meucursor = minhaconexao.cursor()

print('Cadastro de Usuários no Sistema GED\n')
print('Digite a opção desejada: ')

opcao = int(input('1 - Cadastro;\n2 - Consulta;\n3 - Atualização;\n4 - Exclusão;\n : '))

if (opcao == 1):
    print('Digite os dados do usuário: ')
    login = input('login: ')
    senha = input('senha: ')
    email = input('email: ')

    SQL = 'INSERT INTO usuarios(login, senha, email, tipo, status) VALUES (%s, %s, %s, %s, %s)'

    DADOS = (login, senha, email, 'U', 'A')

    meucursor.execute(SQL, DADOS)

    print('Número de Registros Afetados: ', meucursor.rowcount)
    print('Usuário Cadastrado com Sucesso!')
    minhaconexao.commit()

if (opcao == 2):
    print('Você escolheu a opção Consulta.')
    login = input(str('Digite o login: '))


    SQL = "select * from usuarios where login like %s and status='A'"

    DADOS = ("%"+login+"%", )

    meucursor.execute(SQL, DADOS)

    consultaBanco = meucursor.fetchall()

    for linhaBanco in consultaBanco:
        print('idusuario: ', linhaBanco[0], 'login: ', linhaBanco[1], 'email: ', linhaBanco[3])



if (opcao == 3):
    print('Você escolheu a opção de Atualizar: ')
    email = input('Email: ')
    novaSenha = input('Nova senha: ')

    SQL = 'Update usuarios set senha=%s where email=%s'

    DADOS = (novaSenha, email)

    meucursor.execute(SQL, DADOS)

    print('Número de registros afetados: ', meucursor.rowcount)
    minhaconexao.commit()

if (opcao == 4):
    print('Você escolheu a opção Excluir: ')
    print('Digite o filtro para exclusão: ')
    email = input('email: ')

    SQL = "update usuarios set status='B' where email = %s"

    DADOS = (email, )

    meucursor.execute(SQL, DADOS)

    print('Número de registros afetados: ', meucursor.rowcount)
    print('Registro excluído com sucesso!')
    minhaconexao.commit()


meucursor.close()
minhaconexao.close()








