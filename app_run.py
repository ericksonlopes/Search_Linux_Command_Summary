from database import DataBase

# instânciando classe para
db = DataBase()

while True:
    option = int(input("""
Selecione uma das opções abaixo!
        
0) Finaliza o programa.
1) Exebir todos os itens.

Digite: """))
    if option == 0:
        break

    elif option == 1:
        db.select_all_summary()
