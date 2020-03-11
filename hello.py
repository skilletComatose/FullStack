from flask import Flask,render_template,redirect,url_for,request,jsonify    
from flask_sqlalchemy import SQLAlchemy                                 
from flask_marshmallow import Marshmallow                                   
from sqlalchemy import desc                                                  
import hashlib                                                                      


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///basedatos/tasks.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Datos(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    hash=db.Column(db.String(100))


class DatoSchema(ma.ModelSchema):
    class Meta:
        model = Datos



@app.route("/")
def home():
    last= Datos.query.all()
    return render_template('index.html',last=last)

@app.route('/chain', methods=['POST','GET'])
def guardar():
    if(request.method=='POST'):
        has1=request.form['contenedor']
        has=hashlib.new('sha1',(has1.encode('utf-8')))
        hash=Datos(hash=has.hexdigest())
        db.session.add(hash)
        db.session.commit()
        return redirect(url_for('home'))

    if(request.method=='GET'):
        datos= Datos.query.all()
        return render_template('index.html',datos=datos)
        

@app.route('/chain/last')
def last():
    Datos.query.order_by(desc(Datos.id)).limit(5)
    last= Datos.query.order_by(desc(Datos.id)).first()
    return render_template('2.html',last=last)   

@app.route('/api/v1/chain')
def showJason():
    hashSchema = DatoSchema(many=True)
    hashes = Datos.query.all()
    output = hashSchema.dump(hashes)

    return(jsonify( {'datos':output} ))
    
if __name__ =='__main__':
    app.run(debug=True)
