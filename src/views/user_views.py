#!/usr/bin/env python3
###############################################################################
# Author: Agustin Bassi
# Date: July 2020
# Copyright: Bankar
# Project: Bankar Python code challenge
# Brief: Project to test skill working with Python & REST APIs
###############################################################################

#########[ Imports ]########################################################### 

from flask import Blueprint, Response, abort, json, jsonify, request, url_for

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from ..shared.utils import custom_response
from ..models.user_model import UserModel

#########[ Settings & Data ]###################################################

user_api = Blueprint('users', __name__)

#########[ Module main code ]##################################################

@user_api.route('/', methods=['GET'])
def get_all_users():
    # return the response with the status code
    return custom_response({'user': "fake user"}, 200)

@user_api.route('/<user_id>/', methods=['GET'])
def get_user(user_id):
    # obtain the first device with the device_id
    user = UserModel.query.filter_by(id=user_id).first()
    # abort if no device found
    if user is None:
        abort(404)
    # return the response with the status code
    return custom_response({'user': "fake user"}, 200)

@user_api.route('/', methods=['POST'])
def create_user():
    data = {
        "name" : "Agustin",
        "age"  : 30
    }

    user = UserModel(data)
    # user.save()
    # return the response with the status code
    return custom_response({'user': user.name}, 201)

#########[ end of file ]#######################################################
