# The Tour Guide - Defines API endpoints
# It uses APIRouter() to keep things modular and clean.

from fastapi import APIRouter
from app.data import sample_quiz

router = APIRouter()


@router.get("/quiz")
def get_quiz():
    return sample_quiz


@router.get("/quiz/{question_id}")
def get_question(question_id: int):
    question = None

    for q in sample_quiz.questions:
        if q.id == question_id:
            question = q
            break
    return question or {"error": "Question not found"}
