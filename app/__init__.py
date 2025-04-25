import os
from flask import Flask, render_template, request, redirect
import app.database as db
import app.options_db as odb
import app.participants_db as pdb

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # register the database commands
    db.init_app(app)

    with app.app_context():
        db.init_db()
    
    @app.route('/')
    def home():
        options = odb.get_all_options()
        print("Options:", options)
        participants = pdb.get_all_participants()
        return render_template('home.html', options=options, participants=participants)
    
    @app.route('/add-option', methods=['GET', 'POST'])
    def add_option():
        if request.method == 'POST':
            option = request.form.get('option_name')
            odb.add_option(option)
            return redirect('/')
        elif request.method == 'GET':
            return render_template('add_option.html')
        
    @app.route('/add-participant', methods=['GET', 'POST'])
    def add_participant():
        if request.method == 'POST':
            participant = request.form.get('participant_name')
            pdb.add_participant(participant)
            return redirect('/')
        elif request.method == 'GET':
            return render_template('add_participant.html')
        
    @app.route('/delete-all-options')
    def delete_all_options():
        odb.delete_all_options()
        return redirect('/')

    return app