from flask import Flask, escape, request, render_template, send_from_directory, redirect
from os import path
import json
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<string:page_name>')
def return_page(page_name):
    return render_template(page_name)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        email = data['email']
        return redirect('/thankyou.html', <string:email>)
    else:
        return render_template('index.html')