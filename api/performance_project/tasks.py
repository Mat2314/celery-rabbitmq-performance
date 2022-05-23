from .celery import app
import random

@app.task()
def simulate_heavy_task():
    """Simulate heavy process to test celery and rabbitmq performance"""
    base = 1000000000
    factor = random.randint(1,10)
    
    for i in range(base*factor):
        x = i*i