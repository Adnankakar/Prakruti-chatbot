# Prakruti Frontend

React + Vite + Tailwind frontend for the AI-Assisted Prakruti Self-Assessment Chatbot.

## Setup

```bash
cd frontend
npm install
cp .env.example .env   # already created with defaults
npm run dev
```

Open http://localhost:5173

## Environment

`.env`:
```
VITE_API_BASE_URL=http://localhost:8000
```

## Running with the backend

Start the FastAPI backend first:
```bash
# From project root
$env:PYTHONPATH="backend"; uvicorn app.main:app --reload
```

Then in a second terminal:
```bash
cd frontend
npm run dev
```

## Project structure

```
src/
  pages/          # Home, Assessment, Result
  components/
    common/       # Logo, Button, Disclaimer, ErrorState, LoadingScreen
    assessment/   # ProgressBar, QuestionCard, AnswerOption
    results/      # DominantDoshaCard, DoshaChart, RecommendationSection, ResultDisclaimer
  context/        # AssessmentContext (state management)
  services/       # api.js (all backend calls)
```

## Build

```bash
npm run build
npm run preview
```
