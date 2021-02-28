from celery import Celery
celery = Celery('tasks', broker='redis://localhost:6379/0')
@celery.task
def analyze_heavy(tx_id):
    import time
    time.sleep(5)
    print(f'Analyzed {tx_id}')