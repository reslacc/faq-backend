from fastapi import APIRouter
from pydantic import BaseModel
from app.database.repository import get_answer_by_intent

router = APIRouter()

class FAQRequest(BaseModel):
    intent: str

class FAQResponse(BaseModel):
    answer: str

@router.post("/faq", response_model=FAQResponse)
def faq_endpoint(request: FAQRequest):
    answer = get_answer_by_intent(request.intent)
    return {"answer": answer}