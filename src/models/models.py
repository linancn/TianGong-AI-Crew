from pydantic import BaseModel


class ResearchInput(BaseModel):
    topic: str
    current_year: str


class ResearchOutput(BaseModel):
    results: str
