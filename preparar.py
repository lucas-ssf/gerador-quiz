import json

def criar_html(quiz_json):
    quiz = json.loads(quiz_json)['quiz']
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="static/estilo.css">
        <title>Quiz</title>
    </head>
    <body>
    
    <div class="container">
        <h1>Quiz</h1>
    """
    html_radio = ""
    
    html_tabs = """
        <div class="tabs">"""
    
    html_content = """
        <div class="content">"""
    
    for question in quiz['questions']:
        html_radio += f"""
        <input type="radio" name="tab" id="t{question['id']}">"""
    
        html_tabs += f"""
            <label for="t{question['id']}">Q{question['id']}</label>"""
    
        html_content += f"""
            <div class="page q{question['id']}">
                <p>{question['text']}</p>"""
        for key, value in question['options'].items():
                html_content += f"""
                <div class="opt"><input type="radio" name="q{question['id']}" id="q{question['id']}{key}"><label for="q{question['id']}{key}">{value}</label>
                </div>"""
        html_content += """
            </div>"""
    html_tabs +="""
        </div>"""
    
    
    html += html_radio
    html += html_tabs
    html += html_content
    html += """
        </div>
    </div>
    
    </body>
    </html>"""
    return html
