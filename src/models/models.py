from typing import List, Tuple

from pydantic import BaseModel


class TextElementWithPageNum(BaseModel):
    text: str
    page_number: int


class ResponseWithPageNum(BaseModel):
    result: List[TextElementWithPageNum]

    @classmethod
    def from_result(cls, result: List[Tuple[str, int]]):
        items = [TextElementWithPageNum(text=item[0], page_number=item[1]) for item in result]
        return cls(result=items)
