class Word:
    def __init__(self, value) -> None:
        self.value = value

    def get_word(self):
        return self.make_lowercase().remove_symbols()

    def make_lowercase(self):
        return Word(self.value.lower())
    
    def remove_symbols(self):
        unnecessary_symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        for i in str(self.value):
            if i in unnecessary_symbols:
                new = str(self.value).replace(i, '')
            else:
                
        return Word(new)

    def __repr__(self) -> str:
        return str(self.get_word.value)