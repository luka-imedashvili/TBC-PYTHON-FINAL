from flask import Flask, render_template
app = Flask(__name__)

genres = [{"name": "Fantasy", 'img': "category1.png"},
          {"name": "Science Fiction", 'img': "category2.png"},
          {"name": "Mystery", 'img': "category3.png"},
          {"name": "Romance", 'img': "category4.png"},
          {"name": "Historical Fiction", 'img': "category5.png"}]



@app.route('/')
def index():
    return render_template('index.html', genres=genres)

@app.route('/books')
def books():
    return render_template('books.html')



app.run(debug=True)
