#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # host='0.0.0.0' bütün şəbəkə interfeyslərini dinləmək üçün vacibdir
    app.run(debug=True, host='0.0.0.0', port=5000)
