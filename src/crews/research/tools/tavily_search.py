import os
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from pydantic import Field
from tavily import TavilyClient
from typing import Annotated, Optional, Any, Type

from src.config.config import TAVILY_API_KEY

os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY


class TavilySearchInput(BaseModel):
    query: Annotated[str, Field(description="The search query string")]
    max_results: Annotated[
        int, Field(description="Maximum number of results to return", ge=1, le=20)
    ] = 5
    search_depth: Annotated[
        str,
        Field(
            description="Search depth: 'basic' or 'advanced'",
            choices=["basic", "advanced"],
        ),
    ] = "basic"


class TavilySearchTool(BaseTool):
    name: str = "Tavily Search"
    description: str = "Use the Tavily API to perform a web search and get AI-curated results."
    args_schema: Type[BaseModel] = TavilySearchInput
    client: Optional[Any] = None

    def __init__(self, api_key: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.client = TavilyClient(api_key=api_key)

    def _run(self, query: str, max_results=5, search_depth="basic") -> str:
        if not self.client.api_key:
            raise ValueError("TAVILY_API_KEY environment variable not set")

        try:
            response = self.client.search(
                query=query, max_results=max_results, search_depth=search_depth
            )
            return self._process_response(response)
        except Exception as e:
            return f"An error occurred while performing the search: {str(e)}"

    def _process_response(self, response: dict) -> str:
        if not response.get("results"):
            return "No results found."

        results = []
        for item in response["results"][:5]:  # Limit to top 5 results
            title = item.get("title", "No title")
            content = item.get("content", "No content available")
            url = item.get("url", "No URL available")
            results.append(f"Title: {title}\nContent: {content}\nURL: {url}\n")

        return "\n".join(results)
