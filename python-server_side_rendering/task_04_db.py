#!/usr/bin/python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# JSON oxuma funksiyası
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

# CSV oxuma funksiyası
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# SQL oxuma funksiyası
def read_sql(p_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Bu sətir nəticələri dict kimi götürməyə imkan verir
        cursor = conn.cursor()
        
        if p_id:
            cursor.execute("SELECT name, category, price FROM Products WHERE id = ?", (p_id,))
        else:
            cursor.execute("SELECT name, category, price FROM Products")
            
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error:
        return None
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # 1. Source yoxlanışı
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    products = []

    # 2. Məlumatın mənbəyə görə götürülməsi
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql(product_id if source == 'sql' else None)
        if products is None: # Database xətası halı
            return render_template('product_display.html', error="Database error")

    # 3. ID filterləmə (JSON və CSV üçün, çünki SQL-də sorğunun daxilində etdik)
    if source != 'sql' and product_id:
        products = [p for p in products if p['id'] == product_id]

    # 4. Tapılmama halı
    if not products:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
