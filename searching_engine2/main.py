from text import Text
from file_parser import parse_file
from inverted_index import InvertedIndex


"""Version 1"""
# text1 = Text('1.txt')
# text2 = Text('2.txt')

# parse_file('1.txt', '2.txt')

"""Version 2"""
ii = InvertedIndex('1.txt', '2.txt')
ii.display()