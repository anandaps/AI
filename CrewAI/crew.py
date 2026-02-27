# crew_ai/crew.py
from agent import Agent

class Crew:
    def __init__(self, agents):
        self.agents = agents

    def broadcast(self, message):
        responses = []
        for agent in self.agents:
            responses.append(agent.act(message))
        return responses

    def collaborate(self, message):
        # Simple round-robin collaboration
        result = message
        for agent in self.agents:
            result = agent.act(result)
        return result
