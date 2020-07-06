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

from ..shared.utils import Utils
from ..models.state_model import StateModel

#########[ Settings & Data ]###################################################

state_api = Blueprint('states', __name__)

#########[ Module main code ]##################################################

@state_api.route('/', methods=['GET'])
def get_all_states():
    # create response for all users
    response = {
        'states': list(map(
            lambda user: user.serialize(), StateModel.query.all()
            ))
    }
    # return the response with the status code
    return Utils.create_json_response(response, 200)

@state_api.route('/<int:state_id>/', methods=['GET'])
def get_state(state_id):
    # obtain the first user with the device_id
    state = StateModel.get_one_state(state_id)
    # abort if no device found
    if state is None:
        return Utils.create_json_response({"error" : "not found"}, 404)
    # return the response with the status code
    return Utils.create_json_response(state.serialize(), 200)

@state_api.route('/', methods=['POST'])
def create_state():

    def __validate_request_data():
        # at this place validates all required fields
        if  request.json is None or \
            request.headers['Content-Type'] != 'application/json' or \
            not 'name' in request.json or \
            not 'code' in request.json:
            return False
        
        if not Utils.validate_value(request.json['name'], allowed_types=[str], lenght=128) or \
            not Utils.validate_value(request.json['code'], allowed_types=[int], min_val=1, max_val=999999):
            return False

        return True

    # evaluates request data before to do anything
    if not __validate_request_data():
        return Utils.create_json_response({"error" : "bad request"}, 400)

    # if program reaches this section request data is OK
    state = StateModel(request.json)
    status = state.save()
    if not status:
        return Utils.create_json_response({"error" : "not allowed"}, 405)
    # return the response with the status code
    return Utils.create_json_response(state.serialize(), 201)

@state_api.route('/<int:state_id>/', methods=['PUT'])
def update_state(state_id):

    def __validate_request_data():
        # at this place validates all required fields
        if  request.json is None or \
            request.headers['Content-Type'] != 'application/json' or \
            not 'name' in request.json or \
            not 'code' in request.json:
            return False
        
        if request.json.get('name') is not None and \
            not Utils.validate_value(request.json['name'], allowed_types=[str], lenght=128):
            return False
        if request.json.get('code') is not None and \
            not Utils.validate_value(request.json['code'], allowed_types=[int], min_val=1, max_val=999999):
            return False

        return True

    # obtain the first user with the device_id
    state = StateModel.get_one_state(state_id)
    # abort if no device found
    if state is None:
        return Utils.create_json_response({"error" : "not found"}, 404)

    # evaluates request data before to do anything
    if not __validate_request_data():
        return Utils.create_json_response({"error" : "bad request"}, 400)
    
    status = state.update(request.json)
    if not status:
        return Utils.create_json_response({"error" : "not allowed"}, 405)
    # return the response with the status code
    return Utils.create_json_response(state.serialize(), 200)

@state_api.route('/<int:state_id>/', methods=['DELETE'])
def delete_user(state_id):
    # obtain the first user with the device_id
    state = StateModel.get_one_state(state_id)
    # abort if no device found
    if state is None:
        return Utils.create_json_response({"error" : "not found"}, 404)
    
    state.delete()
    # return the response with the status code
    return Utils.create_json_response({'message' : 'deleted'}, 204)

#########[ end of file ]#######################################################
