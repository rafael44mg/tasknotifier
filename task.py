import logging
from abc import ABC, abstractmethod

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sujeito
class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.status = 'Pending'
        self._observers = []

    def add_observer(self, observer):
        """Adiciona um observador à lista."""
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        """Remove um observador da lista."""
        self._observers.remove(observer)

    def notify_observers(self):
        """Notifica todos os observadores sobre a mudança de estado."""
        for observer in self._observers:
            observer.update(self)

    def set_status(self, status: str):
        """Altera o status da tarefa e notifica os observadores."""
        self.status = status
        self.notify_observers()

# Observador
class User(ABC):
    @abstractmethod
    def update(self, task: Task):
        pass

# Implementação concreta do Observador
class Manager(User):
    def __init__(self, name: str):
        self.name = name

    def update(self, task: Task):
        # Substituindo print por logger
        logger.info(f"Manager {self.name} is notified about the task '{task.title}' status change to {task.status}.")

class Developer(User):
    def __init__(self, name: str):
        self.name = name

    def update(self, task: Task):
        # Substituindo print por logger
        logger.info(f"Developer {self.name} is notified about the task '{task.title}' status change to {task.status}.")
