from flask import Flask,render_template ,url_for,request, jsonify

import sqlite3 as sql
app = Flask(__name__)

#hashes = []


def CreateTable(): 
    conn = sql.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS hashes (HASH text )')
    print("table created")
    conn.close()

CreateTable()

@app.route("/")
def main():
    return render_template('index.html')


@app.route('/chain',  methods=['GET','POST'] )
def InsertHash():
    if request.method == 'POST':
        new_hash = request.form['h']
    
        try:                                                             
                                    
            with sql.connect("database.db") as con:

                cur = con.cursor()                                      
                                                                        
                cur.execute('INSERT INTO hashes (HASH) VALUES (?)',(new_hash))
                
                con.commit()

                mensaje = "    *************    Successful ************* "

        except:
            con.rollback()
            mensaje = "        *************      Error    ************** "

        finally:
            con.close()
           
            return render_template("resultado.html",msg = mensaje)

    
        def Show():
             con = sql.connect('database.db')
             con.row_factory = sql.Row
             cur = con.cursor()
             cur.execute('select HASH from hashes')
             registers_saved = cur.fetchall()
             return render_template('index.html',rows =  registers_saved)     
    
    return render_template('insert.html')
    

'''
@app.route("/chain, methods=['GET','POST']")


def InsertHash():
    if request.method == 'POST':
        
        try:                                                            #detecta un error 
                                      #obtiene los datos del form
            nam = request.form['NAME']
            Vhash = request.form['HASH']

            with sql.connect("database.db") as con:

                cur = con.cursor()                                      #prepara in cursor
                                                                        #ejecuta insercion
                cur.execute('INSERT INTO hashes (ID,NAME,HASH) VALUES (?,?,?)',(nam,Vhash))
                
                con.commit()

                mensaje = "mensaje exitoso "

        except:
                                                                        #hace un rollback debido al error
            con.rollback()
            mensaje = "error en la insercion"

        finally:

            con.close()
            #renderiza a template de resultados 
            return render_template("resultado.html",msg = mensaje)

    
          


@app.route('/chain', methods=['GET', 'POST']) #decorador, metodos permitidos para esa ruta  
def chain():
    if request.method == 'POST':                # validar metodo 
        new_hash = request.args.get('hash')
        if new_hash is None:                   #verificar que haya un hash
            return ""
        #hashes.append(new_hash)                #agrega nuevo hash
    else:
       # return jsonify(hashes)
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)