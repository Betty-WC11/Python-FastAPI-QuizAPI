# The Architect - Defines data structure using Pydantic models
# Ensures that every quiz, question, or answer follows a consistent format.
# Helps FastAPI validate and document your API automatically.

from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    answer_index: int

class Quiz(BaseModel):
    id: int
    title: str
    questions: List[Question]
