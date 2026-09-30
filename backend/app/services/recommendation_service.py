"""
Structured wellness recommendations by Prakruti/Dosha class.

These are general Ayurvedic lifestyle guidelines for educational purposes.
They are NOT medical advice, treatment, or diagnosis.
"""

RECOMMENDATIONS: dict[str, dict] = {
    "Vata": {
        "description": "Vata types tend to be creative, quick-thinking, and energetic, but may experience anxiety, dryness, and irregular routines when imbalanced.",
        "diet": [
            "Favour warm, cooked, and slightly oily foods.",
            "Include sweet, sour, and salty tastes.",
            "Avoid raw, cold, and dry foods.",
            "Eat at regular times each day.",
        ],
        "lifestyle": [
            "Maintain a consistent daily routine.",
            "Prefer gentle exercise such as yoga, walking, or swimming.",
            "Ensure adequate rest and sleep.",
            "Stay warm and avoid excessive wind or cold.",
        ],
        "wellness_tips": [
            "Practice grounding meditation or breathing exercises.",
            "Warm oil self-massage (Abhyanga) is beneficial.",
            "Reduce overstimulation from screens and noise.",
        ],
    },
    "Pitta": {
        "description": "Pitta types are typically focused, ambitious, and intense, but may experience irritability, inflammation, and burnout when imbalanced.",
        "diet": [
            "Favour cool, fresh, and lightly cooked foods.",
            "Include sweet, bitter, and astringent tastes.",
            "Avoid spicy, oily, fried, and very sour foods.",
            "Limit caffeine and alcohol.",
        ],
        "lifestyle": [
            "Avoid excessive heat and direct sunlight.",
            "Take breaks to avoid overworking.",
            "Enjoy cooling activities such as swimming or leisurely walks.",
            "Cultivate patience and avoid competitive stress.",
        ],
        "wellness_tips": [
            "Practice cooling breathwork such as Sheetali pranayama.",
            "Spend time in nature, especially near water.",
            "Prioritise relaxation alongside productivity.",
        ],
    },
    "Kapha": {
        "description": "Kapha types are typically calm, nurturing, and steady, but may experience sluggishness, weight gain, and resistance to change when imbalanced.",
        "diet": [
            "Favour light, warm, and dry foods.",
            "Include pungent, bitter, and astringent tastes.",
            "Reduce heavy, oily, sweet, and dairy-rich foods.",
            "Avoid overeating and late-night meals.",
        ],
        "lifestyle": [
            "Maintain an active lifestyle with regular vigorous exercise.",
            "Wake up early and avoid excessive sleep.",
            "Seek variety and new experiences to stay stimulated.",
            "Avoid prolonged sitting or sedentary habits.",
        ],
        "wellness_tips": [
            "Dry brushing and invigorating massage are beneficial.",
            "Practice energising breathing exercises such as Kapalabhati.",
            "Set clear goals to maintain motivation.",
        ],
    },
    "pitta+kapha": {
        "description": "Pitta-Kapha dual types share the intensity of Pitta and the stability of Kapha. Focus on keeping both doshas balanced by avoiding excess heat and heaviness.",
        "diet": [
            "Favour light, cool to moderately warm foods.",
            "Include bitter and astringent tastes.",
            "Avoid spicy, oily, and heavy foods.",
            "Eat moderate portions at regular times.",
        ],
        "lifestyle": [
            "Balance vigorous exercise with adequate rest.",
            "Avoid excess heat and overexertion.",
            "Maintain a structured daily routine.",
        ],
        "wellness_tips": [
            "Cooling and grounding practices work well together.",
            "Monitor both inflammation and sluggishness as early imbalance signals.",
        ],
    },
    "vata+kapha": {
        "description": "Vata-Kapha dual types combine Vata's lightness with Kapha's heaviness. Warmth and gentle stimulation help keep both doshas in balance.",
        "diet": [
            "Favour warm, nourishing, and mildly spiced foods.",
            "Include sweet, sour, and salty tastes.",
            "Avoid cold, raw, and very heavy foods.",
        ],
        "lifestyle": [
            "Maintain a consistent daily routine.",
            "Engage in moderate, warming exercise.",
            "Stay warm and dry.",
        ],
        "wellness_tips": [
            "Warm oil massage supports both Vata and Kapha.",
            "Watch for both anxiety (Vata) and sluggishness (Kapha) as imbalance signs.",
        ],
    },
    "vata+pitta": {
        "description": "Vata-Pitta dual types are often creative and driven, but can be prone to both anxiety and irritability. Cooling and grounding practices are helpful.",
        "diet": [
            "Favour cool to warm, moderately nourishing foods.",
            "Include sweet and slightly bitter tastes.",
            "Avoid very spicy, dry, and cold foods.",
        ],
        "lifestyle": [
            "Avoid overworking and overheating.",
            "Balance activity with regular relaxation.",
            "Gentle to moderate exercise is best.",
        ],
        "wellness_tips": [
            "Cooling breathwork and grounding meditation both help.",
            "Watch for both restlessness (Vata) and irritability (Pitta) as early signals.",
        ],
    },
}

KNOWN_CLASSES = set(RECOMMENDATIONS.keys())


def get_recommendation(dosha: str) -> dict:
    """
    Return structured wellness recommendations for the given dosha class.
    Falls back to the closest single-dosha recommendation for unknown combos.
    """
    rec = RECOMMENDATIONS.get(dosha)
    if rec is None:
        raise ValueError(
            f"Unknown dosha class: '{dosha}'. "
            f"Expected one of: {sorted(KNOWN_CLASSES)}"
        )
    return rec
