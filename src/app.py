#!/usr/bin/env python3
###############################################################################
# Author: Agustin Bassi
# Date: July 2020
# Copyright: Bankar
# Project: Bankar Python code challenge
# Brief: Project to test skill working with Python & REST APIs
###############################################################################

#########[ Imports ]########################################################### 

from flask import Flask

from .config import app_config
from .models import db
from .views.user_views import user_api as user_blueprint 
from .views.state_views import state_api as state_blueprint 

#########[ Module main code ]##################################################

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
