"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favorites
from sqlalchemy import select
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def get_users():
    try:
        data = db.session.scalars(select(User)).all()
        results = list(map(lambda item: item.serialize(), data))
        
        response_body = {
            "results": results
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400


@app.route('/user/favorites', methods=['GET'])
def get_favorites():
    try:
        user = User.query.first()
        if not user:
            return jsonify({'error': 'No users found'}), 404
        
        favs = Favorites.query.filter_by(user_id=user.id).all()
        people = []
        planets = []
        list(map(lambda item: people.append(item.serialize()) if item.serialize()["people"] else planets.append(item.serialize()), favs))

        response_body = {
            "results": {
                "fav_people": people,
                "fav_planets": planets
            }
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400


@app.route('/people', methods=['GET'])
def get_people():
    try:
        data = db.session.scalars(select(People)).all()
        results = list(map(lambda item: item.serialize(), data))
        response_body = {
            "results": results
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400
    

@app.route('/people/<int:id>', methods=['GET'])
def get_people_id(id):
    try:
        people = db.session.execute(db.select(People).filter_by(id=id)).scalar_one().serialize()
        response_body = {
            "results": people
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400


@app.route('/people', methods=['POST'])
def post_people():
    try:
        request_data = request.json
        people = People(name=request_data["name"], age=request_data["age"])
        db.session.add(people)
        db.session.commit()
        
        response_body = {
            "msg": "Person added"
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400


@app.route('/people/<int:id>', methods=['DELETE'])
def delete_people(id):
    try:
        people = db.session.execute(db.select(People).filter_by(id=id)).scalar_one()
        db.session.delete(people)
        db.session.commit()
        
        response_body = {
            "msg": "Person deleted",
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400


@app.route('/favorites/people/<int:id>', methods=['POST'])
def post_people_favorite(id):
    try:
        user = User.query.first()
        if not user:
            return jsonify({'error': 'No users found'}), 404
        
        people = db.session.execute(db.select(People).filter_by(id=id)).scalar_one().serialize()
        fav = Favorites(user_id=user.id, people_id=people["id"])
        db.session.add(fav)
        db.session.commit()

        response_body = {
            "msg": "Person added to fav"
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400
    

@app.route('/favorites/people/<int:id>', methods=['DELETE'])
def delete_favorite_people(id):
    user = User.query.first()
    if not user:
        return jsonify({'error': 'No users found'}), 404

    favorite = Favorites.query.filter_by(user_id=user.id, people_id=id).first()
    if not favorite:
        return jsonify({'error': 'Favorite not found'}), 404

    db.session.delete(favorite)
    db.session.commit()
    return jsonify({'message': f'Person with id {id} removed from favorites'})
    

@app.route('/planets', methods=['GET'])
def get_planets():
    try:
        data = db.session.scalars(select(Planets)).all()
        results = list(map(lambda item: item.serialize(), data))
        response_body = {
            "msg": "Hello, this is your GET /user response ",
            "results": results
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400
    
    
@app.route('/planets/<int:id>', methods=['GET'])
def get_planets_id(id):
    try:
        planets = db.session.execute(db.select(Planets).filter_by(id=id)).scalar_one().serialize()
        response_body = {
            "msg": "Hello, this is your GET /user response ",
            "results": planets
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400


@app.route('/planets', methods=['POST'])
def post_planets():
    try:
        request_data = request.json
        planets = Planets(name=request_data["name"], size=request_data["size"])
        db.session.add(planets)
        db.session.commit()
        
        response_body = {
            "msg": "Planet added"
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400


@app.route('/planets/<int:id>', methods=['DELETE'])
def delete_planets(id):
    try:
        planets = db.session.execute(db.select(Planets).filter_by(id=id)).scalar_one()
        db.session.delete(planets)
        db.session.commit()
        
        response_body = {
            "msg": "Planet deleted",
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400


@app.route('/favorites/planets/<int:id>', methods=['POST'])
def post_planet_favorite(id):
    try:
        user = User.query.first()
        if not user:
            return jsonify({'error': 'No users found'}), 404
        
        planets = db.session.execute(db.select(Planets).filter_by(id=id)).scalar_one().serialize()
        fav = Favorites(user_id=user.id, planets_id=planets["id"])
        db.session.add(fav)
        db.session.commit()
        response_body = {
            "msg": "planet added to fav"
        }

        return jsonify(response_body), 200
    
    except:
        return "Error", 400


@app.route('/favorites/planets/<int:id>', methods=['DELETE'])
def delete_favorite_planet(id):
    user = User.query.first()
    if not user:
        return jsonify({'error': 'No users found'}), 404

    favorite = Favorites.query.filter_by(user_id=user.id, planets_id=id).first()
    if not favorite:
        return jsonify({'error': 'Favorite not found'}), 404

    db.session.delete(favorite)
    db.session.commit()
    return jsonify({'message': f'Planet with id {id} removed from favorites'})



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
