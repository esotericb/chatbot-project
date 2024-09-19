from transformers import pipeline

# Load a pre-trained BERT model for question-answering
nlp_model = pipeline('question-answering', model='distilbert-base-cased-distilled-squad', revision='626af31')

def get_answer_from_model(question, context):
    result = nlp_model(question=question, context=context)
    return result['answer']