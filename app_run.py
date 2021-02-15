import os

from colorama import init, Fore
from prettytable import from_db_cursor
from functions.database import DataBase

# instancia a classe do banco de dados
db = DataBase()

# função do colorama que limita por linha a cor
init(autoreset=True)

while True:
    option = int(input(Fore.CYAN + """
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
        # pergunta ao usuario qual o comando desejado retirando os espaços em branco
        command = input(Fore.CYAN + 'Digite o commando que deseja encontrar: ').strip()

        print('\n')

        # Utiliza a função para buscar o comando desejado (string do comando em minusculo)
        search_data = db.select_command(command.lower())

        # Se for retornado o conteúdo do comando
        if search_data:

            # Exibe ao usuario o resultado da consulta
            print(Fore.BLUE + 'Comando:', f'{search_data[0][1]}')
            print(Fore.BLUE + 'Função:', f"{search_data[0][2]}")
        else:
            # Caso o programa não seja encontrado
            print(Fore.RED + f"[!] O comando '{command}' Não foi encontrado! Por favor, tente novamente!")

        print('\n' * 2)

    option_end = input(Fore.CYAN + 'Deseja continuar? (S/N): ')

    if option_end.upper() == 'N':
        break
