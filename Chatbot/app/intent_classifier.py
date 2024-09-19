import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load intents from JSON
def load_intents():
    # Construct the path to the intents.json file dynamically
    current_dir = os.path.dirname(os.path.abspath(__file__))
    intents_file_path = os.path.join(current_dir, 'intents.json')

    # Load intents file
    try:
        with open(intents_file_path, 'r') as file:
            intents = json.load(file)
        return intents['intents']
    except FileNotFoundError:
        print(f"Error: The intents.json file was not found at {intents_file_path}")
        raise

# Prepare and train the model
def train_intent_model():
    intents = load_intents()
    X = []
    y = []
    for intent in intents:
        for pattern in intent['patterns']:
            X.append(pattern)
            y.append(intent['tag'])

    # Create and train the model
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X, y)
    return model

# Initialize and store the trained model
intent_model = train_intent_model()

# Process query with context management
def process_query(query, user_id):
    global context
    # Print current context for debugging
    print(f"Current Context for user {user_id}: {context.get(user_id)}")


# Function to classify a user query
def classify_intent(query):
    return intent_model.predict([query])[0]
    print(f"Classified Intent: {intent}") # Debug: Print classified intent
    return intent

