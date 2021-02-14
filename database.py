import os
import sqlite3

from web_scraping import scraping_summary


class DataBase:
    def __init__(self):
        # nome da base de dados
        self.name_file = 'database.db'
        # verifica se não existe o arquivo
        if not os.path.exists(self.name_file):
            try:
                # tenta criar o arquivo e se conectar a ele
                self.conn = sqlite3.connect(self.name_file)
                # cria um cursor
                cursor = self.conn.cursor()
                # executa um script para criar uma tabela com duas colunas
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS summary (
                    id integer primary key,
                    command text,
                    overview text,
                    link text
                )
                """)

                self.add_items_summary()
                # fecha a conexão
                self.conn.close()
            except Exception as err:
                print(err)
                # caso de erro, tenta apagar o documento
                os.remove(self.name_file)

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

        cursor = self.conn.cursor()

        cursor.execute('SELECT * FROM tablename')

        for table in cursor:
            print(table)

        self.add_items_summary()
        # realize as alterações dentro do banco de dados

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
        conn = sqlite3.connect(self.name_file)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM summary')
        result = cursor.fetchall()

        for item in result:
            print(item)


# create_table()
if __name__ == '__main__':
    db = DataBase()

    # db.select_all()
