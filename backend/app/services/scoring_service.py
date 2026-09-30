"""
Rule-based Vata/Pitta/Kapha scoring service.

This is INDEPENDENT from the ML prediction.

SCORE_MAP structure:
    { feature_name: { option_value: {"vata": w, "pitta": w, "kapha": w} } }

The weights below are derived from classical Ayurvedic tridosha
characteristic associations commonly referenced in Prakruti assessment
literature. They are indicative only and NOT clinically validated.

Each weight represents how strongly a given answer indicates that dosha.
Scale: 0 (no association) to 3 (strong association).
"""

from typing import Dict

# ---------------------------------------------------------------------------
# Scoring weights per feature / option
# ---------------------------------------------------------------------------
# Format: SCORE_MAP[feature][option_value] = {"vata": x, "pitta": x, "kapha": x}
# ---------------------------------------------------------------------------

SCORE_MAP: Dict[str, Dict[str, Dict[str, float]]] = {
    "Body Size": {
        "Slim":   {"vata": 3, "pitta": 1, "kapha": 0},
        "Medium": {"vata": 1, "pitta": 3, "kapha": 1},
        "Large":  {"vata": 0, "pitta": 1, "kapha": 3},
    },
    "Body Weight": {
        "Low - difficulties in gaining weight":                     {"vata": 3, "pitta": 1, "kapha": 0},
        "Moderate - no difficulties in gaining or losing weight":   {"vata": 1, "pitta": 3, "kapha": 1},
        "Heavy - difficulties in losing weight":                    {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Height": {
        "Short":   {"vata": 1, "pitta": 1, "kapha": 3},
        "Average": {"vata": 1, "pitta": 3, "kapha": 1},
        "Tall":    {"vata": 3, "pitta": 1, "kapha": 0},
    },
    "Bone Structure": {
        "Light, Small bones, prominent joints":          {"vata": 3, "pitta": 1, "kapha": 0},
        "Medium bone structure":                         {"vata": 1, "pitta": 3, "kapha": 1},
        "Large, broad shoulders , heavy bone structure": {"vata": 0, "pitta": 1, "kapha": 3},
    },
    "Complexion": {
        "Dark-Complexion, tans easily":   {"vata": 3, "pitta": 1, "kapha": 0},
        "Fair-skin sunburns easily":      {"vata": 0, "pitta": 3, "kapha": 1},
        "White, pale, tans easily":       {"vata": 1, "pitta": 0, "kapha": 3},
    },
    "General feel of skin": {
        "Dry and thin, cool to touch, rough":  {"vata": 3, "pitta": 0, "kapha": 0},
        "Smooth and warm, oily T-zone":        {"vata": 0, "pitta": 3, "kapha": 1},
        "Thick and moist/greasy, cold":        {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Texture of Skin": {
        "Dry, pigments and aging":                  {"vata": 3, "pitta": 0, "kapha": 0},
        "Freckles, many moles, redness and rashes": {"vata": 0, "pitta": 3, "kapha": 0},
        "Oily":                                     {"vata": 0, "pitta": 1, "kapha": 3},
    },
    "Hair Color": {
        "Black/Brown,dull":        {"vata": 3, "pitta": 0, "kapha": 1},
        "Brown":                   {"vata": 1, "pitta": 3, "kapha": 0},
        "Red, light brown, yellow":{"vata": 0, "pitta": 3, "kapha": 0},
    },
    "Appearance of Hair": {
        "Dry, black, knotted, brittle": {"vata": 3, "pitta": 0, "kapha": 0},
        "Straight, oily":               {"vata": 0, "pitta": 3, "kapha": 1},
        "Thick, curly":                 {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Shape of face": {
        "Long, angular, thin":     {"vata": 3, "pitta": 0, "kapha": 0},
        "Heart-shaped, pointed chin": {"vata": 0, "pitta": 3, "kapha": 0},
        "Large, round, full":      {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Eyes": {
        "Small, active, darting, dark eyes":              {"vata": 3, "pitta": 0, "kapha": 0},
        "Medium-sized, penetrating, light-sensitive eyes":{"vata": 0, "pitta": 3, "kapha": 0},
        "Big, round, beautiful, glowing eyes":            {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Eyelashes": {
        "Scanty eyelashes":      {"vata": 3, "pitta": 1, "kapha": 0},
        "Moderate eyelashes":    {"vata": 0, "pitta": 3, "kapha": 1},
        "Thick/Fused eyelashes": {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Blinking of Eyes": {
        "Excessive Blinking":   {"vata": 3, "pitta": 0, "kapha": 0},
        "Moderate Blinking":    {"vata": 0, "pitta": 3, "kapha": 0},
        "More or less stable":  {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Cheeks": {
        "Wrinkled, Sunken": {"vata": 3, "pitta": 0, "kapha": 0},
        "Smooth, Flat":     {"vata": 0, "pitta": 3, "kapha": 0},
        "Rounded, Plump":   {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Nose": {
        "Crooked, Narrow":              {"vata": 3, "pitta": 0, "kapha": 0},
        "Pointed, Average":             {"vata": 0, "pitta": 3, "kapha": 0},
        "Rounded, Large open nostrils": {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Teeth and gums": {
        "Irregular, Protruding teeth, Receding gums": {"vata": 3, "pitta": 0, "kapha": 0},
        "Medium-sized teeth, Reddish gums":           {"vata": 0, "pitta": 3, "kapha": 0},
        "Big, White, Strong teeth, Healthy gums":     {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Lips": {
        "Tight, thin, dry lips which chaps easily": {"vata": 3, "pitta": 0, "kapha": 0},
        "Lips are soft, medium-sized":              {"vata": 0, "pitta": 3, "kapha": 0},
        "Lips are large, soft, pink, and full":     {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Nails": {
        "Dry, Rough, Brittle, Break":   {"vata": 3, "pitta": 0, "kapha": 0},
        "Sharp, Flexible, Pink, Lustrous": {"vata": 0, "pitta": 3, "kapha": 0},
        "Thick, Oily, Smooth, Polished":   {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Appetite": {
        "Irregular, Scanty":   {"vata": 3, "pitta": 0, "kapha": 0},
        "Strong, Unbearable":  {"vata": 0, "pitta": 3, "kapha": 0},
        "Slow but steady":     {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Liking tastes": {
        "Pungent / Bitter / Astringent": {"vata": 3, "pitta": 0, "kapha": 0},
        "Sweet / Sour / Salty":          {"vata": 0, "pitta": 3, "kapha": 0},
        "Sweet / Bitter / Astringent":   {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Metabolism Type": {
        "fast":     {"vata": 2, "pitta": 3, "kapha": 0},
        "moderate": {"vata": 1, "pitta": 1, "kapha": 2},
        "slow":     {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Climate Preference": {
        "warm": {"vata": 3, "pitta": 0, "kapha": 0},
        "moderate": {"vata": 1, "pitta": 1, "kapha": 1},
        "cool": {"vata": 0, "pitta": 3, "kapha": 2},
    },
    "Stress Levels": {
        "high":     {"vata": 3, "pitta": 2, "kapha": 0},
        "moderate": {"vata": 1, "pitta": 2, "kapha": 1},
        "low":      {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Sleep Patterns": {
        "short":    {"vata": 3, "pitta": 1, "kapha": 0},
        "moderate": {"vata": 1, "pitta": 2, "kapha": 1},
        "long":     {"vata": 0, "pitta": 0, "kapha": 3},
    },
    "Dietary Habits": {
        "vegan":       {"vata": 2, "pitta": 1, "kapha": 2},
        "vegetarian":  {"vata": 1, "pitta": 1, "kapha": 2},
        "omnivorous":  {"vata": 1, "pitta": 2, "kapha": 1},
    },
    "Physical Activity Level": {
        "sedentary": {"vata": 1, "pitta": 0, "kapha": 3},
        "moderate":  {"vata": 1, "pitta": 2, "kapha": 1},
        "high":      {"vata": 2, "pitta": 3, "kapha": 0},
    },
    "Water Intake": {
        "low":      {"vata": 3, "pitta": 1, "kapha": 0},
        "moderate": {"vata": 1, "pitta": 1, "kapha": 1},
        "high":     {"vata": 0, "pitta": 2, "kapha": 3},
    },
    "Digestion Quality": {
        "weak":     {"vata": 3, "pitta": 0, "kapha": 1},
        "moderate": {"vata": 1, "pitta": 1, "kapha": 2},
        "strong":   {"vata": 0, "pitta": 3, "kapha": 0},
    },
    "Skin Sensitivity": {
        "insensitive": {"vata": 0, "pitta": 0, "kapha": 3},
        "normal":      {"vata": 1, "pitta": 1, "kapha": 1},
        "sensitive":   {"vata": 1, "pitta": 3, "kapha": 0},
    },
}


def calculate_vpk_scores(answers: dict[str, str]) -> dict[str, float]:
    """
    Calculate Vata/Pitta/Kapha percentage scores from a
    dict of {feature_name: option_value}.

    Returns {"vata": %, "pitta": %, "kapha": %} summing to 100.
    Raises ValueError if a feature or option value is not in SCORE_MAP.
    """
    scores = {"vata": 0.0, "pitta": 0.0, "kapha": 0.0}

    for feature, value in answers.items():
        feature_map = SCORE_MAP.get(feature)
        if feature_map is None:
            raise ValueError(f"No scoring rule for feature: '{feature}'")
        option_scores = feature_map.get(value)
        if option_scores is None:
            raise ValueError(f"No scoring rule for '{feature}' = '{value}'")
        scores["vata"]  += option_scores["vata"]
        scores["pitta"] += option_scores["pitta"]
        scores["kapha"] += option_scores["kapha"]

    total = sum(scores.values())
    if total <= 0:
        raise ValueError("VPK scoring produced a zero total. Check SCORE_MAP.")

    percentages = {k: round((v / total) * 100, 2) for k, v in scores.items()}

    # Correct rounding drift so total is exactly 100
    drift = round(100.0 - sum(percentages.values()), 2)
    percentages["kapha"] = round(percentages["kapha"] + drift, 2)

    return percentages
