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
    if page_name == 'thankyou.html':
        email = request.args.get('email')
        return render_template('/thankyou.html', email=email)
    else:
        return render_template(page_name)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        redirect_page = '/thankyou.html?email='+ data['email']
        return redirect(redirect_page)
    else:
        return render_template('index.html')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
