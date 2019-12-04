# -*- coding: utf-8 -*-

from flask_restful import Api
from resources.person import PersonResource
from resources.company import CompanyResource

#Define app end points
def get_endpoints(app):
    api = Api(app)
    api.add_resource(PersonResource,'/people','/people/<string:username>')
    api.add_resource(CompanyResource,'/company/<string:name>')
    return api
