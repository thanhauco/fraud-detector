from prometheus_client import Counter
FRAUD_DETECTED = Counter('fraud_detected', 'Number of frauds detected')
TX_PROCESSED = Counter('tx_processed', 'Number of transactions processed')