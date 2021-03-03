from flask import Flask, request, jsonify
from src.tasks import analyze_heavy
# ... imports
app = Flask(__name__)
# ... setup
@app.route('/check', methods=['POST'])
def check():
    # ... check logic
    analyze_heavy.delay(123)
    return jsonify({'fraud': False})
if __name__ == '__main__': app.run()