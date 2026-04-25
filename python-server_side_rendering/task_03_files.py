#!/usr/bin/python3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # CSV-dən gələn məlumat string olur, id və price-ı rəqəmə çevirək
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # 1. Source yoxlanışı
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Faylın oxunması
    try:
        if source == 'json':
            products = read_json()
        else:
            products = read_csv()
    except Exception:
        return render_template('product_display.html', error="File not found")

    # 3. ID-yə görə filterləmə
    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
