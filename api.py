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
    A opção correta deve ser identificada com a chave "T" (de Verdadeiro/Certa), substituindo a letra correspondente à sua posição original.
    As outras três opções permanecem com as chaves "A", "B", "C", "D" (excluindo a que foi substituída por "T").
    A chave "T" ocupa a MESMA POSICAO da opção correta original — não a movas para o final nem para outro lugar. Por exemplo, se a resposta correta era a B, as chaves ficam na ordem: A, T, C, D.
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
                    "T": "Opção Correta (que originalmente seria B)",
                    "C": "Opção C",
                    "D": "Opção D"
                }
            },
            {
                "id": 2,
                "text": "Texto da pergunta",
                "options": {
                    "T": "Opção Correta (que originalmente seria A)",
                    "B": "Opção B",
                    "C": "Opção C",
                    "D": "Opção D"
                }
            }
        ]
    }
}

Observações importantes:
- Se a opção correta original era A, então o objeto options terá chaves na ordem: T, B, C, D (sem A)
- Se a opção correta original era B, então o objeto options terá chaves na ordem: A, T, C, D (sem B)
- Se a opção correta original era C, então o objeto options terá chaves na ordem: A, B, T, D (sem C)
- Se a opção correta original era D, então o objeto options terá chaves na ordem: A, B, C, T (sem D)
- Nunca inclua mais de uma chave "T" por pergunta
- A chave "T" aparece na mesma posição que a letra original ocupava

Texto:
"""

def gerar_quiz(texto):
    if not texto or not texto.strip():
        return None
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
