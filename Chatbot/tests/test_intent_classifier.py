import pytest
from app.intent_classifier import classify_intent, train_intent_model

# Re-train model for tests
intent_model = train_intent_model()


def test_classify_intent():
    query_1 = "How do I pay my bill?"
    query_2 = "What's the water quality like?"

    intent_1 = classify_intent(query_1)
    intent_2 = classify_intent(query_2)

    assert intent_1 == "payment_method"
    assert intent_2 == "water_quality"


def test_intent_classifier_unknown():
    query = "I need some assistance."
    intent = classify_intent(query)
    assert intent in ["default", "unknown"], "Should fall back to a default or unknown intent."
