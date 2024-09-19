from flask import Blueprint, render_template, request, jsonify
from . import db
from .nlp_engine import process_query
from .interaction_logger import log_interaction


bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    from .models import create_default_user
    create_default_user()
    return render_template('index.html')

@bp.route('/chat', methods=['POST'])
def chat():
    from .models import create_default_user
    create_default_user()

    user_query = request.json.get('query')
    response = process_query(user_query)

    if response is None:
        response = "I'm here to help. Please provide more details or try asking in a different way."


    log_interaction(user_id=1, query=user_query, response=response)
    return jsonify({'response': response})