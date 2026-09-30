import sys
from pathlib import Path

# Allow `from app.xxx import ...` (FastAPI app uses this style)
# and `from backend.app.xxx import ...` (tests use this style)
sys.path.insert(0, str(Path(__file__).parent / "backend"))
