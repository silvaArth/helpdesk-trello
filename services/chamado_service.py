import sqlite3 as lite
from datetime import datetime
import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def criar_chamado(dados):
    BASE_DIR = get_base_path()
    db_path = os.path.join(BASE_DIR, "database.db")

    con = lite.connect(db_path)
    cursor = con.cursor()

    data_atual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    cursor.execute("""
        INSERT INTO chamados_ti 
        (nome, setor, problema, descricao, urgencia, status, data_chamado)
        VALUES (?,?,?,?,?,?,?)
        """, (
            dados["nome"],
            dados["setor"],
            dados["problema"],
            dados["descricao"],
            dados["urgencia"],
            "Aberto",
            data_atual
        ))
    
    con.commit()
    con.close()

    print("Chamado criado com sucesso!")