import unittest
from todo import Todo

class TestTodo(unittest.TestCase):
    def setUp(self):
        self.todo = Todo()

    def test_add_task(self):
        self.assertTrue(self.todo.add_task("Learn Python"))
        self.assertEqual(len(self.todo.tasks), 1)

    def test_remove_task(self):
        self.todo.add_task("Learn Python")
        self.assertTrue(self.todo.remove_task(0))
        self.assertEqual(len(self.todo.tasks), 0)

    def test_mark_completed(self):
        self.todo.add_task("Learn Python")
        self.assertTrue(self.todo.mark_completed(0))
        self.assertTrue(self.todo.tasks[0]["completed"])

if __name__ == '__main__':
    unittest.main()
#added one more line
