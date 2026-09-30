from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

router = APIRouter(prefix="/questions", tags=["Questions"])

# Each option "value" matches the exact categorical string in Data.csv
# so the model pipeline receives the same values it was trained on.

QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": 1,
        "feature": "Body Size",
        "question": "How would you describe your body size?",
        "options": [
            {"value": "Slim", "label": "Slim"},
            {"value": "Medium", "label": "Medium"},
            {"value": "Large", "label": "Large"},
        ],
    },
    {
        "id": 2,
        "feature": "Body Weight",
        "question": "How would you describe your body weight?",
        "options": [
            {"value": "Low - difficulties in gaining weight", "label": "Low \u2013 difficulty gaining weight"},
            {"value": "Moderate - no difficulties in gaining or losing weight", "label": "Moderate – no difficulty"},
            {"value": "Heavy - difficulties in losing weight", "label": "Heavy – difficulty losing weight"},
        ],
    },
    {
        "id": 3,
        "feature": "Height",
        "question": "How would you describe your height?",
        "options": [
            {"value": "Short", "label": "Short"},
            {"value": "Average", "label": "Average"},
            {"value": "Tall", "label": "Tall"},
        ],
    },
    {
        "id": 4,
        "feature": "Bone Structure",
        "question": "How would you describe your bone structure?",
        "options": [
            {"value": "Light, Small bones, prominent joints", "label": "Light, small bones, prominent joints"},
            {"value": "Medium bone structure", "label": "Medium bone structure"},
            {"value": "Large, broad shoulders , heavy bone structure", "label": "Large, broad shoulders, heavy bone structure"},
        ],
    },
    {
        "id": 5,
        "feature": "Complexion",
        "question": "How would you describe your complexion?",
        "options": [
            {"value": "Dark-Complexion, tans easily", "label": "Dark complexion, tans easily"},
            {"value": "Fair-skin sunburns easily", "label": "Fair skin, sunburns easily"},
            {"value": "White, pale, tans easily", "label": "White/pale, tans easily"},
        ],
    },
    {
        "id": 6,
        "feature": "General feel of skin",
        "question": "How does your skin generally feel?",
        "options": [
            {"value": "Dry and thin, cool to touch, rough", "label": "Dry, thin, cool to touch, rough"},
            {"value": "Smooth and warm, oily T-zone", "label": "Smooth and warm, oily T-zone"},
            {"value": "Thick and moist/greasy, cold", "label": "Thick, moist/greasy, cold"},
        ],
    },
    {
        "id": 7,
        "feature": "Texture of Skin",
        "question": "What best describes your skin texture?",
        "options": [
            {"value": "Dry, pigments and aging", "label": "Dry, pigmentation and early aging"},
            {"value": "Freckles, many moles, redness and rashes", "label": "Freckles, moles, redness, rashes"},
            {"value": "Oily", "label": "Oily"},
        ],
    },
    {
        "id": 8,
        "feature": "Hair Color",
        "question": "What is your natural hair color?",
        "options": [
            {"value": "Black/Brown,dull", "label": "Black/Brown, dull"},
            {"value": "Brown", "label": "Brown"},
            {"value": "Red, light brown, yellow", "label": "Red, light brown, or yellow"},
        ],
    },
    {
        "id": 9,
        "feature": "Appearance of Hair",
        "question": "How would you describe the appearance of your hair?",
        "options": [
            {"value": "Dry, black, knotted, brittle", "label": "Dry, black, knotted, brittle"},
            {"value": "Straight, oily", "label": "Straight and oily"},
            {"value": "Thick, curly", "label": "Thick and curly"},
        ],
    },
    {
        "id": 10,
        "feature": "Shape of face",
        "question": "What is the shape of your face?",
        "options": [
            {"value": "Heart-shaped, pointed chin", "label": "Heart-shaped, pointed chin"},
            {"value": "Large, round, full", "label": "Large, round, full"},
            {"value": "Long, angular, thin", "label": "Long, angular, thin"},
        ],
    },
    {
        "id": 11,
        "feature": "Eyes",
        "question": "How would you describe your eyes?",
        "options": [
            {"value": "Small, active, darting, dark eyes", "label": "Small, active, darting, dark"},
            {"value": "Medium-sized, penetrating, light-sensitive eyes", "label": "Medium-sized, penetrating, light-sensitive"},
            {"value": "Big, round, beautiful, glowing eyes", "label": "Big, round, beautiful, glowing"},
        ],
    },
    {
        "id": 12,
        "feature": "Eyelashes",
        "question": "How would you describe your eyelashes?",
        "options": [
            {"value": "Scanty eyelashes", "label": "Scanty"},
            {"value": "Moderate eyelashes", "label": "Moderate"},
            {"value": "Thick/Fused eyelashes", "label": "Thick/Fused"},
        ],
    },
    {
        "id": 13,
        "feature": "Blinking of Eyes",
        "question": "How often do you blink?",
        "options": [
            {"value": "Excessive Blinking", "label": "Excessive blinking"},
            {"value": "Moderate Blinking", "label": "Moderate blinking"},
            {"value": "More or less stable", "label": "Stable, infrequent blinking"},
        ],
    },
    {
        "id": 14,
        "feature": "Cheeks",
        "question": "How would you describe your cheeks?",
        "options": [
            {"value": "Wrinkled, Sunken", "label": "Wrinkled and sunken"},
            {"value": "Smooth, Flat", "label": "Smooth and flat"},
            {"value": "Rounded, Plump", "label": "Rounded and plump"},
        ],
    },
    {
        "id": 15,
        "feature": "Nose",
        "question": "How would you describe your nose?",
        "options": [
            {"value": "Crooked, Narrow", "label": "Crooked and narrow"},
            {"value": "Pointed, Average", "label": "Pointed, average size"},
            {"value": "Rounded, Large open nostrils", "label": "Rounded, large open nostrils"},
        ],
    },
    {
        "id": 16,
        "feature": "Teeth and gums",
        "question": "How would you describe your teeth and gums?",
        "options": [
            {"value": "Irregular, Protruding teeth, Receding gums", "label": "Irregular, protruding teeth, receding gums"},
            {"value": "Medium-sized teeth, Reddish gums", "label": "Medium-sized teeth, reddish gums"},
            {"value": "Big, White, Strong teeth, Healthy gums", "label": "Big, white, strong teeth, healthy gums"},
        ],
    },
    {
        "id": 17,
        "feature": "Lips",
        "question": "How would you describe your lips?",
        "options": [
            {"value": "Tight, thin, dry lips which chaps easily", "label": "Tight, thin, dry, chaps easily"},
            {"value": "Lips are soft, medium-sized", "label": "Soft, medium-sized"},
            {"value": "Lips are large, soft, pink, and full", "label": "Large, soft, pink, and full"},
        ],
    },
    {
        "id": 18,
        "feature": "Nails",
        "question": "How would you describe your nails?",
        "options": [
            {"value": "Dry, Rough, Brittle, Break", "label": "Dry, rough, brittle, break easily"},
            {"value": "Sharp, Flexible, Pink, Lustrous", "label": "Sharp, flexible, pink, lustrous"},
            {"value": "Thick, Oily, Smooth, Polished", "label": "Thick, oily, smooth, polished"},
        ],
    },
    {
        "id": 19,
        "feature": "Appetite",
        "question": "How would you describe your appetite?",
        "options": [
            {"value": "Irregular, Scanty", "label": "Irregular and scanty"},
            {"value": "Strong, Unbearable", "label": "Strong and hard to ignore"},
            {"value": "Slow but steady", "label": "Slow but steady"},
        ],
    },
    {
        "id": 20,
        "feature": "Liking tastes",
        "question": "Which taste combination do you prefer most?",
        "options": [
            {"value": "Pungent / Bitter / Astringent", "label": "Pungent, bitter, astringent"},
            {"value": "Sweet / Sour / Salty", "label": "Sweet, sour, salty"},
            {"value": "Sweet / Bitter / Astringent", "label": "Sweet, bitter, astringent"},
        ],
    },
    {
        "id": 21,
        "feature": "Metabolism Type",
        "question": "How would you describe your metabolism?",
        "options": [
            {"value": "fast", "label": "Fast"},
            {"value": "moderate", "label": "Moderate"},
            {"value": "slow", "label": "Slow"},
        ],
    },
    {
        "id": 22,
        "feature": "Climate Preference",
        "question": "What climate do you prefer or feel best in?",
        "options": [
            {"value": "cool", "label": "Cool"},
            {"value": "moderate", "label": "Moderate"},
            {"value": "warm", "label": "Warm"},
        ],
    },
    {
        "id": 23,
        "feature": "Stress Levels",
        "question": "How would you describe your typical stress levels?",
        "options": [
            {"value": "low", "label": "Low"},
            {"value": "moderate", "label": "Moderate"},
            {"value": "high", "label": "High"},
        ],
    },
    {
        "id": 24,
        "feature": "Sleep Patterns",
        "question": "How would you describe your sleep?",
        "options": [
            {"value": "short", "label": "Short (less sleep needed)"},
            {"value": "moderate", "label": "Moderate"},
            {"value": "long", "label": "Long (need a lot of sleep)"},
        ],
    },
    {
        "id": 25,
        "feature": "Dietary Habits",
        "question": "What are your dietary habits?",
        "options": [
            {"value": "vegan", "label": "Vegan"},
            {"value": "vegetarian", "label": "Vegetarian"},
            {"value": "omnivorous", "label": "Omnivorous"},
        ],
    },
    {
        "id": 26,
        "feature": "Physical Activity Level",
        "question": "How would you describe your physical activity level?",
        "options": [
            {"value": "sedentary", "label": "Sedentary"},
            {"value": "moderate", "label": "Moderate"},
            {"value": "high", "label": "High"},
        ],
    },
    {
        "id": 27,
        "feature": "Water Intake",
        "question": "How much water do you typically drink daily?",
        "options": [
            {"value": "low", "label": "Low"},
            {"value": "moderate", "label": "Moderate"},
            {"value": "high", "label": "High"},
        ],
    },
    {
        "id": 28,
        "feature": "Digestion Quality",
        "question": "How would you describe your digestion?",
        "options": [
            {"value": "weak", "label": "Weak"},
            {"value": "moderate", "label": "Moderate"},
            {"value": "strong", "label": "Strong"},
        ],
    },
    {
        "id": 29,
        "feature": "Skin Sensitivity",
        "question": "How sensitive is your skin?",
        "options": [
            {"value": "insensitive", "label": "Not sensitive"},
            {"value": "normal", "label": "Normal"},
            {"value": "sensitive", "label": "Sensitive"},
        ],
    },
]

# Build a lookup for fast validation: feature -> set of valid values
VALID_OPTIONS: Dict[str, set] = {
    q["feature"]: {opt["value"] for opt in q["options"]}
    for q in QUESTIONS
}

FEATURE_BY_ID: Dict[int, str] = {q["id"]: q["feature"] for q in QUESTIONS}


@router.get("")
def get_questions():
    return {"total_questions": len(QUESTIONS), "questions": QUESTIONS}


@router.get("/{question_id}")
def get_question(question_id: int):
    for q in QUESTIONS:
        if q["id"] == question_id:
            return q
    raise HTTPException(status_code=404, detail=f"Question {question_id} not found.")
