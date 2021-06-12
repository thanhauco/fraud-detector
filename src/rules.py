class RuleEngine:
    def __init__(self):
        self.rules = [AmountRule()]
    def check(self, tx):
        return any(r.check(tx) for r in self.rules)