from flask import Flask
from flask import render_template, request
import sqlite3 

app = Flask(__name__)



@app.route('/')
def login():
    return render_template('login.html')

@app.route('/loginmanager', methods = ['POST', 'GET'])
def loginmanager():
    conn = sqlite3.connect('Deliverable3.db')
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            print(username)
            print(password)
            statement = conn.execute('SELECT username FROM managers')
            msg = "SUCCESS"
            count = -1
            for row in statement:
                count = count + 1
                if username in row:
                    fnstatement = conn.execute("SELECT firstname FROM managers WHERE username=username")
                    firstname = fnstatement.fetchall()[count][0]
                    lnstatement = conn.execute("SELECT lastname FROM managers WHERE username=username")
                    lastname = lnstatement.fetchall()[count][0]
                    return render_template('index-manager.html', firstname=firstname, lastname=lastname)
            conn.close()
        except:
            msg = "ERROR"
            return render_template('message.html', msg=msg)
        finally:
            conn.close() 

@app.route('/manager-register')
def manager_register():
    return render_template('manager-register.html')

@app.route('/addmanager', methods = ['POST', 'GET'])
def addmanager():
    if request.method == 'POST':
        try:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            username = request.form['username']
            email = request.form['email']
            password = request.form['inputpassword']
            usertype = 'manager'
            data = (firstname, lastname, username, email, password, usertype)
            with sqlite3.connect("Deliverable3.db") as con:
                cur = con.cursor()
                statement = """INSERT INTO 'managers' (firstname, lastname, username, email, password, usertype) VALUES (?,?,?,?,?,?);"""
                cur.execute(statement, data)
                con.commit()
                print('SUCCESS')
                msg = "SUCCESS"
        except:
            con.rollback()
            msg = "ERROR"
        finally:
            return render_template('message.html', msg=msg)
            con.close()

@app.route('/logintester', methods = ['POST', 'GET'])
def logintester():
    conn = sqlite3.connect('Deliverable3.db')
    if request.method == 'POST':
        try:
            employeeID = request.form['employeeID']
            password = request.form['password']
            statement = conn.execute('SELECT employeeID FROM testermembers')
            count = -1
            for row in statement:
                msg = "SUCCESS"
                count = count + 1
                if employeeID in row:
                    fnstatement = conn.execute("SELECT firstname FROM testermembers WHERE employeeID=employeeID")
                    firstname = fnstatement.fetchall()[count][0]
                    lnstatement = conn.execute("SELECT lastname FROM testermembers WHERE employeeID=employeeID")
                    lastname = lnstatement.fetchall()[count][0]
                    if (int(employeeID[0])) == 0:
                        return render_template('index-tester.html', firstname=firstname, lastname=lastname)
                    else:
                        return render_template('index-tester.html', firstname=firstname, lastname=lastname)
            conn.close()
        except:
            print('ERROR')
            msg = "ERROR"
            return render_template('message.html', msg=msg)
        finally:
            conn.close()

@app.route('/tester-register')
def tester_register():
    return render_template('tester-register.html')

@app.route('/addtester', methods = ['POST', 'GET'])
def addtester():
    if request.method == 'POST':
        try:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            employeeID = request.form['employeeID']
            username = request.form['username']
            email = request.form['email']
            password = request.form['inputpassword']
            usertype = 'tester'
            data = (firstname, lastname, employeeID, username, email, password, usertype)
            with sqlite3.connect("Deliverable3.db") as con:
                cur = con.cursor()
                statement = """INSERT INTO 'testermembers' (firstname, lastname, employeeID, username, email, password, usertype) VALUES (?,?,?,?,?,?,?);"""
                cur.execute(statement, data)
                con.commit()
                print('SUCCESS')
                msg = 'SUCCESS'
        except:
            print('ERROR')
            msg = 'ERROR'
            con.rollback()
        finally:
            return render_template('message.html', msg=msg)
            con.close()


# dashboard pages
@app.route('/Project Manager')
def manager():
    return render_template('index-manager.html')

@app.route('/tester')
def tester():
    return render_template('index-tester.html')



# manager tabs
@app.route('/manager-services')
def manager_services():
    return render_template('manager-services.html')

@app.route('/manager-payments')
def manager_payments():
    return render_template('manager-payments.html')

@app.route('/manager-catalog')
def manager_catalog():
    return render_template('manager-catalog.html')



@app.route('/tester-tasks')
def tester_tasks():
    return render_template('tester-tasks.html')



if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=80)\
    app.run()
    


