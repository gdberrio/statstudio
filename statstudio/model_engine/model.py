from abc import ABC, abstractmethod
from dataclasses import dataclass

class Model(ABC):
    """
    Abstract class to hold Model
    """


class Backend(ABC):
    pass

class Runner(ABC):
    """
    Abscract class to handle methods needed to run model
    """
    
    @abstractmethod
    def setup(self, backend: Backend) -> None:
        """
        Abstract method to be implemented to setup runner
        """

    def run(self, backend: Backend):
        """
        Abstract method to run simulation
        """

class DataLoader(ABC):
    pass
