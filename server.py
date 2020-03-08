from flask import Flask, escape, request, render_template, send_from_directory
from os import path
import json
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
