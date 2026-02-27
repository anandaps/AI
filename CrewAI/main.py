# crew_ai/main.py
from agent import Agent
from crew import Crew

if __name__ == "__main__":
    # Create agents
    agent1 = Agent("Alice", "Planner")
    agent2 = Agent("Bob", "Researcher")
    agent3 = Agent("Charlie", "Executor")

    # Create crew
    crew = Crew([agent1, agent2, agent3])

    # Broadcast message
    print("Broadcast responses:")
    for response in crew.broadcast("Start project"): 
        print(response)

    # Collaborate on a task
    print("\nCollaboration result:")
    print(crew.collaborate("Initial task"))
