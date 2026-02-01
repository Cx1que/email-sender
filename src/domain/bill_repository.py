from abc import ABC, abstractmethod

class BillRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass