from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
from werkzeug.utils import secure_filename

import sqlite3
from flask import g


app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/products/list')
def productslist():
    products = query_db("select * from products")
    return render_template("/products/list.html", products = products)

@app.route('/products/create', methods = ['POST', 'GET'])
def producstcreate():
    if request.method == 'GET':
        return render_template("/products/create.html")
    else:
        titol = request.form['titol']
        desc = request.form['description']
        preu = request.form['preu']
        cat_id = 1
        sell_id = 1
        created = datetime.now()
        updated = datetime.now()
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto and allowed_file(foto.filename):
                with get_db() as db:
                    db.execute(
                        "INSERT INTO products (title, description, photo, price, category_id, seller_id, created, updated) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (titol, desc, foto.filename, preu, cat_id, sell_id, created, updated)
                    )   
        
        return redirect(url_for('productslist'))

@app.route('/products/read/<int:product_id>', methods = ['GET'])
def readprod(product_id):
    with get_db() as db:
        res = db.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        items = res.fetchone()
    
    return render_template('/products/read.html', product = items)



if __name__ == 'main':
    app.run(debug = True)   