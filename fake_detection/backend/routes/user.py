from flask import Flask, request, jsonify, make_response
from fake_detection.backend.routes.token_generator import token_required
from fake_detection.backend import app
from fake_detection.backend.db_model import User

@app.route('/user', methods =['GET'])
@token_required
def get_all_users(current_user):
    # querying the database
    # for all the entries in it
    users = User.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for user in users:
        # appending the user data json
        # to the response list
        output.append({
            'public_id': user.public_id,
            'name' : user.name,
            'email' : user.email
        })
  
    return jsonify({'users': output})