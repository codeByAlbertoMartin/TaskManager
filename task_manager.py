class Task:

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed
    
    def __str__(self):
        status = "✅" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:

    def __init__(self):
        self._tasks = []
        self._next__id = 1

    def add_task(self, description):
        task = Task(self._next__id, description)
        self._tasks.append(task)
        self._next__id += 1
        return task
    
    def list_tasks(self):
        if not self._tasks:
            print("No hay tareas disponibles.")
        else:
            for task in self._tasks:
                print(task)

    
    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Tarea completada: {task}")
                return task
        print(f"No se encontró ninguna tarea con ID: {id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Tarea eliminada: {task}")
                return task
        print(f"No se encontró ninguna tarea con ID: {id}")