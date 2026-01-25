from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Shopper():
    """Shopper crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['evaluator'], # type: ignore[index]
            verbose=True
        )

    @agent
    def selector(self) -> Agent:
        return Agent(
            config=self.agents_config['selector'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def evaluate_mg_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_mg_task'], # type: ignore[index]
        )

    @task
    def evaluate_tr_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_tr_task'], # type: ignore[index]
        )

    @task
    def evaluate_fiat_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_fiat_task'], # type: ignore[index]
        )

    @task
    def evaluate_datsun_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_datsun_task'], # type: ignore[index]
        )

    @task
    def selector_task(self) -> Task:
        return Task(
            config=self.tasks_config['selector_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Shopper crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
