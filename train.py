import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
def train():
    conn = sqlite3.connect('fraud.db')
    df = pd.read_sql('SELECT * FROM transactions', conn)
    if len(df) < 10: return
    X = df[['amount']]
    y = df['is_fraud']
    clf = RandomForestClassifier()
    clf.fit(X, y)
    with open('model.pkl', 'wb') as f: pickle.dump(clf, f)
    print('Model trained')
if __name__ == '__main__': train()