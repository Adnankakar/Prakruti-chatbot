from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.questions import router as questions_router
from app.api.assessment import router as assessment_router


app = FastAPI(
    title="Prakruti Self-Assessment API",
    description=(
        "FastAPI backend for the AI-Assisted Prakruti "
        "Self-Assessment Chatbot."
    ),
    version="1.0.0",
)


# ---------------------------------------------------------
# CORS
# ---------------------------------------------------------
# React frontend will communicate with this FastAPI backend.
# During development we allow localhost.
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# Routers
# ---------------------------------------------------------

app.include_router(
    questions_router,
    prefix="/api",
)

app.include_router(
    assessment_router,
    prefix="/api",
)


# ---------------------------------------------------------
# Root
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Prakruti Self-Assessment API is running",
        "version": "1.0.0",
        "docs": "/docs",
    }


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }