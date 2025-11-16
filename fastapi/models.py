from pydantic import BaseModel
from typing import List, Optional

class TextInput(BaseModel):
    text: str

class ResumeInput(BaseModel):
    candidate_id: str
    resume_text: str

class MatchRequest(BaseModel):
    jd_text: str
    required_skills: Optional[List[str]] = None
    top_k: int = 5

class ScoreRequest(BaseModel):
    jd_text: str
    candidate_id: str
    required_skills: Optional[List[str]] = None
