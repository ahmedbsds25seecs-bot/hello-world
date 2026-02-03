import unittest
from task_manager import Task, TaskManager


class TestTask(unittest.TestCase):
    """Test cases for Task class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.task = Task("Test Task", "Test Description", "high")
    
    def test_task_creation(self):
        """Test task creation with valid inputs."""
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "Test Description")
        self.assertEqual(self.task.priority, "high")
        self.assertFalse(self.task.completed)
    
    def test_priority_case_insensitive(self):
        """Test that priority is case-insensitive."""
        task = Task("Title", "Desc", "HIGH")
        self.assertEqual(task.priority, "high")
    
    def test_mark_complete(self):
        """Test marking task as complete."""
        self.assertFalse(self.task.completed)
        self.task.mark_complete()
        self.assertTrue(self.task.completed)
    
    def test_task_string_representation(self):
        """Test task string formatting."""
        result = str(self.task)
        self.assertIn("Test Task", result)
        self.assertIn("high", result)
        self.assertIn("○", result)  # Incomplete marker


class TestTaskManager(unittest.TestCase):
    """Test cases for TaskManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.manager = TaskManager()
    
    def test_add_task(self):
        """Test adding a task."""
        task = self.manager.add_task("Title", "Description", "medium")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertIsNotNone(task.id)
    
    def test_add_multiple_tasks(self):
        """Test adding multiple tasks."""
        self.manager.add_task("Task 1", "Desc 1", "high")
        self.manager.add_task("Task 2", "Desc 2", "low")
        self.manager.add_task("Task 3", "Desc 3", "medium")
        self.assertEqual(len(self.manager.tasks), 3)
    
    def test_invalid_priority(self):
        """Test that invalid priority raises error."""
        with self.assertRaises(ValueError):
            self.manager.add_task("Title", "Desc", "urgent")
    
    def test_list_all_tasks(self):
        """Test listing all tasks."""
        self.manager.add_task("Task 1", "Desc 1", "high")
        self.manager.add_task("Task 2", "Desc 2", "low")
        tasks = self.manager.list_all_tasks()
        self.assertEqual(len(tasks), 2)
    
    def test_mark_complete(self):
        """Test marking task as complete."""
        task = self.manager.add_task("Title", "Desc", "high")
        task_id = id(task)
        self.assertTrue(self.manager.mark_complete(task_id))
        self.assertTrue(task.completed)
    
    def test_mark_complete_invalid_id(self):
        """Test marking non-existent task returns False."""
        result = self.manager.mark_complete(99999)
        self.assertFalse(result)
    
    def test_delete_task(self):
        """Test deleting a task."""
        task = self.manager.add_task("Title", "Desc", "high")
        task_id = id(task)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertTrue(self.manager.delete_task(task_id))
        self.assertEqual(len(self.manager.tasks), 0)
    
    def test_delete_invalid_id(self):
        """Test deleting non-existent task returns False."""
        result = self.manager.delete_task(99999)
        self.assertFalse(result)
    
    def test_filter_by_priority(self):
        """Test filtering tasks by priority."""
        self.manager.add_task("Task 1", "Desc 1", "high")
        self.manager.add_task("Task 2", "Desc 2", "high")
        self.manager.add_task("Task 3", "Desc 3", "low")
        
        high_tasks = self.manager.filter_by_priority("high")
        low_tasks = self.manager.filter_by_priority("low")
        
        self.assertEqual(len(high_tasks), 2)
        self.assertEqual(len(low_tasks), 1)
    
    def test_filter_by_priority_case_insensitive(self):
        """Test filter is case-insensitive."""
        self.manager.add_task("Task", "Desc", "high")
        result = self.manager.filter_by_priority("HIGH")
        self.assertEqual(len(result), 1)
    
    def test_filter_empty_result(self):
        """Test filtering with no matching tasks."""
        self.manager.add_task("Task", "Desc", "high")
        result = self.manager.filter_by_priority("low")
        self.assertEqual(len(result), 0)
    
    def test_search_by_title(self):
        """Test searching by title."""
        self.manager.add_task("Python Project", "Description", "high")
        self.manager.add_task("Java Project", "Description", "low")
        
        results = self.manager.search_by_keyword("Python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Python Project")
    
    def test_search_by_description(self):
        """Test searching by description."""
        self.manager.add_task("Task 1", "Fix database issue", "high")
        self.manager.add_task("Task 2", "Update UI", "low")
        
        results = self.manager.search_by_keyword("database")
        self.assertEqual(len(results), 1)
    
    def test_search_case_insensitive(self):
        """Test search is case-insensitive."""
        self.manager.add_task("Python Project", "Description", "high")
        results = self.manager.search_by_keyword("python")
        self.assertEqual(len(results), 1)
    
    def test_search_no_results(self):
        """Test search with no matching tasks."""
        self.manager.add_task("Task", "Description", "high")
        results = self.manager.search_by_keyword("nonexistent")
        self.assertEqual(len(results), 0)
    
    def test_search_empty_keyword(self):
        """Test search with empty keyword."""
        self.manager.add_task("Task 1", "Desc", "high")
        self.manager.add_task("Task 2", "Desc", "low")
        results = self.manager.search_by_keyword("")
        self.assertEqual(len(results), 2)  # Empty string matches all


if __name__ == "__main__":
    unittest.main()