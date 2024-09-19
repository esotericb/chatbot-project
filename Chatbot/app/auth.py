from flask import request, jsonify
from . import oauth

@oauth.token_handler
def access_token():
    return jsonify({'token': 'your_token_here'})