import sqlite3
from pathlib import Path

CAMINHO_BANCO = Path('dados/aula-01.db')
CAMINHO_BANCO.parent.mkdir(exist_ok=True)

def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.execute('PRAGMA foreign_keys = ON')
    return conexao

with conectar() as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
                id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                curso TEXT NOT NULL,
                ano INTEGER NOT NULL
                );
    ''');
    conn.commit()

nome = input("Nome: ")
curso = input("Curso: ")
ano = int(input("Ano: "))

with conectar() as conn:
    conn.execute('''
        INSERT INTO turmas(nome, curso, ano) 
        VALUES(?,?,?)''',
        (nome, curso, ano)
    )
    conn.commit()

conn.close()