from .models import InteractionLog, db

def log_interaction(user_id, query, response):
    log = InteractionLog(user_id=user_id, query=query, response=response)
    db.session.add(log)
    db.session.commit()