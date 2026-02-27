# crew_ai/agent.py

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def act(self, message):
        return f"{self.name} ({self.role}) received: {message}"
