import time
from plyer import notification

def lembrete():
    notification.notify(
        title= "Hidrata ai mano",
        message= "Bebe água ai paizão💧",
        timeout=10
    )
    
while True:
    lembrete()
    time.sleep(3600)