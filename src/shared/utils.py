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

import json

#########[ Module main code ]##################################################

class Utils:
    
    def __init__(self):
        pass

    @staticmethod
    def create_json_response(res, status_code):
        """
        JSON Response Function
        """
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=status_code
        )

    @staticmethod
    def validate_value(value=None, allowed_types=[], min_val=0, max_val=0, lenght=0):
        # at first checks if the key exists
        if value is None:
            return False
        # then, validates key type before to continue
        invalid_type = True
        for allowed_type in allowed_types:
            if isinstance(value, allowed_type):
                invalid_type = False
                break
        if invalid_type:
            return False
        # for each data type evaluate different things
        if isinstance(value, int) or isinstance(value, float):
            if value < min_val or value > max_val:
                return False
        elif isinstance(value, str):
            if len(value) > lenght:
                return False
        elif isinstance(value, bool):
            pass
        else:
            return False
        # if program reaches this line, the data is correct to assing
        return True

#########[ end of file ]#######################################################
