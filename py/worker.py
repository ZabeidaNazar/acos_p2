import os
import sys
import time
import signal

stop = False

def handle_signal(signum, frame):
    global stop
    if signum == 2: print("\n")
    print(f"Отримано сигнал {signum}")
    stop = True


signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

print(f"Запущено (PID: {os.getpid()}). Очікую сигналів...")

cnt = 1
while not stop:
    print(f"tick={cnt}")
    cnt += 1
    time.sleep(1)
    
print("cleanup...")
sys.exit(0)
