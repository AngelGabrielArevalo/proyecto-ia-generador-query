from pydantic import BaseModel
from typing import List


class PromptQuery(BaseModel):
    id: str
    prompt: str
    query: str
    embedding: List[float]
