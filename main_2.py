import sqlite3
from db import db_utils as u
conn = sqlite3.connect('db/Estudante.db')
cursor = conn.cursor()
u.criar_tabela()
estudantes = [("Ana Silva", "Computação", 2019), ("Pedro Mendes", "Física", 2021),
              ("Carla Souza", "Computação", 2020), ("João Alves", "Matemática", 2018),
              ("Maria Oliveira", "Química", 2012)]
#cursor.executemany("""
#INSERT INTO Estudante (Nome,Curso,Anodeingresso)
#VALUES (?, ?, ?);
#""", estudantes)
conn.commit()
u.checar()
u.atualizar('Curso','Nome','Medicina','Carla Souza')
conn.close()