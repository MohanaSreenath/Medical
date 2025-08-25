condition_cards = [
    {
        "name": "Viral URI (Common Cold)",
        "requires_any": ["cough", "sore throat", "runny nose"],
        "supports": ["sneezing", "headache", "fatigue", "body aches", "nasal congestion"],
        "excludes": ["severe shortness of breath", "chest pain"],
        "home_remedies": [
            "Drink warm fluids like ginger tea or soup",
            "Steam inhalation for nasal congestion",
            "Rest and stay hydrated"
        ],
        "when_to_see_doctor": [
            "High fever lasting >3 days",
            "Severe shortness of breath or chest pain"
        ]
    },
    {
        "name": "Flu",
        "requires_any": ["fever", "cough", "body aches"],
        "supports": ["headache", "fatigue", "chills", "sore throat"],
        "excludes": ["chest pain", "severe shortness of breath"],
        "home_remedies": [
            "Plenty of rest and hydration",
            "Warm soups or broths",
            "Paracetamol for fever (if available over-the-counter)"
        ],
        "when_to_see_doctor": [
            "Difficulty breathing",
            "Persistent high fever"
        ]
    },
    {
        "name": "Allergy (Allergic Rhinitis)",
        "requires_any": ["sneezing", "runny nose"],
        "supports": ["itchy eyes", "watery eyes", "nasal congestion", "cough"],
        "excludes": ["fever"],
        "home_remedies": [
            "Wash face and hands after being outdoors",
            "Stay indoors on high pollen days",
            "Use saline nasal rinse"
        ],
        "when_to_see_doctor": [
            "Breathing difficulties",
            "Severe swelling of face or throat"
        ]
    },
    {
        "name": "Dyspepsia/Indigestion-like",
        "requires_any": ["abdominal pain"],
        "supports": ["bloating", "nausea", "burping"],
        "excludes": ["black tarry stool", "severe abdominal pain", "persistent vomiting"],
        "home_remedies": [
            "Drink jeera (cumin) water",
            "Avoid spicy/fried foods",
            "Eat smaller frequent meals"
        ],
        "when_to_see_doctor": [
            "Black stool",
            "Persistent vomiting",
            "Severe abdominal pain"
        ]
    },
    {
        "name": "Tension-type Headache",
        "requires_any": ["headache"],
        "supports": ["fatigue", "neck tension", "stress"],
        "excludes": ["confusion", "stiff neck with fever", "new weakness"],
        "home_remedies": [
            "Drink ginger tea",
            "Apply warm compress to neck",
            "Try relaxation or meditation"
        ],
        "when_to_see_doctor": [
            "Headache with confusion or vision loss",
            "Sudden severe headache"
        ]
    }
]
