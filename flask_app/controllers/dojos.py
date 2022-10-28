from flask import redirect, render_template, request, session
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', all_dojos = all_dojos)

@app.route('/dojos/<int:dojo_id>')
def view_one_dojo(dojo_id):
    data = {
        'id' : dojo_id
    }
    one_dojo = Dojo.get_one_dojo(data)
    session['current_dojo'] = one_dojo.id
    return render_template('one_dojo.html', one_dojo = one_dojo)

@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    
    data = {
        'name' : request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')