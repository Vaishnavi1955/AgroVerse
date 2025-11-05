from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# ✅ Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agri.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ✅ Market Model (database table)
class MarketItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<MarketItem {self.crop_name}>"

# ✅ Create Tables Automatically (before first request)
@app.before_request
def create_tables():
    db.create_all()

# ✅ Routes
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
    items = MarketItem.query.all()
    return render_template('market.html', items=items)

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
