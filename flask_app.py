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

@app.route("/agify")
def agify():
    nom = request.args.get("name", "emilie")

    url = f"https://api.agify.io?name={nom}"

    response = requests.get(url)
    data = response.json()

    return render_template("agify.html", data=data)
