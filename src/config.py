#!/usr/bin/env python3
###############################################################################
# Author: Agustin Bassi
# Date: July 2020
# Copyright: Bankar
# Project: Bankar Python code challenge
# Brief: Project to test skill working with Python & REST APIs
###############################################################################

#########[ Imports ]########################################################### 

import os

#########[ Module main code ]##################################################

class Development(object):
    """
    Development environment configuration
    """
    HOST="0.0.0.0"
    PORT = 5000

    DEBUG = True
    TESTING = False

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STATES_CSV_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        "../data/states.csv"
        )
    

class Production(object):
    """
    Production environment configurations
    """
    PORT = 5100
    HOST="0.0.0.0"

    DEBUG = False
    TESTING = False
    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STATES_CSV_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        "../data/states.csv"
        )

class Testing(object):
    """
    Testing environment configuration
    """
    PORT = 5100
    HOST="0.0.0.0"

    TESTING = True
    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STATES_CSV_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        "../data/states.csv"
        )

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing,
}

#########[ end of file ]#######################################################