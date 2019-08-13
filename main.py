import unittest
from lexer import Lexer
from parserr import Parser

file = open(raw_input("Enter Filename: "),'r')

data = file.readlines()
file.close()

currentline = 1

for lines in data:
    print "Proposition: " + lines.rstrip()
    tokenlist = Lexer(lines.rstrip()).tokenize(currentline)
    print "Lexer: ", tokenlist
    grammarlist = Parser().parse(tokenlist)
    print "Parser:", grammarlist
    print
    currentline += 1

'''
class Test(unittest.TestCase):
    def test1(self):
        tokenlist = Lexer('Q').tokenize(1)
        self.assertEqual(tokenlist[0].kind, "ID")
        self.assertEqual(tokenlist[0].loc.col, 1)
        self.assertEqual(tokenlist[0].loc.line, 1)

    def test2(self):
        tokenlist = Lexer('Q').tokenize(1)
        grammarlist = Parser().parse(tokenlist)
        self.assertEqual(grammarlist[0].kind, "propositions")
        self.assertEqual(grammarlist[1].kind, "proposition")
        self.assertEqual(grammarlist[2].kind, "atomic")
        self.assertEqual(grammarlist[3].kind, "ID")
        self.assertEqual(grammarlist[4].kind, "more-proposition")
        self.assertEqual(grammarlist[5].kind, "epsilon")

if __name__ == '__main__':
    unittest.main()
    '''