from flask import Flask, request, jsonify, make_response
from fake_detection.backend.routes.token_generator import token_required
from fake_detection.backend import app
from fake_detection.backend.db_model import User
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta


# route for logging user in
@app.route('/login', methods =['POST'])
def login():
    # creates dictionary of form data
    # auth = request.form
    auth = request.get_json()
    print(auth)
    email = auth['email']
    password = auth['password']
    print(auth.get('email'))
    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    user = User.query\
        .filter_by(email = auth.get('email'))\
        .first()
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'public_id': user.public_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, app.config['SECRET_KEY'])
  
        return make_response(jsonify({'token' : token.encode().decode('UTF-8')}), 201)
    #returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )