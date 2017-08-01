from celery import Celery

app = Celery("task", broker="redis://localhost")

@app.task
def add(x, y):
    return x + y
