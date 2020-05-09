from flask import Flask, escape, request, render_template, send_from_directory, redirect
from os import path
import csv
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
        write_to_csv(data)
        return redirect('/thankyou.html', <string:email>)
    else:
        return render_template('index.html')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
