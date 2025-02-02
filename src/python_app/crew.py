from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class PythonApp():
	"""PythonApp crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def SystemDesigner(self) -> Agent:
		return Agent(
			config=self.agents_config['SystemDesigner'],
			verbose=True
		)

	@agent
	def Coder(self) -> Agent:
		return Agent(
			config=self.agents_config['Coder'],
			verbose=True
		)

	@agent
	def Debugger(self) -> Agent:
		return Agent(
			config=self.agents_config['Debugger'],
			verbose=True
		)

  # To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def system_design_task(self) -> Task:
		return Task(
			config=self.tasks_config['system_design_task'],
		)

	@task
	def coding_task(self) -> Task:
		return Task(
			config=self.tasks_config['coding_task'],
			output_file='report.md'
		)

	@task
	def debugging_task(self) -> Task:
		return Task(
			config=self.tasks_config['debugging_task'],
			output_file='report.md'
		)

	@task
	def output_task(self) -> Task:
		return Task(
			config=self.tasks_config['output_task'],
			output_file='final_project_summary.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PythonApp crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
