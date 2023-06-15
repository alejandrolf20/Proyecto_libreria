from flask import Flask, render_template, abort
import json

app = Flask(__name__)

with open('books.json') as f:
    books_data = json.load(f)

@app.route('/')
def inicio():
    return render_template('base.html', books=books_data)

@app.route('/libro/<isbn>')
def libro(isbn):
    for book in books_data:
        if 'isbn' in book and book['isbn'] == isbn:
            return render_template('libro.html', book=book)
    abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
    filtered_books = [book for book in books_data if categoria in book['categories']]
    return render_template('categoria.html', categoria=categoria, libros=filtered_books)

if __name__ == '__main__':
    app.run(debug=True)