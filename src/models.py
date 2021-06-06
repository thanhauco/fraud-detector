class Transaction:
    def __init__(self, amount: float, location: str, user_id: str = None):
        self.amount = amount
        self.location = location
        self.user_id = user_id