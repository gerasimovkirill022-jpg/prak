from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    """Главная страница — возвращает HTML-строку."""
    return """
    <html>
        <head><title>Список задач</title></head>
        <body>
            <h1>Мой список задач</h1>
            <p>Скоро здесь будет список задач из базы данных.</p>
            <p><a href="/about">О проекте</a></p>
        </body>
    </html>
    """
@app.route('/about')
def about():
    """Страница «О проекте»."""
    return "Я работаю."
if __name__ == '__main__':
    app.run(debug=True, port=5000)
1