class Node:
    def __init__(self, key, value) -> None:
        self.value = value 
        self.next = None
        self.key = key

class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [None] * size

    def hashing(self, key):
        key_bytes = key.encode('utf-8')
        hash_value = 0

        for byte in key_bytes:
            hash_value = (hash_value * 31 + byte) % self.size

        return hash_value


    def insert(self, key, value):
        index = self.hashing(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self.hashing(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def display(self):
        for index in range(self.size):
            current = self.table[index]
            elements = []
            while current:
                elements.append(f"({current.key}: {current.value})")
                current = current.next
            print(f"{index}: {' -> '.join(elements)}")