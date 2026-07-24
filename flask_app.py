from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)

@app.get("/")
def consignes():
     return render_template('consignes.html')

if __name__ == "__main__":
    # utile en local uniquement
    app.run(host="0.0.0.0", port=5000, debug=True)
     
@app.get("/phishstats")
def phishstats():
    url = "https://phishstats.info:2096/api/phishing"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        # On limite à 20 résultats
        return render_template("phishstats.html", data=data[:20])

    except requests.RequestException as e:
        return f"Erreur : {e}"
