import pandas as pd
# ... imports
def train():
    # ... existing
    df = pd.read_sql('SELECT * FROM transactions', conn)
    df['amount'] = df['amount'].astype('float32')
    # ... rest