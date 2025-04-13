class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the todo list."""
        if task and isinstance(task, str):
            self.tasks.append({"task": task, "completed": False})
            return True
        return False

    def remove_task(self, index):
        """Remove a task from the todo list."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def mark_completed(self, index):
        """Mark a task as completed."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            return True
        return False

    def get_tasks(self):
        """Return all tasks."""
        return self.tasks
