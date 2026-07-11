import requests
from secrets import api_key

url = "https://models.github.ai/inference/chat/completions"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {api_key}",
    "X-GitHub-Api-Version": "2022-11-28",
    "Content-Type": "application/json"
}

inicio_prompt="""
Lê o seguinte texto e gera um quiz com 7 perguntas de múltipla escolha (4 opções: A, B, C, D) baseadas exclusivamente no conteúdo desse texto.

Regras:

    Gera exatamente 7 perguntas diferentes, sem repetições.
    Cada pergunta deve ter exatamente 4 opções.
    O quiz deve cobrir os pontos principais do texto.

Devolve o resultado estritamente no seguinte formato JSON, sem texto adicional antes ou depois:

{
    "quiz": {
        "questions": [
            {
                "id": 1,
                "text": "Texto da pergunta",
                "options": {
                    "A": "Opção A",
                    "B": "Opção B",
                    "C": "Opção C",
                    "D": "Opção D"
                },
            }
        ]
    }
}

Texto:
"""

def gerar_quiz(texto):
    content = inicio_prompt
    content += texto
    payload = {
        "model": "openai/gpt-4.1",
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    print(response.status_code)
    print(response.json()['choices'][0]['message']['content'])
    quiz = response.json()['choices'][0]['message']['content']
    return quiz
