import sqlite3
from pathlib import Path

CAMINHO_BANCO = Path('dados/grupo1_Carbono.db')
CAMINHO_BANCO.parent.mkdir(exist_ok=True)

def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.execute('PRAGMA foreign_keys = ON')
    return conexao

with conectar() as conn:

    # Tabela Área
    conn.execute('''
        CREATE TABLE IF NOT EXISTS area (
            id_area INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_area TEXT NOT NULL,
            localizacao TEXT NOT NULL,
            tamanho_hectares REAL NOT NULL CHECK(tamanho_hectares > 0),
            status_recuperacao TEXT NOT NULL,
            data_inicio_recuperacao TEXT
        );
    ''')

    # Tabela Espécie
    conn.execute('''
        CREATE TABLE IF NOT EXISTS especie (
            id_especie INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cientifico TEXT NOT NULL UNIQUE,
            nome_popular TEXT,
            tipo_especie TEXT,
            regiao_recomendada TEXT
        );
    ''')

    # Tabela Plantio
    conn.execute('''
        CREATE TABLE IF NOT EXISTS plantio (
            id_plantio INTEGER PRIMARY KEY AUTOINCREMENT,
            data_plantio TEXT NOT NULL,
            quantidade_mudas INTEGER NOT NULL CHECK(quantidade_mudas > 0),
            id_area INTEGER NOT NULL,
            id_especie INTEGER NOT NULL,

            FOREIGN KEY (id_area)
                REFERENCES area(id_area),

            FOREIGN KEY (id_especie)
                REFERENCES especie(id_especie)
        );
    ''')

    # Tabela Medição de Carbono
    conn.execute('''
        CREATE TABLE IF NOT EXISTS medicao_carbono (
            id_medicao INTEGER PRIMARY KEY AUTOINCREMENT,
            data_medicao TEXT NOT NULL,
            nivel_carbono REAL NOT NULL,
            unidade_medida TEXT NOT NULL,
            id_area INTEGER NOT NULL,

            FOREIGN KEY (id_area)
                REFERENCES area(id_area)
        );
    ''')

    # Tabela Técnico Ambiental
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tecnico_ambiental (
            id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            telefone TEXT UNIQUE,
            email TEXT UNIQUE
        );
    ''')

    # Tabela Relatório
    conn.execute('''
        CREATE TABLE IF NOT EXISTS relatorio (
            id_relatorio INTEGER PRIMARY KEY AUTOINCREMENT,
            data_relatorio TEXT NOT NULL,
            descricao TEXT NOT NULL,
            resultado TEXT NOT NULL,
            id_area INTEGER NOT NULL,
            id_tecnico INTEGER NOT NULL,

            FOREIGN KEY (id_area)
                REFERENCES area(id_area),

            FOREIGN KEY (id_tecnico)
                REFERENCES tecnico_ambiental(id_tecnico)
        );
    ''')

    conn.commit()

print("Banco de dados e tabelas criados com sucesso!")