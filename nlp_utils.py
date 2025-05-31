import re

def tokenize(text):
    # Split words and punctuation
    return re.findall(r"\w+|[^\w\s]", text)

def recognize_intent(query):
    # dummy implementation
    return "sustainable"

def extract_entities(query):
    # dummy implementation
    return ["Bitcoin"]

def process_query(query):
    # Dummy implementation: just return the query as a string or list of keywords
    return query.lower()
