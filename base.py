from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name, llm):
        self.name = name
        self.llm = llm

    @abstractmethod
    def act(self, memory):
        pass
