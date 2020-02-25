from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///basedatos/tasks.db'
db = SQLAlchemy(app)

class Datos(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    hash=db.Column(db.String(100))
    


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/chain', methods=['POST','GET'])
def guardar():
    if(request.method=='POST'):
        has=Datos(hash=request.form['contenedor'])
        db.session.add(has)
        db.session.commit()
        return redirect(url_for('home'))
    
    if(request.method=='GET'):
        datos= Datos.query.all()
        return render_template('index.html',datos=datos)
        
    

if __name__ =='__main__':
    app.run(debug=True)
