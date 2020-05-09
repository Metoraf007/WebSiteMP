from flask import Flask, escape, request, render_template, send_from_directory
from os import path
import json
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<page>')
def return_page(page):
    return render_template(page)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')