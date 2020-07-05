#!/usr/bin/env python3
###############################################################################
# Author: Agustin Bassi
# Date: July 2020
# Copyright: Bankar
# Project: Bankar Python code challenge
# Brief: Project to test skill working with Python & REST APIs
###############################################################################

#########[ Module main code ]##################################################

from flask_sqlalchemy import SQLAlchemy

# initialize database
db = SQLAlchemy()

from .user_model import UserModel
from .state_model import StateModel

#########[ end of file ]#######################################################