# Customer Service Chatbot for Water Utility Company

This project is an intelligent customer service chatbot designed to assist customers of a water utility company. The chatbot is capable of handling customer queries related to billing, payments, water services, and more. It uses natural language processing (NLP) techniques, a pre-trained BERT model for question-answering, a knowledge base, and context management to provide intelligent and personalized responses.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Memory Storage](#memory-storage)
- [Context Management](#context-management)
- [Pre-trained Model Integration](#pre-trained-model-integration)
- [Known Issues](#known-issues)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Intent Classification:** Uses a machine learning model to classify user queries into predefined intents.
- **Knowledge Base Integration:** Searches a knowledge base to provide accurate answers for user queries.
- **Memory Storage:** Stores user preferences for a more personalized interaction.
- **Context Management:** Maintains conversation context for multi-turn conversations.
- **Pre-trained Model (BERT):** Integrates a pre-trained BERT model for complex question-answering tasks.
- **Named Entity Recognition:** Extracts key entities like account numbers from user queries.
- **Sentiment Analysis:** Analyzes user sentiment to adjust responses and provide a more empathetic interaction.

## Technologies Used
- **Python**: Core language used for developing the chatbot.
- **Flask**: Web framework for building the application.
- **spaCy**: NLP library for processing and understanding natural language queries.
- **Hugging Face Transformers**: Provides pre-trained models for advanced question-answering.
- **TextBlob**: Used for sentiment analysis.
- **scikit-learn**: Used for training the intent classification model.
- **MySQL**: Database for storing user interactions and knowledge base information.
- **HTML/CSS/JavaScript**: Front-end for interacting with the chatbot.
- **Celery with Redis**: Handles asynchronous tasks for improved performance.

## Project Structure
Directories:

- **app/**: Contains the core application logic.
- **init.py**: Initializes the Flask application.
- **main.py**: The main entry point of the application.
- **nlp_engine.py**: Processes user queries using Natural Language Processing (NLP) techniques.
- **nlp_transformers.py**: Integrates a pre-trained BERT model for advanced NLP tasks.
- **intent_classifier.py**: Handles intent classification using scikit-learn library.
- **interaction_logger.py**: Logs user interactions for analysis and improvement.
- **models.py**: Defines database models for user preferences and chatbot interactions.
- **intents.json**: Contains definitions of user intents, patterns, and corresponding responses.
- **templates/**: Houses the front-end interface files.
- **index.html**: The main HTML template for the chatbot interface.
- **static/**: Stores static assets used by the front-end.
- **css/**: Contains Cascading Style Sheets (CSS) files for styling the interface.
- **styles.css**: The main CSS file for the chatbot.
- **migrations/**: Stores database migration files used for managing schema changes.
- **requirements.txt**: Lists the required Python packages for running the project.
- **README.md**: The current file you are reading, which provides project documentation.

## Key Components:

- **Flask Application**: The chatbot is built upon the Flask web framework, providing a flexible foundation for building web applications.
- **Natural Language Processing (NLP) Engine**: This core component utilizes NLP techniques to understand the user's intent from their queries.
- **BERT Model Integration**: The project incorporates a pre-trained BERT model, enhancing the NLP engine's ability to handle complex language and improve understanding.
- **Intent Classification**: The intent_classifier.py module utilizes scikit-learn to classify user queries into predefined intents, allowing the chatbot to respond appropriately.
- **Interaction Logging**: User interactions are logged to analyze user behavior and improve the chatbot's performance over time.
- **Database Models**: The models.py file defines database models to store user preferences and chatbot interaction data.
- **Intents Definition (intents.json)**: This file specifies user intents, along with corresponding patterns and responses, guiding the chatbot's behavior.
- **Front-end Interface**: The templates/index.html file provides the visual interface for users to interact with the chatbot.
- **Static Assets (CSS)**: The styles.css file defines the visual style of the chatbot interface.


## Installation
To set up the project locally, follow these steps:

1. **Clone the Repository:**
   git clone https://github.com/your-username/chatbot-water-utility.git
   cd chatbot-water-utility
2. **Set Up a Virtual Environment:**
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. **Install Dependencies:** 
pip install -r requirements.txt
4. Set Up the Database:
a. Install MySQL and create a database named water_utility_db.
b. Update database configuration in app/__init__.py.
c. Run the migrations to set up the tables:
flask db upgrade
5. **Run the Application:** python app/main.py


## Usage
1. Navigate to http://127.0.0.1:5000 in your browser.
2. Interact with the chatbot by asking questions related to billing, payments, water quality, etc.
3. The chatbot will classify your query, look up the knowledge base, and respond intelligently.


## Memory Storage
1. The chatbot uses an in-memory dictionary to store user-specific preferences during a session.
2. For persistent storage, it uses a MySQL database to store user interactions and preferences.

## Context Management
1. The chatbot maintains context using a global context dictionary to handle multi-turn conversations.
2. It tracks the user’s last intent and adjusts responses accordingly.

## Pre-trained Model Integration
1. The chatbot integrates a pre-trained BERT model using the Hugging Face Transformers library for question-answering tasks.
2. To change or fine-tune the model, modify app/nlp_transformers.py.

## Known Issues
1. The chatbot's intelligence is limited by the patterns and training data provided in intents.json.
2. Context management is session-based and does not persist across multiple user sessions.
3. Pre-trained model responses may be too generic if not fine-tuned for the water utility domain.


## Future Enhancements
1. **Fine-tune BERT Model:** Fine-tune the pre-trained BERT model on a domain-specific dataset to improve its accuracy.
2. **User Authentication:** Integrate user authentication to provide personalized experiences across sessions.
3. **Feedback Mechanism:** Implement a feedback loop for users to rate responses, allowing iterative improvements to the model.
4. **Synonym Recognition:** Use word embeddings or a synonym dictionary to handle query variations more effectively.
5. **API Integration:** Connect to external APIs (e.g., billing systems) for real-time information retrieval.


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


### **Explanation of Sections**
- **Features:** Describes the key capabilities of the chatbot.
- **Technologies Used:** Lists the tools and libraries used to build the chatbot.
- **Project Structure:** Provides a directory structure to help users navigate the project.
- **Installation and Usage:** Offers step-by-step instructions for setting up and running the chatbot.
- **Memory Storage & Context Management:** Explains how the chatbot manages user preferences and conversation context.
- **Pre-trained Model Integration:** Outlines how the chatbot integrates with BERT for complex queries.
- **Known Issues & Future Enhancements:** Provides insights into current limitations and possible future improvements.
- **Contributing:** Details how others can contribute to the project.

This README.md provides a comprehensive overview of the project, helping users understand its functionality and how to set it up.
