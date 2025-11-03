from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
