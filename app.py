from flask import Flask, request, jsonify
from src.models import Transaction
from src.rules import RuleEngine
from src.db import init_db, get_db
import os
import pickle
app = Flask(__name__)
if not os.path.exists('fraud.db'): init_db()
engine = RuleEngine()
model = None
if os.path.exists('model.pkl'):
    with open('model.pkl', 'rb') as f: model = pickle.load(f)
@app.route('/health')
def health(): return 'OK'
@app.route('/check', methods=['POST'])
def check():
    data = request.json
    tx = Transaction(data['amount'], data['location'], data.get('user_id'))
    is_fraud = engine.check(tx)
    if not is_fraud and model:
        is_fraud = model.predict([[tx.amount]])[0] == 1
    with get_db() as conn:
        conn.execute('INSERT INTO transactions (amount, location, is_fraud) VALUES (?, ?, ?)', (tx.amount, tx.location, 1 if is_fraud else 0))
    return jsonify({'fraud': bool(is_fraud)})
if __name__ == '__main__': app.run()