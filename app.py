from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Operations, Currency, Employee

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cur')
def currency():
    curs = Currency.query.all()
    return render_template('cur.html',curs=curs)

@app.route('/emp')
def employee():
    emps=Employee.query.all()
    return render_template('emp.html',emps=emps)

@app.route('/op')
def operations():
    ops=Operations.query.all()
    return render_template('op.html',ops=ops)

@app.route('/addcur', methods=['GET', 'POST'])
def add_cur():
    if request.method == 'POST':
        name = request.form['name']
        rate = request.form['rate']
        cur = Currency(name=name, rate=rate)
        db.session.add(cur)
        db.session.commit()
        return redirect('/')
    return render_template('addcur.html')

@app.route('/addemp', methods=['GET', 'POST'])
def add_emp():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        job = request.form['job']
        emp = Employee(name=name, age=age, job=job)
        db.session.add(emp)
        db.session.commit()
        return redirect('/emp')
    return render_template('addemp.html')

@app.route('/addop', methods=['GET', 'POST'])
def add_op():
    if request.method == 'POST':
        value = request.form['value']
        fromName = request.form['fromName']
        toName = request.form['toName']
        op = Operations(value=value,fromName=fromName,toName=toName)
        db.session.add(op)
        db.session.commit()
        return redirect('/op')
    return render_template('addop.html')

@app.route('/editcur/<int:id>', methods=['GET', 'POST'])
def edit_cur(id):
    cur = Currency.query.get_or_404(id)
    if request.method == 'POST':
        cur.name = request.form['name']
        cur.rate = request.form['rate']
        db.session.commit()
        return redirect('/cur')
    return render_template('editcur.html', cur=cur)

@app.route('/editemp/<int:id>', methods=['GET', 'POST'])
def edit_emp(id):
    emp = Employee.query.get_or_404(id)
    if request.method == 'POST':
        emp.name = request.form['name']
        emp.age = request.form['age']
        emp.job = request.form['job']
        db.session.commit()
        return redirect('/emp')
    return render_template('editemp.html', emp=emp)

@app.route('/editop/<int:id>', methods=['GET', 'POST'])
def edit_op(id):
    op = Operations.query.get_or_404(id)
    if request.method == 'POST':
        op.value = request.form['value']
        op.fromName = request.form['fromName']
        op.toName = request.form['toName']
        db.session.commit()
        return redirect('/op')
    return render_template('editop.html', op=op)

@app.route('/delete_cur/<int:id>', methods=['POST'])
def delete_cur(id):
    cur= Currency.query.get_or_404(id)
    db.session.delete(cur)
    db.session.commit()
    return redirect('/cur')

@app.route('/delete_op/<int:id>', methods=['POST'])
def delete_op(id):
    op = Operations.query.get_or_404(id)
    db.session.delete(op)
    db.session.commit()
    return redirect('/op')

@app.route('/delete_emp/<int:id>', methods=['POST'])
def delete_emp(id):
    emp= Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect('/emp')

if __name__ == '__main__':
    app.run(debug=True)