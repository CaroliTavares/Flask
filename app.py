import requests

from flask import Flask, render_template, request


app = Flask(__name__)

API_KEY = 'abb2a5ed64fefcde71408537c18e6b58'
API_URL = 'http://api.openweathermap.org/'
API_URL += 'data/2.5/weather?q={}&mode=json'
API_URL += '&units=metric&appid={}'


cidades = [
{'name':'Uberaba'},
{'name':'Campinas'},
]

@app.route("/index")

def index():
    return render_template("index.html", data=cidades)

@app.route("/result", methods=["POST"])
def result():
    city = request.form.get('comp_select')
    data = requests.get(API_URL.format(city, API_KEY)).json()
    return render_template('result.html',d=data)

app.run()