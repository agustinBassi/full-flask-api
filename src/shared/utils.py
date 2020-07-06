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

    # TODO: create function to validate if headers has required application/json. Can be a decorator

    @staticmethod
    def create_json_response(res, status_code):
        """
        Custom Response Function
        """
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=status_code
        )

    @staticmethod
    def to_json(inst, cls):
        """
        Jsonify the sql alchemy query result.
        """
        convert = dict()
        # add your coversions for things like datetime's 
        # and what-not that aren't serializable.
        d = dict()
        for c in cls.__table__.columns:
            v = getattr(inst, c.name)
            if c.type in convert.keys() and v is not None:
                try:
                    d[c.name] = convert[c.type](v)
                except:
                    d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
            elif v is None:
                d[c.name] = str()
            else:
                d[c.name] = v
        return json.dumps(d)

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
