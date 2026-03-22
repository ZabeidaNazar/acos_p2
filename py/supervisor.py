import subprocess
import time
import sys

MAX_RESTARTS = 3

restarts = 0

while restarts <= MAX_RESTARTS:
    print(f"\n[Supervisor] Запуск worker.py (Спроба {restarts + 1} з {MAX_RESTARTS + 1})")
    
    process = subprocess.Popen([sys.executable, "worker.py"])
    
    try:
        process.wait()
        print(f"[Supervisor] Worker (PID: {process.pid}) завершився з кодом {process.returncode}")
        
    except KeyboardInterrupt:
        print("\n[Supervisor] Отримано Ctrl+C. Зупиняю worker...")
        process.terminate()
        process.wait()
        print("[Supervisor] Роботу завершено.")
        break
        
    if restarts < MAX_RESTARTS:
        print("[Supervisor] Перезапуск через 2 секунди...")
        time.sleep(2)
        
    restarts += 1
    
if restarts > MAX_RESTARTS:
    print("[Supervisor] Досягнуто ліміт перезапусків. Робота Supervisor завершена.")
