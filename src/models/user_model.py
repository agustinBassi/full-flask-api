#!/usr/bin/env python3
###############################################################################
# Author: Agustin Bassi
# Date: July 2020
# Copyright: Bankar
# Project: Bankar Python code challenge
# Brief: Project to test skill working with Python & REST APIs
###############################################################################

#########[ Imports ]########################################################### 

import datetime
import json

from . import db

from .state_model import StateModel

#########[ Settings & Data ]###################################################

class UserModel(db.Model):
    """
    User Model
    """

    # table name
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    state_code = db.Column(db.Integer, db.ForeignKey("states.code"))

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.age = data.get('age')
        self.state_code = data.get('state_code')
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

        # TODO: Resolve state here

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.updated_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)

    @staticmethod
    def check_if_table_exists():
        users = None
        try:
            users = UserModel.get_all_users()
        except:
            pass
        if not users:
            db.create_all()

    def __repr__(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "age" : self.age,
            "created_at" : self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at" : self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def serialize(self):

        state = StateModel.get_by_code(self.state_code).serialize()

        return {
            "id" : self.id,
            "name" : self.name,
            "age" : self.age,
            "created_at" : self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "state" : state
            
            # TODO: Check why not works updated_at
            # "updated_at" : self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

#########[ end of file ]#######################################################
