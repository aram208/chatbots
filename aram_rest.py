#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:01:52 2017

@author: aram
"""

from flask import Flask
from flask_restful import Resource, Api

from chatbrain import brain

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world2'}

class ConversationResource(Resource):
    def get(self):
        

# api.add_resource(HelloWorld, '/')
api.add_resource(ConversationResource, '/')
        
if __name__ == '__main__':
    app.run(debug=True)