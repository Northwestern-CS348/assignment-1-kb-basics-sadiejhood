import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        isFact = True
        if (fact.name != 'fact'):
            # not a fact....
            isFact = False

        contains = False
        for f in self.facts:
            if match(f.statement, fact.statement):
                # We don't add this fact, because it is already in
                contains = True

        if ( (not contains) and isFact):
            self.facts.append(fact)

        print("Asserting {!r}".format(fact))

    def kb_ask(self, fact):

        cur_match = []
        for f in self.facts:
            if match(f.statement, fact.statement):
                cur_match.append(match(f.statement, fact.statement))
        return cur_match
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
