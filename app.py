from flask import Flask, request, jsonify
from src.models import Transaction
from src.rules import RuleEngine
app = Flask(__name__)
engine = RuleEngine()
@app.route('/health')
def health(): return 'OK'
@app.route('/check', methods=['POST'])
def check():
    data = request.json
    tx = Transaction(data['amount'], data['location'], data.get('user_id'))
    is_fraud = engine.check(tx)
    return jsonify({'fraud': is_fraud})
if __name__ == '__main__': app.run()