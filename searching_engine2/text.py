from word import Word

class Text:
    def __init__(self, file_path) -> None:
        self.words = []
        self.file_path = file_path

        with open(self.file_path, 'r') as f:
            self.file_content = f.read()
        for item in self.file_content.split():
            word = Word(item)
            if word.get_normalized_word():
                self.words.append(word.get_normalized_word())

    def __repr__(self):
        return str(self.words)

    def __add__(self, other):
        return self.words + other.words