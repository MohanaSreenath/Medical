def lower_text(Symptoms):
    return Symptoms.lower()

import string, re

def remove_punctiation_spaces(Symptoms):
    Symptoms = Symptoms.translate(str.maketrans('', '', string.punctuation))
    return re.sub(r'\s+', ' ', Symptoms).strip()

def split_string(Symptoms):
    return Symptoms.split(' ')

def detect_phrases(text):
    # list of multi-word symptom phrases to detect first
    phrases = [
        "sore throat",
        "shortness of breath",
        "runny nose",
        "chest pain",
        "high fever",
        "body aches",
        "stomach pain",
        "abdominal pain",
        "facial pressure",
        "nasal congestion",
        "swollen neck glands",
        "post-nasal drip",
        "reduced urination",
        "black tarry stool"
        ]    
    found = []
    lowered = text.lower()
    
    # detect phrases first
    for phrase in phrases:
        pattern = re.escape(phrase)
        if re.search(r'\b' + pattern + r'\b', lowered):
            found.append(phrase)
            # remove phrase words to avoid double counting later
            lowered = re.sub(r'\b' + pattern + r'\b', ' ', lowered)
    
    # collapse leftover spaces after removal
    lowered = re.sub(r'\s+', ' ', lowered).strip()
    
    # detect single words on the remaining text
    lowered_tokens = split_string(lowered)
    singles_found = detect_single_words(lowered_tokens)

    return found , singles_found

def detect_single_words(tokens):
    singles = [
        "fever", "cough", "diarrhea", "nausea", "vomiting",
        "headache", "fatigue", "sneezing", "chills", "bloating",
        "burping", "dizziness", "thirst", "stress", "wheeze",
        "itchy", "watery", "eyes"
        ]
    found = [tok for tok in tokens if tok in singles]
    return found
