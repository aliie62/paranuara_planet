from flask_restful import Resource,reqparse
from models.person import Person


class PersonResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username1', type=str, required=True)
    parser.add_argument('username2',  type=str, required=True)
   

    def get(self, username):
        try:
            person = Person.find_by_username(username)
            if person:
                return person, 200
            else:
                return {'message':'Person not found.'} , 404
        except:
            return {'message':'An error occurred in reading the data.'}, 500
        
    def post(self):
        try:
            params = PersonResource.parser.parse_args()
        except:
            return {'message':'The passed data is not in expected format.'}, 400
        else:
            try:
                result = Person.find_two(params['username1'], params['username2'])
                if result:
                    return result, 200
                else:
                    return {'message':'The provided username(s)not found'}, 404
            except:
                return {'message':'An error occurred in reading the data.'}, 500