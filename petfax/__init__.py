# config                    
from flask import Flask
from flask_migrate import Migrate 
from .models import db
import os
# TRY THIS: from models import db



# factory
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    # TRY THIS: app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/petfax')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # from . import models 
    # models.db.init_app(app)
    # migrate = Migrate(app, models.db)

    db.init_app(app)
    migrate = Migrate(app, db)

    # index route
    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet 
    app.register_blueprint(pet.bp)

    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    for rule in app.url_map.iter_rules():
        print(rule)

    # return the app 
    return app