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
    add_items_summary()


def add_items_summary():
    sql = 'INSERT INTO summary (command, overview, link) VALUES (?, ?, ?)'
    val = scraping_summary()

    conn.executemany(sql, val)

    conn.commit()


def add_item():
    pass


create_table()
