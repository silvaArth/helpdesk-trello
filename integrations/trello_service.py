import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("TRELLO_API_KEY")
api_token = os.getenv("TRELLO_API_TOKEN")
board_id = os.getenv("TRELLO_BOARD_ID")
list_id = os.getenv("TRELLO_LIST_ID")

LABELS = {
    "Alta": "69de9f2426cbc60478fb2343",
    "Média": "69de9f347387a612f8e11d78",
    "Baixa": "69de9f3c7ee29a23b77e085c"
}

def criar_cartao(dados):
    url = "https://api.trello.com/1/cards"

    id_label = LABELS.get(dados["urgencia"])

    headers = {
    "Accept": "application/json"
    }

    query = {
    'idList': {list_id},
    'key': {api_key},
    'token': {api_token},
    'name': dados["setor"] + " - " + dados["nome"] + ": " + dados["problema"],
    'desc': dados["descricao"],
    'idLabels': id_label
    }

    response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))