# --------------------------------------------------------------------------------------------------#
# !/usr/bin/env python
# !python 3.5
""" pydel_web_tier.py: Web Tier Layer responsible for intaking UI request. """
# __module_       = ""   PyDel - Core  ""
# __author__      = "Tata Consultancy Services "
# __copyright__   = "Copyright 2019"
# --------------------------------------------------------------------------------------------------#

##############################################################
# IMPORTING PACKAGES
##############################################################

import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from model.core.pydel_controller import do_check_validation
from model.core.pydel_controller import do_submit_job
import pandas as pd

##############################################################
# DEFINING GLOBAL VARIABLES
##############################################################

app = Flask(__name__)
api = Api(app)

CORS(app, resources={r"/*": {"origins": "*"}})



##############################################################
# DEFINING CLASS VARIABLES
##############################################################

class doValidate(Resource):
    def get(self):
        print('Data Validation ')
        #__do_start_config_validation()
        return jsonify({"response": 'test', "response1": 'test1'})

class doSubmit(Resource):
    def get(self):
        print('Class data ingest ')
        #__do_start_config_validation()
        #__do_start_config_validation()
        config = pd.read_csv('resource/pydel_config.csv')
        do_submit_job(config)
        return jsonify({"response": 'test', "response1": 'test1'})

api.add_resource(doSubmit,'/doSubmit')
api.add_resource(doValidate,'/doValidate')
api.add_resource(doValidate,'/doexplore')

if __name__ == "__main__":
    app.run(debug=True)