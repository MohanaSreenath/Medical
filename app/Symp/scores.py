
from typing import List, Dict, Any


def score_conditions(detected_symptoms: List[str],
                     conditions: List[Dict[str, Any]],
                     phrase_bonus: float = 0.5,
                     top_k: int = 3,
                     tie_window: float = 1.0) -> Dict[str, Any]:
    
    scores = {}

    for cond in conditions:
        cond_name = cond["name"]
        scores[cond_name] = {
            "score": 0,
            "requires_hits": [],
            "supports_hits": [],
            "excluded": False,
            "excluded_by": []
        }

        # 1. requires_any (+2)
        for sym in detected_symptoms:
            if sym in cond.get("requires_any", []):
                scores[cond_name]["score"] += 2
                scores[cond_name]["requires_hits"].append(sym)

        # 2. supports (+1)
        for sym in detected_symptoms:
            if sym in cond.get("supports", []):
                scores[cond_name]["score"] += 1
                scores[cond_name]["supports_hits"].append(sym)

        # 3. excludes
        for sym in detected_symptoms:
            if sym in cond.get("excludes", []):
                scores[cond_name]["excluded"] = True
                scores[cond_name]["excluded_by"].append(sym)
                scores[cond_name]["score"] = 0
                break

        # 4. phrase bonus
        for sym in detected_symptoms:
            if " " in sym and (sym in cond.get("requires_any", []) or sym in cond.get("supports", [])):
                scores[cond_name]["score"] += phrase_bonus

    # Ranking
    results = [
        {"condition": c, **info} for c, info in scores.items()
    ]

    top_candidates = [
        r for r in results if not r["excluded"] and r["score"] > 0
    ]
    top_candidates.sort(key=lambda x: x["score"], reverse=True)

    if top_candidates:
        cutoff_score = top_candidates[min(top_k, len(top_candidates)) - 1]["score"]
        top_candidates = [
            r for r in top_candidates if r["score"] >= cutoff_score - tie_window
        ]

    return {
        "top_candidates": top_candidates,
        "full_scores": scores
    }
