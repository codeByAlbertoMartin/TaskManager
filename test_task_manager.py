import unittest
import os
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    TEST_FILENAME = "test_tasks.json"

    def setUp(self):
        # Usar un archivo de tareas de prueba sin modificar el atributo de clase
        self.manager = TaskManager(filename=self.TEST_FILENAME)
        self.manager._tasks = []
        self.manager._next_id = 1  # Corregido: un solo guion bajo
        self.manager.save_tasks()

    def tearDown(self):
        # Eliminar el archivo de prueba si existe
        if os.path.exists(self.TEST_FILENAME):
            os.remove(self.TEST_FILENAME)

    def test_add_task(self):
        task = self.manager.add_task("Tarea de prueba")
        self.assertEqual(task.description, "Tarea de prueba")
        self.assertFalse(task.completed)
        self.assertEqual(task.id, 1)
        self.assertEqual(len(self.manager._tasks), 1)

    def test_list_tasks(self):
        self.manager.add_task("Tarea 1")
        self.manager.add_task("Tarea 2")
        tasks = self.manager._tasks
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].description, "Tarea 1")
        self.assertEqual(tasks[1].description, "Tarea 2")

    def test_complete_task(self):
        self.manager.add_task("Tarea a completar")
        task = self.manager.complete_task(1)
        self.assertIsNotNone(task)

    def test_delete_task(self):
        self.manager.add_task("Tarea a eliminar")
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager._tasks), 0)

    def test_complete_task_id_inexistente(self):
        result = self.manager.complete_task(99)
        self.assertIsNone(result)

    def test_delete_task_id_inexistente(self):
        result = self.manager.delete_task(99)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
