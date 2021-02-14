from database import DataBase
from prettytable import from_db_cursor

# instânciando classe para
db = DataBase()

while True:
    option = int(input("""
Selecione uma das opções abaixo!
        
0) Finaliza o programa.
1) Exebir todos os itens.
2) Procurar por comando.

Digite: """))
    # fecha aplicação
    if option == 0:
        break

    # Exibe todos os comandos
    elif option == 1:
        # Exibe a tabela criada pelo  prettytable com o cursor recebido do banco de dados
        print(from_db_cursor(db.select_all_summary()), '\n')

    # Pesquisa por um comando
    elif option == 2:
        # pergunta ao usuario qual o comando desejado
        command = input('Digite o commando que deseja encontrar: ')
        print('\n')
        # Utiliza a função para buscar o comando desejado
        search_data = db.select_command(command)

        # Se for retornado o conteúdo do comando
        if search_data:
            # exibe ao usuario
            print(search_data)

        print(f"O comando '{command}' Não foi encontrado!")

    option_end = input('Deseja continuar? (S/N)')

    if option_end.upper() == 'N':
        break

