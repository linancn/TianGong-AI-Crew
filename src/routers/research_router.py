from fastapi import APIRouter, HTTPException

from src.models.models import ResearchInput, ResearchOutput
from src.crews.research.main import run

router = APIRouter()


@router.post(
    "/research",
    response_model=ResearchOutput,
    response_description="Crews research result.",
)
async def research(input: ResearchInput):
    """
    This endpoint allows you to write a research.
    """

    try:
        data = run(input.model_dump())
        return ResearchOutput(result=data.raw)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
