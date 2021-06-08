from abc import ABC, abstractmethod
class Rule(ABC):
    @abstractmethod
    def check(self, tx) -> bool:
        pass
class AmountRule(Rule):
    def check(self, tx):
        return tx.amount > 10000