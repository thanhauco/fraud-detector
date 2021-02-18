import unittest
from src.rules import RuleEngine
from src.models import Transaction
class TestRules(unittest.TestCase):
    def test_high_amount(self):
        e = RuleEngine()
        t = Transaction(20000, 'US', 'u1')
        self.assertTrue(e.check(t))
if __name__ == '__main__': unittest.main()