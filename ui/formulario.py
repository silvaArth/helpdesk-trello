import tkinter as tk
from tkinter import ttk
from services.chamado_service import criar_chamado
from integrations.trello_service import criar_cartao

def abrir_formulario():
    janela = tk.Tk()
    janela.title("Abertura chamado TI")
    janela.geometry("1000x800")
    janela.resizable(False, False)

    label = tk.Label(janela, text="Sistema de Chamados TI")
    label.pack(pady=20)

    tk.Label(janela, text="Nome do solicitante:").pack()
    entrada_nome = tk.Entry(janela, width=40)
    entrada_nome.pack(pady=5)

    tk.Label(janela, text="Setor solicitante:").pack()
    entrada_setor = tk.Entry(janela, width=40)
    entrada_setor.pack(pady=5)

    list_problemas = ["","Computador", "Impressora", "Internet", "Scanner", "Telefone", "Outros"]
    tk.Label(janela, text="Tipo do problema:").pack()
    combo_problemas = ttk.Combobox(janela, values=list_problemas, state="readonly")
    combo_problemas.pack(pady=5)

    tk.Label(janela, text="Descrição do problema:").pack()
    entrada_desc = tk.Text(janela, width=50, height=10)
    entrada_desc.pack(pady=5)

    list_urgencia = ["","Baixa", "Média", "Alta"]
    tk.Label(janela, text="Nível de urgência:").pack()
    combo_urgencia = ttk.Combobox(janela, values=list_urgencia, state="readonly")
    combo_urgencia.pack(pady=5)

    def enviar():
        nome = entrada_nome.get()
        setor = entrada_setor.get()
        problema = combo_problemas.get()
        descricao = entrada_desc.get("1.0", tk.END).strip()
        urgencia = combo_urgencia.get()

        dados = {
            "nome": nome,
            "setor": setor,
            "problema": problema,
            "descricao": descricao,
            "urgencia": urgencia
        }

        criar_chamado(dados)
        criar_cartao(dados)  

    btn_enviar = tk.Button(janela, text="Enviar", command=enviar)
    btn_enviar.pack(pady=15)

    janela.mainloop()
