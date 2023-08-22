import sqlite3
from db import db_utils

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/Estudante.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudante (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Anodeingresso INTEGER
);
""")
estudantes = [("Ana Silva", "Computação", 2019), ("Pedro Mendes", "Física", 2021),
              ("Carla Souza", "Computação", 2020), ("João Alves", "Matemática", 2018),
              ("Maria Oliveira", "Química", 2012)]

cursor.executemany("""
INSERT INTO Estudante (Nome,Curso,Anodeingresso)
VALUES (?, ?, ?);
""", estudantes)
conn.commit()
cursor.execute("SELECT * FROM Estudante WHERE [Anodeingresso] >= ? AND [Anodeingresso] <= ?", (2019,2020))
print(cursor.fetchall())
cursor.execute("UPDATE Estudante SET [Anodeingresso] = ? WHERE [Nome] = ?", (2020,'Ana Silva'))
conn.commit()
db_utils.checar()
cursor.execute("DELETE FROM Estudante WHERE [ID]=?",(5,))
conn.commit()
db_utils.checar()
cursor.execute("SELECT * FROM Estudante WHERE [Anodeingresso]>=?",(2019,))
print(cursor.fetchall())
cursor.execute("UPDATE Estudante SET [Anodeingresso]=? WHERE [Nome]!=?",(2018,'LI'))
conn.commit()
db_utils.checar()
conn.close()




# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

