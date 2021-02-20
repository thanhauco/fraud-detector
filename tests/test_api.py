import unittest
import requests
class TestApi(unittest.TestCase):
    def test_health(self):
        r = requests.get('http://localhost:5000/health')
        self.assertEqual(r.status_code, 200)
if __name__ == '__main__': unittest.main()