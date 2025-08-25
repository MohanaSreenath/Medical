import re
def detect_phrases(text):
    
    # list of multi-word symptom phrases to detect first
    phrases = [
        "sore throat",
        "shortness of breath",
        "runny nose",
        "chest pain",
        "high fever"
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
    return found + lowered.split(' ')

b=detect_phrases("hii I am mohana sreenath chest pain cold fever sre throat")
#print(a)
print(b)