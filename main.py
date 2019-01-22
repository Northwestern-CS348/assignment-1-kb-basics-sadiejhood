import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase

class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)


    def test1(self):
        ask1 = read.parse_input("fact: (color bigbox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        #self.assertEqual(answer.list_of_bindings[0][1][0], ask1)

    def test2(self):
        ask1 = read.parse_input("fact: (color littlebox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)

    def test3(self):
        ask1 = read.parse_input("fact: (color ?X red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox")
        self.assertEqual(str(answer[1]), "?X : pyramid3")
        self.assertEqual(str(answer[2]), "?X : pyramid4")


    def test4(self):
        ask1 = read.parse_input("fact: (color bigbox ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?Y : red")

    def test5(self):
        ask1 = read.parse_input("fact: (color ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox, ?Y : red")
        self.assertEqual(str(answer[1]), "?X : littlebox, ?Y : blue")
        self.assertEqual(str(answer[2]), "?X : pyramid1, ?Y : blue")
        self.assertEqual(str(answer[3]), "?X : pyramid2, ?Y : green")
        self.assertEqual(str(answer[4]), "?X : pyramid3, ?Y : red")
        self.assertEqual(str(answer[5]), "?X : pyramid4, ?Y : red")


if __name__ == '__main__':
    unittest.main()

# class KBTest(unittest.TestCase):
#
#     def setUp(self):
#         # Assert starter facts
#         file = 'statements_kb2.txt'
#         data = read.read_tokenize(file)
#         self.KB = KnowledgeBase([], [])
#         for item in data:
#             if isinstance(item, Fact):
#                 self.KB.kb_assert(item)
#
#     def test1(self):
#         ask1 = read.parse_input("fact: (inst Sarorah Sorceress)")
#         print(' Asking if', ask1)
#         answer = self.KB.kb_ask(ask1)
#         self.assertEqual(answer[0].bindings, [])
#         #self.assertEqual(answer.list_of_bindings[0][1][0], ask1)
#
#     def test2(self):
#         ask2 = read.parse_input("fact: (possesses Ai Loot)")
#         print(' Asking if', ask2)
#         answer = self.KB.kb_ask(ask2)
#         self.assertEqual(answer[0].bindings, [])
#
#
# if __name__ == '__main__':
#     unittest.main()

# class KBTest(unittest.TestCase):
#
#     def setUp(self):
#         # Assert starter facts
#         file = 'statements_kb3.txt'
#         data = read.read_tokenize(file)
#         self.KB = KnowledgeBase([], [])
#         for item in data:
#             if isinstance(item, Fact):
#                 self.KB.kb_assert(item)
#
#     def test1(self):
#         ask1 = read.parse_input("fact: (inst Caspa giant)")
#         print(' Asking if', ask1)
#         answer = self.KB.kb_ask(ask1)
#         self.assertEqual(answer[0].bindings, [])
#         #self.assertEqual(answer.list_of_bindings[0][1][0], ask1)
#
#     def test2(self):
#         ask2 = read.parse_input("fact: (friendly Hershey)")
#         print(' Asking if', ask2)
#         answer = self.KB.kb_ask(ask2)
#         self.assertEqual(answer[0].bindings, [])
#
#     def test3(self):
#         ask3 = read.parse_input("fact: (isa ?X ?Y)")
#         print(' Asking if', ask3)
#         answer = self.KB.kb_ask(ask3)
#         self.assertEqual(str(answer[0]), "?X : dragon, ?Y : monster")
#         self.assertEqual(str(answer[1]), "?X : giant, ?Y : monster")
#
#
# if __name__ == '__main__':
#     unittest.main()
