import unittest
from task import Task, Manager, Developer

class TestTaskSystem(unittest.TestCase):
    def test_task_status_update_notifies_users(self):
        task = Task("Implement feature X", "Develop the new feature for the project.")
        manager = Manager("Alice")
        developer = Developer("Bob")

        task.add_observer(manager)
        task.add_observer(developer)

        # Teste de alteração de status e verificação da notificação
        with self.assertLogs('task', level="INFO") as log:
            task.set_status("In Progress")
            task.set_status("Completed")

        # Verifique se os observadores foram notificados sobre as mudanças
        self.assertIn("INFO:task:Manager Alice is notified about the task 'Implement feature X' status change to In Progress.", log.output)
        self.assertIn("INFO:task:Developer Bob is notified about the task 'Implement feature X' status change to In Progress.", log.output)
        self.assertIn("INFO:task:Manager Alice is notified about the task 'Implement feature X' status change to Completed.", log.output)
        self.assertIn("INFO:task:Developer Bob is notified about the task 'Implement feature X' status change to Completed.", log.output)

if __name__ == "__main__":
    unittest.main()
