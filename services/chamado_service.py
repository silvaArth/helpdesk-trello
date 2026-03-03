import sqlite3 as lite
from datetime import datetime

def criar_chamado(dados):
    con = lite.connect("database/database.db")
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