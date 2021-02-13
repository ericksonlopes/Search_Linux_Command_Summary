import os
import sqlite3
from time import sleep
from web_scraping import scraping_summary


class DataBase:
    def __init__(self):
        name_db = 'database.db'

        # tenta conectar a base de dados
        self.conn = sqlite3.connect(name_db)

        if not os.path.exists(name_db):
            try:
                self.create_table()
            except Exception as error:
                print(error)

    # if not os.path.exists('database.db'):
    def create_table(self):
        """ Cria a tabela pricipal """
        # Executa a criação da tabela no banco de dados
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS summary (
            id integer primary key,
            command text,
            overview text,
            link text
        )
        """)
        # Comita as alterações no banco de dados
        self.conn.commit()

        # executa a função para adicionar todos os itens do sumário dentro da bd
        self.add_items_summary()

    # Adicionar todos os itens do sumário dentro da bd
    def add_items_summary(self):
        # instancia um cursos
        cursor = self.conn.cursor()
        # Sql para adicionar itens dentro da base de dados
        sql = 'INSERT INTO summary (command, overview, link) VALUES (?, ?, ?)'
        # Carrega os itens recebidos da função de scraping
        val = scraping_summary()
        # Realiza a query de inserção de todos os itens da lista
        cursor.executemany(sql, val)
        # Comita dentro da base de dados, salvando as alterações
        self.conn.commit()
        # Exibe o total de linhas afetadas
        print(cursor.rowcount, 'Linha(s) afetada(s)')

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM summary')
        result = cursor.fetchall()

        for item in result:
            print(item)


# create_table()

db = DataBase()

db.select_all()
