# Gerador de Quiz

Aplicação em Flask para gerar Quiz com IA.

## Como rodar

Definir a chave da sua API do [Marketplace](https://docs.github.com/en/github-models/quickstart)

    export API_KEY=insira-aqui-sua-chave

Instalar os requerimentos e rodar a aplicação

    pip install -r requirements.txt
    gunicorn app:app


## Gerando o Quiz
Envie um texto qualquer, a IA responderá no formato *json*, conforme o exemplo. 
O texto da resposta será transformado num Quiz interativo em *HTML*.

    {
        "quiz": {
            "questions": [
                {
                    "id": 1,
                    "text": "Qual é o maior planeta do Sistema Solar?",
                    "options": {
                        "A": "Terra",
                        "B": "Júpiter",
                        "C": "Saturno",
                        "D": "Netuno"
                    }
                },
                {
                    "id": 2,
                    "text": "Em que ano caiu o Muro de Berlim?",
                    "options": {
                        "A": "1987",
                        "B": "1989",
                        "C": "1991",
                        "D": "1993"
                    }
                }
            ]
        }
    }



