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

#########[ Module main code ]##################################################

class StateModel(db.Model):

    """
    StateModel Model
    """

    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, nullable=False, index=True, unique=True)
    name = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    user = db.relationship('UserModel', backref='state', lazy='dynamic')

    def __init__(self, data):
        self.code = data.get('code')
        self.name = data.get('name')
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
        StateModel.check_if_table_exists()


    def save(self):
        if not StateModel.check_if_code_exists(self.code):
            db.session.add(self)
            db.session.commit()
            return True
        return False

    def update(self, data):
        if not StateModel.check_if_code_exists(self.code):
            for key, item in data.items():
                setattr(self, key, item)
            self.updated_at = datetime.datetime.utcnow()
            db.session.commit()
            return True
        return False

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_states():
        return StateModel.query.all()

    @staticmethod
    def get_one_state(id):
        return StateModel.query.get(id)

    @staticmethod
    def get_by_code(code):
        return StateModel.query.filter_by(code=code).first()

    @staticmethod
    def check_if_code_exists(code):
        if StateModel.query.filter_by(code=code).first():
            return True
        return False

    @staticmethod
    def check_if_table_exists():
        states = None
        try:
            states = StateModel.get_all_states()
        except:
            pass
        if not states:
            db.create_all()
    
    def __repr__(self):
        return {
            "id" : self.id,
            "code" : self.code,
            "name" : self.name,
            "created_at" : self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at" : self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def serialize(self):
        return {
            "id" : self.id,
            "code" : self.code,
            "name" : self.name,
            "created_at" : self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at" : self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

#########[ end of file ]#######################################################