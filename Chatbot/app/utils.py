from flask import jsonify

def validate_input(data, required_fields):
     for field in required_fields:
         if field not in data:
             return False, f"Missing field: {field}"
         return True, None

def create_response(message, status_code=200):
    return jsonify({'message': message}), status_code