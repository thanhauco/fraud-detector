import sys
import requests
if len(sys.argv) < 2: print('Usage: cli.py <amount>'); sys.exit(1)
amount = float(sys.argv[1])
resp = requests.post('http://localhost:5000/check', json={'amount': amount, 'location': 'CLI', 'user_id': 'admin'})
print(resp.json())