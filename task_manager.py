# Task Manager Application
# Features:
# 1. Add task with title, description, priority (high/medium/low)
# 2. List all tasks
# 3. Mark task as complete
# 4. Delete task
# 5. Filter tasks by priority
# 6. Search tasks by keyword

from datetime import datetime
from typing import List, Optional


class Task:
    """Represents a single task with metadata."""
    
    def __init__(self, title: str, description: str, priority: str):
        """
        Initialize a new Task.
        
        Args:
            title (str): The task title
            description (str): Detailed description of the task
            priority (str): Priority level - 'high', 'medium', or 'low'
        """
        self.id = id(self)  # Generate unique ID using Python's id() function
        self.title = title  # Store task title
        self.description = description  # Store task description
        self.priority = priority.lower()  # Normalize priority to lowercase
        self.completed = False  # Initialize task as incomplete
        self.created_at = datetime.now()  # Record task creation timestamp
    
    def mark_complete(self):
        """Mark task as completed."""
        self.completed = True
    
    def __str__(self):
        """
        Return a formatted string representation of the task.
        
        Returns:
            str: Formatted task display with status, title, priority and description
        """
        # Show checkmark (✓) if completed, circle (○) if pending
        status = "✓" if self.completed else "○"
        # Format: [status] title (Priority: level) - description
        return f"[{status}] {self.title} (Priority: {self.priority}) - {self.description}"


class TaskManager:
    """Manages a collection of tasks."""
    
    def __init__(self):
        self.tasks: List[Task] = []
    
    def add_task(self, title: str, description: str, priority: str) -> Task:
        """
        Add a new task to the task manager.
        
        Args:
            title (str): The task title
            description (str): Detailed task description
            priority (str): Priority level ('high', 'medium', 'low')
            
        Returns:
            Task: The newly created task object
            
        Raises:
            ValueError: If priority is not one of the valid options
        """
        # Validate priority before creating task
        if priority.lower() not in ["high", "medium", "low"]:
            raise ValueError("Priority must be 'high', 'medium', or 'low'")
        
        # Create new task instance
        task = Task(title, description, priority)
        # Add task to tasks list
        self.tasks.append(task)
        # Return the created task
        return task
    
    def list_all_tasks(self) -> List[Task]:
        """Return all tasks."""
        return self.tasks
    
    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a specific task as complete by its ID.
        
        Args:
            task_id (int): The unique ID of the task to mark complete
            
        Returns:
            bool: True if task was found and marked complete, False otherwise
        """
        # Search through all tasks for matching ID
        for task in self.tasks:
            if id(task) == task_id:
                # Mark the task as complete
                task.mark_complete()
                return True  # Success
        # Task not found
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the manager by its ID.
        
        Args:
            task_id (int): The unique ID of the task to delete
            
        Returns:
            bool: True if task was found and deleted, False otherwise
        """
        # Search through tasks with enumeration to get index
        for i, task in enumerate(self.tasks):
            if id(task) == task_id:
                # Remove task from list by index
                self.tasks.pop(i)
                return True  # Success
        # Task not found
        return False
    
    def filter_by_priority(self, priority: str) -> List[Task]:
        """
        Filter tasks by priority level.
        
        Args:
            priority (str): Priority level to filter by ('high', 'medium', 'low')
            
        Returns:
            List[Task]: List of tasks matching the specified priority
        """
        # Use list comprehension to filter tasks by priority (case-insensitive)
        return [t for t in self.tasks if t.priority == priority.lower()]
    
    def search_by_keyword(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description.
        
        Args:
            keyword (str): Search term to find in tasks
            
        Returns:
            List[Task]: List of tasks containing the keyword (case-insensitive search)
        """
        # Convert keyword to lowercase for case-insensitive comparison
        keyword_lower = keyword.lower()
        # Filter tasks where keyword appears in title OR description
        return [t for t in self.tasks 
                if keyword_lower in t.title.lower() or keyword_lower in t.description.lower()]
    
    def display_tasks(self, tasks: Optional[List[Task]] = None):
        """
        Display tasks in a formatted table layout.
        
        Args:
            tasks (Optional[List[Task]]): Specific tasks to display. 
                                         If None, displays all tasks in manager.
        """
        # Use provided tasks list or default to all tasks
        display_list = tasks if tasks is not None else self.tasks
        
        # Handle empty task list
        if not display_list:
            print("No tasks found.")
            return
        
        # Print formatted task list with borders
        print("\n" + "="*60)
        # Enumerate starting from 1 for user-friendly numbering
        for i, task in enumerate(display_list, 1):
            print(f"{i}. {task}")
        # Print bottom border
        print("="*60 + "\n")


def main():
    """
    Main entry point demonstrating all TaskManager features.
    
    This function showcases:
    - Creating a TaskManager instance
    - Adding multiple tasks with different priorities
    - Displaying all tasks
    - Filtering tasks by priority
    - Searching for tasks by keyword
    - Marking tasks as complete
    """
    # Initialize a new TaskManager instance
    manager = TaskManager()
    
    # Add sample tasks with various priorities
    manager.add_task("Complete project", "Finish the Python project", "high")
    manager.add_task("Review code", "Review pull requests", "medium")
    manager.add_task("Update docs", "Update documentation", "low")
    manager.add_task("Bug fix", "Fix critical bug in payment system", "high")
    
    # Display all tasks in the manager
    print("All Tasks:")
    manager.display_tasks()
    
    # Filter and display only high priority tasks
    print("High Priority Tasks:")
    manager.display_tasks(manager.filter_by_priority("high"))
    
    # Search for tasks containing the keyword 'project'
    print("Search results for 'project':")
    manager.display_tasks(manager.search_by_keyword("project"))
    
    # Mark the first task as complete and display updated list
    first_task = manager.list_all_tasks()[0]
    manager.mark_complete(id(first_task))
    print("After marking first task as complete:")
    manager.display_tasks()


if __name__ == "__main__":
    main()
    # generate Docstrings for all functions
    # add comments to explain the code
    