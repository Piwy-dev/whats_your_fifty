import os
from flask import Flask, render_template, request, redirect
import app.database as db
import app.options_db as odb

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
        print(options)
        return render_template('home.html', options=options)
    
    @app.route('/add-option', methods=['GET', 'POST'])
    def add_option():
        if request.method == 'POST':
            option = request.form.get('option_name')
            odb.add_option(option)
            return redirect('/')
        elif request.method == 'GET':
            return render_template('add_option.html')

    return app