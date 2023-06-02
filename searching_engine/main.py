from text import Text
from file_parser import parse_file

text1 = Text('1.txt')
text2 = Text('2.txt')

# print('text1:', text1)
# print('text2:', text2)

parse_file('1.txt', '2.txt')