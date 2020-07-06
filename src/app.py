#!/usr/bin/env python3
###############################################################################
# Author: Agustin Bassi
# Date: July 2020
# Copyright: Bankar
# Project: Bankar Python code challenge
# Brief: Project to test skill working with Python & REST APIs
###############################################################################

#########[ Imports ]########################################################### 

import csv
import logging

from flask import Flask

from sqlalchemy_utils import create_database, database_exists, drop_database

from .config import app_config
from .models import db
from .models.state_model import StateModel
from .models.user_model import UserModel
from .views.state_views import state_api as state_blueprint
from .views.user_views import user_api as user_blueprint

#########[ Module main code ]##################################################

def initialize_database(app):
    
    def _fill_states_table():
        # read states tables
        states = None
        try:
            states = StateModel.get_all_states()
        except:
            pass
        # if table has not loaded values ...
        if not states:
            # read csv from app config
            csv_states_path = app.config['STATES_CSV_FILE'] 
            # convert csv to dict
            dict_states = csv.DictReader(open(csv_states_path), delimiter=";")
            # iterate over each csv row creating a state object
            for state_row in dict_states:
                # adapt spanish headers to english headers
                state_data = {
                    'code' : int(state_row["codigo"]),
                    'name' : state_row["nombre"],
                }
                # create and save each state into DB
                state = StateModel(state_data)
                state.save()
        else:
            pass
    
    # at first check if database exists, if not, create it.
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    # create all tables from models
    db.create_all()
    # fill states tables from CSV
    _fill_states_table()


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)
    # initialize app from object depending on environment
    app.config.from_object(app_config[env_name])
    # set db
    db.init_app(app) 
    # registers app blueprints
    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(state_blueprint, url_prefix='/api/v1/states')
    # push context in order to get app instance in other modules
    app.app_context().push()
    # create the database of application or check if exists
    initialize_database(app)

    @app.route('/', methods=['GET'])
    def index():
        """
        return available resources
        """
        return """
            <h1>Bankar API</h1>
            <br>
            <h3>Available resources are</h3>
            <br>
            <ul>
                <li>http://localhost:5000/api/v1/users</li>
                <li>http://localhost:5000/api/v1/states</li>
            </ul>
            """

    return app


#########[ end of file ]#######################################################
