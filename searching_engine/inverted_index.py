from linked_list import LinkedList
class InvertedIndex:
    def __init__(self) -> None:
        self.keys = []
        with open('db.txt', 'r') as f:
            for line in f:
                idx = line.find(':')
                self.keys.append(line[:idx])
                ls = line[idx + 1] 
                ll = 
        print(self.keys)        
i = InvertedIndex()