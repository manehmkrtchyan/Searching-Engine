from word import Word
from text import Text

text = Text()
with open('lorem.txt', 'r') as f:
    file_as_str = f.read()
for i in file_as_str.split():
    word = Word(i)
    text.words.append(word.get_word())

for i in text.words:
    print(i.value)
