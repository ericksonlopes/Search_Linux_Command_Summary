import sqlite3

conn = sqlite3.connect('database.db')


def create_table():
    """ Cria a tabela pricipal """
    cursor = conn.cursor()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS summary (
        id integer primary key,
        command text,
        overview text,
        link text
    )
    """)
    conn.commit()

create_table()