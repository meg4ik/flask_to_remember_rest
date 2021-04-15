from flask_restful import Resource
from src import api

class Smoke(Resource):
    def get(self):
        return {"message":200}, 200

def get_all_films():
    return [{'id':'1', 'title':'Harry Pot','release':'2000'},{'id':'2', 'title':'Harry Shpot','release':'2050'},{'id':'3', 'title':'Harry Snoop','release':'2051'}]

def get_all_films_by_uuid(uuid:str) -> dict:
    films = get_all_films()
    film = list(filter( lambda x: x["id"]==uuid , films))
    return film[0] if film else {}

def create_film(film_json:dict) -> list[dict]:
    films = get_all_films()
    films.append(film_json)
    return films


class FilmListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            films = get_all_films()
            return films, 200
        film = get_all_films_by_uuid(uuid)
        if not film:
            return '', 404
        else:
            return film, 200
            
    def post(self):
        film_json = request.json
        return create_film(film_json), 201
    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass

class FilmListApi(Resource):
    def get(self, uuid=None):
        pass   
    def post(self):
        pass
    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass

api.add_resource(Smoke, "/smoke", strict_slashes = False)
api.add_resource(FilmListApi, "/films", "/films/<uuid>", strict_slashes = False)