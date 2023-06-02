class Word:
    def __init__(self, value):
        self.value = value

    def make_lowercase(self):
        return Word(self.value.lower())

    def remove_symbols(self):
        special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                              '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        if not self.value.isalpha():
            for i in special_characters:
                self.value.replace(i, '')
        return Word(self.value)

    def is_in_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if self.value in line:
                    return True
        return False

    def normalize(self, file_path):
        # not complete
        if self.is_in_file(file_path):
            return self.value

    def get_normalized_word(self, file_for_normalizing='words_alpha.txt'):
        lowercase_word = self.make_lowercase()
        clean_word = lowercase_word.remove_symbols()
        normalized_word = clean_word.normalize(file_for_normalizing)

        return normalized_word