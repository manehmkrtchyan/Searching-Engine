from hashtable import HashTable
from file_parser import parse_file

class InvertedIndex:
    def __init__(self, file1, file2):
        di = parse_file(file1, file2)
        self.index = HashTable(size=len(di))  
        for key, value in di.items():
            self.index.insert(key, value)

    
    def display(self):
        (self.index.display())