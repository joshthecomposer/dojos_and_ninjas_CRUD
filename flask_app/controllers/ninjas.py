from flask import redirect, render_template, request, url_for
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/ninjas')
def ninjas():
    all_dojos = Dojo.get_all_dojos()
    all_ninjas = Ninja.get_all_ninjas()
    return render_template('ninjas.html', all_dojos=all_dojos, all_ninjas=all_ninjas)

@app.route('/add_ninja', methods=['POST'])
def add_ninja():
    data = {
        'dojo_id' : request.form['dojo_id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    
    Ninja.save(data)
    return redirect('/dojos/'+ data['dojo_id'])

@app.route('/ninja/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    
    Ninja.delete(data)
    return redirect('/dojos')

@app.route('/ninja/edit/<int:id>')
def edit(id):
    data = {
        'id' : id
    }
    one_ninja = Ninja.get_one_ninja(data)
    return render_template('edit_ninja.html', one_ninja=one_ninja[0])

@app.route('/update_ninja', methods=['POST'])
def update_ninja():
    data = {
        'id' : request.form['id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    Ninja.update_ninja(data)
    return redirect('/ninjas')