class Orchestrator:
    def __init__(self, agents, max_rounds=6):
        self.agents = agents
        self.max_rounds = max_rounds

    def run(self, memory):
        for _ in range(self.max_rounds):
            for agent in self.agents:
                agent.act(memory)
