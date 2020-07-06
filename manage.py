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
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app, db

#########[ Settings & Data ]###################################################

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)
migrate = Migrate(app=app, db=db)
manager = Manager(app=app)

#########[ Module main code ]##################################################

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()

#########[ end of file ]#######################################################


