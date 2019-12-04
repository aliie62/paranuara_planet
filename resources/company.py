from flask_restful import Resource
from models.company import Company


class CompanyResource(Resource):
    def get(self, name):
        try:
            result = Company.find_by_name(name)
            if result:
                return result, 200
            else:
                return {'message':'Company not found.'} , 404
        except:
            return {'message':'An error occurred in reading the data.'}, 500
        