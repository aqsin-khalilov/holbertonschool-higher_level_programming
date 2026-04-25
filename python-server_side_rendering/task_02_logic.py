#!/usr/bin/python3
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        # JSON faylını oxuyuruq
        with open('items.json', 'r') as f:
            data = json.load(f)
        
        # Siyahını götürürük (əgər "items" açarı yoxdursa boş siyahı qaytarırıq)
        items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Fayl yoxdursa və ya formatı səhvdirsə boş siyahı göndəririk
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
