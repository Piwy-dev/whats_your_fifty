import os
from flask import Flask, render_template, request
import app.database as db

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
        return render_template('home.html')
    
    @app.route('/add-option', methods=['GET', 'POST'])
    def add_option():
        if request.method == 'POST':
            option = request.form.get('option_name')
            print(f"Option added: {option}")
            return render_template('add_option.html', success=True, option=option)
        elif request.method == 'GET':
            return render_template('add_option.html')

    return app