from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3
import requests

app = Flask(__name__)

@app.get("/")
def consignes():
     return render_template('consignes.html')

if __name__ == "__main__":
    # utile en local uniquement
    app.run(host="0.0.0.0", port=5000, debug=True)
     
@app.route("/dogfacts")
def dogfacts():
    url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=5"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        facts = response.json()

        return render_template("dogfacts.html", facts=facts)

    except requests.exceptions.RequestException as e:
        return f"Erreur : {e}"
