from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from src.crews.research.tools.tavily_search import TavilySearchTool
from src.config.config import OPENAI_API_KEY, OPENAI_MODEL

llm = LLM(
    model=OPENAI_MODEL,
    api_key=OPENAI_API_KEY,
)

tavily_search_tool = TavilySearchTool()


@CrewBase
class TiangongAiCrew:
    """TiangongAiCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            verbose=True,
            tools=[tavily_search_tool],
            llm=llm,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(config=self.agents_config["reporting_analyst"], verbose=True, llm=llm)

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],  # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],  # type: ignore[index]
            # output_file="report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TiangongAiCrew crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
