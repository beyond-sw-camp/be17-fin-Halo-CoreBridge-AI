import os
import numpy as np
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

from models import TextInput, ResumeInput, MatchRequest, ScoreRequest
from vector_store import create_index, save_resume, search_similar, get_resume
from llm import summarize, extract_skills

from scoring import rule_score

# Backends
import ollama
from openai import OpenAI

load_dotenv()
app = FastAPI(title="AI Matching Service (Ollama)")

GEN_MODEL = os.getenv("GEN_MODEL", "llama3")
EMBEDDING_BACKEND = os.getenv("EMBEDDING_BACKEND", "ollama")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")

openai_client = None
if EMBEDDING_BACKEND == "openai":
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed(text: str):
    if EMBEDDING_BACKEND == "ollama":
        # Use Ollama embeddings; ensure the model supports embeddings
        resp = ollama.embeddings(model=EMBEDDING_MODEL, prompt=text)
        return resp["embedding"]
    else:
        resp = openai_client.embeddings.create(model=EMBEDDING_MODEL, input=text)
        return resp.data[0].embedding

def cosine(a: np.ndarray, b: np.ndarray) -> float:
    if a is None or b is None:
        return 0.0
    if a.ndim != 1: a = a.ravel()
    if b.ndim != 1: b = b.ravel()
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)

# Ensure Redis index
create_index()

@app.post("/summary")
def api_summary(req: TextInput):
    # inject model at runtime
    import llm as _llm
    _llm.GEN_MODEL = GEN_MODEL
    return {"summary": summarize(req.text)}

@app.post("/skills")
def api_skills(req: TextInput):
    import llm as _llm
    _llm.GEN_MODEL = GEN_MODEL
    return {"skills": extract_skills(req.text)}

@app.post("/save_resume")
def api_save_resume(req: ResumeInput):
    emb = embed(req.resume_text)
    save_resume(req.candidate_id, emb, req.resume_text)
    return {"status": "saved", "candidate_id": req.candidate_id}

@app.post("/match_jd")
def api_match(req: MatchRequest):
    jd_emb = embed(req.jd_text)
    hits = search_similar(jd_emb, k=req.top_k)
    return {"matches": hits}

@app.post("/score")
def api_score(req: ScoreRequest):
    cand = get_resume(req.candidate_id)
    if not cand:
        raise HTTPException(status_code=404, detail="candidate not found. Save resume first.")
    cand_emb = cand["embedding"]
    cand_text = cand["resume_text"]

    jd_emb = embed(req.jd_text)
    cos = cosine(np.array(jd_emb, dtype=np.float32), cand_emb)

    jd_skills = req.required_skills or extract_skills(req.jd_text)
    cand_skills = extract_skills(cand_text)

    detail = rule_score(jd_skills, cand_skills, cos)
    return {
        "candidate_id": req.candidate_id,
        "required_skills": jd_skills,
        "candidate_skills": cand_skills,
        "cosine_similarity": round(cos, 4),
        "score_detail": detail,
    }
