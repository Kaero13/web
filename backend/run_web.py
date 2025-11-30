from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__,
    template_folder=str(Path(__file__).parent.parent / 'frontend' / 'templates'),
    static_folder=str(Path(__file__).parent.parent / 'frontend')
)
@app.route('/')
@app.route('/main')
def index():
    return render_template("main_page.html")

@app.route('/download')
def download():
    return "Download my app"

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)