import sqlite3

from web_scraping import scraping_summary

name_db = 'database.db'

# tenta conectar a base de dados
conn = sqlite3.connect('database.db')


def create_table():
    """ Cria a tabela pricipal """
    # Executa a criação da tabela no banco de dados
    conn.execute("""
    CREATE TABLE IF NOT EXISTS summary (
        id integer primary key,
        command text,
        overview text,
        link text
    )
    """)
    # Comita as alterações no banco de dados
    conn.commit()

    # executa a função para adicionar todos os itens do sumário dentro da bd
    add_items_summary()


# Adicionar todos os itens do sumário dentro da bd
def add_items_summary():
    # instancia um cursos
    cursor = conn.cursor()
    # Sql para adicionar itens dentro da base de dados
    sql = 'INSERT INTO summary (command, overview, link) VALUES (?, ?, ?)'
    # Carrega os itens recebidos da função de scraping
    val = scraping_summary()
    # Realiza a query de inserção de todos os itens da lista
    cursor.executemany(sql, val)
    # Comita dentro da base de dados, salvando as alterações
    conn.commit()
    print(cursor.rowcount, 'Linha(s) afetada(s)')


def add_item():
    pass


create_table()
