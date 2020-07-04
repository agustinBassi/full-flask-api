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

    # TODO: return all users as JSON

    all_users = UserModel.get_all_users()
    # return the response with the status code
    return custom_response({'users': "all_users"}, 200)

@user_api.route('/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    # obtain the first device with the device_id
    user = UserModel.query.filter_by(id=user_id).first()
    # abort if no device found
    if user is None:
        abort(404)

    # TODO: Apply some more filter to check the user

    # TODO: representate user as json.

    # return the response with the status code
    return custom_response({'user' : user.serialize()}, 200)

@user_api.route('/', methods=['POST'])
def create_user():

    # TODO: Apply validation for received JSON

    data = {
        "name" : "Agustin",
        "age"  : 30
    }

    user = UserModel(data)
    user.save()
    # return the response with the status code
    return custom_response({'user' : user.serialize()}, 201)

@user_api.route('/', methods=['UPDATE'])
def update_user():

    # TODO: implement same validation as put.

    # TODO: return 200 Code because not post

    pass

@user_api.route('/', methods=['DELETE'])
def delete_user():

    # TODO: implement same validation as put.

    # TODO: return 200 Code because not post

    # TODO: check response to return
    
    pass

#########[ end of file ]#######################################################
