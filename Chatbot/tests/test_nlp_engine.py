from app.nlp_engine import process_query

def test_process_query():
    response = process_query('What is my bill?')
    assert 'To check your billing details' in response