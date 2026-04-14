import sqlite3 as sql
import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def criar_tabela():
    BASE_DIR = get_base_path()
    db_path = os.path.join(BASE_DIR, "database.db")

    con = sql.connect(db_path)
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS chamados_ti (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                setor TEXT NOT NULL,
                problema TEXT NOT NULL,
                descricao TEXT NOT NULL,
                urgencia TEXT NOT NULL,
                status TEXT NOT NULL,
                data_chamado TEXT NOT NULL)
                """)
    con.commit()
    con.close()