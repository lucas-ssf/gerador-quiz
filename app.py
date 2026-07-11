from flask import Flask, request, render_template, render_template_string, send_file
from preparar import criar_html
from api import gerar_quiz

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def receber_texto():
    if request.method == 'POST':
        quiz_json = gerar_quiz(request.form['texto'])
        html = criar_html(quiz_json)
        return render_template_string(html)
    return render_template('index.html')
