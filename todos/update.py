from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Todo
from . import mail

# checking for time
def checkTime():
    todos = Todo.objects.all()
    present = datetime.now(timezone.utc)

    for i, todo in enumerate(todos):
        # print (i, present, todo.title, todo.due_date)
        total_sec = (todo.due_date - present).total_seconds()
        if (total_sec <= 0):
            print ("Sending mail...")
            mail.send(todo.id)


def check():
    todos = Todo.objects.all()

    # sending the todo list to the user via mail
    mail.sendAll(todos)

    
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check, 'interval', hours=10)
    scheduler.add_job(checkTime, 'interval', minutes=5)
    scheduler.start()