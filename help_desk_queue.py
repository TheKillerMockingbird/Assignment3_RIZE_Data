# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None   # points to the first node in line
        self.rear = None    # points to the last node in line

    def enqueue(self, value):
        """Add a new customer (Node) to the end of the queue."""
        new_node = Node(value)
        
        if self.rear is None:          # queue is currently empty
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node  # link the old rear to the new node
            self.rear = new_node       # move the rear pointer forward

    def dequeue(self):
        """Remove and return the customer at the front of the queue.
           Returns None if the queue is empty."""
        if self.front is None:
            return None                # nothing to dequeue
        
        value = self.front.value
        self.front = self.front.next   # move the front pointer forward
        
        if self.front is None:         # queue became empty
            self.rear = None           # also reset the rear pointer
        
        return value

    def peek(self):
        """Return the value at the front without removing it.
           Returns None if the queue is empty."""
        if self.front is None:
            return None
        return self.front.value

    def print_queue(self):
        """Print all customers currently waiting (front → rear)."""
        current = self.front
        if current is None:
            print("(empty)")
            return
        while current is not None:
            print(current.value)
            current = current.next
    


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            # Help the next customer
            customer = queue.dequeue()
            if customer is not None:
                print(f"{customer} has been helped.")
            else:
                print("No customers waiting.")

        elif choice == "3":
            # Peek at the next customer
            customer = queue.peek()
            if customer is not None:
                print(f"Next customer: {customer}")
            else:
                print("No customers waiting.")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
