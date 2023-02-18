from flask import Flask, request, jsonify, make_response
from fake_detection.backend.routes.token_generator import token_required
from fake_detection.backend import app
from fake_detection.backend.db_model import User, db
import uuid # for public id
from  werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta

  
# signup route
@app.route('/signup', methods =['POST'])
def signup():
    req_data = request.get_json()
    name = req_data['name']
    email = req_data['email']
    password = req_data['password']
  
    # checking for existing user
    user = User.query\
        .filter_by(email = email)\
        .first()
    if not user:
        # database ORM object
        user = User(
            public_id = str(uuid.uuid4()),
            name = name,
            email = email,
            password = generate_password_hash(password)
        )
        # insert user
        db.session.add(user)
        db.session.commit()
  
        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)