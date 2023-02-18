from flask import Flask, request, jsonify, make_response
from fake_detection.backend.routes.token_generator import token_required
from fake_detection.backend import app
from fake_detection.backend.db_model import Banknote, db

@app.route('/get_banknote', methods =['POST'])
@token_required
def get_all_users(current_user):
    uid = current_user.id
    email = current_user.email
    if 'image_file' not in request.files:
        response = make_response(
                    jsonify(
                        { "success" : True, "message" : 'No image file found'}
                    ),
                    200,
                )
        return response
    file = request.files['image_file']
    user = Banknote(
            email = email,
            isReal = "true"
        )
        # insert user
    db.session.add(user)
    db.session.commit()
  
    return make_response('Successfully registered.', 201)