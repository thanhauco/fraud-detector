class RuleEngine:
    def check(self, tx):
        # ... existing
        if tx.amount > 10000: return True
        # Velocity check mock
        return False