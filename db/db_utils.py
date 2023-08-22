import sqlite3
conn = sqlite3.connect('db/Estudante.db')
cursor=conn.cursor()
def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Estudante (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Curso TEXT NOT NULL,
        Anodeingresso INTEGER
    );
    """)
def checar():
    cursor.execute("SELECT * FROM Estudante")
    print(cursor.fetchall())
def atualizar(coluna_set, coluna_condicao, valor_set, valor_condicao):
    query = f"UPDATE Estudante SET [{coluna_set}] = ? WHERE [{coluna_condicao}] = ?"
    cursor.execute(query, (valor_set, valor_condicao))
    conn.commit()
def deletar(condicao):
    query = f"DELETE Estudante WHERE [{condicao}] = ?"
    cursor.execute(query, (condicao,))
    conn.commit()