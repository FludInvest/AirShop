from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
#db = SQLAlchemy(app)
#
#
#class Users(db.Model):
#    id = db.Column(db.Integer,primary_key = True)
#    email = db.Column(db.String,nullable = False)
#    password = db.Column(db.String,nullable = False)




@app.route('/')

def index():
    return render_template('main.html')

@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/price')

def price():
    
    return render_template('price.html')

@app.route('/1')
def page():
    return render_template('rr.html' ,data ="1")

@app.route('/2')
def page2():
    return render_template('rr.html' ,data ="2")

@app.route('/3')
def page3():
    return render_template('rr.html' ,data ="3")

@app.route('/4')
def page4():
    return render_template('rr.html' ,data ="4")

@app.route('/5')
def page5():
    return render_template('rr.html' ,data ="5")

@app.route('/6')
def page6():
    return render_template('rr.html' ,data ="6")

@app.route('/7')
def page7():
    return render_template('rr.html' ,data ="7")

@app.route('/8')
def page8():
    return render_template('rr.html' ,data ="8")

@app.route('/9')
def page9():
    return render_template('rr.html' ,data ="9")




if __name__ == "__main__":
    app.run(debug = True)