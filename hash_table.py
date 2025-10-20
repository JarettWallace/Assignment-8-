class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size: int):
        self.size = size 
        self.data = [None] * size
    def hash_function(self, key: str) -> int:

        return sum(ord(char) for char in key) % self.size
    def insert(self, key: str, value: Contact): 
        index = self.hash_function(key)
        new_node = Node(key, value)

        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while current:
                if current.key == key:
                    current.value.number = value.number 
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node 

    def search(self,key: str) -> Contact:
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None 
    def print_table(self):
        for i, node in enumerate(self.data):
            if node is None:
                print(f"Index {i}: empty")
            else:
                print(f"Index {i}: ", end="")
                current = node 
                while current:
                    print(f"[{current.value}]", end=" -> ")
                    current = current.next
                print("None")


# Test your hash table implementation here.   
if __name__ == "__main__":
    hash_table = HashTable(10)

    hash_table.insert("Alice", Contact("Alice", "123-456-7890"))
    hash_table.insert("Bob", Contact("Bob", "234-567-8901"))
    hash_table.insert("Charlie", Contact("Charlie", "345-678-9012")) 

    hash_table.insert("Eve", Contact("Eve", "456-789-0123"))
    hash_table.insert("Alice", Contact("Alice", "111-222-3333")) 
    hash_table.print_table() 
    contact = hash_table.search("Alice")
    if contact:
        print(f"Found contact: {contact}")
    else:
        print("Contact not found.") 

    