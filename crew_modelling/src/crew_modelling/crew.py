from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from crew_modelling.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool


@CrewBase
class CrewModellingCrew:
    """CrewModelling crew"""

    @agent
    def Research_Planner(self) -> Agent:
        return Agent(
            config=self.agents_config["Research_Planner"],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
        )

    @agent
    def Literature_Review_Researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["Literature_Review_Researcher"], verbose=True
        )

    @agent
    def Literature_Review_Writer(self) -> Agent:
        return Agent(
            config=self.agents_config["Literature_Review_Writer"], verbose=True
        )

    @agent
    def Data_Collector_Agent(self) -> Agent:
        return Agent(config=self.agents_config["Data_Collector_Agent"], verbose=True)

    @agent
    def Data_Preprocessing_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config["Data_Preprocessing_Agent"], verbose=True
        )

    @agent
    def Results_Analysis_Agent(self) -> Agent:
        return Agent(config=self.agents_config["Results_Analysis_Agent"], verbose=True)

    @agent
    def Documentation_Agent(self) -> Agent:
        return Agent(config=self.agents_config["Documentation_Agent"], verbose=True)

    @agent
    def Bibliography_Agent(self) -> Agent:
        return Agent(config=self.agents_config["Bibliography_Agent"], verbose=True)

    @agent
    def Presentation_Agent(self) -> Agent:
        return Agent(config=self.agents_config["Presentation_Agent"], verbose=True)

    @task
    def research_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_planning_task"],
        )

    @task
    def literature_review_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["literature_review_research_task"],
        )

    @task
    def literature_review_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["literature_review_writing_task"],
            output_file="report.md",
        )

    @task
    def data_collecting_task(self) -> Task:
        return Task(
            config=self.tasks_config["data_collecting_task"], output_file="report.md"
        )

    @task
    def data_preprocessing_task(self) -> Task:
        return Task(
            config=self.tasks_config["data_preprocessing_task"],
        )

    @task
    def result_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["result_analysis_task"],
        )

    @task
    def documentation_task(self) -> Task:
        return Task(
            config=self.tasks_config["documentation_task"], output_file="report.md"
        )

    @task
    def bibliography_task(self) -> Task:
        return Task(
            config=self.tasks_config["bibliography_task"], output_file="report.md"
        )

    @task
    def presentation_task(self) -> Task:
        return Task(
            config=self.tasks_config["presentation_task"], output_file="report.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewModelling crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
