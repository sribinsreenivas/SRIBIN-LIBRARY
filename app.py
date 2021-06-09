from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
 
 
 
 
app = Flask(__name __)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    bookbookname  = db.Column(db.String(100))
    authorname  = db.Column(db.String(100))
    isbn = db.Column(db.string(100))
 
 
    def __init__(self, bookname , authorname , isbn):
 
        self.bookname  = bookname 
        self.authorname  = authorname 
        self.isbn = isbn
 
 
 
 
 
#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()
 
    return render_template("index.html", employees = all_data)
 
 
 
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        bookname  = request.form['bookname ']
        authorname  = request.form['authorname ']
        isbn = request.form['isbn']
 
 
        my_data = Data(bookname , authorname , isbn)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Employee Inserted Successfully")
 
        return redirect(url_for('Index'))
 
 
#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
 
        my_data.bookname  = request.form['bookname ']
        my_data.authorname  = request.form['authorname ']
        my_data.isbn = request.form['isbn']
 
        db.session.commit()
        flash("Employee Updated Successfully")
 
        return redirect(url_for('Index'))
 
 
 
 
#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
 
    return redirect(url_for('Index'))
 
 
 
 
 
 
if __name __ == "__main__":
    app.run(debug=True)
 

