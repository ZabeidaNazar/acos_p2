import subprocess
import signal
import time


print("--- Запуск процесу ---")
process = subprocess.Popen(["sleep", "100"])
print(f"Процес 'sleep 100' запущено. PID: {process.pid}")
time.sleep(1)

process.send_signal(signal.SIGSTOP)
print("Процес зупинено")
time.sleep(2)

process.send_signal(signal.SIGCONT)
print("Процес продовжено")
time.sleep(2)

process.terminate()

process.wait()

print(f"Процес завершено")
print(f"returncode: {process.returncode}")
