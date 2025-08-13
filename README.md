# Double Linked List in Python

This project contains a **custom implementation** of a Doubly Linked List in Python.  
It supports insertion, deletion, indexing, iteration, and other list-like operations, while raising a custom `EmptyDoubleLinkedListError` for invalid actions on an empty list.

## 📚 Features

- **Custom Node Structure** – Each node stores `value`, `prev`, and `next` references.
- **List-Like Operations**:
  - Append
  - Insert at any index
  - Extend with another DoubleLinkedList
  - Remove by value
  - Pop last element
  - Index lookup
  - Item assignment (`dll[index] = value`)
  - Item deletion (`del dll[index]`)
  - Containment check (`value in dll`)
- **Iteration Support** – Works with `for` loops.
- **Negative Index Support** – Access elements from the end.
- **Error Handling** – Raises:
  - `EmptyDoubleLinkedListError` for operations on empty lists.
  - `IndexError` for out-of-range access.
  - `ValueError` for invalid value lookups.

## 🛠 Usage Example

```python
from doublelinkedlist import DoubleLinkedList

# Create a DoubleLinkedList with initial values
dll = DoubleLinkedList(1, 2, 3)

# Append a value
dll.append(4)

# Insert at position 1
dll.insert(1, 99)

# Remove a value
dll.remove(2)

# Access and modify
print(dll[0])      # Output: 1
dll[0] = 42

# Delete an element
del dll[1]

# Check membership
if 3 in dll:
    print("3 is in the list")

# Iterate over the list
for value in dll:
    print(value)

# Pop last element
last_value = dll.pop()
print("Popped:", last_value)

Custom Exception
EmptyDoubleLinkedListError is raised when attempting to:

Access or delete from an empty list

Pop from an empty list

Remove from an empty list
# Clear the list
dll.clear()

License
This project is open-source and can be used for learning or personal projects.
