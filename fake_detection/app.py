from flask import Flask, request, jsonify, make_response
from fake_detection.backend import app

    

if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port = 5000, debug=True,threaded=True)
