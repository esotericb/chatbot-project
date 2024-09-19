import os
import json
import random
from .models import KnowledgeBase
import spacy
from spacy.matcher import PhraseMatcher
from .nlp_transformers import get_answer_from_model
from .intent_classifier import classify_intent
import requests
from textblob import TextBlob

nlp = spacy.load('en_core_web_sm')

# Construct the path to the intents.json file dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))
intents_file_path = os.path.join(current_dir, 'intents.json')

# Load intents file
try:
    with open(intents_file_path, 'r') as file:
        intents = json.load(file)
except FileNotFoundError:
    print(f"Error: The intents.json file was not found at {intents_file_path}")
    raise

# Initialize spaCy's phrase matcher
matcher = PhraseMatcher(nlp.vocab)

# Add patterns from intents.json to the matcher
intent_patterns = {}
for intent in intents['intents']:
    patterns = [nlp(text.lower()) for text in intent['patterns']]
    matcher.add(intent['tag'], None, *patterns)
    intent_patterns[intent['tag']] = intent

# Function to get response based on the detected intent
def get_response(intent_tag):
    intent = intent_patterns.get(intent_tag)
    if intent:
        return random.choice(intent['responses'])
    return None

# Function for sentiment analysis
def analyze_sentiment(query):
    analysis = TextBlob(query)
    if analysis.sentiment.polarity < 0:
        return "negative"
    return "positive"

# function to query the knowledge base
def query_knowledge_base(query):
    # Process the query to extract keywords
    doc = nlp(query)
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]
    print(f"Extracted Keywords: {keywords}") # Debug: Print keywords


    # Query the knowledge base using any of the keywords
    for keyword in keywords:
        result = KnowledgeBase.query.filter(KnowledgeBase.question.ilike(f"%{keyword}%")).first()
        if result:
            print(f"Knowledge Base Match: {result.answer}")  # Debug: Print matched answer
            return result.answer
    print("No match found in the knowledge base.")  # Debug: No match found
    return None

# Function to process the user query and generate a response
def process_query(query):
    # Perform sentiment analysis
    sentiment = analyze_sentiment(query)
    if sentiment == "negative":
        return "I'm sorry to hear that you're experiencing issues. How can I assist you further?"

    # Use the trained model to classify the intent
    intent = classify_intent(query)
    response = get_response(intent)
    if response:
        return response

    # call `get_answer_from_model` when detailed answers are needed
    context = "This is some context that the model can use to answer questions."
    if 'payment' in query.lower():
        return get_answer_from_model(query, context)

    # Process the query with spaCy
    doc = nlp(query.lower())


    # Match the query to patterns in the intents file
    matches = matcher(doc)
    if matches:
        # Take the first matched intent
        match_id, start, end = matches[0]
        intent_tag = nlp.vocab.strings[match_id]

        # Return a response from the matched intent
        response = get_response(intent_tag)
        if response:
            return response
    # If no pattern matches, try querying the knowledge base
    kb_response = query_knowledge_base(query)
    if kb_response:
        return kb_response

        # Default response if nothing else matches
        return "I'm here to help. Please provide more details or try asking in a different way."





def get_billing_information(account_number):
    api_url = f"https://example.com/api/billing/{account_number}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return f"Your current bill is {data['amount']}."
        else:
            return "Couldn't retrieve billing information."
    except Exception as e:
        return "Error fetching billing information."


