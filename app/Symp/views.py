from django.http import HttpResponse
from django.shortcuts import render
from . import methods,database,scores

#declaring global variable

#allSymptoms = None

# below are functions for the logic
def run(request):
    Symptoms = request.GET.get('Symptoms','')
    Symptoms = Normalize(Symptoms)
    matched_phrases , detected_symptoms = methods.detect_phrases(Symptoms)
    all_symptoms = matched_phrases + detected_symptoms
    
    results = scores.score_conditions(all_symptoms, database.condition_cards)

    # attach remedies + warnings
    enriched_candidates = []
    for cand in results["top_candidates"]:
        cond_data = next(c for c in database.condition_cards if c["name"] == cand["condition"])
        cand["home_remedies"] = cond_data.get("home_remedies", [])
        cand["when_to_see_doctor"] = cond_data.get("when_to_see_doctor", [])
        enriched_candidates.append(cand)

    return render(request, 'Input.html', {
        'symptoms': all_symptoms,
        'top_candidates': enriched_candidates,
        'full_scores': results["full_scores"]
    })

def run_opt(request):
    Symptoms = request.GET.get('Symptoms','')
    Symptoms = Normalize(Symptoms)
    matched_phrases , detected_symptoms = methods.detect_phrases(Symptoms)
    all_symptoms = matched_phrases + detected_symptoms
    request.session['last_symptoms'] = all_symptoms
    # get raw results (reuse existing logic)
    results = scores.score_conditions(all_symptoms, database.condition_cards)

    # optimization step
    enriched_candidates = []
    remedies_pool = []
    warnings_pool = []

    for cand in results["top_candidates"][:3]:  # only top 3
        cond_data = next(c for c in database.condition_cards if c["name"] == cand["condition"])
        remedies = cond_data.get("home_remedies", [])
        warnings = cond_data.get("when_to_see_doctor", [])

        cand["home_remedies"] = remedies
        cand["when_to_see_doctor"] = warnings

        enriched_candidates.append(cand)
        remedies_pool.extend(remedies)
        warnings_pool.extend(warnings)

    # deduplicate while preserving order
    # take only first few (say 6 remedies, 6 warnings)
    final_remedies = dedup(remedies_pool)[:6]
    final_warnings = dedup(warnings_pool)[:6]

    return render(request, 'optimize.html', {
        'symptoms': all_symptoms,
        'top_candidates': enriched_candidates,
        'general_remedies': final_remedies,
        'general_warnings': final_warnings
    })

def dedup(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

def re_run(request):
    all_symptoms = request.session.get('last_symptoms', [])
    results = scores.score_conditions(all_symptoms, database.condition_cards)

    # attach remedies + warnings
    enriched_candidates = []
    for cand in results["top_candidates"]:
        cond_data = next(c for c in database.condition_cards if c["name"] == cand["condition"])
        cand["home_remedies"] = cond_data.get("home_remedies", [])
        cand["when_to_see_doctor"] = cond_data.get("when_to_see_doctor", [])
        enriched_candidates.append(cand)

    return render(request, 'Input.html', {
        'symptoms': all_symptoms,
        'top_candidates': enriched_candidates,
        'full_scores': results["full_scores"]
    })

def Normalize(text):
    if not text:  # catches None or empty string
        return ""
    text = text.lower()
    text = methods.remove_punctiation_spaces(text)
    return text

