# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """Add a new Node with the given value to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Remove the top Node and return its value. Returns None if empty."""
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """Return the value at the top without removing it. Returns None if empty."""
        if self.top is None:
            return None
        return self.top.value

    def print_stack(self):
        """Print all values currently in the stack (top → bottom)."""
        current = self.top
        if current is None:
            print("(empty)")
            return
        while current is not None:
            print(current.value)
            current = current.next

def run_undo_redo():
    # Create two stacks
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack
            undo_stack.push(action)
            # Clear the redo stack by creating a brand-new empty Stack
            redo_stack = Stack()
            print(f"Action performed: {action}")

        elif choice == "2":
            # Pop from undo stack
            action = undo_stack.pop()
            if action is not None:
                # Move it to the redo stack
                redo_stack.push(action)
                print(f"Undid action: {action}")
            else:
                print("No actions to undo")

        elif choice == "3":
            # Pop from redo stack
            action = redo_stack.pop()
            if action is not None:
                # Move it back to the undo stack
                undo_stack.push(action)
                print(f"Redid action: {action}")
            else:
                print("No actions to redo")

        elif choice == "4":
            print("\nUndo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            print("\nRedo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()