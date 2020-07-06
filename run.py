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
from src.app import create_app

#########[ Module main code ]##################################################


env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':
    env_name = os.getenv('FLASK_ENV')
    app = create_app(env_name)
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT']
        )

#########[ end of file ]#######################################################