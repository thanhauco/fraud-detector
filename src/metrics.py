from prometheus_client import Counter
REQUESTS = Counter('requests_total', 'Total requests')
def inc_requests():
    REQUESTS.inc()