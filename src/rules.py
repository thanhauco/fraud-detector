class RuleEngine:
    def check(self, tx):
        if tx.amount > 10000: return True
        return False