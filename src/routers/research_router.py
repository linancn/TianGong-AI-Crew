from fastapi import APIRouter, HTTPException

from src.models.models import ResearchInput
from src.crews.research.main import run

router = APIRouter()


@router.post(
    "/research",
    # response_model=ResponseWithoutPageNum,
    response_description="Crews research result.",
)
async def research(input: ResearchInput):
    """
    This endpoint allows you to extract text from a PDF document.
    It takes a PDF file as input and returns a list of chunks with page numbers.
    """

    try:
        result = run(input.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
